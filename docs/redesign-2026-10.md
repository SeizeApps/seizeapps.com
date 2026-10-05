# seizeapps.com redesign — October 2026

Rationale, short. The identity is fixed (SEIZE 2026: Electric Blue, Cyan, Deep Navy, Stone, ribbon-S, system fonts, dark only); this pass changes composition, rhythm and motion, not the brand.

- **Flighty** (flighty.com): one device held at an angle in front of a dark, structured field, lit by a single coloured glow. Taken: the home hero's three-phone fan of real screenshots on Deep Navy with one blue glow, leaning towards the pointer. Not taken: its violet/magenta glow (no purple, anywhere).
- **Things** (culturedcode.com/things): the product UI *is* the artwork, shown in perspective, with everything else quiet. Taken: screenshots as the only imagery, a perspective tilt on them, restraint everywhere else (hairlines, no ornaments, no stock art).
- **Mercury Weather** (mercuryweather.app): pill chips and fast (~160 ms) hover feedback. Taken: the chip language for tags/meta and the "App Store" / "Coming soon" status pills. Not taken: its purple gradients.
- **TakeControl** (gettakecontrol.app, via minimal.gallery): a confident one-line statement with a compact proof line under it. Taken: the hero proof line (app count · live on the App Store · Basque Country), computed from the data so it never goes stale.
- **Reel Motion** (reelmotion.fit, Awwwards): a fan of phones as the hero's evidence. Taken: the fan composition, but in the brand's palette and with our own screenshots.

Decisions that follow from the brand rules: one dominant colour (blue, with cyan only for eyebrows, focus rings and tiny accents); neutral navy surfaces for 80 %+ of every page; hierarchy by weight (600/700 headings against 400 body), four type sizes per section at most; Inter is self-hosted (no request to Google: a privacy-first studio shouldn't send visitors to a font CDN); buttons use `#006EE6` instead of `#007AFF` because white on `#007AFF` is 4.0:1 and fails AA for 15 px text, while `#006EE6` measures 4.8:1.

Motion is the brand spring (`response 0.30 / damping 0.75`, sampled into CSS `linear()`), used for hover, press and the hero entrance; section reveals are CSS scroll-driven (no JS, content visible where unsupported); the icon marquee is the only automatic loop and it stops on hover. Everything stops under `prefers-reduced-motion: reduce`, including cross-page View Transitions (app icon → app page hero).
