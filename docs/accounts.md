# Accounts & ownership

Every official account, who controls it, and which email it's tied to. **No passwords or 2FA codes in this file. Ever.** Credentials live in the Stewards' password manager.

*Last updated: after 2026-11-16 (website and signup launch)*

## Rules
1. Official logins use `@unitedradicals.com` addresses, so they belong to the Union rather than to a person.
2. Where a platform requires a personal profile as admin (LinkedIn, Facebook), keep **at least 2 admins**.
3. Every account has **2FA enabled**.
4. When the legal entity is formed, or the Stewards Council changes, review this list and transfer ownership.

## Email (Zoho Mail, free plan)
| Address | Type | Purpose |
|---|---|---|
| `admin@unitedradicals.com` | Mailbox | Account sign-ups, recovery, DMARC reports |
| `hello@unitedradicals.com` | Alias | Public contact |
| `stewards@unitedradicals.com` | Alias | Governance, Code of Conduct reports |

## Domains
| Domain | Registrar | DNS | Expires | Auto-renew |
|---|---|---|---|---|
| unitedradicals.com | AWS Route 53 | Cloudflare | 2027-11-15 | On |
| unitedradicals.org | Cloudflare | Cloudflare (301 redirect to .com) | 2027-11-15 | On |
| unitedradicals.dev | Cloudflare | Cloudflare (301 redirect to .com) | 2027-11-15 | On |

Registrar accounts (AWS, Cloudflare) are currently held by the founder. Move them to `admin@`, or add it as a member, before the first Stewards election.

## Platforms
| Platform | URL | Login / owner | Notes |
|---|---|---|---|
| GitHub | [github.com/unitedradicals](https://github.com/unitedradicals) | Organization; contact email `admin@` | Owned by the founder's GitHub account. Add a second owner. |
| X | [x.com/unitedradicals](https://x.com/unitedradicals) | `admin@` | Standalone brand account. |
| Reddit | [r/unitedradicals](https://www.reddit.com/r/unitedradicals/) | Created by the founder's personal account; moderated by [u/unitedradicals](https://www.reddit.com/user/unitedradicals) (`admin@`) | Launch posts in other subreddits come from personal accounts, not the brand account. |
| Discord | [unitedradicals.com/discord](https://unitedradicals.com/discord) | Server owner: `admin@` | Always link to unitedradicals.com/discord: it redirects to the current invite (set in the website's `public/_redirects`). If the invite changes, update only that file. The invite itself is created on `#start-here` and never expires. The private `#signups` channel receives Tally signups through the Tally bot, which can only see that channel. |
| LinkedIn | [linkedin.com/company/unitedradicals](https://www.linkedin.com/company/unitedradicals) | Company page managed by the founder's personal profile | LinkedIn pages have no separate login. Add a second admin. |
| Facebook | [facebook.com/UnitedRadicals](https://www.facebook.com/UnitedRadicals/) | Page managed by the founder's personal profile; public contact `hello@` | Add a second admin. |

## Website & tools
| Service | What | Login / owner | Notes |
|---|---|---|---|
| Cloudflare Workers | Hosts unitedradicals.com (Worker `unitedradicals-website`) | Founder's Cloudflare account | Deploys automatically from [unitedradicals/website](https://github.com/unitedradicals/website) on every push to `main`. |
| Tally | Founding member signup form (`VpPElN`) | `admin@` | Notifications go to `admin@` and Discord `#signups`. Holds members' personal data (see the [privacy policy](https://unitedradicals.com/privacy)). |
| Zoho Mail | Email for unitedradicals.com | `admin@` | Free plan. |

## Open items
- [x] Confirm expiry dates and turn on auto-renew for all domains
- [ ] Add second admins/owners on GitHub, LinkedIn and Facebook (once a trusted co-founder or Steward exists)
- [x] Add the Discord invite link
- [ ] Move the registrar accounts to `admin@`
