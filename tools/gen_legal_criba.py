"""Criba's own legal pages (privacy and terms), 26/09/2026.

Criba is the first Seize app with accounts, a server and user content, so it can't live under
the studio-wide policy («no accounts, nothing on our side»). Its pages:
  /criba/privacidad/  /criba/condiciones/   (castellano, the ones the app opens in Spanish)
  /criba/privacy/     /criba/terms/         (English)
Built with gen_site's chrome; run `python3 tools/gen_site.py`, which calls build_criba().
"""
from gen_site import head, header, footer, write

UPDATED = {'es': 'En vigor desde el 26 de septiembre de 2026', 'en': 'Effective September 26, 2026'}

PRIVACY = {
'es': '''
  <p class="eyebrow">Criba · Legal</p>
  <h1>Privacidad de Criba</h1>
  <p class="effective">{updated}</p>
  <p><strong>La versión corta:</strong> mirar el mapa no pide nada. Si decides aportar (proponer, respaldar, comentar, seguir a gente), entras con Apple, eliges un nombre de usuario y un nombre, y lo que aportas se publica con ellos. Tu ubicación no sale del iPhone. Sin publicidad, sin analítica y sin vender nada.</p>

  <h2>Quién es el responsable</h2>
  <p>Criba la publica en el App Store <strong>Sendoa Sola</strong> (Seize Apps, País Vasco, España), que es el responsable del tratamiento. Contacto para todo lo relativo a tus datos: <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>.</p>

  <h2>Qué datos tratamos</h2>
  <ul>
    <li><strong>Sin cuenta:</strong> nada tuyo. La app descarga los sitios publicados y los guarda en el iPhone para abrir al instante.</li>
    <li><strong>Tus Guardados</strong> viven en tu dispositivo y en tu propia cuenta de iCloud (puedes apagar la sincronización en Ajustes). No los vemos.</li>
    <li><strong>Tu ubicación</strong> se usa solo en el iPhone, cuando tocas «Cerca de mí», para centrar el mapa. No se envía a Criba.</li>
    <li><strong>Si entras con Apple:</strong> Apple nos da un identificador de cuenta. Criba no pide tu nombre ni tu correo. Guardamos ese identificador, tu <strong>perfil</strong> (nombre de usuario, nombre y, si los pones, foto, bio y un enlace) y lo que aportas: sitios que propones, respaldos (motivos y comentario), notas si eres Curator, a quién sigues, a quién bloqueas y las denuncias que envías.</li>
    <li><strong>Si activas los avisos:</strong> el identificador de avisos que Apple da a tu iPhone (para enviártelos a través del servicio de avisos de Apple) y qué tipos de aviso quieres recibir. Se borra al cerrar sesión o borrar la cuenta. Los avisos solo tratan de ti (tus propuestas, tus fotos, quién te sigue, tu papel) y nunca son publicidad.</li>
    <li><strong>Registros técnicos:</strong> el servidor anota durante poco tiempo datos técnicos de las peticiones (como la dirección IP) para funcionar y protegerse de abusos.</li>
  </ul>

  <h2>Qué es público</h2>
  <p>Criba es también una red de gustos: <strong>tu perfil (nombre de usuario, nombre, foto, bio y enlace), tus respaldos, tus comentarios, tus notas y los sitios que propones y respaldas son visibles para cualquiera</strong>, y a partir de ellos la app sugiere gente con gustos parecidos. El número de seguidores solo se muestra por tramos (10+, 50+…). Son privados: tu identificador de Apple, a quién bloqueas, las denuncias que envías y las propuestas que aún no han entrado en el mapa.</p>

  <h2>Para qué y con qué base</h2>
  <ul>
    <li>Darte la cuenta y publicar lo que aportas: la ejecución de las <a href="../condiciones/">condiciones de uso</a> que aceptas al entrar.</li>
    <li>Moderar, evitar abusos y mantener el servicio seguro: nuestro interés legítimo.</li>
    <li>Atender denuncias y explicar cada retirada: la obligación legal del Reglamento de Servicios Digitales (DSA).</li>
  </ul>

  <h2>Quién más interviene</h2>
  <ul>
    <li><strong>Supabase</strong> aloja la base de datos y las cuentas, en servidores de la Unión Europea (Fráncfort).</li>
    <li><strong>Apple</strong>: el inicio de sesión, los mapas (MapKit) y tu iCloud, bajo sus condiciones.</li>
    <li>Guardamos <strong>copias de seguridad</strong> de la base de datos en un equipo propio en España durante 30 días.</li>
  </ul>
  <p>No hay SDK de publicidad ni de analítica, y no vendemos ni cedemos datos a nadie.</p>

  <h2>Cuánto tiempo</h2>
  <p>Mientras tengas la cuenta. <strong>Puedes borrarla desde la app</strong> (Ajustes › Tu cuenta › Borrar la cuenta): se eliminan tu perfil, tus respaldos, tus notas, tus seguidos y tus bloqueos, y las propuestas tuyas que nadie más respalde. Las denuncias que enviaste se conservan sin autor, y el registro de las decisiones de moderación que te afectaron se guarda el tiempo que exige la ley. Al borrarla, la app te pide confirmar con Apple y <strong>Criba revoca su acceso a tu cuenta de Apple</strong>. Las copias de seguridad desaparecen en 30 días.</p>

  <h2>Tus derechos</h2>
  <p>Puedes acceder a tus datos, corregirlos (tu perfil se edita en la app), suprimirlos (borrando la cuenta), llevártelos u oponerte a su tratamiento escribiendo a <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>. Si no te respondemos bien, puedes reclamar ante la Agencia Española de Protección de Datos (<a href="https://www.aepd.es" rel="noopener">aepd.es</a>).</p>

  <h2>Menores</h2>
  <p>Para crear una cuenta hay que tener al menos 14 años. Mirar el mapa no pide nada a nadie.</p>

  <h2>Cambios</h2>
  <p>Si cambia algo de lo anterior, lo actualizaremos aquí y en la ficha de privacidad del App Store antes de que llegue a la app.</p>
''',
'en': '''
  <p class="eyebrow">Criba · Legal</p>
  <h1>Criba privacy</h1>
  <p class="effective">{updated}</p>
  <p><strong>The short version:</strong> looking at the map asks for nothing. If you choose to contribute (propose, back, comment, follow people), you sign in with Apple, pick a username and a name, and what you contribute is published under them. Your location never leaves your iPhone. No ads, no analytics, nothing sold.</p>

  <h2>Who is responsible</h2>
  <p>Criba is published on the App Store by <strong>Sendoa Sola</strong> (Seize Apps, Basque Country, Spain), the data controller. Contact for anything about your data: <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>.</p>

  <h2>What we process</h2>
  <ul>
    <li><strong>Without an account:</strong> nothing of yours. The app downloads the published places and keeps them on the iPhone so it opens at once.</li>
    <li><strong>Your Saved places</strong> live on your device and in your own iCloud account (you can turn sync off in Settings). We can't see them.</li>
    <li><strong>Your location</strong> is used only on the iPhone, when you tap «Near me», to centre the map. It is not sent to Criba.</li>
    <li><strong>If you sign in with Apple:</strong> Apple gives us an account identifier. Criba doesn't ask for your name or email. We keep that identifier, your <strong>profile</strong> (username, name and, if you add them, photo, bio and a link) and what you contribute: places you propose, backings (reasons and comment), notes if you are a Curator, who you follow, who you block and the reports you send.</li>
    <li><strong>If you turn on notifications:</strong> the notification identifier Apple gives your iPhone (to send them through Apple's push service) and which kinds you want. It's deleted when you sign out or delete the account. Notifications are only about you (your proposals, your photos, who follows you, your role) and never ads.</li>
    <li><strong>Technical logs:</strong> the server briefly records technical request data (such as the IP address) to run and to protect itself from abuse.</li>
  </ul>

  <h2>What is public</h2>
  <p>Criba is also a taste network: <strong>your profile (username, name, photo, bio and link), your backings, comments and notes, and the places you propose and back are visible to anyone</strong>, and the app suggests people with similar taste from them. Follower numbers are only shown in bands (10+, 50+…). Private: your Apple identifier, who you block, the reports you send, and proposals that haven't made it onto the map.</p>

  <h2>Why, and on what basis</h2>
  <ul>
    <li>Giving you an account and publishing what you contribute: performing the <a href="../terms/">terms of use</a> you accept when signing in.</li>
    <li>Moderation, abuse prevention and keeping the service safe: our legitimate interest.</li>
    <li>Handling reports and explaining every removal: the legal obligation under the EU Digital Services Act (DSA).</li>
  </ul>

  <h2>Who else is involved</h2>
  <ul>
    <li><strong>Supabase</strong> hosts the database and accounts, on servers in the European Union (Frankfurt).</li>
    <li><strong>Apple</strong>: sign-in, maps (MapKit) and your iCloud, under its terms.</li>
    <li>We keep <strong>database backups</strong> on our own machine in Spain for 30 days.</li>
  </ul>
  <p>No advertising or analytics SDKs, and we don't sell or share data with anyone.</p>

  <h2>How long</h2>
  <p>As long as you keep the account. <strong>You can delete it in the app</strong> (Settings › Your account › Delete account): your profile, backings, notes, follows and blocks are removed, along with your proposals nobody else backs. Reports you sent are kept without an author, and the record of moderation decisions that affected you is kept as long as the law requires. When you delete it, the app asks you to confirm with Apple and <strong>Criba revokes its access to your Apple account</strong>. Backups expire within 30 days.</p>

  <h2>Your rights</h2>
  <p>You can access, correct (your profile is edited in the app), erase (by deleting the account), port or object to the processing of your data by writing to <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>. You can also complain to the Spanish Data Protection Agency (<a href="https://www.aepd.es" rel="noopener">aepd.es</a>).</p>

  <h2>Children</h2>
  <p>You must be at least 14 to create an account. Looking at the map asks nothing of anyone.</p>

  <h2>Changes</h2>
  <p>If anything above changes, we'll update it here and in the App Store privacy label before it reaches the app.</p>
''',
}

TERMS = {
'es': '''
  <p class="eyebrow">Criba · Legal</p>
  <h1>Condiciones de uso de Criba</h1>
  <p class="effective">{updated}</p>
  <p>Criba es un mapa de sitios que están por algo: entran por mérito, cada uno con su porqué. Al entrar con tu cuenta para aportar, aceptas estas condiciones. Mirar el mapa no requiere cuenta.</p>

  <h2>Tu cuenta</h2>
  <p>Entras con Apple y eliges un nombre de usuario (único; se puede cambiar una vez cada 30 días) y un nombre; no tienen por qué ser los reales, pero no pueden suplantar a nadie ni ser ofensivos, y algunos (como «Criba») están reservados. Lo mismo vale para la foto, la bio y el enlace del perfil: la moderación puede retirarlos, y te dirá por qué. Debes tener al menos 14 años. Puedes borrar la cuenta cuando quieras desde la app.</p>

  <h2>Lo que aportas</h2>
  <p>Propuestas, respaldos, comentarios, notas y lo que pones en tu perfil se publican con tu nombre. Te comprometes a que sean:</p>
  <ul>
    <li><strong>Honestos:</strong> sobre sitios que conoces, y sin conflicto de interés — no se respalda ni se firma un sitio propio, de tu familia o donde trabajas.</li>
    <li><strong>Gratuitos:</strong> nada a cambio de dinero, invitaciones ni favores. No se compran ni se venden respaldos.</li>
    <li><strong>Respetuosos:</strong> describir, no atacar. Nada de insultos, acoso, discriminación, datos personales de terceros, spam, publicidad ni contenido ilegal.</li>
  </ul>
  <p>Sigues siendo el autor de lo que escribes. Nos das permiso, gratuito y mientras esté publicado, para mostrarlo en Criba y en lo que promocione a Criba; si lo borras o borras la cuenta, deja de mostrarse.</p>

  <h2>Cómo curamos y moderamos</h2>
  <p>Un sitio entra en el mapa cuando lo firma un Curator o lo respaldan varias personas de confianza; las reglas completas están en la app («Cómo curamos»). La moderación de Criba puede retirar contenido o limitar cuentas que incumplan estas condiciones. <strong>Cada decisión lleva su motivo</strong>, que ves en Ajustes › Tu cuenta, y puedes pedir que se revise escribiendo a <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>.</p>

  <h2>Denunciar</h2>
  <p>Cualquier sitio, nota, comentario o persona se puede denunciar desde la app (menú «…»), o escribiendo a <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>, que es también el punto de contacto para autoridades y usuarios a efectos del Reglamento de Servicios Digitales. Puedes bloquear a cualquier persona para dejar de ver lo suyo.</p>

  <h2>Lo que no garantizamos</h2>
  <p>Criba reúne opiniones firmadas sobre sitios; no es una guía oficial ni responde de lo que ofrecen los locales. Horarios, teléfonos y direcciones vienen de Apple Maps y pueden no estar al día. El servicio se ofrece tal cual y puede cambiar o interrumpirse.</p>

  <h2>Cambios y ley aplicable</h2>
  <p>Si cambiamos estas condiciones, te lo diremos en la app antes de que se apliquen. Se rigen por la ley española, sin perjuicio de los derechos que te dé la ley de tu país como consumidor.</p>
  <p>Responsable: Sendoa Sola (Seize Apps) · <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a> · <a href="../privacidad/">Privacidad</a></p>
''',
'en': '''
  <p class="eyebrow">Criba · Legal</p>
  <h1>Criba terms of use</h1>
  <p class="effective">{updated}</p>
  <p>Criba is a map of places that are there for a reason: they get in on merit, each with its why. By signing in to contribute, you accept these terms. Looking at the map needs no account.</p>

  <h2>Your account</h2>
  <p>You sign in with Apple and choose a username (unique; it can change once every 30 days) and a name; they needn't be your real ones, but they can't impersonate anyone or be offensive, and some (such as «Criba») are reserved. The same goes for your profile photo, bio and link: moderation can remove them, and will tell you why. You must be at least 14. You can delete the account at any time in the app.</p>

  <h2>What you contribute</h2>
  <p>Proposals, backings, comments, notes and what you put on your profile are published under your name. You agree they are:</p>
  <ul>
    <li><strong>Honest:</strong> about places you know, with no conflict of interest — nobody backs or signs their own place, their family's or where they work.</li>
    <li><strong>Free:</strong> nothing in exchange for money, invitations or favours. Backings are never bought or sold.</li>
    <li><strong>Respectful:</strong> describe, don't attack. No insults, harassment, discrimination, other people's personal data, spam, advertising or illegal content.</li>
  </ul>
  <p>You remain the author of what you write. You give us a free permission, while it is published, to show it in Criba and in what promotes Criba; if you delete it or your account, it stops being shown.</p>

  <h2>How we curate and moderate</h2>
  <p>A place gets onto the map when a Curator signs it or several trusted people back it; the full rules are in the app («How we curate»). Criba's moderation may remove content or limit accounts that break these terms. <strong>Every decision comes with its reason</strong>, shown in Settings › Your account, and you can ask for a review at <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>.</p>

  <h2>Reporting</h2>
  <p>Any place, note, comment or person can be reported from the app («…» menu) or by writing to <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>, which is also the point of contact for authorities and users under the EU Digital Services Act. You can block anyone to stop seeing their content.</p>

  <h2>What we don't guarantee</h2>
  <p>Criba gathers signed opinions about places; it is not an official guide and doesn't answer for what places offer. Opening hours, phone numbers and addresses come from Apple Maps and may be out of date. The service is provided as is and may change or stop.</p>

  <h2>Changes and governing law</h2>
  <p>If we change these terms, we'll tell you in the app before they apply. They are governed by Spanish law, without prejudice to the rights your country's consumer law gives you.</p>
  <p>Responsible: Sendoa Sola (Seize Apps) · <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a> · <a href="../privacy/">Privacy</a></p>
''',
}

PAGES = [  # (lang, kind, slug, title, desc)
    ('es', 'privacy', 'privacidad', 'Privacidad de Criba — Seize Apps', 'Cómo trata Criba tus datos: el mapa sin cuenta, y qué se publica cuando aportas.'),
    ('es', 'terms', 'condiciones', 'Condiciones de uso de Criba — Seize Apps', 'Las normas para aportar a Criba: cuentas, contenido, moderación y denuncias.'),
    ('en', 'privacy', 'privacy', 'Criba privacy — Seize Apps', 'How Criba handles your data: the map without an account, and what is published when you contribute.'),
    ('en', 'terms', 'terms', 'Criba terms of use — Seize Apps', 'The rules for contributing to Criba: accounts, content, moderation and reports.'),
]


def build_criba():
    for lang, kind, slug, title, desc in PAGES:
        root = '../../'
        body = (PRIVACY if kind == 'privacy' else TERMS)[lang].replace('{updated}', UPDATED[lang])
        canonical = f'criba/{slug}/'
        html = (head(lang, title, desc, root, canonical) + header(lang, root, canonical)
                + f'<main class="shell legal">\n{body}\n</main>\n' + footer(lang, root))
        # One tree for both languages: the slugs already differ (privacidad/privacy).
        html = html.replace('https://seizeapps.com/es/criba/', 'https://seizeapps.com/criba/')
        # hreflang and the language switch point at the page in the other language.
        pair = {'privacidad': 'privacy', 'privacy': 'privacidad', 'condiciones': 'terms', 'terms': 'condiciones'}[slug]
        es_slug, en_slug = (slug, pair) if lang == 'es' else (pair, slug)
        html = (html.replace(f'hreflang="en" href="https://seizeapps.com/criba/{slug}/"', f'hreflang="en" href="https://seizeapps.com/criba/{en_slug}/"')
                    .replace(f'hreflang="es" href="https://seizeapps.com/criba/{slug}/"', f'hreflang="es" href="https://seizeapps.com/criba/{es_slug}/"')
                    .replace(f'hreflang="x-default" href="https://seizeapps.com/criba/{slug}/"', f'hreflang="x-default" href="https://seizeapps.com/criba/{en_slug}/"'))
        other = 'en' if lang == 'es' else 'es'
        for prefix in ('../../es/', '../../'):
            html = html.replace(f'class="lang" href="{prefix}criba/{slug}/"', f'class="lang" href="../../criba/{pair}/"')
        write(f'criba/{slug}/index.html', html)
