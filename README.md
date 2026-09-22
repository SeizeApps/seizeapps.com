# seizeapps.com

Static site for **Seize Apps**, served by GitHub Pages at https://seizeapps.com (custom domain, DNS on Cloudflare, HTTPS enforced). Pushing to `main` deploys.

## Identity

SEIZE 2026 (locked 2026-09-16): ribbon-S mark, Electric Blue `#007AFF`, Cyan `#22D3EE`, Deep Navy `#060E1F`, Stone `#E5E7EB`; SF Pro Display / SF Pro on Apple platforms, Inter elsewhere. Sources of truth live in the SeizeRepo: `brand/design-tokens.json` (v2.1), `brand/sheets/02-web-ui-system.png`, `brand/logo-masters/`. The mark here (`assets/seize-mark.png`, favicons) is cut from `01-s-mark-white-bg.png`; replace it with the SVG when the masters ship one.

## Structure

```
index.html            studio home: hero · Apps · Philosophy · Work with us · Studio · Contact
apps/<slug>.html      one page per app (one per entry in `APPS`): icon, lede, screenshots, what it does, privacy
privacy.html          privacy policy, one section per app (#cycle-timers … #meso)
terms.html            terms of use
es/…                  the same four kinds of page in Spanish (same paths under es/; hreflang both ways)
assets/site.css       the whole visual system (dark only)
assets/seize-mark.png · assets/og.jpg · favicon*.png · apple-touch-icon.png
assets/icons/*.png    app icons, 256 px, from each app's AppIcon.png
assets/shots/*.jpg    real screenshots, 600 px wide, JPEG 70, English simulator
```

The HTML is **generated** by `tools/gen_site.py` (UI strings and app copy in both languages) with the legal bodies in `tools/gen_legal_copy.py` (EN) and `tools/gen_legal_es.py` (ES). Edit the generators, run `python3 tools/gen_site.py`, commit the output. Don't hand-edit the HTML. Bump `CSS_V` in `gen_site.py` whenever `site.css` changes (cache-busting: the path is shared with the previous site).

## Adding an app

1. Add an entry to `APPS` in `gen_site.py` (slug, name, icon, lead developer, screenshots, and the copy block in English and Spanish: one-liner, tags, lede, meta, three features, privacy paragraph, captions).
2. Drop the icon in `assets/icons/` (256 px) and 2–4 screenshots in `assets/shots/` (600 px wide, English).
3. Add its section to the privacy policy in both `gen_legal_copy.py` and `gen_legal_es.py`, with the same id as the slug and the "Published on the App Store by …" line.
4. Regenerate, check links, commit.

## App Store badge

El badge lo decide un dato, no una edición a mano del HTML: cada entrada de
`APPS` en `tools/gen_site.py` admite `appstore='<id de ASC>'`. Con id, la
página saca el badge; sin id, no hay badge. La URL va sin país (`https://apps.apple.com/app/id<id>`)
porque Apple redirige a la tienda del visitante.

**Solo se pone el id cuando la app está viva de verdad**, comprobado con
`curl -s "https://itunes.apple.com/lookup?id=<id>"` (resultCount 1). El sitio
no menciona revisión, TestFlight ni fechas de lanzamiento, a propósito.

Vivas a 22/09/2026: Cycle Timers (6796827400), Drip (6812332005), Kover (6812714562)
y Anchor (6812615752). Tempo y Meso, sin id hasta que `lookup` devuelva 1. Tandem
está aprobada pero **retirada de la venta** desde el 22/09/2026 (decisión de Sendoa):
sin id mientras siga retirada.

En la portada, cada tarjeta con `appstore` lleva además un icono redondo de la
Store (`.store-icon`, arriba a la derecha) que enlaza a la ficha sin pasar por la
página de la app. Es un `<a>` hermano de la tarjeta dentro de `.app-card-wrap`,
porque un enlace no puede ir dentro de otro.

## Redirector

`Kasempiternal/seizeapps.com` (the old GitHub Pages URL) is a meta-refresh redirector to this domain, kept because its URL is baked into shipped builds. Don't move `index.html`, `privacy.html` or `terms.html`.
