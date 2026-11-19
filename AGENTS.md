# AGENTS.md: charter repo

Guidance for AI coding agents (Claude Code, Codex, Cursor, Copilot…) working in this repository. Humans: start with [README.md](README.md) and [CONTRIBUTING.md](CONTRIBUTING.md).

## What this repo is
The **founding documents of United Radicals**, a worker-owned co-op of software engineers displaced by AI. Members propose products, vote on what to build, build in small teams and share the revenue. This repo is **public**. It holds the rules (Charter), the vision (Manifesto), governance and economics docs, and brand assets. GitHub Discussions on this repo are the **official membership record** and where proposals and votes happen.

Everything is a **v0.1 draft**. Values marked **[placeholder]** are set by founding members in the [Founding round](docs/founding-round.md) (ratification vote Dec 7–13, 2026).

## The United Radicals repos
| Repo | Visibility | What |
|---|---|---|
| `unitedradicals/charter` (this one) | public | Founding docs, governance, brand assets, Discussions |
| `unitedradicals/website` | private | unitedradicals.com (Astro, Cloudflare Workers) |
| `unitedradicals/ops` | private | Stewards' working files: launch plan, templates, drafts |
| `unitedradicals/.github` | public | Org profile page (`profile/README.md`) |

## Map
| Path | Contents |
|---|---|
| `MANIFESTO.md` | Why we exist, beliefs. **Mirrored on the website** (see below) |
| `CHARTER.md` | The constitution: membership, roles, decisions, amendments, ratification |
| `CONTRIBUTING.md` | How to join, propose, back a proposal |
| `docs/governance/` | `voting.md`, `proposal-lifecycle.md`, `reputation.md` |
| `docs/economics/` | `model.md` (revenue splits), `ip-and-licensing.md`, `legal-entity-options.md` |
| `docs/founding-round.md` | Founding round timeline (Nov 23 – Dec 2026) |
| `docs/roadmap.md`, `docs/open-questions.md` | Phases and unresolved decisions |
| `docs/brand.md` | Name, logo rules, colors, typography, **voice**. Read before writing copy |
| `docs/accounts.md` | Which accounts exist and who owns them. **No secrets** |
| `brand/` | Logo SVG, fonts, PNG renders; `python3 brand/render.py` regenerates PNGs (needs Google Chrome) |
| `.github/ISSUE_TEMPLATE/proposal.md` | Proposal template |

## Rules
1. **Governance docs change through pull requests**, never by pushing to `main`. That covers the Manifesto, Charter, governance, economics and the founding round. Members review and comment there. When the idea came from a member, credit them by GitHub handle in the commit and the PR. Typo fixes and agent/tooling files may go straight to `main`.
2. **Keep numbers consistent.** A value such as the backer threshold (5), quorum (20% or 30%), vote duration (7 or 14 days), the 2× vote cap or the revenue splits (60/25/15 for products, 85/15 for client work) appears in several files: `CHARTER.md`, `docs/governance/*`, `docs/economics/model.md`, `docs/founding-round.md`, `CONTRIBUTING.md`, `docs/open-questions.md`. Change one, grep for and change all. Keep **[placeholder]** until a value is ratified.
3. **The Manifesto lives in two places.** When `MANIFESTO.md` changes, apply the same edit to `src/content/manifesto.md` in the website repo. The two files are identical except for the italic draft note on line 3.
4. **Links:**
   - Discord: always `https://unitedradicals.com/discord`, never a raw `discord.gg` invite, because invites change.
   - Joining: `https://unitedradicals.com/#join`, then Discussion #1 (the introduction template).
   - Site pages use trailing slashes, e.g. `/manifesto/`.
5. **Voice** (`docs/brand.md`):
   - Direct, warm, plain words. No hype and no corporate filler.
   - Sentence case. "We" for the Union, "you" for the reader.
   - Write "United Radicals" in text. "United √adicals" is for display and logo contexts only.
   - "Radical" is about how software is built and owned. No partisan politics.
6. **Never name members' former employers.** Say "our office in Sofia" or "a large tech company". Severance agreements and NDAs may apply.
7. **No personal data** in this public repo: no personal emails, signup data or member details beyond what members post themselves.
8. **Don't edit members' Discussions posts.** Introductions are the membership record.

## GitHub
- Discussion categories: Announcements, General, Ideas, Polls, Q&A, Show and tell, **Introductions** (membership record), **Proposals**.
- Labels: `proposal`, `charter`, `stage:idea|backed|voting|approved|planning|building|shipped|stalled|rejected|expired|retired`.
- The `gh` CLI works for issues, PRs and Discussions (GraphQL). Pinning a discussion can't be done through the API; a maintainer does it in the web UI.
- Posting anything public (Discussions, comments, PRs) speaks for the Union. Do it only when a maintainer has asked for it.

## Commits
Short imperative subject, e.g. "Manifesto: add the directness argument". Explain the why in the body when it isn't obvious.
