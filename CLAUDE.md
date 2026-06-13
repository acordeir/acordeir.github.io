# Project: Personal Website

## Overview
Building a personal website hosted on GitHub Pages with a custom domain purchased from Porkbun.

## Tech Stack
- **Static site framework:** Astro
- **Content:** Python (scripting/data), LaTeX (math notation)
- **Hosting:** GitHub Pages (free, no separate hosting needed)
- **Domain:** Purchased from Porkbun — DNS CNAME points to GitHub Pages, SSL via Let's Encrypt

## Planned Site Sections
1. **Math notes** — an online mathematical statistics textbook
2. **Data science & statistics simulations** — interactive apps and visualizations; possibly fun games (inspired by neal.fun)
3. **GenAI playground** — connect to a headless server running a GenAI harness
4. **Buy me a coffee** — donation link

## Inspirations
- https://brianmcfee.net/dstbook-site/content/intro.html
- https://neal.fun
- Paul's Online Math Notes

## Architecture Notes
- GitHub Pages only serves static content — the Astro site covers the textbook, simulations, and static pages
- The Python backend and GenAI server connection will be added later; options include Fly.io, Railway, or Render for a lightweight backend, or proxying directly to the headless server from the client
- Math rendering: likely KaTeX or MathJax for the web, with LaTeX source files for authoring

## Setup Steps (in progress)
- [ ] Scaffold Astro project
- [ ] Set up GitHub Actions deploy workflow for GitHub Pages
- [ ] Configure Porkbun DNS (CNAME `www` → `yourusername.github.io`)
- [ ] Add custom domain in GitHub repo Pages settings
- [ ] Build initial site layout and navigation
