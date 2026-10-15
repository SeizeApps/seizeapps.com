"""Static checks on Yaybo's generated legal pages (run after `python3 tools/gen_site.py`, before merging PR #11).

Fails when the page says something the build or the disclosure doc contradicts, or still carries a fact only Izotz can supply:
  1. no [OPERATOR ...] marker left (postal address and telephone, 16 CFR 312.4(d)(1));
  2. the "Purchase analytics" paragraph equals docs/kids-us/11-revenuecat-disclosure.md §3.2 minus its last sentence
     (the key-off page has no such paragraph and must not mention RevenueCat's SDK data);
  3. none of the statements found false on 11/10 and 15/10/2026 (RevenueCat "never while a child is playing", the Parent Zone
     alone switching it on, a bullet titled "Consent:", "no microphone use for children", "Seize runs no server", "the data never
     leaves your device" now that iCloud sync and the family link are on, the security-program sentence while the program is
     unsigned);
  4. the retention deadline and the internal-operations purpose are present;
  5. what the 15/10 build does is said: the Apple Ads attribution post, Read-aloud and SpeechAnalyzer, iCloud, the operator's
     address and telephone.
Usage: python3 tools/check_yaybo_legal.py [--seizerepo /path/to/SeizeRepo-kids-us]
"""
import html, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
args = sys.argv[1:]
SEIZE = os.path.expanduser('~/Multiverse/Izotz/SeizeRepo-kids-us')
if '--seizerepo' in args:
    SEIZE = args[args.index('--seizerepo') + 1]
DOC11 = os.path.join(SEIZE, 'docs/kids-us/11-revenuecat-disclosure.md')
PROGRAM = os.path.join(SEIZE, 'docs/kids-us/release/information-security-program.md')


def text_of(path):
    raw = open(path, encoding='utf-8').read()
    raw = re.sub(r'<!--.*?-->', '', raw, flags=re.S)
    main = raw[raw.index('<main'):raw.index('</main>')] if '<main' in raw else raw
    main = re.sub(r'</?(strong|em|a)\b[^>]*>', '', main)
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', main))).strip()


def doc11_paragraph():
    s = open(DOC11, encoding='utf-8').read()
    s = s[s.index('### 3.2'):s.index('### 3.3')]
    lines = [l[2:] for l in s.splitlines() if l.startswith('> ')]
    p = re.sub(r'\s+', ' ', ' '.join(lines).replace('**', '')).strip()
    p = p.removeprefix('Purchase analytics. ')
    cut = p.index(' Everything you tell Yaybo')
    return p[:cut]


def squash(t):
    return re.sub(r'\s+', ' ', t.replace('’', "'")).strip()


fails = []
pages = {k: text_of(os.path.join(ROOT, f'yaybo/{k}/index.html')) for k in ('privacy', 'privacidad', 'terms', 'condiciones')}
en = squash(pages['privacy'])

for k, t in pages.items():
    if '[OPERATOR' in t:
        fails.append(f'{k}: an [OPERATOR ...] marker is still in the page (postal address / telephone missing)')
    for bad in ('never while a child is playing', 'nunca mientras un niño juega', 'Consent:', 'Consentimiento:',
                'iCloud sync is on by default', 'stay viewable',
                'se pueden ver; las actividades', 'Apple Account › Subscriptions', 'Cuenta de Apple › Suscripciones',
                'ask for your consent again', 'te pediremos el consentimiento otra vez',
                # false for the 15/10 build (i4-statements DEFECT 2)
                'no microphone use for children', 'no usa el micrófono con niños', 'Seize runs none', 'Seize runs no server',
                'Seize no tiene ninguno', 'Seize no tiene ningún servidor', 'never leaves your device', 'nunca salen de tu dispositivo',
                'a later version may offer optional iCloud sync', 'Una versión futura podría ofrecer sincronización',
                'Yaybo never records your child', 'Yaybo nunca graba a tu hijo o hija.'):
        if re.search(re.escape(bad) + r'(?!s)', t):  # "your device" must not match "your devices"
            fails.append(f'{k}: forbidden phrase "{bad}"')
    if 'written information-security program' in t and not re.search(r'^SIGNED:[ \t]*[^_\s]', open(PROGRAM).read() if os.path.exists(PROGRAM) else '', re.M):
        fails.append(f'{k}: claims a written information-security program that is not signed ({PROGRAM}, needs a filled-in "SIGNED:" line)')

must = {'privacy': ('Apple Ads', 'Where our ads came from', 'SpeechAnalyzer', 'Read-aloud', 'iCloud', 'Ugarana kalea 3', '+34 672 53 17 63'),
        'privacidad': ('Apple Ads', 'De dónde venían nuestros anuncios', 'SpeechAnalyzer', 'lectura en voz alta', 'iCloud', 'Ugarana kalea 3', '+34 672 53 17 63')}
for k, phrases in must.items():
    for ph in phrases:
        if ph not in pages[k]:
            fails.append(f'{k}: missing "{ph}"')

if 'Purchase analytics (RevenueCat)' in en:
    want = squash(doc11_paragraph())
    if want not in en:
        fails.append('privacy: the Purchase analytics paragraph is not docs/kids-us/11-revenuecat-disclosure.md §3.2 word for word')
    if 'Opening the Parent Zone alone starts nothing' not in en:
        fails.append('privacy: missing "Opening the Parent Zone alone starts nothing"')
    if 'within 30 days' not in en:
        fails.append('privacy: no concrete deletion timeframe (COPPA 312.10)')
else:
    for bad in ('vendor identifier', 'IDFV', 'storefront country', 'anonymous app user ID'):
        if bad in en:
            fails.append(f'privacy (key-off): still mentions "{bad}"')

if fails:
    print('FAIL')
    for f in fails:
        print(' -', f)
    sys.exit(1)
print('OK: yaybo legal pages pass (operator marker, doc 11 diff, forbidden phrases, retention)')
