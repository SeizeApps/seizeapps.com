"""Edits the studio-wide privacy policy (privacy.html, es/, fr/) so that the seven apps with their own pages
(tools/gen_legal_apps.py) do not contradict them. Applied to LEGAL by gen_legal_copy.py; the section ids stay
(#cycle-timers, #tempo, ... are linked from shipped builds), each section becomes a short pointer, and the
exception paragraphs and the RevenueCat lists at the top are corrected. Every substitution must match exactly
once, so a wording change in the copy files fails the build instead of silently skipping.

Tempo stays in the RevenueCat lists: the live Tempo 1.0.3 (59, release/tempo-main ed010b291) ships RevenueCat; only
main's 1.0.2 does not. Cycle: the live build is 0.0.22 (feedback to Supabase + a Telegram copy, funnel to RevenueCat);
0.0.23 (not yet on sale) turns feedback into a mailto: draft and keeps the funnel on the device, so the Cycle texts
name the version."""
import re

FOLDER = {'cycle-timers': 'cycle', 'tempo': 'tempo', 'readably': 'readably', 'atino': 'atino', 'roomy': 'roomy',
          'gaminghub': 'gaminghub', 'overbit': 'overbit'}
NAME = {'cycle-timers': 'Cycle Timers', 'tempo': 'Tempo', 'readably': 'Readably', 'atino': 'Atino', 'roomy': 'Roomy',
        'gaminghub': 'GamingHub', 'overbit': 'Overbit'}

SUMMARY = {
 'en': {
  'cycle-timers': "Your timers stay on your device, in a container shared only with the app's own widgets; there is no account, no advertising, no iCloud and no server of ours that receives them. Purchase bookkeeping goes to RevenueCat (an anonymous ID, your device's vendor identifier and your Cycle Pro purchase; up to version 0.0.22 also how you moved through the Pro screen). From version 0.0.23 feedback is an email you send from your own mail app; before that, Message the developer (Cycle Pro) sent your message to a server of ours, as its policy explains. Your timers, history and notes never leave the device.",
  'tempo': "Your work history, zones and settings stay on your iPhone, with no account, no advertising, no iCloud and no server of ours that receives them. Location is used on the device; only the text you search for and the coordinates of your first home and work zones go to Apple's maps service. Purchase bookkeeping goes to RevenueCat (an anonymous ID, your device's vendor identifier, your Tempo purchases and which Pro screen you opened).",
  'readably': "What you read stays on your iPhone and no text goes to any AI service: every voice runs on the device. Readably downloads its voices once from Hugging Face when you ask for them, fetches a web page only when a Pro user names it, and uses RevenueCat for purchase bookkeeping. There is no account and no server of ours.",
  'atino': "Atino ranks job ads against your CV. Your CV stays on your iPhone: Atino never uploads the PDF, and it removes your name and contact details on the phone before any text leaves it. Only after you allow it, the redacted text is sent through the Seize relay to Command Code and TypeSafe AI (Jev) to rank jobs and explain the fit; they may keep it under their own terms. The relay, which runs on Supabase in the EU (Frankfurt, Germany), keeps a small record per install and deletes it after 60 days without activity. There is no account, no advertising and no tracking. Apple processes the subscription; once you have consented, Atino also reports it to RevenueCat for purchase analytics, and RevenueCat receives no CV text.",
  'roomy': "Your photos, videos and their metadata never leave your iPhone. There is no account, no advertising, no tracking and no server of ours; RevenueCat receives an anonymous ID, your device's vendor identifier, your Roomy purchases and which screen led you to the purchase screen. If a photo is in iCloud Photos, iOS downloads it for Roomy when needed, between your iPhone and Apple.",
  'gaminghub': "There is no account. To run a room, GamingHub sends your display name, avatar, an anonymous ID and your moves to our server (Supabase), where the other players in that room can see them; rooms are deleted when they empty and in any case after 12 hours. Secret game data goes only to your device, the camera is used only to scan a room's QR code, and RevenueCat handles purchase bookkeeping.",
  'overbit': "There is no account. Overbit keeps one record per install, under a random ID, on our server (Supabase) to fetch prices and push alerts, and you can delete it in the app; what you type in the Pro feedback box reaches us, and RevenueCat handles purchase bookkeeping. Nothing is sold and nothing tracks you.",
 },
 'es': {
  'cycle-timers': "Tus temporizadores se quedan en tu dispositivo, en un contenedor compartido solo con los widgets de la propia app; no hay cuenta, ni publicidad, ni iCloud, ni servidor nuestro que los reciba. La contabilidad de compras va a RevenueCat (un identificador anónimo, el identificador de proveedor de tu dispositivo y tu compra de Cycle Pro; hasta la versión 0.0.22 también cómo avanzabas por la pantalla Pro). Desde la versión 0.0.23 los comentarios son un correo que envías desde tu propia app de correo; antes, Message the developer (Cycle Pro) enviaba tu mensaje a un servidor nuestro, como explica su política. Tus temporizadores, tu historial y tus notas nunca salen del dispositivo.",
  'tempo': "Tu historial de trabajo, tus zonas y tus ajustes se quedan en tu iPhone, sin cuenta, sin publicidad, sin iCloud y sin ningún servidor nuestro que los reciba. La ubicación se usa en el dispositivo; solo el texto que buscas y las coordenadas de tu primera zona de casa y de trabajo van al servicio de mapas de Apple. La contabilidad de compras va a RevenueCat (un identificador anónimo, el identificador de proveedor de tu dispositivo, tus compras de Tempo y qué pantalla Pro abriste).",
  'readably': "Lo que lees se queda en tu iPhone y ningún texto va a ningún servicio de IA: todas las voces funcionan en el dispositivo. Readably descarga sus voces una sola vez desde Hugging Face cuando se lo pides, pide una página web solo cuando un usuario Pro la indica, y usa RevenueCat para la contabilidad de compras. No hay cuenta ni servidor nuestro.",
  'atino': "Atino ordena ofertas de empleo frente a tu CV. Tu CV se queda en tu iPhone: Atino nunca sube el PDF y quita tu nombre y tus datos de contacto en el teléfono antes de que salga ningún texto. Solo después de que lo permitas, el texto redactado se envía a través de la pasarela de Seize a Command Code y TypeSafe AI (Jev) para ordenar las ofertas y explicar el encaje; pueden conservarlo según sus propias condiciones. La pasarela, que funciona en Supabase en la UE (Fráncfort, Alemania), guarda un registro pequeño por instalación y lo borra a los 60 días sin actividad. No hay cuenta, ni publicidad, ni seguimiento. Apple procesa la suscripción; una vez que has dado tu permiso, Atino también la comunica a RevenueCat para analítica de compras, y RevenueCat no recibe ningún texto del CV.",
  'roomy': "Tus fotos, vídeos y sus metadatos nunca salen de tu iPhone. No hay cuenta, ni publicidad, ni seguimiento, ni servidor nuestro; RevenueCat recibe un identificador anónimo, el identificador de proveedor de tu dispositivo, tus compras de Roomy y qué pantalla te llevó a la de compra. Si una foto está en iCloud Fotos, iOS la descarga para Roomy cuando hace falta, entre tu iPhone y Apple.",
  'gaminghub': "No hay cuenta. Para llevar una sala, GamingHub envía tu nombre, tu avatar, un identificador anónimo y tus jugadas a nuestro servidor (Supabase), donde las otras personas de esa sala pueden verlos; las salas se borran cuando se vacían y, en todo caso, a las 12 horas. Los datos secretos de la partida van solo a tu dispositivo, la cámara solo se usa para escanear el QR de una sala y RevenueCat se ocupa de la contabilidad de compras.",
  'overbit': "No hay cuenta. Overbit guarda un registro por instalación, con un identificador aleatorio, en nuestro servidor (Supabase) para traer precios y enviar alertas, y puedes borrarlo en la app; lo que escribes en el buzón de comentarios Pro nos llega, y RevenueCat se ocupa de la contabilidad de compras. No se vende nada y nada te rastrea.",
 },
 'fr': {
  'cycle-timers': "Tes minuteurs restent sur ton appareil, dans un conteneur partagé seulement avec les widgets de l’app ; il n’y a ni compte, ni publicité, ni iCloud, ni serveur à nous qui les reçoive. Le suivi des achats passe par RevenueCat (un identifiant anonyme, l’identifiant de fournisseur de ton appareil et ton achat de Cycle Pro ; jusqu’à la version 0.0.22, aussi ton parcours dans l’écran Pro). Depuis la version 0.0.23, les commentaires sont un e-mail que tu envoies depuis ta propre app de messagerie ; avant, Message the developer (Cycle Pro) envoyait ton message à un serveur à nous, comme l’explique sa politique. Tes minuteurs, ton historique et tes notes ne quittent jamais l’appareil.",
  'tempo': "Ton historique de travail, tes zones et tes réglages restent sur ton iPhone, sans compte, sans publicité, sans iCloud et sans aucun serveur à nous qui les reçoive. La localisation est utilisée sur l’appareil ; seuls le texte que tu cherches et les coordonnées de ta première zone de domicile et de travail vont au service de cartes d’Apple. Le suivi des achats passe par RevenueCat (un identifiant anonyme, l’identifiant de fournisseur de ton appareil, tes achats de Tempo et l’écran Pro que tu as ouvert).",
  'readably': "Ce que tu lis reste sur ton iPhone et aucun texte ne va à un service d’IA : toutes les voix fonctionnent sur l’appareil. Readably télécharge ses voix une seule fois depuis Hugging Face quand tu le demandes, récupère une page web seulement quand un utilisateur Pro l’indique, et utilise RevenueCat pour le suivi des achats. Il n’y a ni compte ni serveur à nous.",
  'atino': "Atino classe des offres d’emploi par rapport à ton CV. Ton CV reste sur ton iPhone : Atino ne téléverse jamais le PDF et retire ton nom et tes coordonnées sur le téléphone avant qu’aucun texte ne parte. Seulement après ton autorisation, le texte expurgé est envoyé par le relais de Seize à Command Code et TypeSafe AI (Jev) pour classer les offres et expliquer l’adéquation ; ils peuvent le conserver selon leurs propres conditions. Le relais, qui tourne sur Supabase dans l’UE (Francfort, Allemagne), conserve un petit enregistrement par installation et le supprime après 60 jours sans activité. Il n’y a ni compte, ni publicité, ni suivi. Apple traite l’abonnement ; une fois ton autorisation donnée, Atino le signale aussi à RevenueCat pour la mesure des achats, et RevenueCat ne reçoit aucun texte du CV.",
  'roomy': "Tes photos, vidéos et leurs métadonnées ne quittent jamais ton iPhone. Il n’y a ni compte, ni publicité, ni suivi, ni serveur à nous ; RevenueCat reçoit un identifiant anonyme, l’identifiant de fournisseur de ton appareil, tes achats Roomy et l’écran qui t’a mené à celui d’achat. Si une photo est dans iCloud Photos, iOS la télécharge pour Roomy quand il le faut, entre ton iPhone et Apple.",
  'gaminghub': "Il n’y a pas de compte. Pour faire tourner un salon, GamingHub envoie ton nom, ton avatar, un identifiant anonyme et tes coups à notre serveur (Supabase), où les autres joueurs du salon peuvent les voir ; les salons sont supprimés quand ils se vident et, en tout cas, au bout de 12 heures. Les données secrètes de la partie vont seulement à ton appareil, la caméra ne sert qu’à scanner le QR d’un salon et RevenueCat s’occupe du suivi des achats.",
  'overbit': "Il n’y a pas de compte. Overbit conserve un enregistrement par installation, sous un identifiant aléatoire, sur notre serveur (Supabase) pour récupérer les prix et envoyer les alertes, et tu peux le supprimer dans l’app ; ce que tu écris dans la boîte de commentaires Pro nous parvient, et RevenueCat s’occupe du suivi des achats. Rien n’est vendu et rien ne te suit.",
 },
}
LINKS = {
 'en': ('The full details — what is stored, what leaves your device, purchases, deletion and your rights — are in <a href="{p}">{n} privacy policy</a>; its <a href="{t}">terms</a> and <a href="{s}">support</a> pages are alongside.', 'Published on the App Store by {by}.'),
 'es': ('Los detalles completos —qué se guarda, qué sale de tu dispositivo, compras, borrado y tus derechos— están en <a href="{p}">la política de privacidad de {n}</a> (en inglés{es}); sus <a href="{t}">condiciones</a> y su <a href="{s}">soporte</a> están al lado.', 'Publicada en la App Store por {by}.'),
 'fr': ('Tous les détails — ce qui est conservé, ce qui quitte ton appareil, achats, suppression et tes droits — sont dans <a href="{p}">la politique de confidentialité de {n}</a> (en anglais{es}) ; ses <a href="{t}">conditions</a> et son <a href="{s}">assistance</a> sont à côté.', 'Publiée sur l’App Store par {by}.'),
}
BY = {'cycle-timers': 'Izotz Cristobal Mota', 'atino': 'Izotz Cristobal Mota'}


def nbsp(lang, s):
    """French typography: a no-break space before : and ; (outside tags)."""
    if lang != 'fr': return s
    return re.sub(r'(?<=[^\s>]) ([:;])(?=\s)', '\u00a0\\1', s)


def pointer(lang, sid):
    f = FOLDER[sid]; up = '' if lang == 'en' else '../'
    pg = 'privacidad' if (sid == 'atino' and lang == 'es') else 'privacy'
    p = f'{up}{f}/{pg}.html'
    link, pub = LINKS[lang]
    if sid == 'atino' and lang != 'en':
        link = link.replace('(en inglés{es})', '(en inglés y castellano)').replace('(en anglais{es})', '(en anglais et en espagnol)')
    by = BY.get(sid, 'Izotz Cristobal Mota')
    out = (f'<section id="{sid}">\n  <h3>{NAME[sid]}</h3>\n  <p>{SUMMARY[lang][sid]}</p>\n'
           f'  <p>{link.format(p=p, n=(NAME[sid] + "'" if (lang == 'en' and NAME[sid].endswith('s')) else NAME[sid] + ("'s" if lang == 'en' else '')), t=f"{up}{f}/terms.html", s=f"{up}{f}/support.html", es="")}</p>\n'
           f'  <p><em>{pub.format(by=by)}</em></p>\n  </section>')
    return nbsp(lang, out)


def sub(text, old, new, count=1):
    assert text.count(old) == count, (text.count(old), old[:80])
    return text.replace(old, new)


def patch_body(lang, b):
    def S(t, o, n):
        # French copy mixes no-break spaces (U+00A0, U+202F) before : and ; - match whichever the text uses
        if lang != 'fr': return sub(t, o, n)
        for sep in ('\u202f', '\u00a0', ' '):
            fix = lambda x: re.sub(r'(?<=[^\s>]) ([:;])(?=\s)', sep + r'\1', x)
            if t.count(fix(o)) == 1: return t.replace(fix(o), fix(n))
        raise AssertionError(('no match', o[:80]))
    # 1. per-app sections become pointers
    for sid in FOLDER:
        rx = re.compile(r'<section id="%s">.*?</section>' % sid, re.S)
        n = len(rx.findall(b))
        assert n == 1 or (n == 0 and lang == 'fr' and sid == 'readably'), (lang, sid, n)
        if n: b = rx.sub(lambda m: pointer(lang, sid), b)
    up = '' if lang == 'en' else '../'
    T = {'en': dict(cyc="<strong>Cycle Timers is another exception:</strong> its purchases are reported to RevenueCat for purchase bookkeeping and, up to version 0.0.22, what you wrote in Message the developer (Cycle Pro) was sent to a server of ours, so it has <a href=\"cycle/privacy.html\">its own privacy policy</a>.",
                    tem="<strong>Tempo is another exception:</strong> it uses your location on your iPhone, Apple's maps service receives the places you search for and the coordinates of your first home and work zones, and its purchases are reported to RevenueCat for purchase analytics, so it has <a href=\"tempo/privacy.html\">its own privacy policy</a>.",
                    roo="<strong>Roomy is another exception:</strong> from version 0.0.3 its purchases are reported to RevenueCat for purchase analytics, so it has <a href=\"roomy/privacy.html\">its own privacy policy</a> (English).",
                    ),
         'es': dict(cyc="<strong>Cycle Timers es otra excepción:</strong> sus compras se comunican a RevenueCat para la contabilidad de compras y, hasta la versión 0.0.22, lo que escribías en Message the developer (Cycle Pro) se enviaba a un servidor nuestro, así que tiene <a href=\"../cycle/privacy.html\">su propia política de privacidad</a> (en inglés).",
                    tem="<strong>Tempo es otra excepción:</strong> usa tu ubicación en tu iPhone, el servicio de mapas de Apple recibe los sitios que buscas y las coordenadas de tu primera zona de casa y de trabajo, y sus compras se comunican a RevenueCat para analítica de compras, así que tiene <a href=\"../tempo/privacy.html\">su propia política de privacidad</a> (en inglés).",
                    roo="<strong>Roomy es otra excepción:</strong> desde la versión 0.0.3 sus compras se comunican a RevenueCat para analítica de compras, así que tiene <a href=\"../roomy/privacy.html\">su propia política de privacidad</a> (en inglés).",
                    ),
         'fr': dict(cyc="<strong>Cycle Timers est une autre exception :</strong> ses achats sont signalés à RevenueCat pour le suivi des achats et, jusqu’à la version 0.0.22, ce que tu écrivais dans Message the developer (Cycle Pro) était envoyé à un serveur à nous ; elle a donc <a href=\"../cycle/privacy.html\">sa propre politique de confidentialité</a> (en anglais).",
                    tem="<strong>Tempo est une autre exception :</strong> il utilise ta position sur ton iPhone, le service de cartes d’Apple reçoit les lieux que tu cherches et les coordonnées de ta première zone de domicile et de travail, et ses achats sont signalés à RevenueCat pour le suivi des achats ; il a donc <a href=\"../tempo/privacy.html\">sa propre politique de confidentialité</a> (en anglais).",
                    roo="<strong>Roomy est une autre exception :</strong> depuis la version 0.0.3, ses achats sont signalés à RevenueCat pour la mesure des achats ; elle a donc <a href=\"../roomy/privacy.html\">sa propre politique de confidentialité</a> (en anglais).",
                    )}[lang]
    def para(b, who, new):
        rx = re.compile(r'<p><strong>%s</strong>.*?</p>' % re.escape(who).replace('\\ :', '[\\s\u00a0\u202f]:'), re.S)
        assert len(rx.findall(b)) == 1, (lang, who)
        return rx.sub(lambda m: '<p>' + nbsp(lang, new) + '</p>', b)
    first = {'en': ('Cycle Timers is another exception:', 'Tempo is another exception:', 'Roomy is another exception:'),
             'es': ('Cycle Timers es otra excepción:', 'Tempo es otra excepción:', 'Roomy es otra excepción:'),
             'fr': ('Cycle Timers est une autre exception :', 'Tempo est une autre exception :', 'Roomy est une autre exception :')}[lang]
    b = para(b, first[0], T['cyc']); b = para(b, first[1], T['tem']); b = para(b, first[2], T['roo'])
    # 2. Atino exception paragraph: consent first, own page
    b = {'en': lambda: S(b, "and its subscription is reported to RevenueCat for purchase analytics, so it has <a href=\"atino/privacy/\">its own privacy policy</a>.",
                           "and, once you have consented, its subscription is reported to RevenueCat for purchase analytics, so it has <a href=\"atino/privacy.html\">its own privacy policy</a>."),
         'es': lambda: S(b, "y su suscripción se comunica a RevenueCat para analítica de compras, así que tiene <a href=\"../atino/privacidad/\">su propia política de privacidad</a>.",
                           "y, una vez que has dado tu permiso, su suscripción se comunica a RevenueCat para analítica de compras, así que tiene <a href=\"../atino/privacidad.html\">su propia política de privacidad</a>."),
         'fr': lambda: S(b, "et son abonnement est signalé à RevenueCat pour la mesure des achats ; elle a donc <a href=\"../atino/privacy/\">sa propre politique de confidentialité</a> (en anglais et en espagnol).",
                           "et, une fois ton autorisation donnée, son abonnement est signalé à RevenueCat pour la mesure des achats ; elle a donc <a href=\"../atino/privacy.html\">sa propre politique de confidentialité</a> (en anglais et en espagnol).")}[lang]()
    # 3. Roomy joins the RevenueCat lists (Tempo is already in them: the live 1.0.3 ships RevenueCat)
    if lang == 'en':
        b = S(b, 'RevenueCat\'s purchase analytics in Atino, Cycle Timers, GamingHub, Tempo, Readably, Yaybo and', 'RevenueCat\'s purchase analytics in Atino, Cycle Timers, GamingHub, Tempo, Roomy, Readably, Yaybo and')
        b = S(b, '(Atino, Cycle Timers, GamingHub, Tempo, Readably and, from version 0.1.2, Overbit also report', '(Atino, Cycle Timers, GamingHub, Tempo, Roomy, Readably and, from version 0.1.2, Overbit also report')
        b = S(b, '<li><strong>In your iCloud.</strong> Our apps sync through your personal iCloud account under Apple\'s terms, unless you turn it off in Settings or the app\'s own section below says otherwise — we never have access to it.</li>',
                   '<li><strong>In your iCloud.</strong> Apps that sync do so through your personal iCloud account under Apple\'s terms, unless you turn it off in Settings or the app\'s own section below says otherwise — we never have access to it. Cycle Timers, Tempo, Readably, Atino, Roomy, GamingHub and Overbit do not sync through iCloud.</li>')
    elif lang == 'es':
        b = S(b, 'RevenueCat en Atino, Cycle Timers, GamingHub, Tempo, Readably, Yaybo y', 'RevenueCat en Atino, Cycle Timers, GamingHub, Tempo, Roomy, Readably, Yaybo y')
        b = S(b, '(Atino, Cycle Timers, GamingHub, Tempo, Readably y, desde la versión 0.1.2, Overbit también', '(Atino, Cycle Timers, GamingHub, Tempo, Roomy, Readably y, desde la versión 0.1.2, Overbit también')
        b = S(b, '<li><strong>En tu iCloud.</strong> Nuestras apps sincronizan a través de tu cuenta personal de iCloud, bajo las condiciones de Apple, salvo que lo desactives en Ajustes o que la sección de esa app diga otra cosa; nosotros nunca tenemos acceso.</li>',
                   '<li><strong>En tu iCloud.</strong> Las apps que sincronizan lo hacen a través de tu cuenta personal de iCloud, bajo las condiciones de Apple, salvo que lo desactives en Ajustes o que la sección de esa app diga otra cosa; nosotros nunca tenemos acceso. Cycle Timers, Tempo, Readably, Atino, Roomy, GamingHub y Overbit no sincronizan por iCloud.</li>')
    else:
        b = S(b, 'RevenueCat dans Atino, Cycle Timers, GamingHub, Tempo, Yaybo et', 'RevenueCat dans Atino, Cycle Timers, GamingHub, Tempo, Roomy, Yaybo et')
        b = S(b, '(Atino, Cycle Timers, GamingHub, Tempo et, depuis la version 0.1.2, Overbit signalent aussi', '(Atino, Cycle Timers, GamingHub, Tempo, Roomy et, depuis la version 0.1.2, Overbit signalent aussi')
        b = S(b, '<li><strong>Dans ton iCloud.</strong> Nos apps se synchronisent via ton compte iCloud personnel, selon les conditions d’Apple, sauf si tu désactives la synchronisation dans Réglages ou si la section de cette app dit autre chose ; nous n’y avons jamais accès.</li>',
                   '<li><strong>Dans ton iCloud.</strong> Les apps qui se synchronisent le font via ton compte iCloud personnel, selon les conditions d’Apple, sauf si tu désactives la synchronisation dans Réglages ou si la section de cette app dit autre chose ; nous n’y avons jamais accès. Cycle Timers, Tempo, Atino, Roomy, GamingHub et Overbit ne se synchronisent pas par iCloud.</li>')
    return b


def patch_legal(LEGAL):
    for lang in ('en', 'es', 'fr'):
        LEGAL[lang]['privacy']['body'] = patch_body(lang, LEGAL[lang]['privacy']['body'])
    return LEGAL
