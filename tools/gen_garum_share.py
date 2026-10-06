"""Garum's share links (Garum 0.0.26, 30/09/2026): the page a collection or a place opens on the web, and the
Universal Links file that makes the same link open the app when it's installed.

  garum/c/index.html   a collection  — https://seizeapps.com/garum/c/?<code>
  garum/p/index.html   a place       — https://seizeapps.com/garum/p/?<code>
  garum/share.js · garum/share.css   the page's script and styles (one copy for both)
  .well-known/apple-app-site-association   /garum/c/* and /garum/p/* belong to the app (team 5487U4H5BK)
  _config.yml          GitHub Pages runs Jekyll, which skips dot-folders: it has to include .well-known

The site is static, so the code travels in the query (`?k7m2p9x3ab`): the page is always the same file and reads the
code in the browser. It asks Garum's server (`shared_page`, Supabase, with the *publishable* key — the same one inside
the app; the function only returns what the link already shows: public or «only with the link» collections, visible
places) in the browser's language (en/es/fr; fr-CA → fr) and draws it read-only, the notes included (Sendoa's decision:
notes are seen without an account). Since Garum 0.0.27 a collection's title, introduction and notes come translated by
Garum's server when there is a translation, and the page says so with one switch, «Translated · See the original» (the
same for a place's signed notes and «What to order»). Nothing is indexed (`noindex`: a «link only» collection must not end up in a search
engine), no cookies, no analytics, no photos (data egress on the free plan). Everything written by people goes in with
`textContent`, never as HTML. No city in the page's own texts.

App Store: GARUM_APP_ID is Garum's ASC id; set GARUM_ON_STORE to True only when `lookup` says it's live (README,
«App Store badge»). Until then the page says, neutrally, that Garum isn't on the App Store yet.

Built by `python3 tools/gen_site.py`, which calls build_garum_share().
"""
import json
from gen_site import write

GARUM_APP_ID = '6816385891'
GARUM_ON_STORE = True
TEAM_ID = '5487U4H5BK'
BUNDLE_ID = 'com.seizeapps.criba'   # Garum's bundle id (the app was called Criba)
BACKEND = 'https://rbiyqvizjwcysfhvdyox.supabase.co'
PUBLISHABLE_KEY = 'sb_publishable_rTonGbzHP5mre-oHDfxcVQ_vJOmUaBa'
ASSETS_V = '2026-09-30b'

AASA = {
    'applinks': {
        'details': [{
            'appIDs': [f'{TEAM_ID}.{BUNDLE_ID}'],
            'components': [
                {'/': '/garum/c/*', 'comment': 'Garum: a shared collection'},
                {'/': '/garum/p/*', 'comment': 'Garum: a shared place'},
            ],
        }],
    },
}

# The page's texts, in the three languages of the app. «tú» in Spanish and French, as in the app.
T = {
    'en': {
        'loading': 'Loading…',
        'list': 'List', 'itinerary': 'Itinerary',
        'places': ['{n} place', '{n} places'], 'stops': ['{n} stop', '{n} stops'],
        'by': 'by {who}',
        'unvalidated': 'Not validated yet',
        'unvalidated_hint': 'Proposed by the author; not on Garum’s map yet.',
        'maps': 'Open in Maps',
        'why': 'Why it’s here', 'order': 'What to order', 'signed': 'Signed by {who}', 'translated': 'Translated',
        'see_original': 'Translated · See the original', 'see_translation': 'See the translation',
        'season': 'Closed for the season', 'season_until': 'Closed for the season · back on {date}',
        'era': {'clasico': 'Classic · over 25 years', 'establecido': 'Established · 3 to 25 years', 'nuevo': 'New · under 3 years'},
        'gone_title': 'This link doesn’t lead anywhere now',
        'gone_c': 'The collection may have been deleted or made private by its author.',
        'gone_p': 'The place may have closed or left Garum’s map.',
        'error_title': 'This page couldn’t load',
        'error_body': 'Check your connection and try again.',
        'retry': 'Try again',
        'app_title': 'Garum', 'app_line': 'A map of places that are there for a reason, each with its why, everything signed.',
        'app_store': 'Download on the App Store',
        'app_installed': 'If you have Garum on your iPhone, this link opens in the app.',
        'app_not_yet': 'Garum is an iPhone app, and it isn’t on the App Store yet.',
        'more': 'About Garum', 'privacy': 'Privacy', 'terms': 'Terms',
        'desc_c': 'A collection on Garum', 'desc_p': 'A place on Garum',
    },
    'es': {
        'loading': 'Cargando…',
        'list': 'Lista', 'itinerary': 'Itinerario',
        'places': ['{n} sitio', '{n} sitios'], 'stops': ['{n} parada', '{n} paradas'],
        'by': 'de {who}',
        'unvalidated': 'Sin validar',
        'unvalidated_hint': 'Lo ha propuesto el autor; aún no está en el mapa de Garum.',
        'maps': 'Abrir en Mapas',
        'why': 'Por qué está aquí', 'order': 'Qué pedir', 'signed': 'Firmado por {who}', 'translated': 'Traducido',
        'see_original': 'Traducido · Ver el original', 'see_translation': 'Ver la traducción',
        'season': 'Cerrado por temporada', 'season_until': 'Cerrado por temporada · vuelve el {date}',
        'era': {'clasico': 'Clásico · más de 25 años', 'establecido': 'Establecido · de 3 a 25 años', 'nuevo': 'Nuevo · menos de 3 años'},
        'gone_title': 'Este enlace ya no lleva a nada',
        'gone_c': 'Puede que su autor haya borrado la colección o la haya hecho privada.',
        'gone_p': 'Puede que el sitio haya cerrado o haya salido del mapa de Garum.',
        'error_title': 'No se ha podido cargar',
        'error_body': 'Mira la conexión y vuelve a probar.',
        'retry': 'Volver a probar',
        'app_title': 'Garum', 'app_line': 'Un mapa de sitios que están por algo, cada uno con su porqué, todo firmado.',
        'app_store': 'Descargar en el App Store',
        'app_installed': 'Si tienes Garum en el iPhone, este enlace se abre en la app.',
        'app_not_yet': 'Garum es una app para iPhone y todavía no está en el App Store.',
        'more': 'Sobre Garum', 'privacy': 'Privacidad', 'terms': 'Condiciones',
        'desc_c': 'Una colección en Garum', 'desc_p': 'Un sitio en Garum',
    },
    'fr': {
        'loading': 'Chargement…',
        'list': 'Liste', 'itinerary': 'Itinéraire',
        'places': ['{n} lieu', '{n} lieux'], 'stops': ['{n} étape', '{n} étapes'],
        'by': 'par {who}',
        'unvalidated': 'Pas encore validé',
        'unvalidated_hint': 'Proposé par l’auteur ; pas encore sur la carte de Garum.',
        'maps': 'Ouvrir dans Plans',
        'why': 'Pourquoi il est là', 'order': 'Que commander', 'signed': 'Signé par {who}', 'translated': 'Traduit',
        'see_original': 'Traduit · Voir l’original', 'see_translation': 'Voir la traduction',
        'season': 'Fermé pour la saison', 'season_until': 'Fermé pour la saison · retour le {date}',
        'era': {'clasico': 'Classique · plus de 25 ans', 'establecido': 'Établi · de 3 à 25 ans', 'nuevo': 'Nouveau · moins de 3 ans'},
        'gone_title': 'Ce lien ne mène plus nulle part',
        'gone_c': 'L’auteur a peut-être supprimé la collection ou l’a rendue privée.',
        'gone_p': 'Le lieu a peut-être fermé ou quitté la carte de Garum.',
        'error_title': 'Impossible de charger la page',
        'error_body': 'Vérifie ta connexion et réessaie.',
        'retry': 'Réessayer',
        'app_title': 'Garum', 'app_line': 'Une carte de lieux qui sont là pour une raison, chacun avec son pourquoi, tout est signé.',
        'app_store': 'Télécharger dans l’App Store',
        'app_installed': 'Si tu as Garum sur ton iPhone, ce lien s’ouvre dans l’app.',
        'app_not_yet': 'Garum est une app pour iPhone, et elle n’est pas encore sur l’App Store.',
        'more': 'À propos de Garum', 'privacy': 'Confidentialité', 'terms': 'Conditions',
        'desc_c': 'Une collection sur Garum', 'desc_p': 'Un lieu sur Garum',
    },
}

CSS = '''/* Garum's share page (tools/gen_garum_share.py). The app's paper and ink («Cedazo»), light and dark. */
:root{
  --paper:#F3EFE6;--card:#FBF9F4;--ink:#151412;--sec:#5D574C;--line:#DDD6C8;--blue:#0062CC;
  --clasico:#A2461F;--establecido:#5F6F2A;--nuevo:#A37D00;--on-nuevo:#151412;--on-era:#FFFFFF;
  --radius:16px;
}
@media (prefers-color-scheme:dark){:root{
  --paper:#151412;--card:#201E1B;--ink:#EDE8DD;--sec:#B3AB9C;--line:#35312B;--blue:#5AA9FF;
  --clasico:#E0764B;--establecido:#A9B96A;--nuevo:#E8BE55;--on-nuevo:#151412;--on-era:#151412;
}}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--paper);color:var(--ink);font:17px/1.5 -apple-system,BlinkMacSystemFont,"SF Pro Text",Inter,system-ui,sans-serif}
a{color:var(--blue)}
[hidden]{display:none !important}
.sr{position:absolute;left:-9999px}
.wrap{max-width:640px;margin:0 auto;padding:20px 16px 40px}
header.top{display:flex;align-items:center;gap:10px;padding:4px 0 18px}
header.top img{width:36px;height:36px;border-radius:9px}
header.top .name{font-weight:700;letter-spacing:.2px}
header.top .by{color:var(--sec);font-size:13px;margin-left:auto}
.eyebrow{color:var(--sec);font-size:13px;font-weight:600;text-transform:uppercase;letter-spacing:.6px;margin:0 0 6px}
h1{font-size:30px;line-height:1.2;margin:0 0 8px;font-weight:700;overflow-wrap:anywhere}
.byline{color:var(--sec);margin:0 0 12px;font-weight:500}
.intro{margin:0 0 18px;white-space:pre-line}
ol.items{list-style:none;margin:0;padding:0;display:grid;gap:10px}
.item{display:flex;gap:12px;background:var(--card);border:1px solid var(--line);border-radius:var(--radius);padding:14px}
.item > div{min-width:0}
.mark{flex:none;width:28px;height:28px;display:flex;align-items:center;justify-content:center}
.num{border-radius:50%;font-weight:700;font-size:15px;font-variant-numeric:tabular-nums;color:var(--on-era)}
.num.nuevo{color:var(--on-nuevo)}
.num.unvalidated{background:transparent;border:1.5px dashed var(--sec);color:var(--sec)}
.shape{width:12px;height:12px}
.shape.clasico{border-radius:50%}
.shape.establecido{border-radius:2px}
.shape.nuevo{transform:rotate(45deg) scale(.85);border-radius:1px}
.shape.unvalidated{border-radius:50%;background:transparent;border:1.5px dashed var(--sec)}
.bg-clasico{background:var(--clasico)}.bg-establecido{background:var(--establecido)}.bg-nuevo{background:var(--nuevo)}
.item h2{font-size:17px;margin:0;font-weight:600;overflow-wrap:anywhere}
.meta{color:var(--sec);font-size:15px;margin:2px 0 0}
.tag{display:inline-block;font-size:12px;font-weight:600;color:var(--sec);border:1px dashed var(--sec);border-radius:6px;padding:0 6px;margin-left:6px;vertical-align:2px}
blockquote{margin:8px 0 0;padding:0;font-size:16px;overflow-wrap:anywhere}
.maps{display:inline-block;margin-top:4px;font-size:15px;font-weight:600;text-decoration:none;min-height:44px;line-height:44px}
.section{margin:22px 0 0}
.section h2{font-size:13px;font-weight:600;text-transform:uppercase;letter-spacing:.6px;color:var(--sec);margin:0 0 8px}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin:0;padding:0;list-style:none}
.chips li{border:1px solid var(--line);background:var(--card);border-radius:10px;padding:5px 11px;font-size:15px}
.note{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);padding:14px;margin:10px 0 0}
.note p{margin:0;overflow-wrap:anywhere}
.note .who{color:var(--sec);font-size:14px;margin-top:8px}
.order{margin:0;padding-left:20px}
.orig{font:inherit;font-size:15px;color:var(--blue);background:none;border:0;padding:0;min-height:44px;cursor:pointer;text-align:left}
.season{display:inline-block;background:var(--card);border:1px solid var(--line);border-radius:10px;padding:4px 10px;font-size:15px;font-weight:500;margin:0 0 4px}
.cta{margin:28px 0 0;background:var(--card);border:1px solid var(--line);border-radius:var(--radius);padding:18px;display:flex;gap:14px;align-items:flex-start}
.cta img{width:56px;height:56px;border-radius:13px;flex:none}
.cta h2{font-size:17px;margin:0 0 2px}
.cta p{margin:0 0 8px;color:var(--sec);font-size:15px}
.cta p:last-child{margin-bottom:0}
.cta .store{display:inline-block;background:var(--ink);color:var(--paper);text-decoration:none;font-weight:600;border-radius:12px;padding:0 16px;line-height:44px;margin:4px 0 8px}
.state{padding:24px 0}
.state h1{font-size:24px}
.state button{font:inherit;font-weight:600;color:var(--blue);background:none;border:1px solid var(--line);border-radius:12px;padding:0 16px;min-height:44px;cursor:pointer}
.skeleton div{background:var(--line);border-radius:8px;height:18px;margin:10px 0;opacity:.6}
.skeleton .h{height:34px;width:70%}.skeleton .s{width:40%}.skeleton .b{height:72px}
footer{margin-top:32px;color:var(--sec);font-size:14px;display:flex;flex-wrap:wrap;gap:4px 16px}
footer a{color:var(--sec);min-height:44px;line-height:44px}
footer span{line-height:44px}
@media (prefers-reduced-motion:no-preference){.content{animation:in .25s ease-out}@keyframes in{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:none}}}
'''

JS = r'''// Garum's share page (tools/gen_garum_share.py): reads the code from the address, asks the server and draws it.
// Everything written by people goes in with textContent, never as HTML.
(function () {
  'use strict';
  var API = %(api)s, KEY = %(key)s, ON_STORE = %(on_store)s, APP_ID = %(app_id)s, T = %(texts)s;
  var type = document.body.getAttribute('data-type');            // 'collection' | 'place'
  var lang = (function () {
    var tags = navigator.languages && navigator.languages.length ? navigator.languages : [navigator.language || 'en'];
    for (var i = 0; i < tags.length; i++) {
      var l = String(tags[i]).toLowerCase().split('-')[0];
      if (T[l]) return l;
    }
    return 'en';
  })();
  var t = T[lang];
  document.documentElement.lang = lang;

  function code() {
    var q = location.search.replace(/^\?/, '').split('&')[0] || '';
    var kv = q.split('=');
    var c = kv.length > 1 ? kv[1] : kv[0];
    if (!c) { var parts = location.pathname.split('/').filter(Boolean); c = parts[parts.length - 1] || ''; }
    try { c = decodeURIComponent(c).toLowerCase(); } catch (e) { return null; }
    return /^[a-z0-9]{6,16}$/.test(c) ? c : null;
  }
  function el(tag, cls, text) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text != null) e.textContent = text;
    return e;
  }
  function fmt(s, vars) { return s.replace(/\{(\w+)\}/g, function (_, k) { return vars[k]; }); }
  function plural(forms, n) { return fmt(forms[n === 1 ? 0 : 1], { n: n }); }
  function quoted(s) { return lang === 'fr' ? '« ' + s + ' »' : lang === 'en' ? '“' + s + '”' : '«' + s + '»'; }
  function price(p) { return p ? new Array(p + 1).join('€') : null; }
  function mapsURL(name, lat, lng) {
    return 'https://maps.apple.com/?q=' + encodeURIComponent(name) + '&ll=' + Number(lat) + ',' + Number(lng);
  }
  function labels(list) { return (list || []).map(function (x) { return x.label; }); }
  function meta(parts) { return parts.filter(function (x) { return x; }).join(' · '); }
  function who(owner) { return owner.username ? owner.alias + ' · @' + owner.username : owner.alias; }
  var ERAS = { clasico: 1, establecido: 1, nuevo: 1 };
  function era(e) { return ERAS[e] ? e : 'clasico'; }

  var main = document.getElementById('main');
  // Lo último que llegó y si se lee el original (Garum 0.0.27: títulos, introducciones y notas traducidos por el
  // servidor; un solo interruptor, «Traducido · Ver el original», como en la app).
  var data = null, original = false;
  function render() { show(type === 'collection' ? collection(data) : place(data)); }
  function toggle() {
    var b = el('button', 'orig', original ? t.see_translation : t.see_original);
    b.type = 'button';
    b.setAttribute('aria-pressed', original ? 'true' : 'false');
    b.onclick = function () { original = !original; render(); };
    return b;
  }
  function show(nodes) {
    main.textContent = '';
    var box = el('div', 'content');
    nodes.forEach(function (n) { box.appendChild(n); });
    main.appendChild(box);
    main.setAttribute('aria-busy', 'false');
  }

  function collection(d) {
    var items = d.items || [];
    var translated = !!(d.text_translated && d.title_local) || items.some(function (it) { return it.note_translated && it.note_local; });
    var useLocal = translated && !original;
    var title = useLocal && d.text_translated && d.title_local ? d.title_local : d.title;
    var intro = useLocal && d.text_translated ? d.intro_local : d.intro;
    document.title = title + ' · Garum';
    var nodes = [];
    var kind = d.kind === 'itinerario' ? 'itinerary' : 'list';
    nodes.push(el('p', 'eyebrow', t[kind] + ' · ' + plural(kind === 'itinerary' ? t.stops : t.places, items.length)));
    nodes.push(el('h1', null, title));
    nodes.push(el('p', 'byline', fmt(t.by, { who: who(d.owner) })));
    if (intro) nodes.push(el('p', 'intro', intro));
    if (translated) nodes.push(toggle());
    var ol = el('ol', 'items');
    items.forEach(function (it, i) {
      var li = el('li', 'item');
      var e = era(it.era), mark;
      if (kind === 'itinerary') {
        mark = el('span', 'mark num ' + (it.unvalidated ? 'unvalidated' : 'bg-' + e + ' ' + e), String(i + 1));
      } else {
        mark = el('span', 'mark');
        mark.appendChild(el('span', 'shape ' + (it.unvalidated ? 'unvalidated' : 'bg-' + e + ' ' + e)));
      }
      mark.setAttribute('aria-hidden', 'true');
      li.appendChild(mark);
      var body = el('div');
      var h = el('h2', null, it.name);
      if (it.unvalidated) { var tag = el('span', 'tag', t.unvalidated); tag.title = t.unvalidated_hint; h.appendChild(tag); }
      body.appendChild(h);
      var m = meta([labels(it.kind_labels)[0], price(it.price), it.neighborhood || it.city]);
      if (m) body.appendChild(el('p', 'meta', m));
      var note = useLocal && it.note_translated && it.note_local ? it.note_local : it.note;
      if (note) body.appendChild(el('blockquote', null, quoted(note)));
      var a = el('a', 'maps', t.maps); a.href = mapsURL(it.name, it.lat, it.lng); a.rel = 'noopener';
      body.appendChild(a);
      li.appendChild(body);
      ol.appendChild(li);
    });
    nodes.push(ol);
    return nodes;
  }

  function place(d) {
    document.title = d.name + ' · Garum';
    var nodes = [];
    if (t.era[d.era]) nodes.push(el('p', 'eyebrow', t.era[d.era]));
    nodes.push(el('h1', null, d.name));
    var m = meta([labels(d.kind_labels).concat(labels(d.cuisine_labels)).join(' · '), price(d.price)]);
    if (m) nodes.push(el('p', 'byline', m));
    var where = meta([d.address, d.neighborhood, d.city]);
    if (where) nodes.push(el('p', 'meta', where));
    if (d.season_closed) {
      var date = d.reopens_on ? new Date(d.reopens_on + 'T12:00:00').toLocaleDateString(lang, { day: 'numeric', month: 'long' }) : null;
      nodes.push(el('p', 'season', date ? fmt(t.season_until, { date: date }) : t.season));
    }
    var a = el('a', 'maps', t.maps); a.href = mapsURL(d.name, d.lat, d.lng); a.rel = 'noopener';
    nodes.push(a);
    var notes = d.notes || [];
    var translated = notes.some(function (n) { return n.translated && n.original; });
    var useLocal = !original;
    if ((d.reasons || []).length || notes.length) {
      var why = el('section', 'section');
      why.appendChild(el('h2', null, t.why));
      if ((d.reasons || []).length) {
        var ul = el('ul', 'chips');
        d.reasons.forEach(function (r) { ul.appendChild(el('li', null, r.label)); });
        why.appendChild(ul);
      }
      notes.forEach(function (n) {
        var box = el('div', 'note');
        box.appendChild(el('p', null, !useLocal && n.original ? n.original : n.note));
        var by = fmt(t.signed, { who: n.username ? n.alias + ' · @' + n.username : n.alias });
        box.appendChild(el('p', 'who', n.translated && !n.original && useLocal ? by + ' · ' + t.translated : by));
        why.appendChild(box);
      });
      if (translated) why.appendChild(toggle());
      nodes.push(why);
    }
    var order = !useLocal && (d.order_this_original || []).length ? d.order_this_original : (d.order_this || []);
    if (order.length) {
      var sec = el('section', 'section');
      sec.appendChild(el('h2', null, t.order));
      var ol = el('ul', 'order');
      order.forEach(function (o) { ol.appendChild(el('li', null, o)); });
      sec.appendChild(ol);
      nodes.push(sec);
    }
    return nodes;
  }

  function state(title, body, retry) {
    var box = el('div', 'state');
    box.appendChild(el('h1', null, title));
    box.appendChild(el('p', null, body));
    if (retry) { var b = el('button', null, t.retry); b.type = 'button'; b.onclick = load; box.appendChild(b); }
    show([box]);
  }

  function load() {
    var c = code();
    if (!c) { state(t.gone_title, type === 'collection' ? t.gone_c : t.gone_p); return; }
    main.setAttribute('aria-busy', 'true');
    fetch(API, {
      method: 'POST',
      headers: { 'apikey': KEY, 'Content-Type': 'application/json', 'Accept-Language': lang },
      body: JSON.stringify({ p_type: type, p_code: c })
    }).then(function (r) {
      if (!r.ok) throw new Error(String(r.status));
      return r.json();
    }).then(function (d) {
      if (!d || d.type !== type) { state(t.gone_title, type === 'collection' ? t.gone_c : t.gone_p); return; }
      data = d; original = false;
      render();
    }).catch(function () { state(t.error_title, t.error_body, true); });
  }

  // The app box and the footer, in the reader's language.
  (function () {
    var cta = document.getElementById('cta');
    cta.querySelector('h2').textContent = t.app_title;
    cta.querySelector('.line').textContent = t.app_line;
    var store = cta.querySelector('.store');
    var note = cta.querySelector('.note-line');
    if (ON_STORE) {
      store.textContent = t.app_store; store.href = 'https://apps.apple.com/app/id' + APP_ID; store.hidden = false;
      note.textContent = t.app_installed;
    } else {
      store.hidden = true;
      note.textContent = t.app_not_yet;
    }
    var f = document.getElementById('foot');
    var legal = lang === 'es' ? { p: 'privacidad', t: 'condiciones' } : { p: 'privacy', t: 'terms' };
    f.querySelector('.more').textContent = t.more;
    f.querySelector('.more').href = '../../' + (lang === 'es' ? 'es/' : '') + 'apps/garum.html';
    f.querySelector('.privacy').textContent = t.privacy;
    f.querySelector('.privacy').href = '../' + legal.p + '/';
    f.querySelector('.terms').textContent = t.terms;
    f.querySelector('.terms').href = '../' + legal.t + '/';
    document.querySelector('meta[name=description]').setAttribute('content', type === 'collection' ? t.desc_c : t.desc_p);
    document.getElementById('loading').textContent = t.loading;
  })();

  load();
})();
'''


def page(kind):
    desc = T['en']['desc_c'] if kind == 'collection' else T['en']['desc_p']
    banner = f'<meta name="apple-itunes-app" content="app-id={GARUM_APP_ID}">\n' if GARUM_ON_STORE else ''
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="robots" content="noindex, nofollow">
<meta name="referrer" content="no-referrer">
<meta name="format-detection" content="telephone=no">
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; connect-src {BACKEND}; img-src 'self'; style-src 'self'; script-src 'self'; base-uri 'none'; form-action 'none'">
<meta name="color-scheme" content="light dark">
<meta name="theme-color" content="#F3EFE6" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#151412" media="(prefers-color-scheme: dark)">
<meta name="description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Garum">
<meta property="og:title" content="Garum">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="https://seizeapps.com/assets/icons/garum.png">
<meta name="twitter:card" content="summary">
{banner}<title>Garum</title>
<link rel="icon" type="image/png" href="../../assets/icons/garum.png">
<link rel="apple-touch-icon" href="../../assets/icons/garum.png">
<link rel="stylesheet" href="../share.css?v={ASSETS_V}">
</head>
<body data-type="{kind}">
<div class="wrap">
  <header class="top">
    <img src="../../assets/icons/garum.png" alt="" width="36" height="36">
    <span class="name">Garum</span>
    <span class="by">Seize Apps</span>
  </header>
  <main id="main" aria-busy="true" aria-live="polite">
    <p class="sr" id="loading"></p>
    <div class="skeleton" aria-hidden="true"><div class="s"></div><div class="h"></div><div class="s"></div><div class="b"></div><div class="b"></div><div class="b"></div></div>
  </main>
  <aside class="cta" id="cta">
    <img src="../../assets/icons/garum.png" alt="" width="56" height="56">
    <div>
      <h2>Garum</h2>
      <p class="line"></p>
      <a class="store" hidden></a>
      <p class="note-line"></p>
    </div>
  </aside>
  <footer id="foot">
    <a class="more" href="../../apps/garum.html"></a>
    <a class="privacy" href="../privacy/"></a>
    <a class="terms" href="../terms/"></a>
    <span>© 2026 Seize Apps</span>
  </footer>
</div>
<noscript><p>Garum · <a href="https://seizeapps.com/apps/garum.html">seizeapps.com/apps/garum.html</a></p></noscript>
<script src="../share.js?v={ASSETS_V}"></script>
</body>
</html>
'''


def build_garum_share():
    write('garum/c/index.html', page('collection'))
    write('garum/p/index.html', page('place'))
    write('garum/share.css', CSS)
    write('garum/share.js', JS % {
        'api': json.dumps(BACKEND + '/rest/v1/rpc/shared_page'), 'key': json.dumps(PUBLISHABLE_KEY),
        'on_store': 'true' if GARUM_ON_STORE else 'false', 'app_id': json.dumps(GARUM_APP_ID),
        'texts': json.dumps(T, ensure_ascii=False)})
    write('.well-known/apple-app-site-association', json.dumps(AASA, indent=2) + '\n')
    # GitHub Pages (Jekyll) leaves out folders that start with a dot unless they're included.
    write('_config.yml', '# GitHub Pages: plain HTML, generated by tools/gen_site.py. Jekyll skips dot-folders;\n'
                         '# .well-known holds apple-app-site-association (Garum\'s Universal Links, gen_garum_share.py).\n'
                         '# docs/, tools/ and README.md are the site\'s source notes, not pages: they stay off the web.\n'
                         'include:\n  - .well-known\n'
                         'exclude:\n  - docs\n  - tools\n  - README.md\n')
