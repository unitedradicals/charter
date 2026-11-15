# Proposal lifecycle

*v0.1 draft.* How an idea becomes a shipped product (or gets retired).

```
 Idea ──▶ Backed ──▶ Voting ──▶ Approved ──▶ Planning ──▶ Building ──▶ Shipped
   │         │          │                        │            │           │
   ▼         ▼          ▼                        ▼            ▼           ▼
 Expired  Expired    Rejected                 Stalled ◀──── Stalled    Retired
```

## Stages

### 1. Idea
- Any member opens a proposal using the [proposal template](../../.github/ISSUE_TEMPLATE/proposal.md).
- Must cover: problem, solution, target users, **revenue path**, rough effort, skills needed.
- Discussion is open to all members.
- **Expires** after **30 days [placeholder]** without reaching Backed.

### 2. Backed
- Reaches **5 committed backers [placeholder]** — members who pledge real hours (e.g., ≥ 5 h/week) if it is approved.
- Commitment is the filter: popular-but-unstaffed ideas don't reach a vote.
- The author (or a backer) volunteers as **prospective Project Lead**.

### 3. Voting
- A **Standard vote** per [Voting](voting.md): 7 days, > 50% weighted, 20% quorum.
- **Rejected** proposals may be revised and resubmitted after 30 days.

### 4. Approved
- Backers confirm the **Project Lead**.
- Project gets a channel, a repository, and a slot on the public project board.

### 5. Planning (≤ 2 weeks)
- The team produces a short plan: MVP scope, milestones, roles, and a **first-revenue target**.
- Plan is published to members; no second vote needed unless scope changes materially.

### 6. Building
- The team self-organizes. Maintainers own technical decisions; the Lead owns delivery.
- Monthly public status update (progress, blockers, hours contributed).
- Members can join an active project by agreement with the Lead.
- **Stalled:** no meaningful progress for **60 days [placeholder]** → Stewards check in; the team either recovers, reduces scope, or the project is retired.

### 7. Shipped
- Product is live and (ideally) earning. Revenue flows per the [economic model](../economics/model.md).
- Ongoing maintenance stays with the team; contributors keep earning reputation.

### 8. Retired
- Products that are unprofitable or abandoned can be retired by a Standard vote. Code and learnings remain Union property and may be reused.

## Rules of thumb
- **Scope small.** Proposals targeting an MVP in ≤ 3 months are strongly preferred.
- **Revenue path required.** "We'll figure out monetization later" is not accepted for product proposals (internal tooling for the Union itself is the exception).
- **Max concurrent projects** per member: **2 [placeholder]**, to prevent overcommitment.
