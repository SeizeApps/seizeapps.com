"""Edits the studio-wide privacy policy (privacy.html, es/, fr/). Izotz's apps are not part of it (22/10/2026):
each has its own site with its own policy at /<app>/ (tools/gen_legal_apps.py, tools/gen_legal_yaybo.py). Their
sections, exception paragraphs and every mention go, and the sentences that only listed them are rewritten or
removed. Old links to privacy.html#<app> (shipped builds and the App Store Connect privacy URLs, frozen) are sent on
to the app's own policy by a script at the end of the page. Every edit must match exactly once and no trace of these
apps may be left, so a wording change in the copy files fails the build instead of silently skipping."""
import re

# section id -> (name, its own policy, relative to the site root, per language)
APPS = {
    'cycle-timers': ('Cycle Timers', {'en': 'cycle/privacy.html'}),
    'tempo': ('Tempo', {'en': 'tempo/privacy.html'}),
    'gaminghub': ('GamingHub', {'en': 'gaminghub/privacy.html'}),
    'atino': ('Atino', {'en': 'atino/privacy.html', 'es': 'atino/privacidad.html'}),
    'roomy': ('Roomy', {'en': 'roomy/privacy.html'}),
    'readably': ('Readably', {'en': 'readably/privacy.html'}),
    'overbit': ('Overbit', {'en': 'overbit/privacy.html'}),
    'yaybo': ('Yaybo', {'en': 'yaybo/privacy/', 'es': 'yaybo/privacidad/'}),
}

# The iCloud line no longer says every app syncs (some of Sendoa's apps don't either).
ICLOUD = {
    'en': ('<li><strong>In your iCloud.</strong> Our apps sync through your personal iCloud account under Apple\'s terms, unless you turn it off in Settings or the app\'s own section below says otherwise — we never have access to it.</li>',
           '<li><strong>In your iCloud.</strong> Apps that sync do so through your personal iCloud account under Apple\'s terms, unless you turn it off in Settings or the app\'s own section below says otherwise — we never have access to it. Tempo, Readably, Atino, Roomy, GamingHub and Overbit do not sync through iCloud.</li>'),
    'es': ('<li><strong>En tu iCloud.</strong> Nuestras apps sincronizan a través de tu cuenta personal de iCloud, bajo las condiciones de Apple, salvo que lo desactives en Ajustes o que la sección de esa app diga otra cosa; nosotros nunca tenemos acceso.</li>',
           '<li><strong>En tu iCloud.</strong> Las apps que sincronizan lo hacen a través de tu cuenta personal de iCloud, bajo las condiciones de Apple, salvo que lo desactives en Ajustes o que la sección de esa app diga otra cosa; nosotros nunca tenemos acceso. Tempo, Readably, Atino, Roomy, GamingHub y Overbit no sincronizan por iCloud.</li>'),
    'fr': ('<li><strong>Dans ton iCloud.</strong> Nos apps se synchronisent via ton compte iCloud personnel, selon les conditions d’Apple, sauf si tu désactives la synchronisation dans Réglages ou si la section de cette app dit autre chose ; nous n’y avons jamais accès.</li>',
           '<li><strong>Dans ton iCloud.</strong> Les apps qui se synchronisent le font via ton compte iCloud personnel, selon les conditions d’Apple, sauf si tu désactives la synchronisation dans Réglages ou si la section de cette app dit autre chose ; nous n’y avons jamais accès. Tempo, Atino, Roomy, GamingHub et Overbit ne se synchronisent pas par iCloud.</li>'),
}

S_ = r'[\s\u00a0\u202f]'  # the French copy puts a no-break space before : and ;

# Sentences that exist only because of these apps: (pattern, replacement), each must match exactly once.
EDITS = {
    'en': [
        (r' Some apps use RevenueCat for purchase analytics only \(see [^)]*\)\.', ''),
        (r'\(see <a href="#gaminghub">GamingHub</a>.*?not synced to iCloud\)', '(see <a href="#beatride">BeatRide</a>)'),
        (r' Readably is published by Izotz Cristobal Mota, who is its data controller\.', ''),
        (r' \(the only third-party analytics is RevenueCat[^)]*\)', ''),
        (r' Yaybo is the exception:.*?\(see <a href="#yaybo">Yaybo</a>\)\.', ''),
        (r' \(Atino, [^)]*\)', ''),
        (r' Tempo, Readably, Atino, Roomy, GamingHub and Overbit do not sync through iCloud\.', ''),
        (r'\s*<li><strong>On our server \(only where an app.s section says so\)\.</strong>.*?</li>', ''),
        (r' <a href="#overbit">Overbit</a> is the exception:.*?alerts\.', ''),
        (r' The exception is <a href="#overbit">Overbit</a>.*?write to us\.', ''),
        (r' Readably keeps the text you read on your iPhone\. The exception is <a href="#yaybo">Yaybo</a>.*?explains how\.', ''),
    ],
    'es': [
        (r' Algunas apps usan RevenueCat solo para analítica de compras \(véase [^)]*\)\.', ''),
        (r'\(véase <a href="#gaminghub">GamingHub</a>.*?no se sincronizan con iCloud\)', '(véase <a href="#beatride">BeatRide</a>)'),
        (r' Readably la publica Izotz Cristobal Mota, que es su responsable del tratamiento\.', ''),
        (r' \(la única analítica de terceros es la de compras de RevenueCat[^)]*\)', ''),
        (r' Yaybo es la excepción:.*?\(véase <a href="#yaybo">Yaybo</a>\)\.', ''),
        (r' \(Atino, [^)]*\)', ''),
        (r' Tempo, Readably, Atino, Roomy, GamingHub y Overbit no sincronizan por iCloud\.', ''),
        (r'\s*<li><strong>En nuestro servidor \(solo donde la sección de una app lo diga\)\.</strong>.*?</li>', ''),
        (r' <a href="#overbit">Overbit</a> es la excepción:.*?alertas\.', ''),
        (r' La excepción es <a href="#overbit">Overbit</a>.*?escríbenos\.', ''),
        (r' Readably mantiene en tu iPhone el texto que lees\. La excepción es <a href="#yaybo">Yaybo</a>.*?explica cómo\.', ''),
    ],
    'fr': [
        (r' Quelques apps utilisent RevenueCat uniquement pour mesurer les achats \(voir [^)]*\)\.', ''),
        (r'\(voir <a href="#gaminghub">GamingHub</a>.*?<a href="#beatride">BeatRide</a>\)', '(voir <a href="#beatride">BeatRide</a>)'),
        (r' \(la seule mesure tierce est celle des achats de RevenueCat[^)]*\)', ''),
        (r' Yaybo est une exception' + S_ + r':.*?\(voir <a href="#yaybo">Yaybo</a>\)\.', ''),
        (r' \(Atino, [^)]*\)', ''),
        (r' Tempo, Atino, Roomy, GamingHub et Overbit ne se synchronisent pas par iCloud\.', ''),
        (r'\s*<li><strong>Sur notre serveur \(seulement là où la section d.une app le dit\)\.</strong>.*?</li>', ''),
        (r' <a href="#overbit">Overbit</a> est l.exception' + S_ + r':.*?alertes\.', ''),
        (r' L.exception est <a href="#overbit">Overbit</a>.*?écris-nous\.', ''),
        (r' L.exception est <a href="#yaybo">Yaybo</a>.*?explique comment\.', ''),
    ],
}

CONJ = {'en': ' and ', 'es': ' y ', 'fr': ' et '}


def relist(lang, b):
    """«currently <a>Tempo</a>, <a>Drip</a> … and <a>Yaybo</a>.» keeps only the studio's own apps."""
    conj = CONJ[lang]
    rx = re.compile(r'(currently |actualmente |actuellement )((?:<a href="#[a-z-]+">[^<]+</a>(?:, | and | y | et ))+<a href="#[a-z-]+">[^<]+</a>)\.')
    m = rx.search(b)
    assert m and len(rx.findall(b)) == 1, (lang, 'app list')
    links = re.findall(r'<a href="#[a-z-]+">[^<]+</a>', m.group(2))
    keep = [l for l in links if re.search(r'#([a-z-]+)', l).group(1) not in APPS]
    return b[:m.start(2)] + ', '.join(keep[:-1]) + conj + keep[-1] + '.' + b[m.end():]


def hop(lang):
    """privacy.html#<app> -> that app's own policy (links from shipped builds and App Store Connect)."""
    up = '' if lang == 'en' else '../'
    to = {sid: up + p.get(lang, p['en']) for sid, (_, p) in APPS.items()}
    pairs = ','.join(f'"{k}":"{v}"' for k, v in to.items())
    return f'<script>(function(t){{t=t[location.hash.slice(1)];if(t)location.replace(t)}})({{{pairs}}})</script>'


def patch_body(lang, b):
    old, new = ICLOUD[lang]
    for sep in (' ', '\u202f', '\u00a0'):  # whichever no-break space the French copy uses before ; and :
        o, w = (re.sub(r' (?=[;:])', sep, x) for x in (old, new))
        if b.count(o) == 1: b = b.replace(o, w); break
    else: raise AssertionError((lang, 'iCloud line'))
    toc = re.search(r'<nav class="toc".*?</nav>', b, re.S).group(0)
    b = b.replace(toc, re.sub(r'<a href="#(%s)">[^<]+</a>' % '|'.join(APPS), '', toc))
    for sid, (name, _) in APPS.items():
        b, n = re.subn(r'\s*<section id="%s">.*?</section>' % sid, '', b, flags=re.S)
        assert n <= 1, (lang, sid, 'section', n)
        b = re.sub(r'\s*<p><strong>%s (?:is|es|est) (?:another|otra|une autre) [^<]*</strong>.*?</p>' % re.escape(name), '', b, flags=re.S)
    for rx, rep in EDITS[lang]:
        b, n = re.subn(rx, rep, b, flags=re.S)
        assert n == 1, (lang, rx[:60], n)
    b = relist(lang, b)
    names = '|'.join(re.escape(n) for n, _ in APPS.values())
    m = re.search(r'\b(?:%s)\b|#(?:%s)\b|Cycle Pro' % (names, '|'.join(APPS)), b)
    assert not m, (lang, b[max(0, m.start() - 100):m.start() + 100])
    return b + '\n  ' + hop(lang)


def patch_legal(LEGAL):
    for lang in ('en', 'es', 'fr'):
        LEGAL[lang]['privacy']['body'] = patch_body(lang, LEGAL[lang]['privacy']['body'])
    return LEGAL
