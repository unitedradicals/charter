# Reputation

*v0.1 draft.* Reputation determines **vote weight bonus** (see [Voting](voting.md)) and informs **revenue share** (see [Economic model](../economics/model.md)).

## Principles
- **Earned by delivery, not by talk.** Shipping, reviewing, supporting, and selling count. Posting opinions does not.
- **Transparent.** Every member's score and how it was earned is visible to all members.
- **Decays.** Influence reflects *recent* contribution so power can't be banked forever.
- **Capped.** Reputation grants at most +1.0 vote weight.

## Earning (initial point table — [placeholder])

| Activity | Points |
|---|---|
| Merged pull request (scaled by size/complexity, reviewed) | 1–10 |
| Code review that leads to merge | 1–3 |
| Shipped milestone (split among team) | 20 |
| Leading a project through a milestone | 10 |
| Closing a client contract / sponsor deal | 10–30 |
| Delivering billable client work | 1 per 10 billable hours |
| Mentoring, documentation, community support | 1–5 (approved by a Lead or Steward) |
| Serving a Steward term | 15 |

Points are logged by Project Leads and Stewards, and are open to challenge by any member within 14 days.

## Decay
- Points older than **12 months [placeholder]** count at 50%; older than 24 months, they expire for voting purposes.
- Revenue share accounting uses its own ledger (see economics) and does **not** decay retroactively — earned money stays earned.

## From points to vote weight
```
reputation_bonus = min(active_points / P_max, 1.0)
```
where `P_max` is the **90th-percentile** of active points across Active members, recalculated monthly. This keeps the scale relative as the Union grows.

## Gaming safeguards
- PR points require review by someone other than the author.
- Leads cannot award points to themselves.
- Stewards audit anomalies; abuse is a Code of Conduct violation.
