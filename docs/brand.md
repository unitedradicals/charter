# Brand

*v0.1 draft.*

## Name
**United Radicals**. In text, write it as "United Radicals". Use **United √adicals** only in display and logo contexts. In these documents, "the Union" is shorthand for United Radicals.

## Why "Radicals"
The name is meant to be read in several ways, all of them intended:

| Meaning | What it says about us |
|---|---|
| **√ — a root in math** | We go back to fundamentals. We have *root access*: we own the system. |
| **Latin *radix*, "root"** | Rebuilding software from its roots, better than what exists. |
| **Free radicals (chemistry)** | Independent, energetic, reacting with everything around them. |
| **"Radical!" (90s slang)** | Awesome. We build software people love. |
| **United** | A worker-owned union. Together, not alone. |

## Positioning guardrail
"Radical" also has political connotations. We are **radical about how software is built and owned**, not a political movement. To keep that clear:
- Always show the tech meaning: use the √ mark and pair the name with a software tagline.
- Keep the visual identity clean and professional. The edge comes from confidence, not aggression.
- Stay out of partisan politics in official channels. Members from all backgrounds are welcome.

## Taglines (drafts)
- **They deprecated us. We united.** *(primary)*
- Radical software. Owned by those who build it.
- Back to the roots. Forward together.
- Every orphaned process gets adopted.

## Domains & handles
- unitedradicals.com (primary). unitedradicals.org and unitedradicals.dev redirect to it.
- `unitedradicals` on GitHub, Reddit, X, LinkedIn, Discord and Facebook (see [Accounts](accounts.md))

## Logo
The logo is the **√ sign**, whose bar extends over whatever it shelters: the name, a headline, the community. That one idea runs through every asset.

| Asset | File | Use it for |
|---|---|---|
| Mark (vector) | [`brand/logo-mark.svg`](../brand/logo-mark.svg) | Favicons, stickers, anywhere small |
| Avatar, dark | [`brand/png/avatar-dark.png`](../brand/png/avatar-dark.png) (1024²) | **Default profile picture** on every platform |
| Avatar, light | [`brand/png/avatar-light.png`](../brand/png/avatar-light.png) (1024²) | Where a light avatar fits better |
| Wordmark on light | [`brand/png/wordmark-on-light.png`](../brand/png/wordmark-on-light.png) | Documents, slides and partner pages on white |
| Wordmark on dark | [`brand/png/wordmark-on-dark.png`](../brand/png/wordmark-on-dark.png) | Dark slides and videos |

**Rules**
- Keep the mark at least **16px** tall on screen. Below about 32px, use the mark alone, without the name.
- Don't recolor, stretch, rotate, add shadows, or place the mark on a busy photo.
- Leave clear space around the logo at least as wide as the mark's short tick.
- The avatar is designed to survive circular cropping (X, Facebook, Discord, Reddit).

## Social covers
All are in [`brand/png/`](../brand/png/), sized to each platform's recommendation:

| Platform | File | Notes |
|---|---|---|
| X header | `cover-x-1500x500.png` | Text sits right, because the avatar covers the bottom-left |
| LinkedIn company cover | `cover-linkedin-1128x191.png` | Text sits right of the logo overlap |
| Facebook cover | `cover-facebook-1640x624.png` | Centred, because mobile crops the sides |
| Reddit banner | `cover-reddit-1920x384.png` | Centred |
| Discord banner and invite splash | `cover-discord-960x540.png` | The banner needs server boost level 2 |
| Link preview (Open Graph) | `og-1200x630.png` | Already used by unitedradicals.com |

To change or add assets, edit [`brand/render.py`](../brand/render.py) and run `python3 brand/render.py`. It needs Google Chrome.

## Colors
One accent (marigold) for the √ only, one action color (indigo), and quiet neutrals.

| Token | Light | Dark | Use |
|---|---|---|---|
| Ink | `#1A1D3A` | `#ECEDF5` | Text; dark backgrounds use `#1A1D3A` |
| Paper | `#FCFCFB` | `#15172C` | Page background |
| Slate | `#555B76` | `#A3A8C3` | Secondary text |
| Mist | `#EEF0F6` | `#1F2240` | Panels and subtle fills |
| Line | `#DCDFEA` | `#2E3258` | Borders and dividers |
| **Marigold** | `#E0A100` | `#F0B429` | **The √ sign only.** Decorative, never used for text |
| **Indigo** | `#3B4CCA` | `#8C98F5` | Links and primary buttons |

**Chart series**, in this fixed order and checked for color-blind separation: indigo `#3B4CCA` / `#6A78E6` (the people doing the work), marigold `#E0A100` / `#B8860F` (treasury), teal `#1F9A8A` / `#279E8E` (all members). A recipient keeps its color on every chart.

## Typography
| Role | Typeface | Weights | Notes |
|---|---|---|---|
| Headlines and logo | **Bricolage Grotesque** | 650 to 700 | Tight leading (1.02 to 1.1), letter-spacing −0.02em |
| Body and UI | **Figtree** | 400 to 600 | 17 to 19px on the web, line-height 1.6 |

Both are free (SIL Open Font License) and available from Google Fonts or Fontsource. Copies are in [`brand/fonts/`](../brand/fonts/). On the web, serve them from our own site, not from Google.

**Style:** sentence case for headings and buttons, no all-caps labels, and plain verbs ("Join as a founding member", not "Submit").

## Voice
Direct, warm and confident. Builders talking to builders.
- Say what things do in plain words. No hype, no corporate filler.
- Own the story without bitterness: we were let go, and now we build.
- Use "we" for the Union and "you" for the reader.
