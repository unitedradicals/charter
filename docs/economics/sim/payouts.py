#!/usr/bin/env python3
"""Payout simulator for the United Radicals economic model.

The single source of truth for every number in docs/economics/payouts.md.
Run it to print the worked example as Markdown tables:

    python3 docs/economics/sim/payouts.py

After changing the scenario or the rules, refresh the tables in the doc with:

    python3 docs/economics/sim/payouts.py --update-doc

Money is kept in integer cents. Every split uses the largest-remainder method,
so the parts always add up to the whole, to the cent. The script checks that
money in equals money out every month and stops with an error if it doesn't.

All members, products and figures are fictional.
"""

import contextlib
import io
import pathlib
import re
import sys
from collections import defaultdict

# ---------------------------------------------------------------------------
# Rules [placeholder values, set by the founding round]
# ---------------------------------------------------------------------------
PRODUCT_SPLIT = {"contributors": 60, "treasury": 25, "pool": 15}  # 12:5:3
CLIENT_SPLIT = {"members": 85, "treasury": 15}  # 17:3
REVIEW_SHARE = 10  # % of a reviewed task's points that the reviewer earns
MONTHS = 12
MONTH_NAMES = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
               "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def split(total, weights):
    """Split `total` cents by `weights` {key: number}; the parts sum to `total` exactly."""
    weights = {k: w for k, w in weights.items() if w > 0}
    wsum = sum(weights.values())
    if total == 0 or wsum == 0:
        return {}
    exact = {k: total * w / wsum for k, w in weights.items()}
    parts = {k: int(v) for k, v in exact.items()}
    leftover = total - sum(parts.values())
    for k in sorted(exact, key=lambda k: exact[k] - parts[k], reverse=True)[:leftover]:
        parts[k] += 1
    assert sum(parts.values()) == total
    return parts


def pct(total, percent):
    return total * percent // 100


# ---------------------------------------------------------------------------
# Scenario: one product (P), one client contract (K), one sponsor, 12 months
# ---------------------------------------------------------------------------
EUR = 100  # cents

# Product P revenue per month (P launches in May).
product_revenue = [0, 0, 0, 0, 800, 1500, 2500, 3500, 4500, 5500, 6500, 7500]

# Accepted task points on product P per month, reviews included.
# A, B, C build it (Jan-Apr). C leaves the Union at the end of June.
# D joins in July and maintains it.
product_points = {
    "A": [120, 120, 120, 120, 40, 40, 40, 40, 40, 40, 40, 40],
    "B": [100, 100, 100, 100, 20, 20, 0, 0, 0, 0, 0, 0],
    "C": [80, 80, 80, 80, 30, 30, 0, 0, 0, 0, 0, 0],
    "D": [0, 0, 0, 0, 0, 0, 60, 60, 60, 60, 60, 60],
}

# Client contract K: three milestones, €12,000 each, estimated at 150 points each.
# `work` = points earned per month (month index -> {member: points}).
# Milestone 2 is delivered in June, but the client asks for changes and
# accepts and pays only in August.
client_milestones = [
    {"name": "K1", "fee": 12000, "paid": 3,   # April
     "work": {2: {"E": 50, "F": 25}, 3: {"E": 50, "F": 25}}},
    {"name": "K2", "fee": 12000, "paid": 7,   # August (delayed)
     "work": {4: {"E": 45, "B": 30}, 5: {"E": 45, "B": 30}}},
    {"name": "K3", "fee": 12000, "paid": 10,  # November
     "work": {8: {"E": 40, "F": 35}, 9: {"E": 40, "F": 35}}},
]

# Commons work (reviews outside products, governance, mentoring), points per month.
# F serves as a Steward all year.
commons_points = {"F": [10] * 12}

# Sponsor: €500/month from March.
sponsor = [0, 0, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500]

MEMBERS = ["A", "B", "C", "D", "E", "F"]


# ---------------------------------------------------------------------------
# Simulation
# ---------------------------------------------------------------------------
def simulate():
    lifetime = defaultdict(int)          # lifetime points on P
    quarter_points = defaultdict(int)    # all points earned this quarter
    pool_balance = 0
    treasury = 0
    rows = []                            # per-month money flow
    pay = defaultdict(lambda: defaultdict(int))  # pay[member][stream] = cents
    pay_by_month = defaultdict(lambda: defaultdict(int))  # [month][member]
    lifetime_by_month = []
    pool_rounds = []

    for m in range(MONTHS):
        # 1. Points accepted this month.
        for who, pts in product_points.items():
            lifetime[who] += pts[m]
            quarter_points[who] += pts[m]
        for ms in client_milestones:
            for who, p in ms["work"].get(m, {}).items():
                quarter_points[who] += p
        for who, pts in commons_points.items():
            quarter_points[who] += pts[m]
        lifetime_by_month.append(dict(lifetime))

        # 2. Product revenue: 60 / 25 / 15.
        rev = product_revenue[m] * EUR
        to_contrib = pct(rev, PRODUCT_SPLIT["contributors"])
        to_pool = pct(rev, PRODUCT_SPLIT["pool"])
        to_treasury_p = rev - to_contrib - to_pool  # 25%, absorbs rounding
        for who, c in split(to_contrib, lifetime).items():
            pay[who]["product"] += c
            pay_by_month[m][who] += c
        pool_balance += to_pool

        # 3. Client milestones paid this month: 85 / 15 by points on that milestone.
        client_in = to_members_c = 0
        for ms in client_milestones:
            if ms["paid"] != m:
                continue
            fee = ms["fee"] * EUR
            members_part = pct(fee, CLIENT_SPLIT["members"])
            pts = defaultdict(int)
            for work in ms["work"].values():
                for who, p in work.items():
                    pts[who] += p
            for who, c in split(members_part, pts).items():
                pay[who]["client"] += c
                pay_by_month[m][who] += c
            client_in += fee
            to_members_c += members_part
        to_treasury_c = client_in - to_members_c

        # 4. Sponsorship: 100% to the treasury.
        spon = sponsor[m] * EUR

        # 5. Quarter end: pay out the pool by points earned in the quarter.
        pool_paid = 0
        if m % 3 == 2:
            qpts = dict(quarter_points)
            parts = split(pool_balance, qpts)
            if not parts and pool_balance:  # nobody active: pool goes to the treasury
                treasury += pool_balance
                pool_paid = pool_balance
            for who, c in parts.items():
                pay[who]["pool"] += c
                pay_by_month[m][who] += c
                pool_paid += c
            pool_rounds.append({"q": m // 3 + 1, "pool": pool_balance,
                                "points": qpts, "parts": parts})
            pool_balance -= pool_paid
            quarter_points = defaultdict(int)

        treasury += to_treasury_p + to_treasury_c + spon

        # Conservation check: money in == money paid out + treasury in + pool change.
        money_in = rev + client_in + spon
        paid_to_members = sum(pay_by_month[m].values())
        pool_change = to_pool - pool_paid
        treasury_in = to_treasury_p + to_treasury_c + spon
        if m % 3 == 2 and pool_paid and not pool_rounds[-1]["parts"]:
            treasury_in += pool_paid
        assert money_in == paid_to_members + treasury_in + pool_change, m

        rows.append({"m": m, "rev": rev, "contrib": to_contrib, "pool_in": to_pool,
                     "treasury_p": to_treasury_p, "client_in": client_in,
                     "client_members": to_members_c, "treasury_c": to_treasury_c,
                     "sponsor": spon, "pool_paid": pool_paid,
                     "treasury": treasury})

    # Whole-year check.
    total_in = sum(r["rev"] + r["client_in"] + r["sponsor"] for r in rows)
    total_paid = sum(sum(s.values()) for s in pay.values())
    assert total_in == total_paid + treasury + pool_balance
    return rows, pay, pay_by_month, lifetime_by_month, pool_rounds, treasury, pool_balance


# ---------------------------------------------------------------------------
# Markdown output
# ---------------------------------------------------------------------------
def eur(cents):
    return "—" if cents == 0 else f"€{cents / 100:,.2f}".replace(".00", "")


def table(head, body):
    out = ["| " + " | ".join(head) + " |", "|" + "|".join("---:" if i else "---" for i in range(len(head))) + "|"]
    out += ["| " + " | ".join(str(c) for c in row) + " |" for row in body]
    return "\n".join(out)


# How points are earned: a few tasks from product P.
# estimate = agreed before work starts; final = after an open re-estimate (if any);
# hours = time actually spent (shown only to make the point: it doesn't count).
TASKS = [
    {"task": "Signup flow", "estimate": 20, "final": 20, "by": "C", "hours": 18, "reviewer": "A"},
    {"task": "Billing integration", "estimate": 40, "final": 50, "by": "B", "hours": 52, "reviewer": "A"},
    {"task": "Landing page", "estimate": 10, "final": 10, "by": "A", "hours": 16, "reviewer": "C"},
    {"task": "Fix login bug (unplanned)", "estimate": None, "final": 3, "by": "B", "hours": 3, "reviewer": None},
]


def task_points():
    earned = defaultdict(int)
    body = []
    for t in TASKS:
        review = t["final"] * REVIEW_SHARE // 100 if t["reviewer"] else 0
        earned[t["by"]] += t["final"]
        if review:
            earned[t["reviewer"]] += review
        est = "— (1 pt/hour)" if t["estimate"] is None else (
            str(t["estimate"]) if t["estimate"] == t["final"] else f"{t['estimate']} → {t['final']}")
        body.append([t["task"], est, t["hours"], f"{t['by']}: {t['final']}",
                     f"{t['reviewer']}: {review}" if review else "—"])
    return body, earned


def main():
    rows, pay, pay_by_month, lifetime_by_month, pool_rounds, treasury, pool_left = simulate()

    print("### How points are earned\n")
    body, earned = task_points()
    print(table(["Task", "Estimate", "Hours spent", "Points to doer", "Points to reviewer"], body))
    print("\nTotals: " + ", ".join(f"{w} {p}" for w, p in sorted(earned.items())) + "\n")

    print("### Product P: lifetime points and contributor shares\n")
    body = []
    for m in (3, 5, 11):
        lt = lifetime_by_month[m]
        tot = sum(lt.values())
        body.append([f"End of {MONTH_NAMES[m]}"] +
                    [f"{lt.get(w, 0)} ({lt.get(w, 0) / tot:.1%})" for w in "ABCD"] + [tot])
    print(table(["", "A", "B", "C", "D", "Total"], body))

    print("\n### Money flow per month\n")
    body = []
    for r in rows:
        body.append([MONTH_NAMES[r["m"]], eur(r["rev"]), eur(r["contrib"]), eur(r["treasury_p"]),
                     eur(r["pool_in"]), eur(r["client_in"]), eur(r["client_members"]),
                     eur(r["treasury_c"]), eur(r["sponsor"]), eur(r["pool_paid"]),
                     eur(r["treasury"])])
    tot = lambda k: eur(sum(r[k] for r in rows))
    body.append(["**Year**", tot("rev"), tot("contrib"), tot("treasury_p"), tot("pool_in"),
                 tot("client_in"), tot("client_members"), tot("treasury_c"), tot("sponsor"),
                 tot("pool_paid"), f"**{eur(treasury)}**"])
    print(table(["Month", "P revenue", "→ contributors 60%", "→ treasury 25%", "→ pool 15%",
                 "Client paid", "→ members 85%", "→ treasury 15%", "Sponsor",
                 "Pool paid out", "Treasury balance"], body))

    print("\n### Quarterly pool rounds\n")
    body = []
    for pr in pool_rounds:
        qtot = sum(pr["points"].values())
        cells = []
        for w in MEMBERS:
            p = pr["points"].get(w, 0)
            cells.append(f"{p} pts → {eur(pr['parts'].get(w, 0))}" if p else "—")
        body.append([f"Q{pr['q']}", eur(pr["pool"]), qtot] + cells)
    print(table(["Quarter", "Pool", "Points"] + MEMBERS, body))

    print("\n### What each member received in the year\n")
    body = []
    for w in MEMBERS:
        s = pay[w]
        body.append([w, eur(s["product"]), eur(s["client"]), eur(s["pool"]),
                     f"**{eur(sum(s.values()))}**"])
    body.append(["**All**"] + [eur(sum(pay[w][k] for w in MEMBERS)) for k in ("product", "client", "pool")]
                + [f"**{eur(sum(sum(pay[w].values()) for w in MEMBERS))}**"])
    print(table(["Member", "Product P (60%)", "Client K (85%)", "Pool (15%)", "Total"], body))

    print("\n### Monthly income per member\n")
    body = [[MONTH_NAMES[m]] + [eur(pay_by_month[m].get(w, 0)) for w in MEMBERS] for m in range(MONTHS)]
    print(table(["Month"] + MEMBERS, body))

    print(f"\nChecks passed: money in = paid to members + treasury + pool, every month. "
          f"Pool left after the last round: {eur(pool_left) if pool_left else '€0'}.")


def update_doc():
    """Write the tables into payouts.md between the <!-- sim:… --> markers."""
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        main()
    text = out.getvalue()
    tasks, example = text.split("### Product P: lifetime", 1)
    example = "### Product P: lifetime" + example.split("\nChecks passed")[0]
    doc = pathlib.Path(__file__).resolve().parent.parent / "payouts.md"
    md = doc.read_text()
    for name, body in (("tasks", tasks), ("example", example)):
        block = f"<!-- sim:{name} -->\n{body.strip()}\n<!-- /sim:{name} -->"
        md, n = re.subn(rf"<!-- sim:{name} -->.*?<!-- /sim:{name} -->", lambda _: block,
                        md, count=1, flags=re.S)
        assert n == 1, f"marker sim:{name} not found"
    doc.write_text(md)
    print(f"Updated {doc}")


if __name__ == "__main__":
    update_doc() if "--update-doc" in sys.argv else main()
