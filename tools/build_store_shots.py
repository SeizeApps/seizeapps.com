#!/usr/bin/env python
"""Las capturas de la App Store, para la web (09/10/2026).

    ~/dev/seize/tools/asc/venv/bin/python tools/build_store_shots.py

Toma las capturas compuestas de la Store (titular + dispositivo, 1320 × 2868) que deja
SeizeRepo/tools/store/compose.py en tools/store/out/<App>/store/<lang>/<prefijo>-<lang>-NN-<slug>.png
y escribe, para cada app y cada idioma:

    assets/store/<slug>/<lang>/NN-<slug>-400.webp  y  …-800.webp   (srcset 1x/2x del carril)

más tools/store_shots.json, el manifiesto que lee gen_site.py: por app y por idioma, cada captura con su
tamaño y el titular y el subtítulo aprobados para la Store (de tools/store/config/<app>.yaml), que van al
texto alternativo. gen_site.py no necesita el SeizeRepo ni Pillow: solo este manifiesto y las webp.

Para una versión nueva: cambiar el prefijo en SOURCES, volver a correr esto y luego gen_site.py.
Hace falta Pillow con WebP (el venv de tools/asc del SeizeRepo lo tiene). Ruta del SeizeRepo: $SEIZE_REPO
o ~/dev/seize.
"""
import json, os, re, shutil, sys
from pathlib import Path

import yaml
from PIL import Image

SITE = Path(__file__).resolve().parents[1]
SEIZE = Path(os.environ.get('SEIZE_REPO', Path.home() / 'dev/seize'))
OUT = SEIZE / 'tools/store/out'
CONFIG = SEIZE / 'tools/store/config'
WIDTHS = (400, 800)
QUALITY = 80

# slug de la web: (carpeta en tools/store/out, prefijo de versión, config de compose, idiomas)
SOURCES = {
    'drip':       ('Drip',       'drip-0.4.6',       'drip.yaml',       ('en', 'es', 'fr')),
    'anchor':     ('Anchor',     'anchor-0.1.9',     'anchor.yaml',     ('en', 'es', 'fr')),
    'kover':      ('Kover',      'kover-0.2.5',      'kover.yaml',      ('en', 'es', 'fr')),
    'tandem':     ('Tandem',     'tandem-0.2.4',     'tandem.yaml',     ('en', 'es', 'fr')),
    'meso':       ('Meso',       'meso-0.3.3',       'meso.yaml',       ('en', 'es', 'fr')),
    'grain':      ('Grain',      'grain-0.1.2',      'grain.yaml',      ('en', 'es', 'fr')),
    'garum':      ('Criba',      'criba-0.1.1',      'criba.yaml',      ('en', 'es', 'fr')),
    # Sacapuntas solo tiene capturas en castellano (la app es castellano y euskera); las páginas en/fr las
    # enseñan con el texto alternativo traducido en gen_site.py (copy['shot_alts']).
    'sacapuntas': ('Sacapuntas', 'sacapuntas-0.7.0', 'sacapuntas.yaml', ('es',)),
}
NAME = re.compile(r'^(?P<prefix>.+)-(?P<lang>[a-z]{2})-(?P<n>\d\d)-(?P<slug>[a-z0-9-]+)\.png$')


def one_line(s):
    return ' '.join((s or '').split())


def main():
    manifest = {}
    for slug, (folder, prefix, cfg_name, langs) in SOURCES.items():
        cfg = yaml.safe_load((CONFIG / cfg_name).read_text())
        by_slug = {s['slug']: s for s in cfg['shots']}
        dest_app = SITE / 'assets/store' / slug
        if dest_app.exists():
            shutil.rmtree(dest_app)
        manifest[slug] = {'source': prefix, 'langs': {}}
        for lang in langs:
            src_dir = OUT / folder / 'store' / lang
            files = sorted(p for p in src_dir.glob(f'{prefix}-{lang}-*.png'))
            if not files:
                sys.exit(f'{slug}: no hay {prefix}-{lang}-*.png en {src_dir}')
            dest = dest_app / lang
            dest.mkdir(parents=True, exist_ok=True)
            shots = []
            for f in files:
                m = NAME.match(f.name)
                if not m or m['prefix'] != prefix:
                    sys.exit(f'{f.name}: nombre inesperado')
                shot_cfg = by_slug.get(m['slug'])
                if shot_cfg is None:
                    sys.exit(f'{f.name}: {m["slug"]} no está en {cfg_name}')
                im = Image.open(f).convert('RGB')
                base = f'{m["n"]}-{m["slug"]}'
                sizes = {}
                for w in WIDTHS:
                    h = round(im.height * w / im.width)
                    out = dest / f'{base}-{w}.webp'
                    im.resize((w, h), Image.LANCZOS).save(out, 'WEBP', quality=QUALITY, method=6)
                    sizes[w] = h
                shots.append({
                    'base': f'assets/store/{slug}/{lang}/{base}',
                    'w': WIDTHS[0], 'h': sizes[WIDTHS[0]],
                    'title': one_line(shot_cfg['title'].get(lang)),
                    'subtitle': one_line((shot_cfg.get('subtitle') or {}).get(lang)),
                })
            manifest[slug]['langs'][lang] = shots
            kb = sum(p.stat().st_size for p in dest.glob('*.webp')) // 1024
            print(f'{slug:11} {lang}  {len(shots):2} capturas  {kb:5} KB')
    (SITE / 'tools/store_shots.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=1) + '\n')
    print('ok → tools/store_shots.json')


if __name__ == '__main__':
    main()
