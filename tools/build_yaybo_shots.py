"""Yaybo's app screenshots for the website: resize the raw simulator captures (light mode, 9:41) to WebP under yaybo/media/.

Usage: python3 tools/build_yaybo_shots.py <folder with the s15-*.png / ipad-landscape-*.png captures>
The originals stay outside the repo. s15-08-parent-zone.png is deliberately not used (it shows an inconsistent "Working on").
"""
import sys
from pathlib import Path
from PIL import Image

OUT = Path(__file__).resolve().parent.parent / 'yaybo' / 'media'
PHONES = {'s15-01-home': 'ui-home', 's15-02-adventure-road': 'ui-road', 's15-03-lesson-counting': 'ui-counting',
          's15-04-celebration': 'ui-celebration', 's15-05-island': 'ui-island', 's15-06-tads-book-page': 'ui-book',
          's15-07-parent-report': 'ui-report'}
PADS = {'ipad-landscape-01-home': 'pad-home'}


def save(src, dst, width, q):
    im = Image.open(src).convert('RGB')
    im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    im.save(OUT / f'{dst}.webp', 'WEBP', quality=q, method=6)
    print(dst, im.size, (OUT / f'{dst}.webp').stat().st_size // 1024, 'KB')


if __name__ == '__main__':
    d = Path(sys.argv[1])
    for k, v in PHONES.items():
        save(d / f'{k}.png', v, 640, 80)
    for k, v in PADS.items():
        save(d / f'{k}.png', v, 1400, 78)
