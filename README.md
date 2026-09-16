# seizeapps.com

Static site of **Seize Apps** (Izotz Cristobal Mota & Sendoa Sola), served by GitHub Pages
at **https://seizeapps.com** (custom domain; DNS at Cloudflare, DNS-only records → GitHub Pages;
HTTPS enforced). `www.seizeapps.com` and `seizeapps.github.io/seizeapps.com` redirect here.
The old `kasempiternal.github.io/seizeapps.com` repo is a redirector and must stay up while any
shipped build still embeds that URL.

## Pages

| Path | What |
|---|---|
| `index.html` | Studio home: hero, apps portfolio, how we build, studio, contact |
| `apps/<slug>.html` | One page per app (icon, real screenshots, what it does, privacy summary, publisher) |
| `privacy.html` | Privacy policy, one section per app (`#cycle-timers`, `#drip`, `#anchor`) — linked from inside the apps and from App Store Connect; keep it truthful before every release |
| `terms.html` | Terms of use |
| `assets/site.css` | Shared stylesheet (index + app pages; legal pages keep their own) |
| `assets/icons/*.png` | App icons, 256 px, exported from each app's `AppIcon.png` |
| `assets/shots/*.jpg` | Real simulator screenshots (iPhone 6.9″, 1200 px tall, JPEG ~70) |

## Adding an app / turning on the App Store badge

1. Export the icon (`sips -Z 256 AppIcon.png -o assets/icons/<slug>.png`) and 3–4 English
   screenshots (`sips -Z 1200 shot.png -s format jpeg -s formatOptions 72`).
2. Add a card in `index.html` (`.app-card`) and a page `apps/<slug>.html` (copy `drip.html`).
3. Add the app's section to `privacy.html` with its publisher line.
4. When the app is live (`https://itunes.apple.com/lookup?bundleId=…` returns it), remove
   `hidden` from the `.store-badge` link on its page and set `href="https://apps.apple.com/app/id<ASC id>"`.
   ASC ids: Drip 6812332005, Anchor 6812615752.

No build step, no framework: edit HTML, push to `main`, Pages deploys in about a minute.
