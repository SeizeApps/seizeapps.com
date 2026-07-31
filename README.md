# seizeapps.com

Static site for Seize Apps, served by GitHub Pages.

- Live now at: https://kasempiternal.github.io/seizeapps.com/
- Pages: `index.html`, `privacy.html`, `terms.html`

## Pointing the real domain (when ready)
1. At your DNS registrar for `seizeapps.com`, add:
   - `A` records for the apex: 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153
   - `CNAME` record `www` → `kasempiternal.github.io`
2. In this repo: Settings → Pages → Custom domain → `seizeapps.com` (this commits a CNAME file).
3. Wait for the certificate, then enable "Enforce HTTPS".

Do NOT add the CNAME file before DNS resolves — it makes the github.io URL
redirect to the dead domain, breaking the App Store privacy-policy links.
