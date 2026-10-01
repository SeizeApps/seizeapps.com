"""Sacapuntas's own privacy pages (01/10/2026, Sacapuntas 0.0.7).

Sacapuntas is a Kids Category app (9–11), so it can't live under the studio-wide policy: Apple and the
law ask for a specific policy, in plain language, and a version a child can read (SeizeRepo,
docs/app-ninos/04-normas-y-ley.md §4.8). Spanish only, like the app:
  /sacapuntas/privacidad/        the full policy, for families (the app opens it behind the parental gate)
  /sacapuntas/privacidad/ninos/  the version for children
Built with gen_site's chrome; run `python3 tools/gen_site.py`, which calls build_sacapuntas().
"""
from gen_site import head, header, footer, write

UPDATED = 'En vigor desde el 1 de octubre de 2026'

PRIVACIDAD = '''
  <p class="eyebrow">Sacapuntas · Legal</p>
  <h1>Privacidad de Sacapuntas</h1>
  <p class="effective">{updated}</p>
  <p><strong>La versión corta:</strong> Sacapuntas no recoge datos de tu hijo o hija ni de nadie. No hay cuentas, ni anuncios, ni analítica, ni seguimiento. El progreso se guarda en el dispositivo y, solo si una persona adulta lo activa, en vuestro propio iCloud, que nosotros no podemos ver. Lo único que sale del dispositivo es la petición con la que la app descarga listas de palabras nuevas, y no lleva nada vuestro. <a href="ninos/">Aquí está la versión para niños</a>.</p>

  <h2>Quién es el responsable</h2>
  <p>Sacapuntas la publica en el App Store <strong>Sendoa Sola</strong> (Seize Apps, País Vasco, España). Para cualquier cosa sobre privacidad: <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>. Respondemos en un plazo máximo de un mes.</p>

  <h2>Lo que no recogemos</h2>
  <ul>
    <li>No hay cuentas ni registro. La app no pide nombre real, correo, teléfono ni fecha de nacimiento.</li>
    <li>No usa la ubicación, la cámara, el micrófono, las fotos ni los contactos.</li>
    <li>No tiene anuncios, ni analítica, ni SDK de terceros, ni identificador publicitario. No hace seguimiento y no crea perfiles de nadie.</li>
    <li>No toma decisiones automatizadas sobre nadie. La dificultad de las fichas se ajusta dentro del dispositivo, con lo que el niño acierta y falla, y no se envía a ningún sitio.</li>
    <li>No envía notificaciones de ningún tipo.</li>
  </ul>

  <h2>Dónde vive el progreso</h2>
  <p>Los perfiles (un alias, que no tiene por qué ser el nombre real, el curso y un color), las páginas hechas, las virutas, el pueblo, las pegatinas, los ajustes de clase y de método, y el informe de la zona de familias se guardan <strong>en el dispositivo</strong>.</p>
  <p><strong>iCloud viene desactivado.</strong> Si una persona adulta lo activa en la zona de familias, el progreso se sincroniza entre vuestros dispositivos a través de <strong>vuestra cuenta de iCloud</strong>, en su base de datos privada. Ese servicio lo presta Apple según sus condiciones, y Seize no puede ver lo que hay en ella.</p>
  <p><strong>Cómo borrarlo:</strong> en la zona de familias, cada perfil tiene «Borrar progreso» y «Borrar perfil». También se borra todo al borrar la app y, si usáis iCloud, desde los ajustes de iCloud del dispositivo.</p>
  <p>La app solo guarda en el dispositivo lo estrictamente necesario para funcionar (como qué perfil está practicando). No usa cookies ni rastreadores.</p>

  <h2>Las palabras nuevas</h2>
  <p>Las fichas de lengua usan una lista de palabras que va dentro de la app. Con conexión, la app pregunta a un servidor nuestro (Supabase, en la Unión Europea, Irlanda) si hay palabras nuevas y, si las hay, las descarga. Esa petición <strong>solo lee</strong>: no lleva nada del niño, de su progreso ni del dispositivo, ni ningún identificador, y no hay cuentas. Como cualquier servidor, el de Supabase ve la dirección IP desde la que llega la petición y la guarda en sus registros técnicos durante un día; Seize no la usa ni la cruza con nada. Supabase actúa como encargado del tratamiento.</p>
  <p>Con Sacapuntas Pro, «Descargar para usar sin conexión» guarda esas listas en el dispositivo; no cambia nada de lo anterior.</p>
  <p>Las listas de palabras se preparan con ayuda de una inteligencia artificial <strong>fuera de la app</strong>; antes de publicarse, cada palabra pasa por un validador con las reglas de la Ortografía de la RAE y la revisa una persona. La app no usa inteligencia artificial y no envía nada a ninguna.</p>

  <h2>Compras</h2>
  <p>Sacapuntas Pro (pago único) y su prueba gratuita de 30 días solo se pueden pedir desde la zona de familias, tras una pregunta para adultos. Las compras las procesa <strong>Apple</strong>, que es quien vende (Apple Distribution International). Seize no recibe datos de pago ni sabe quién ha comprado: la app comprueba la compra con Apple en el dispositivo. El desistimiento y los reembolsos se gestionan con Apple según sus <a href="https://www.apple.com/legal/internet-services/itunes/es/terms.html" rel="noopener">condiciones</a>. Os recomendamos activar <strong>Pedir la compra</strong> en En Familia.</p>

  <h2>Las fichas en PDF</h2>
  <p>Desde la zona de familias se puede crear una ficha en PDF para hacerla en papel. Se crea en el dispositivo y solo sale de él si una persona adulta la comparte (por ejemplo, para imprimirla); lleva una línea para escribir el nombre a mano, nada más.</p>

  <h2>Los correos de soporte</h2>
  <p>Si nos escribís desde la zona de familias o a <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>, recibimos vuestro correo y lo que contéis en él. Lo usamos solo para responderos (base: nuestro interés legítimo en atender a quien nos escribe o, si es sobre una compra o un fallo, la relación con quien usa la app). Lo trata nuestro proveedor de correo electrónico como encargado; si alguna vez eso supone una transferencia fuera del Espacio Económico Europeo, se hará con las garantías que exige el RGPD. Lo guardamos hasta 12 meses después de cerrar la conversación. <strong>Por favor, no incluyáis datos del niño</strong> (la app os lo recuerda antes de abrir el correo). Si nos escribe un niño, contestamos una vez, si hace falta, y borramos el mensaje.</p>

  <h2>Niños</h2>
  <p>Sacapuntas es una app de primaria, pensada para niños de 9 a 11 años, y está en la categoría Niños del App Store. No tratamos datos de los niños. Si algún día hiciera falta, pediríamos antes el consentimiento de sus madres, padres o tutores (en España, para menores de 14 años; en Estados Unidos, para menores de 13).</p>

  <h2>Seguridad</h2>
  <p>Los datos están protegidos por el cifrado del dispositivo y, si usáis iCloud, por el de Apple. Todo lo que sale de la app, compra o cambia ajustes de adultos (iCloud, perfiles, métodos, correo, esta página) está en la zona de familias, detrás de una pregunta para adultos que cambia cada vez y no se recuerda.</p>

  <h2>Vuestros derechos</h2>
  <p>Podéis pedirnos acceso a vuestros datos, que los corrijamos o los borremos, oponeros a su tratamiento o pedir su portabilidad escribiendo a <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>. Como no guardamos datos de la app, en la práctica solo puede tratarse de los correos que nos hayáis enviado. Si no os respondemos bien, podéis reclamar ante la Agencia Española de Protección de Datos (<a href="https://www.aepd.es" rel="noopener">aepd.es</a>).</p>

  <h2>Familias en Estados Unidos y en el Reino Unido</h2>
  <p><strong>COPPA (Estados Unidos).</strong> Sacapuntas no recoge información personal de niños menores de 13 años: ni en la app, ni a través de terceros. Si creéis que nos ha llegado información de un niño (por ejemplo, en un correo), escribidnos y la borraremos.</p>
  <p><strong>Reino Unido.</strong> Seguimos el espíritu del Children's Code de la ICO: privacidad alta por defecto (iCloud desactivado, nada sale del dispositivo), sin rastreo, sin notificaciones y sin trucos para alargar el uso. Podéis consultar a la <a href="https://ico.org.uk" rel="noopener">ICO</a>.</p>

  <h2>Cambios</h2>
  <p>Si cambia algo de lo anterior, lo cambiaremos aquí, con su fecha, y en la ficha de privacidad del App Store antes de que llegue a la app.</p>
'''

NINOS = '''
  <p class="eyebrow">Sacapuntas · Para niños</p>
  <h1>Tus datos en Sacapuntas</h1>
  <p class="effective">{updated}</p>
  <ul>
    <li>📒 Tu progreso se guarda en tu tablet o en tu móvil, para que no lo pierdas.</li>
    <li>🙈 Nosotros no vemos tus respuestas, ni tu pueblo, ni tus pegatinas.</li>
    <li>🚫 Aquí no hay anuncios, y nadie te sigue por internet.</li>
    <li>✏️ No hace falta tu nombre: puedes usar un mote.</li>
    <li>🔑 Para comprar algo o cambiar cosas de mayores hace falta una persona adulta.</li>
    <li>📚 A veces la app descarga palabras nuevas para las fichas. No envía nada tuyo.</li>
    <li>💬 Si algo te preocupa, cuéntaselo a tu familia.</li>
  </ul>
  <p>Las personas adultas pueden leer <a href="../">la versión completa</a>.</p>
'''

PAGES = [  # (path, body, title, desc)
    ('sacapuntas/privacidad/', PRIVACIDAD, 'Privacidad de Sacapuntas — Seize Apps',
     'Sacapuntas no recoge datos: sin cuentas, sin anuncios ni analítica; el progreso, en el dispositivo o en vuestro iCloud.'),
    ('sacapuntas/privacidad/ninos/', NINOS, 'Tus datos en Sacapuntas — Seize Apps',
     'La privacidad de Sacapuntas, explicada para niños.'),
]


def build_sacapuntas():
    for path, body, title, desc in PAGES:
        root = '../' * path.count('/')
        html = (head('es', title, desc, root, path) + header('es', root, path)
                + f'<main class="shell legal">\n{body.replace("{updated}", UPDATED)}\n</main>\n' + footer('es', root))
        # Solo en castellano, como la app: una URL, sin el árbol /es/ ni la versión en inglés.
        url = f'https://seizeapps.com/{path}'
        html = (html.replace(f'https://seizeapps.com/es/{path}', url)
                    .replace(f'<link rel="alternate" hreflang="en" href="{url}">\n', '')
                    .replace(f'<link rel="alternate" hreflang="es" href="{url}">\n', '')
                    .replace(f'<link rel="alternate" hreflang="x-default" href="{url}">\n', ''))
        # El botón de idioma llevaría a una página en inglés que no existe: a la política general.
        html = html.replace(f'class="lang" href="{root}{path}"', f'class="lang" href="{root}privacy.html"')
        write(f'{path}index.html', html)
