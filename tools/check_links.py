"""Internal link checker: every href/src that stays on seizeapps.com must resolve to a file,
and every #fragment to an id on the target page. Run from anywhere: python3 tools/check_links.py"""
import os, re, sys
from urllib.parse import urlsplit, unquote
SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOST = 'seizeapps.com'
ATTR = re.compile(r'<(?:a|link|img|script)\b[^>]*?\b(?:href|src)="([^"]+)"', re.I)
ID = re.compile(r'\bid="([^"]+)"')

def target(page, url):
    u = urlsplit(url)
    if u.scheme in ('mailto', 'tel', 'javascript') or (u.scheme in ('http', 'https') and u.netloc != HOST):
        return None
    if u.scheme in ('http', 'https'):
        path = u.path
        full = os.path.join(SITE, path.lstrip('/'))
    else:
        path = u.path
        full = os.path.join(os.path.dirname(page), unquote(path)) if path else page
    full = os.path.normpath(full)
    if os.path.isdir(full):
        full = os.path.join(full, 'index.html')
    return full, u.fragment

bad, n, ids = [], 0, {}
pages = [os.path.join(d, f) for d, ds, fs in os.walk(SITE) if '.git' not in d.split(os.sep)
         for f in fs if f.endswith('.html')]
for page in pages:
    html = open(page, encoding='utf-8').read()
    html_nc = re.sub(r'<!--.*?-->', '', html, flags=re.S)
    for url in ATTR.findall(html_nc):
        t = target(page, url)
        if t is None: continue
        n += 1
        full, frag = t
        if not os.path.isfile(full):
            bad.append((os.path.relpath(page, SITE), url, 'missing file')); continue
        if frag and full.endswith('.html'):
            if full not in ids: ids[full] = set(ID.findall(open(full, encoding='utf-8').read()))
            if frag not in ids[full]: bad.append((os.path.relpath(page, SITE), url, 'missing #' + frag))
for b in bad: print('BROKEN', *b)
print(f'{len(pages)} pages, {n} internal links, {len(bad)} broken')
sys.exit(1 if bad else 0)
