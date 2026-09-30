// Garum's share page (tools/gen_garum_share.py): reads the code from the address, asks the server and draws it.
// Everything written by people goes in with textContent, never as HTML.
(function () {
  'use strict';
  var API = "https://rbiyqvizjwcysfhvdyox.supabase.co/rest/v1/rpc/shared_page", KEY = "sb_publishable_rTonGbzHP5mre-oHDfxcVQ_vJOmUaBa", ON_STORE = false, APP_ID = "6816385891", T = {"en": {"loading": "Loading…", "list": "List", "itinerary": "Itinerary", "places": ["{n} place", "{n} places"], "stops": ["{n} stop", "{n} stops"], "by": "by {who}", "unvalidated": "Not validated yet", "unvalidated_hint": "Proposed by the author; not on Garum’s map yet.", "maps": "Open in Maps", "why": "Why it’s here", "order": "What to order", "signed": "Signed by {who}", "translated": "Translated", "see_original": "Translated · See the original", "see_translation": "See the translation", "season": "Closed for the season", "season_until": "Closed for the season · back on {date}", "era": {"clasico": "Classic · over 25 years", "establecido": "Established · 3 to 25 years", "nuevo": "New · under 3 years"}, "gone_title": "This link doesn’t lead anywhere now", "gone_c": "The collection may have been deleted or made private by its author.", "gone_p": "The place may have closed or left Garum’s map.", "error_title": "This page couldn’t load", "error_body": "Check your connection and try again.", "retry": "Try again", "app_title": "Garum", "app_line": "A map of places that are there for a reason, each with its why, everything signed.", "app_store": "Download on the App Store", "app_installed": "If you have Garum on your iPhone, this link opens in the app.", "app_not_yet": "Garum is an iPhone app, and it isn’t on the App Store yet.", "more": "About Garum", "privacy": "Privacy", "terms": "Terms", "desc_c": "A collection on Garum", "desc_p": "A place on Garum"}, "es": {"loading": "Cargando…", "list": "Lista", "itinerary": "Itinerario", "places": ["{n} sitio", "{n} sitios"], "stops": ["{n} parada", "{n} paradas"], "by": "de {who}", "unvalidated": "Sin validar", "unvalidated_hint": "Lo ha propuesto el autor; aún no está en el mapa de Garum.", "maps": "Abrir en Mapas", "why": "Por qué está aquí", "order": "Qué pedir", "signed": "Firmado por {who}", "translated": "Traducido", "see_original": "Traducido · Ver el original", "see_translation": "Ver la traducción", "season": "Cerrado por temporada", "season_until": "Cerrado por temporada · vuelve el {date}", "era": {"clasico": "Clásico · más de 25 años", "establecido": "Establecido · de 3 a 25 años", "nuevo": "Nuevo · menos de 3 años"}, "gone_title": "Este enlace ya no lleva a nada", "gone_c": "Puede que su autor haya borrado la colección o la haya hecho privada.", "gone_p": "Puede que el sitio haya cerrado o haya salido del mapa de Garum.", "error_title": "No se ha podido cargar", "error_body": "Mira la conexión y vuelve a probar.", "retry": "Volver a probar", "app_title": "Garum", "app_line": "Un mapa de sitios que están por algo, cada uno con su porqué, todo firmado.", "app_store": "Descargar en el App Store", "app_installed": "Si tienes Garum en el iPhone, este enlace se abre en la app.", "app_not_yet": "Garum es una app para iPhone y todavía no está en el App Store.", "more": "Sobre Garum", "privacy": "Privacidad", "terms": "Condiciones", "desc_c": "Una colección en Garum", "desc_p": "Un sitio en Garum"}, "fr": {"loading": "Chargement…", "list": "Liste", "itinerary": "Itinéraire", "places": ["{n} lieu", "{n} lieux"], "stops": ["{n} étape", "{n} étapes"], "by": "par {who}", "unvalidated": "Pas encore validé", "unvalidated_hint": "Proposé par l’auteur ; pas encore sur la carte de Garum.", "maps": "Ouvrir dans Plans", "why": "Pourquoi il est là", "order": "Que commander", "signed": "Signé par {who}", "translated": "Traduit", "see_original": "Traduit · Voir l’original", "see_translation": "Voir la traduction", "season": "Fermé pour la saison", "season_until": "Fermé pour la saison · retour le {date}", "era": {"clasico": "Classique · plus de 25 ans", "establecido": "Établi · de 3 à 25 ans", "nuevo": "Nouveau · moins de 3 ans"}, "gone_title": "Ce lien ne mène plus nulle part", "gone_c": "L’auteur a peut-être supprimé la collection ou l’a rendue privée.", "gone_p": "Le lieu a peut-être fermé ou quitté la carte de Garum.", "error_title": "Impossible de charger la page", "error_body": "Vérifie ta connexion et réessaie.", "retry": "Réessayer", "app_title": "Garum", "app_line": "Une carte de lieux qui sont là pour une raison, chacun avec son pourquoi, tout est signé.", "app_store": "Télécharger dans l’App Store", "app_installed": "Si tu as Garum sur ton iPhone, ce lien s’ouvre dans l’app.", "app_not_yet": "Garum est une app pour iPhone, et elle n’est pas encore sur l’App Store.", "more": "À propos de Garum", "privacy": "Confidentialité", "terms": "Conditions", "desc_c": "Une collection sur Garum", "desc_p": "Un lieu sur Garum"}};
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
