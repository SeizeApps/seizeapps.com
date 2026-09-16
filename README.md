# seizeapps.com

Static site for **Seize Apps**, served by GitHub Pages at https://seizeapps.com (custom domain, DNS on Cloudflare, HTTPS enforced). Pushing to `main` deploys.

## Identity

SEIZE 2026 (locked 2026-09-16): ribbon-S mark, Electric Blue `#007AFF`, Cyan `#22D3EE`, Deep Navy `#060E1F`, Stone `#E5E7EB`; SF Pro Display / SF Pro on Apple platforms, Inter elsewhere. Sources of truth live in the SeizeRepo: `brand/design-tokens.json` (v2.1), `brand/sheets/02-web-ui-system.png`, `brand/logo-masters/`. The mark here (`assets/seize-mark.png`, favicons) is cut from `01-s-mark-white-bg.png`; replace it with the SVG when the masters ship one.

## Structure

```
index.html            studio home: hero · Apps · Philosophy · Studio · Contact
apps/<slug>.html      one page per app (six): icon, lede, screenshots, what it does, privacy
privacy.html          privacy policy, one section per app (#cycle-timers … #tandem)
terms.html            terms of use
assets/site.css       the whole visual system (dark only)
assets/seize-mark.png · assets/og.jpg · favicon*.png · apple-touch-icon.png
assets/icons/*.png    app icons, 256 px, from each app's AppIcon.png
assets/shots/*.jpg    real screenshots, 600 px wide, JPEG 70, English simulator
```

The HTML is **generated**: `tools/gen_site.py` (index + app pages) and `tools/gen_legal.py` (legal pages). Edit the generators, run `python3 tools/gen_site.py && python3 tools/gen_legal.py` from the repo root, commit the output. Don't hand-edit the HTML.

## Adding an app

1. Add an entry to `APPS` in `gen_site.py` (slug, name, icon, lead developer, one-liner, tags, lede, meta, three features, privacy paragraph, screenshots).
2. Drop the icon in `assets/icons/` (256 px) and 2–4 screenshots in `assets/shots/` (600 px wide, English).
3. Add its section to `PRIVACY` in `gen_legal.py` with the same id as the slug and the "Published on the App Store by …" line.
4. Regenerate, check links, commit.

## App Store badge

Each app page carries `<a class="store-badge button" href="#" hidden>`. When the app is live, remove `hidden` and set `href="https://apps.apple.com/app/id<ASC id>"`. Nothing on the site mentions review, TestFlight or launch dates on purpose.

## Redirector

`Kasempiternal/seizeapps.com` (the old GitHub Pages URL) is a meta-refresh redirector to this domain, kept because its URL is baked into shipped builds. Don't move `index.html`, `privacy.html` or `terms.html`.
