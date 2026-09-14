#!/usr/bin/env python3
"""Wrap rainbow/article.html in pigsfly.ai chrome. Design lives here."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARTICLE = ROOT / "rainbow" / "article.html"
OUT = ROOT / "rainbow" / "index.html"

_ARTICLE_RE = re.compile(r"<article\b[^>]*>.*?</article>", re.I | re.S)


def _article_html(raw: str) -> str:
    text = raw.strip()
    match = _ARTICLE_RE.search(text)
    if match:
        return match.group(0)
    return f'<article class="rainbow-article">\n{text}\n</article>'


def assemble() -> Path:
    if not ARTICLE.is_file():
        raise SystemExit(f"missing {ARTICLE} — run: uv run rainbowmoon publish")
    article = _article_html(ARTICLE.read_text(encoding="utf-8"))
    title_match = re.search(r"<h1>(.*?)</h1>", article, re.I | re.S)
    title = re.sub(r"<[^>]+>", "", title_match.group(1)).strip() if title_match else "Rainbow"
    page = f"""<!DOCTYPE html>
<html lang="en-GB">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{title} | pigsfly.ai</title>
    <meta name="author" content="pigsfly.ai" />
    <meta name="theme-color" content="#67b858" />
    <link rel="icon" href="../assets/images/favicon.ico" sizes="32x32" />
    <link rel="icon" href="../assets/images/favicon-192.png" type="image/png" sizes="192x192" />
    <link rel="apple-touch-icon" href="../assets/images/favicon-512.png" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Cabin:wght@700&family=Lato:ital,wght@0,300;0,400;0,700;1,400&display=swap"
      rel="stylesheet"
    />
    <link rel="stylesheet" href="../assets/css/styles.css" />
  </head>
  <body>
    <header class="site-header site-header--solid">
      <div class="header-inner">
        <a class="logo" href="../index.html">pigsfly.ai</a>
        <nav class="nav" aria-label="Primary">
          <a class="nav-link" href="../index.html">Home</a>
          <a class="nav-link is-active" href="./">Rainbow</a>
          <a class="nav-link" href="../contact-us/">Contact Us</a>
        </nav>
        <button
          class="menu-toggle"
          type="button"
          aria-label="Open menu"
          aria-expanded="false"
          data-drawer-open
        >
          <svg width="28" height="28" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
            <path d="M3 6h18v2H3V6zm0 5h18v2H3v-2zm0 5h18v2H3v-2z" />
          </svg>
        </button>
      </div>
    </header>

    <div class="mobile-drawer" data-drawer aria-hidden="true">
      <div class="drawer-backdrop" data-drawer-close></div>
      <div class="drawer-panel" role="dialog" aria-label="Site menu">
        <button class="drawer-close" type="button" aria-label="Close menu" data-drawer-close>
          <svg width="32" height="32" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
            <path d="M18 6.4 17 5.4 12 10.4 7 5.4 6 6.4 11 11.4 6 16.4 7 17.4 12 12.4 17 17.4 18 16.4 13 11.4z" />
          </svg>
        </button>
        <nav class="drawer-nav">
          <a href="../index.html">Home</a>
          <a href="./">Rainbow</a>
          <a href="../contact-us/">Contact Us</a>
        </nav>
      </div>
    </div>

    <main class="rainbow-page">
      {article}
    </main>

    <footer class="site-footer">
      <p>Copyright © 2021 pigsfly.ai - All Rights Reserved.</p>
    </footer>

    <aside class="cookie" data-cookie hidden>
      <h2>This website uses cookies.</h2>
      <p>
        We use cookies to analyze website traffic and optimize your website experience. By
        accepting our use of cookies, your data will be aggregated with all other user data.
      </p>
      <div class="cookie-actions">
        <button type="button" data-cookie-choice="decline">Decline</button>
        <button type="button" class="cookie-accept" data-cookie-choice="accept">Accept</button>
      </div>
    </aside>

    <script src="../assets/js/main.js"></script>
  </body>
</html>
"""
    OUT.write_text(page, encoding="utf-8")
    return OUT


if __name__ == "__main__":
    path = assemble()
    print(f"wrote {path}", file=sys.stderr)
