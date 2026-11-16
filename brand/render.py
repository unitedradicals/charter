#!/usr/bin/env python3
"""Render the United Radicals brand PNGs (avatars, wordmarks, social covers).

Needs Google Chrome installed. Usage:  python3 brand/render.py
Output goes to brand/png/. Edit the ASSETS list to add or resize assets.
"""
import pathlib
import subprocess
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "png"
FONTS = HERE / "fonts"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

INK = "#1A1D3A"
PAPER = "#FCFCFB"
MARIGOLD = "#E0A100"        # on light backgrounds
MARIGOLD_BRIGHT = "#F0B429" # on dark backgrounds
SLATE_ON_INK = "#A3A8C3"

BASE_CSS = f"""
@font-face {{ font-family: Bricolage; src: url('{(FONTS / "bricolage-grotesque-latin-wght-normal.woff2").as_uri()}'); font-weight: 200 800; }}
@font-face {{ font-family: Figtree; src: url('{(FONTS / "figtree-latin-wght-normal.woff2").as_uri()}'); font-weight: 300 900; }}
* {{ box-sizing: border-box; margin: 0; }}
html, body {{ width: 100%; height: 100%; }}
body {{ font-family: Figtree, sans-serif; overflow: hidden; }}
"""

MARK_PATH = "M6 38 L16 32 L27 54 L41 10 H60"


def avatar(bg, fg):
    return f"""<body style="background:{bg}">
<svg viewBox="-17 -16 96 96" width="100%" height="100%">
  <path d="{MARK_PATH}" fill="none" stroke="{fg}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
</svg></body>"""


def wordmark(text_color, mark_color):
    # The radical's bar runs from the mark over the name, as in the site header.
    return f"""<body style="background:transparent; display:grid; place-items:center">
<div style="display:flex; align-items:stretch; font-family:Bricolage; font-weight:700; font-size:220px; line-height:1; letter-spacing:-0.01em; color:{text_color}">
  <svg viewBox="0 0 20 30" preserveAspectRatio="none" style="width:170px; height:270px; overflow:visible; flex:none">
    <path d="M1.5 18 L6 15.5 L11 28 L18.5 1.5" fill="none" stroke="{mark_color}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
  </svg>
  <span style="position:relative; padding:48px 10px 0 34px; height:270px">
    <span style="position:absolute; top:0; left:-13px; right:0; height:27px; border-radius:0 27px 27px 0; background:{mark_color}"></span>United Radicals</span>
</div></body>"""


def cover(headline, sub, size, align="center", pad="0", stroke=10):
    """A radical sign over the headline, on ink. `align` places the block horizontally."""
    justify = {"center": "center", "right": "end", "left": "start"}[align]
    hook_w = round(size * 0.55)
    sub_html = (
        f'<p style="margin-top:{round(size*0.42)}px; margin-left:{hook_w + round(size*0.25)}px; '
        f'font-size:{round(size*0.3)}px; color:{SLATE_ON_INK}; font-weight:500; letter-spacing:0.01em">{sub}</p>'
        if sub else ""
    )
    return f"""<body style="background:{INK}; display:grid; align-content:center; justify-content:{justify}; padding:{pad}">
<div>
  <div style="display:grid; grid-template-columns:{hook_w}px max-content">
    <svg viewBox="0 0 40 100" preserveAspectRatio="none" style="width:100%; height:100%; overflow:visible">
      <path d="M0 58 L13 50 L24 100 L40 0" vector-effect="non-scaling-stroke" fill="none" stroke="{MARIGOLD_BRIGHT}" stroke-width="{stroke}" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
    <div style="position:relative; padding:{round(size*0.32)}px {round(size*0.2)}px 4px {round(size*0.25)}px">
      <span style="position:absolute; top:-{stroke/2}px; left:0; right:0; height:{stroke}px; border-radius:0 {stroke}px {stroke}px 0; background:{MARIGOLD_BRIGHT}"></span>
      <h1 style="font-family:Bricolage; font-weight:700; font-size:{size}px; line-height:1.04; letter-spacing:-0.02em; color:{PAPER}">{headline}</h1>
    </div>
  </div>
  {sub_html}
</div></body>"""


TAGLINE = "They deprecated us.<br>We united."
TAGLINE_1 = "They deprecated us. We united."
SUB = "A worker-owned collective of software engineers &nbsp;/&nbsp; unitedradicals.com"

ASSETS = [
    # name, width, height, html, transparent
    ("avatar-dark", 1024, 1024, avatar(INK, MARIGOLD_BRIGHT), False),
    ("avatar-light", 1024, 1024, avatar(PAPER, INK), False),
    ("wordmark-on-light", 2400, 520, wordmark(INK, MARIGOLD), True),
    ("wordmark-on-dark", 2400, 520, wordmark(PAPER, MARIGOLD_BRIGHT), True),
    # X header: the avatar overlaps the bottom-left, so the block sits right.
    ("cover-x-1500x500", 1500, 500, cover(TAGLINE, "unitedradicals.com", 82, "right", "0 110px 0 0"), False),
    # LinkedIn cover is very thin, and the logo overlaps the left on desktop.
    ("cover-linkedin-1128x191", 1128, 191, cover(TAGLINE_1, "", 46, "right", "0 70px 0 0", 6), False),
    # Facebook crops the sides on mobile: keep it centred.
    ("cover-facebook-1640x624", 1640, 624, cover(TAGLINE, "unitedradicals.com", 96, "center"), False),
    # Reddit banner: wide and thin, centred.
    ("cover-reddit-1920x384", 1920, 384, cover(TAGLINE_1, "", 74, "center", "0", 8), False),
    # Discord server banner (shown only with boost level 2) and invite splash.
    ("cover-discord-960x540", 960, 540, cover(TAGLINE, "unitedradicals.com", 66, "center", "0", 8), False),
    # Link previews when unitedradicals.com is shared.
    ("og-1200x630", 1200, 630, cover("Software, owned<br>by the people<br>who build it.", SUB, 72, "left", "0 0 0 90px", 9), False),
]


def main():
    OUT.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        for name, w, h, body, transparent in ASSETS:
            page = pathlib.Path(tmp) / f"{name}.html"
            page.write_text(f"<!doctype html><html><head><meta charset='utf-8'><style>{BASE_CSS}</style></head>{body}</html>")
            args = [
                CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                "--force-device-scale-factor=1", f"--window-size={w},{h}",
                "--virtual-time-budget=3000", f"--screenshot={OUT / (name + '.png')}",
            ]
            if transparent:
                args.append("--default-background-color=00000000")
            subprocess.run(args + [page.as_uri()], check=True, capture_output=True)
            print("rendered", name)


if __name__ == "__main__":
    main()
