"""Isolation check for the apps that stand on their own (App Store guideline 4.3): every page under /<app>/ may
point only at that app's own pages and files, its contact address, its own App Store listing, Apple, and the
vendors and regulators its policy names. Anything else (the studio home, another app, the shared /assets/, a font
or script from elsewhere) fails. Prints each offending page and URL, exits 1 on a failure.
Run from anywhere: python3 tools/check_isolation.py"""
import os, re, sys
from urllib.parse import urlsplit

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOST = 'seizeapps.com'

# folder -> (App Store id or None while it is not on sale, contact addresses, extra hosts its policy names)
APPS = {
    'cycle': ('6796827400', {'hello@seizeapps.com'}, {'www.revenuecat.com'}),
    'tempo': ('6761499275', {'izotz@seizeapps.com', 'hello@seizeapps.com'}, {'www.revenuecat.com'}),
    'gaminghub': (None, {'hello@seizeapps.com'}, {'www.revenuecat.com', 'supabase.com'}),
    'atino': (None, {'hello@seizeapps.com'}, {'www.revenuecat.com'}),
    'roomy': (None, {'hello@seizeapps.com'}, {'www.revenuecat.com'}),
    'readably': (None, {'hello@seizeapps.com'}, {'www.revenuecat.com', 'huggingface.co'}),
    'overbit': (None, {'hello@seizeapps.com'}, {'www.revenuecat.com', 'supabase.com'}),
    'yaybo': (None, {'hello@seizeapps.com'}, {'www.revenuecat.com', 'supabase.com', 'elevenlabs.io'}),
}
APPLE = {'www.apple.com', 'apple.com', 'support.apple.com', 'reportaproblem.apple.com', 'apps.apple.com'}
REGULATORS = {'www.aepd.es'}

URL = re.compile(r'''\b(?:href|src|poster|action)=["']([^"']+)["']|\bsrcset=["']([^"']+)["']|url\(\s*["']?([^"')]+)["']?\s*\)''', re.I)


def urls(html):
    for href, srcset, css in URL.findall(html):
        if srcset:
            yield from (part.strip().split()[0] for part in srcset.split(',') if part.strip())
        else:
            yield href or css


def verdict(folder, page, url):
    """None when allowed, else the reason."""
    store, mails, hosts = APPS[folder]
    u = urlsplit(url)
    if url.startswith('#') or u.scheme == 'data':
        return None
    if u.scheme == 'mailto':
        return None if u.path.lower() in mails else 'mail address'
    if u.scheme in ('http', 'https'):
        if u.netloc == HOST:
            path = u.path.lstrip('/')
        elif u.netloc == 'apps.apple.com':
            if '/app/' not in u.path: return None  # Apple account pages (manage subscriptions)
            return None if store and u.path.endswith(f'/id{store}') else 'another App Store listing'
        elif u.netloc in APPLE | REGULATORS | hosts:
            return None
        else:
            return f'outside host {u.netloc}'
    elif u.scheme:
        return f'scheme {u.scheme}'
    else:
        path = os.path.relpath(os.path.normpath(os.path.join(os.path.dirname(page), u.path)), SITE) if u.path else os.path.relpath(page, SITE)
    path = os.path.normpath(path)
    return None if path == folder or path.startswith(folder + os.sep) else f'leaves /{folder}/ ({path})'


def main():
    bad = n = 0
    for folder in APPS:
        root = os.path.join(SITE, folder)
        for d, _, fs in os.walk(root):
            for f in fs:
                if not f.endswith('.html'): continue
                page = os.path.join(d, f)
                for url in urls(open(page, encoding='utf-8').read()):
                    n += 1
                    why = verdict(folder, page, url)
                    if why:
                        bad += 1
                        print(f'{os.path.relpath(page, SITE)}: {url}  <- {why}')
    print(f'{n} URLs in {len(APPS)} app sites, {bad} outside their own site')
    return bad == 0


if __name__ == '__main__':
    sys.exit(0 if main() else 1)
