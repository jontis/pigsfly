# pigsfly.ai

Static site for [pigsfly.ai](https://pigsfly.ai/), meant for **GitHub Pages**.

Agent rules: [`AGENTS.md`](AGENTS.md). Rainbowmoon content: `../rainbowmoon/AGENTS.md`.

## Local

```bash
python3 -m http.server 8080
```

Open http://localhost:8080/

## Pages

- `/` — flying-pig hero and GKMK sponsor
- `/rainbow/` — BTC rainbow snapshot (from Rainbowmoon `publish`)
- `/contact-us/` — [ @DrJonAI ](https://x.com/DrJonAI)

## Refresh the rainbow chart

From the Rainbowmoon repo (writes `site/` there and `rainbow/article.html` here, then assembles chrome):

```bash
uv run rainbowmoon publish --out site
```

Or only wrap existing `rainbow/article.html`:

```bash
python3 scripts/assemble-rainbow.py
```

Commit and push this repo. There is no live price feed on Pages.

## GitHub Pages

Public repo: `jontis/pigsfly` (confirm the GitHub login). Source: `main` branch, **root** (not `/docs`).

1. Create the repo and push this tree.
2. Settings → Pages → Deploy from `main` / `/`.
3. Custom domain: `pigsfly.ai` (this repo already has a `CNAME` file).
4. After DNS works, enable **Enforce HTTPS**.

Add the custom domain in the repo **before** pointing GoDaddy DNS.

## GoDaddy DNS

Remove Website Builder records (`A` 13.248.243.5 and 76.223.105.230). Then:

```
A     @    185.199.108.153
A     @    185.199.109.153
A     @    185.199.110.153
A     @    185.199.111.153
AAAA  @    2606:50c0:8000::153
AAAA  @    2606:50c0:8001::153
AAAA  @    2606:50c0:8002::153
AAAA  @    2606:50c0:8003::153
CNAME www  jontis.github.io
```

Leave MX alone unless you are changing mail.

Until DNS is flipped, the site is `https://jontis.github.io/pigsfly/`.

## Graphics to replace later

- `assets/images/pigsfly_hero.jpg`
- `assets/images/gkmk_logo.jpg`
- `assets/images/favicon-512.png` (and the 192 / 32 / `.ico` variants)
