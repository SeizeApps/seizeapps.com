"""Garum's own legal pages (privacy and terms), 26/09/2026.

Garum is the first Seize app with accounts, a server and user content, so it can't live under
the studio-wide policy («no accounts, nothing on our side»). Its pages:
  /garum/privacidad/  /garum/condiciones/   (castellano, the ones the app opens in Spanish)
  /garum/privacy/     /garum/terms/         (English)
Built with gen_site's chrome; run `python3 tools/gen_site.py`, which calls build_criba().
"""
from gen_site import head, header, footer, write

UPDATED = {'es': 'En vigor desde el 30 de septiembre de 2026', 'en': 'Effective September 30, 2026'}

PRIVACY = {
'es': '''
  <p class="eyebrow">Garum · Legal</p>
  <h1>Privacidad de Garum</h1>
  <p class="effective">{updated}</p>
  <p><strong>La versión corta:</strong> mirar el mapa no pide nada. Si decides aportar (proponer, respaldar, comentar, hacer colecciones, seguir a gente), entras con Apple, eliges un nombre de usuario y un nombre, y lo que aportas se publica con ellos. Tu ubicación no sale del iPhone. Sin publicidad, sin analítica y sin vender nada.</p>

  <h2>Quién es el responsable</h2>
  <p>Garum la publica en el App Store <strong>Sendoa Sola</strong> (Seize Apps, País Vasco, España), que es el responsable del tratamiento. Contacto para todo lo relativo a tus datos: <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>.</p>

  <h2>Qué datos tratamos</h2>
  <ul>
    <li><strong>Sin cuenta:</strong> nada tuyo. La app descarga los sitios publicados y los guarda en el iPhone para abrir al instante.</li>
    <li><strong>Tus Guardados</strong> (la lista) viven en tu dispositivo y en tu propia cuenta de iCloud (puedes apagar la sincronización en Ajustes). Sin cuenta, no nos llega nada de ellos.</li>
    <li><strong>La señal de guardado</strong> (solo con cuenta): desde la versión 0.0.25, cuando guardas un sitio, la app avisa al servidor de qué sitio es y de tu cuenta, y cuando lo quitas, lo borra. Sirve para mostrar en la ficha «Lo guardan N personas · M que sigues»: solo esos dos números, nunca quién. Viene activada; la apagas en Ajustes › Tu cuenta › «Contar mis guardados», y al apagarla se borran del servidor todas las tuyas. Los sitios que guardaste antes de la 0.0.25 no se suben solos.</li>
    <li><strong>Tu ubicación</strong> se usa solo en el iPhone, cuando tocas «Cerca de mí», para centrar el mapa. No se envía a Garum.</li>
    <li><strong>Si entras con Apple:</strong> Apple nos da un identificador de cuenta. Garum no pide tu nombre ni tu correo. Guardamos ese identificador, tu <strong>perfil</strong> (nombre de usuario, nombre y, si los pones, foto, bio y un enlace) y lo que aportas: sitios que propones, respaldos (motivos y comentario), notas, fotos de sitios, <strong>sugerencias de cambio</strong> sobre un sitio (los datos que corriges, si ha cerrado, y un comentario o enlace si los pones), sugerencias de quitar un sitio si eres Curator, <strong>colecciones</strong> (listas e itinerarios: título, introducción, sus sitios, tu nota en cada uno y si son públicas o privadas), los comentarios que dejas en colecciones, las colecciones de otras personas que guardas, a quién sigues, a quién bloqueas y las denuncias que envías.</li>
    <li><strong>Si activas los avisos:</strong> el identificador de avisos que Apple da a tu iPhone (para enviártelos a través del servicio de avisos de Apple) y qué tipos de aviso quieres recibir. Se borra al cerrar sesión o borrar la cuenta. Los avisos solo tratan de ti (tus propuestas, tus fotos, quién te sigue, quién guarda o comparte tus colecciones, tu papel) y nunca son publicidad.</li>
    <li><strong>Registros técnicos:</strong> el servidor anota durante poco tiempo datos técnicos de las peticiones (como la dirección IP) para funcionar y protegerse de abusos.</li>
  </ul>

  <h2>Qué es público</h2>
  <p>Garum es también una red de gustos: <strong>tu perfil (nombre de usuario, nombre, foto, bio y enlace), tus respaldos, tus comentarios, tus notas, las fotos de sitios que subes (con su crédito), los sitios que propones y respaldas y, cuando un Curator aplica un cambio que sugeriste, tu nombre de usuario en la ficha de ese sitio («Datos corregidos por…») y en tu perfil («Ha mejorado N sitios») son visibles para cualquiera</strong>, y a partir de ellos la app sugiere gente con gustos parecidos. El número de seguidores solo se muestra por tramos (10+, 50+…). Son privados: tu identificador de Apple, a quién bloqueas, las denuncias que envías, las sugerencias de quitar un sitio (solo las ve la moderación), el contenido de tus sugerencias de cambio y las que no se aplican (solo las ven los Curators y la moderación), qué sitios guardas, las colecciones de otros que guardas, tus colecciones privadas y las propuestas que aún no han entrado en el mapa (salvo las que tú pones en una colección pública).</p>
  <p><strong>Tus colecciones.</strong> Una colección pública (título, introducción, sus sitios y tus notas) sale con tu nombre en tu perfil y en «De quien sigues» de quien te sigue, la puede ver cualquiera y se puede compartir con un enlace. Puede llevar sitios que has propuesto y aún no han entrado en el mapa: salen marcados «Sin validar», y solo dentro de esa colección. Una colección privada (con Garum Pro) solo la ves tú, aunque se guarda en el servidor ligada a tu cuenta. Los comentarios en una colección los ve, con tu nombre, quien puede ver esa colección. Si alguien guarda o comparte una colección tuya, te avisamos con su nombre; nadie ve cuántas veces se ha guardado una colección.</p>

  <h2>Para qué y con qué base</h2>
  <ul>
    <li>Darte la cuenta y publicar lo que aportas: la ejecución de las <a href="../condiciones/">condiciones de uso</a> que aceptas al entrar.</li>
    <li>Moderar, evitar abusos y mantener el servicio seguro: nuestro interés legítimo.</li>
    <li>Atender denuncias y explicar cada retirada: la obligación legal del Reglamento de Servicios Digitales (DSA).</li>
    <li>Contar los guardados («Lo guardan N personas»): nuestro interés legítimo en mostrar qué sitios guarda la gente, solo como números y con la opción de no contar los tuyos.</li>
  </ul>

  <h2>Quién más interviene</h2>
  <ul>
    <li><strong>Supabase</strong> aloja la base de datos y las cuentas, en servidores de la Unión Europea (Fráncfort).</li>
    <li><strong>Apple</strong>: el inicio de sesión, los mapas (MapKit) y tu iCloud, bajo sus condiciones.</li>
    <li><strong>Anthropic</strong> (Claude, Estados Unidos) nos ayuda a revisar con fuentes públicas las propuestas y las sugerencias de cambio antes de que las vea un Curator, y a traducir las notas. Recibe el texto de la propuesta o de la sugerencia (con el comentario o el enlace), nunca tu identificador ni tu nombre.</li>
    <li>Las <strong>colecciones y los comentarios</strong> se publican al momento. Después, una tarea automática que corre en un equipo de Seize revisa con Claude (Anthropic) el título, la introducción y las notas de las colecciones que ven otros, y los comentarios, y <strong>señala</strong> a la moderación lo que puede incumplir las condiciones; no retira nada, decide la moderación. Para eso Claude recibe ese texto, los sitios de la colección y los datos públicos del perfil del autor (nombre de usuario, nombre, bio y enlace, para ver si alguien promociona un negocio propio), nunca tu identificador de Apple. Las colecciones privadas no se revisan.</li>
    <li>Guardamos <strong>copias de seguridad</strong> de la base de datos en un equipo propio en España durante 30 días.</li>
  </ul>
  <p>No hay SDK de publicidad ni de analítica, y no vendemos ni cedemos datos a nadie.</p>

  <h2>Cuánto tiempo</h2>
  <p>Mientras tengas la cuenta. <strong>Puedes borrarla desde la app</strong> (Ajustes › Tu cuenta › Borrar la cuenta): se eliminan tu perfil (con tu foto de perfil), tus respaldos, tus notas, tus seguidos, tus bloqueos, tus sugerencias de cambio (y con ellas tu nombre en «Datos corregidos por»), tus sugerencias de quitar sitios, tus colecciones (con sus notas), tus comentarios, las colecciones que guardaste y tu señal de guardado, y las propuestas tuyas que nadie más respalde. Las fotos de sitios que subiste se quedan publicadas sin tu nombre (su crédito pasa a ser «un antiguo usuario»; ver las condiciones), las denuncias que enviaste se conservan sin autor, y el registro de las decisiones de moderación que te afectaron se guarda el tiempo que exige la ley. Al borrarla, la app te pide confirmar con Apple y <strong>Garum revoca su acceso a tu cuenta de Apple</strong>. Las copias de seguridad desaparecen en 30 días.</p>

  <h2>Tus derechos</h2>
  <p>Puedes acceder a tus datos, corregirlos (tu perfil se edita en la app), suprimirlos (borrando la cuenta), llevártelos u oponerte a su tratamiento escribiendo a <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>. Si no te respondemos bien, puedes reclamar ante la Agencia Española de Protección de Datos (<a href="https://www.aepd.es" rel="noopener">aepd.es</a>).</p>

  <h2>Menores</h2>
  <p>Para crear una cuenta hay que tener al menos 14 años. Mirar el mapa no pide nada a nadie.</p>

  <h2>Cambios</h2>
  <p>Si cambia algo de lo anterior, lo actualizaremos aquí y en la ficha de privacidad del App Store antes de que llegue a la app.</p>
''',
'en': '''
  <p class="eyebrow">Garum · Legal</p>
  <h1>Garum privacy</h1>
  <p class="effective">{updated}</p>
  <p><strong>The short version:</strong> looking at the map asks for nothing. If you choose to contribute (propose, back, comment, make collections, follow people), you sign in with Apple, pick a username and a name, and what you contribute is published under them. Your location never leaves your iPhone. No ads, no analytics, nothing sold.</p>

  <h2>Who is responsible</h2>
  <p>Garum is published on the App Store by <strong>Sendoa Sola</strong> (Seize Apps, Basque Country, Spain), the data controller. Contact for anything about your data: <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>.</p>

  <h2>What we process</h2>
  <ul>
    <li><strong>Without an account:</strong> nothing of yours. The app downloads the published places and keeps them on the iPhone so it opens at once.</li>
    <li><strong>Your Saved places</strong> (the list) live on your device and in your own iCloud account (you can turn sync off in Settings). Without an account, nothing about them reaches us.</li>
    <li><strong>The save signal</strong> (only with an account): from version 0.0.25, when you save a place, the app tells the server which place it is and your account, and when you remove it, deletes that. It is used to show «Saved by N people · M you follow» on the place's page: only those two numbers, never who. It is on by default; you turn it off in Settings › Your account › «Count my saves», and turning it off deletes all of yours from the server. Places you saved before 0.0.25 are not uploaded on their own.</li>
    <li><strong>Your location</strong> is used only on the iPhone, when you tap «Near me», to centre the map. It is not sent to Garum.</li>
    <li><strong>If you sign in with Apple:</strong> Apple gives us an account identifier. Garum doesn't ask for your name or email. We keep that identifier, your <strong>profile</strong> (username, name and, if you add them, photo, bio and a link) and what you contribute: places you propose, backings (reasons and comment), notes, place photos, <strong>suggested changes</strong> to a place (the details you correct, whether it has closed, and a comment or link if you add them), suggestions to remove a place if you are a Curator, <strong>collections</strong> (lists and itineraries: title, introduction, their places, your note on each and whether they are public or private), the comments you leave on collections, other people's collections you save, who you follow, who you block and the reports you send.</li>
    <li><strong>If you turn on notifications:</strong> the notification identifier Apple gives your iPhone (to send them through Apple's push service) and which kinds you want. It's deleted when you sign out or delete the account. Notifications are only about you (your proposals, your photos, who follows you, who saves or shares your collections, your role) and never ads.</li>
    <li><strong>Technical logs:</strong> the server briefly records technical request data (such as the IP address) to run and to protect itself from abuse.</li>
  </ul>

  <h2>What is public</h2>
  <p>Garum is also a taste network: <strong>your profile (username, name, photo, bio and link), your backings, comments and notes, the place photos you upload (with their credit), the places you propose and back and, when a Curator applies a change you suggested, your username on that place's page («Details corrected by…») and on your profile («Has improved N places») are visible to anyone</strong>, and the app suggests people with similar taste from them. Follower numbers are only shown in bands (10+, 50+…). Private: your Apple identifier, who you block, the reports you send, suggestions to remove a place (only moderation sees them), what your suggested changes say and the ones not applied (only Curators and moderation see them), which places you save, other people's collections you save, your private collections, and proposals that haven't made it onto the map (except those you put in a public collection).</p>
  <p><strong>Your collections.</strong> A public collection (title, introduction, its places and your notes) appears under your name on your profile and in «From people you follow» for those who follow you, anyone can see it, and it can be shared with a link. It can include places you proposed that haven't made it onto the map yet: they are marked «Not validated», and only inside that collection. A private collection (with Garum Pro) is seen only by you, though it is stored on the server, tied to your account. Comments on a collection are seen, with your name, by whoever can see that collection. If someone saves or shares one of your collections, we tell you, with their name; nobody sees how many times a collection has been saved.</p>

  <h2>Why, and on what basis</h2>
  <ul>
    <li>Giving you an account and publishing what you contribute: performing the <a href="../terms/">terms of use</a> you accept when signing in.</li>
    <li>Moderation, abuse prevention and keeping the service safe: our legitimate interest.</li>
    <li>Handling reports and explaining every removal: the legal obligation under the EU Digital Services Act (DSA).</li>
    <li>Counting saves («Saved by N people»): our legitimate interest in showing which places people save, only as numbers and with the option not to count yours.</li>
  </ul>

  <h2>Who else is involved</h2>
  <ul>
    <li><strong>Supabase</strong> hosts the database and accounts, on servers in the European Union (Frankfurt).</li>
    <li><strong>Apple</strong>: sign-in, maps (MapKit) and your iCloud, under its terms.</li>
    <li><strong>Anthropic</strong> (Claude, United States) helps us check proposals and suggested changes against public sources before a Curator sees them, and translate notes. It receives the text of the proposal or suggestion (with its comment or link), never your identifier or your name.</li>
    <li><strong>Collections and comments</strong> are published at once. Afterwards, an automated task running on a Seize machine uses Claude (Anthropic) to review the title, introduction and notes of collections others can see, and comments, and <strong>flags</strong> to moderation anything that may break the terms; it removes nothing, moderation decides. For that Claude receives that text, the collection's places and the author's public profile details (username, name, bio and link, to spot someone promoting their own business), never your Apple identifier. Private collections are not reviewed.</li>
    <li>We keep <strong>database backups</strong> on our own machine in Spain for 30 days.</li>
  </ul>
  <p>No advertising or analytics SDKs, and we don't sell or share data with anyone.</p>

  <h2>How long</h2>
  <p>As long as you keep the account. <strong>You can delete it in the app</strong> (Settings › Your account › Delete account): your profile (with your profile photo), backings, notes, follows, blocks, suggested changes (and with them your name under «Details corrected by»), suggestions to remove places, collections (with their notes), comments, the collections you saved and your save signal are removed, along with your proposals nobody else backs. Place photos you uploaded stay published without your name (their credit becomes «a former user»; see the terms), reports you sent are kept without an author, and the record of moderation decisions that affected you is kept as long as the law requires. When you delete it, the app asks you to confirm with Apple and <strong>Garum revokes its access to your Apple account</strong>. Backups expire within 30 days.</p>

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
  <p class="eyebrow">Garum · Legal</p>
  <h1>Condiciones de uso de Garum</h1>
  <p class="effective">{updated}</p>
  <p>Garum es un mapa de sitios que están por algo: entran por mérito, cada uno con su porqué. Al entrar con tu cuenta para aportar, aceptas estas condiciones. Mirar el mapa no requiere cuenta.</p>

  <h2>Tu cuenta</h2>
  <p>Entras con Apple y eliges un nombre de usuario (único; se puede cambiar una vez cada 30 días) y un nombre; no tienen por qué ser los reales, pero no pueden suplantar a nadie ni ser ofensivos, y algunos (como «Garum») están reservados. Lo mismo vale para la foto, la bio y el enlace del perfil: la moderación puede retirarlos, y te dirá por qué. Debes tener al menos 14 años. Puedes borrar la cuenta cuando quieras desde la app.</p>

  <h2>Lo que aportas</h2>
  <p>Propuestas, respaldos, comentarios, notas, colecciones (salvo las privadas), fotos y lo que pones en tu perfil se publican con tu nombre. Te comprometes a que sean:</p>
  <ul>
    <li><strong>Honestos:</strong> sobre sitios que conoces, y sin conflicto de interés — no se respalda ni se firma un sitio propio, de tu familia o donde trabajas, ni se hace una colección para promocionar un negocio propio o donde trabajas (es la regla 7 de «Cómo curamos»).</li>
    <li><strong>Gratuitos:</strong> nada a cambio de dinero, invitaciones ni favores. No se compran ni se venden respaldos.</li>
    <li><strong>Respetuosos:</strong> describir, no atacar. Nada de insultos, acoso, discriminación, datos personales de terceros, spam, publicidad ni contenido ilegal.</li>
  </ul>
  <p>Las fotos que subes tienen que ser tuyas o tener una licencia libre que permita publicarlas, con su crédito. Sigues siendo el autor de lo que escribes y de tus fotos. Por lo que escribes nos das permiso, gratuito y mientras esté publicado, para mostrarlo en Garum y en lo que promocione a Garum; si lo borras o borras la cuenta, deja de mostrarse. Por las <strong>fotos de sitios</strong> que subes nos das un permiso gratuito, mundial y sin fecha de fin para mostrarlas en Garum y en lo que promocione a Garum, <strong>que sigue aunque borres la cuenta</strong>: entonces se quedan publicadas sin tu nombre, como «un antiguo usuario». Si quieres que retiremos alguna, escríbenos. Tu foto de perfil no entra aquí: se borra con la cuenta.</p>
  <p><strong>Colecciones.</strong> Sigues siendo el autor de tus colecciones (el título, la introducción, la selección y tus notas) y de tus comentarios. Nos das permiso, gratuito y mientras estén publicados, para mostrarlos en Garum, traducirlos a otros idiomas y dejar que se compartan con un enlace. Si borras una colección o la cuenta, deja de mostrarse. Un comentario lo puede borrar quien lo escribió o el autor de la colección. Las colecciones no se venden: si algún día Garum permite venderlas, hará falta un acuerdo aparte contigo, que podrás aceptar o no; este permiso no lo cubre.</p>

  <h2>Cómo curamos y moderamos</h2>
  <p>Un sitio entra en el mapa cuando lo firma un Curator o lo respaldan varias personas de confianza; las reglas completas están en la app («Cómo curamos»). Cualquiera con cuenta puede sugerir un cambio en la ficha de un sitio o avisar de que ha cerrado; un Curator lo revisa y lo aplica o lo rechaza, con su motivo, y si ha cerrado para siempre lo quita del mapa. Los Curators pueden sugerir quitar un sitio que ha cerrado, ya no está a la altura, no encaja en el criterio o está repetido; lo decide la moderación, con su motivo. Las colecciones y los comentarios se publican al momento; después, una revisión automática señala a la moderación lo que puede incumplir estas condiciones, y la moderación decide si retira una colección, una nota o un comentario. La moderación de Garum puede retirar contenido o limitar cuentas que incumplan estas condiciones. <strong>Cada decisión lleva su motivo</strong>, que ves en Ajustes › Tu cuenta, y puedes pedir que se revise escribiendo a <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>.</p>

  <h2>Denunciar</h2>
  <p>Cualquier sitio, nota, colección, comentario o persona se puede denunciar desde la app (menú «…»), o escribiendo a <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>, que es también el punto de contacto para autoridades y usuarios a efectos del Reglamento de Servicios Digitales. Puedes bloquear a cualquier persona para dejar de ver lo suyo.</p>

  <h2>Lo que no garantizamos</h2>
  <p>Garum reúne opiniones firmadas sobre sitios; no es una guía oficial ni responde de lo que ofrecen los locales. Horarios, teléfonos y direcciones vienen de Apple Maps y pueden no estar al día. El servicio se ofrece tal cual y puede cambiar o interrumpirse.</p>

  <h2>Cambios y ley aplicable</h2>
  <p>Si cambiamos estas condiciones, te lo diremos en la app antes de que se apliquen. Se rigen por la ley española, sin perjuicio de los derechos que te dé la ley de tu país como consumidor.</p>
  <p>Responsable: Sendoa Sola (Seize Apps) · <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a> · <a href="../privacidad/">Privacidad</a></p>
''',
'en': '''
  <p class="eyebrow">Garum · Legal</p>
  <h1>Garum terms of use</h1>
  <p class="effective">{updated}</p>
  <p>Garum is a map of places that are there for a reason: they get in on merit, each with its why. By signing in to contribute, you accept these terms. Looking at the map needs no account.</p>

  <h2>Your account</h2>
  <p>You sign in with Apple and choose a username (unique; it can change once every 30 days) and a name; they needn't be your real ones, but they can't impersonate anyone or be offensive, and some (such as «Garum») are reserved. The same goes for your profile photo, bio and link: moderation can remove them, and will tell you why. You must be at least 14. You can delete the account at any time in the app.</p>

  <h2>What you contribute</h2>
  <p>Proposals, backings, comments, notes, collections (except private ones), photos and what you put on your profile are published under your name. You agree they are:</p>
  <ul>
    <li><strong>Honest:</strong> about places you know, with no conflict of interest — nobody backs or signs their own place, their family's or where they work, or makes a collection to promote their own business or where they work (rule 7 of «How we curate»).</li>
    <li><strong>Free:</strong> nothing in exchange for money, invitations or favours. Backings are never bought or sold.</li>
    <li><strong>Respectful:</strong> describe, don't attack. No insults, harassment, discrimination, other people's personal data, spam, advertising or illegal content.</li>
  </ul>
  <p>Photos you upload must be yours or carry a free license that allows publishing them, with their credit. You remain the author of what you write and of your photos. For what you write, you give us a free permission, while it is published, to show it in Garum and in what promotes Garum; if you delete it or your account, it stops being shown. For the <strong>place photos</strong> you upload, you give us a free, worldwide permission with no end date to show them in Garum and in what promotes Garum, <strong>which continues if you delete your account</strong>: they then stay published without your name, as «a former user». If you want us to take one down, write to us. Your profile photo is not part of this: it is deleted with the account.</p>
  <p><strong>Collections.</strong> You remain the author of your collections (the title, the introduction, the selection and your notes) and of your comments. You give us a free permission, while they are published, to show them in Garum, translate them into other languages and let them be shared with a link. If you delete a collection or your account, it stops being shown. A comment can be deleted by whoever wrote it or by the collection's author. Collections are not sold: if Garum ever allows selling them, that will need a separate agreement with you, which you can accept or not; this permission does not cover it.</p>

  <h2>How we curate and moderate</h2>
  <p>A place gets onto the map when a Curator signs it or several trusted people back it; the full rules are in the app («How we curate»). Anyone with an account can suggest a change to a place's details or say it has closed; a Curator reviews it and applies or declines it, with a reason, and takes it off the map if it has closed for good. Curators can suggest removing a place that has closed, is no longer up to standard, does not fit the criteria or is a duplicate; moderation decides, with its reason. Collections and comments are published at once; afterwards, an automated review flags to moderation anything that may break these terms, and moderation decides whether to remove a collection, a note or a comment. Garum's moderation may remove content or limit accounts that break these terms. <strong>Every decision comes with its reason</strong>, shown in Settings › Your account, and you can ask for a review at <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>.</p>

  <h2>Reporting</h2>
  <p>Any place, note, collection, comment or person can be reported from the app («…» menu) or by writing to <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>, which is also the point of contact for authorities and users under the EU Digital Services Act. You can block anyone to stop seeing their content.</p>

  <h2>What we don't guarantee</h2>
  <p>Garum gathers signed opinions about places; it is not an official guide and doesn't answer for what places offer. Opening hours, phone numbers and addresses come from Apple Maps and may be out of date. The service is provided as is and may change or stop.</p>

  <h2>Changes and governing law</h2>
  <p>If we change these terms, we'll tell you in the app before they apply. They are governed by Spanish law, without prejudice to the rights your country's consumer law gives you.</p>
  <p>Responsible: Sendoa Sola (Seize Apps) · <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a> · <a href="../privacy/">Privacy</a></p>
''',
}

PAGES = [  # (lang, kind, slug, title, desc)
    ('es', 'privacy', 'privacidad', 'Privacidad de Garum — Seize Apps', 'Cómo trata Garum tus datos: el mapa sin cuenta, y qué se publica cuando aportas.'),
    ('es', 'terms', 'condiciones', 'Condiciones de uso de Garum — Seize Apps', 'Las normas para aportar a Garum: cuentas, contenido, moderación y denuncias.'),
    ('en', 'privacy', 'privacy', 'Garum privacy — Seize Apps', 'How Garum handles your data: the map without an account, and what is published when you contribute.'),
    ('en', 'terms', 'terms', 'Garum terms of use — Seize Apps', 'The rules for contributing to Garum: accounts, content, moderation and reports.'),
]


def build_criba():
    for lang, kind, slug, title, desc in PAGES:
        root = '../../'
        body = (PRIVACY if kind == 'privacy' else TERMS)[lang].replace('{updated}', UPDATED[lang])
        canonical = f'garum/{slug}/'
        html = (head(lang, title, desc, root, canonical) + header(lang, root, canonical)
                + f'<main class="shell legal">\n{body}\n</main>\n' + footer(lang, root))
        # One tree for both languages: the slugs already differ (privacidad/privacy).
        html = html.replace('https://seizeapps.com/es/garum/', 'https://seizeapps.com/garum/')
        # hreflang and the language switch point at the page in the other language.
        pair = {'privacidad': 'privacy', 'privacy': 'privacidad', 'condiciones': 'terms', 'terms': 'condiciones'}[slug]
        es_slug, en_slug = (slug, pair) if lang == 'es' else (pair, slug)
        html = (html.replace(f'hreflang="en" href="https://seizeapps.com/garum/{slug}/"', f'hreflang="en" href="https://seizeapps.com/garum/{en_slug}/"')
                    .replace(f'hreflang="es" href="https://seizeapps.com/garum/{slug}/"', f'hreflang="es" href="https://seizeapps.com/garum/{es_slug}/"')
                    .replace(f'hreflang="x-default" href="https://seizeapps.com/garum/{slug}/"', f'hreflang="x-default" href="https://seizeapps.com/garum/{en_slug}/"'))
        other = 'en' if lang == 'es' else 'es'
        for prefix in ('../../es/', '../../'):
            html = html.replace(f'class="lang" href="{prefix}garum/{slug}/"', f'class="lang" href="../../garum/{pair}/"')
        write(f'garum/{slug}/index.html', html)
