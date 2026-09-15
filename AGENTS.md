# pigsfly.ai — master agent

You are operating in **this folder**. You own the public site: information architecture, navigation, visual design, and GitHub Pages. Sibling repo `../rainbowmoon` only supplies the Rainbow page **content**.

Live site: https://pigsfly.ai/  
Repo: `jontis/pigsfly` (`main`, Pages from root). Domain DNS stays at GoDaddy; do not reattach Website Builder.

## Routes

| URL | Files | Owner |
| --- | --- | --- |
| `/` | `index.html` | this repo |
| `/contact-us/` | `contact-us/index.html` | this repo |
| `/rainbow/` | `rainbow/index.html` (assembled) | chrome here; article from rainbowmoon |
| 404 | `404.html` | this repo |

Nav on every chrome page: **Home · Rainbow · Contact Us** in the left sidebar. Keep those three in sync. Contact is https://x.com/DrJonAI — no mail form.

## Design

Tokens and chrome live in `assets/css/styles.css` and the HTML sidebars (Cabin + Lato, green `#67b858`, black ground, left nav). Change look-and-feel here, not in rainbowmoon.

Rainbow **content** arrives as `rainbow/article.html` (an `<article class="rainbow-article">`, plus Plotly). Wrap it with site chrome by running:

```bash
python3 scripts/assemble-rainbow.py
```

That writes `rainbow/index.html`. Do not hand-edit `rainbow/index.html` as the source of truth — edit the assembler and CSS, then reassemble. Do not restyle charts inside rainbowmoon.

`rainbow/status.json` is data from rainbowmoon; leave it.

## Do not

- Edit `../rainbowmoon` models, Streamlit UI, or `publish.py` chrome.
- Put a second landing page inside `rainbow/`.
- Host Streamlit on GitHub Pages.

## Publish the website

Commit this tree and `git push origin main`. Pages deploys from `main` `/`.
