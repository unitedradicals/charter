# Voting

*v0.1 draft. Values marked **[placeholder]** are to be confirmed at ratification.*

## The hybrid model

Pure "one person, one vote" is simple but easy to brigade and disconnected from who does the work. Pure meritocracy concentrates power. We combine both:

```
vote_weight = 1 + min(reputation_bonus, 1.0)
```

- **Base vote = 1** for every Active member. Everyone has a voice.
- **Reputation bonus = 0 to 1.0**, earned through contribution (see [Reputation](reputation.md)).
- **Maximum weight = 2×.** The most prolific contributor can never outweigh two newcomers.

## Vote types

| Type | Threshold | Quorum (of Active members) | Duration |
|---|---|---|---|
| **Standard** (proposals, contracts, policies) | > 50% weighted | 20% [placeholder] | 7 days |
| **Constitutional** (Charter amendments, removing Stewards) | ≥ ⅔ weighted | 30% [placeholder] | 14 days |
| **Election** (Stewards Council) | Ranked-choice | 20% [placeholder] | 7 days |

If quorum is not reached, the vote fails and the proposal may be resubmitted after **30 days [placeholder]**.

## Voting options

- **Yes** / **No** / **Abstain** (abstain counts toward quorum, not toward the threshold)
- Members may change their vote until the voting window closes.
- Every vote must be cast by the member personally; no proxies in v0.1.

## Anti-abuse rules

1. **Membership age:** members can vote only after **14 days [placeholder]** of membership — prevents sign-up brigading.
2. **Identity:** one person, one account. Verified via a lightweight check (e.g., linked GitHub/LinkedIn with history) **[to be decided]**.
3. **Conflict of interest:** members with a financial stake outside the Union in a decision must declare it.
4. **Transparency:** individual votes are public to members after the window closes.

## Tooling

- **Phase 0–1:** GitHub Discussions polls or an existing tool (e.g., Loomio, Decidim) with weights computed manually by Stewards from the published reputation table.
- **Phase 2:** a custom Union platform that computes weights automatically (candidate first project — see [Roadmap](../roadmap.md)).
