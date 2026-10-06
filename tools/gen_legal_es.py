# Spanish legal copy. English lives in gen_legal_copy.py (built from the EN bodies).
PRIVACY_ES='''
  <p class="eyebrow">Legal</p>
  <h1>Política de privacidad</h1>
  <p class="effective">En vigor desde el 6 de octubre de 2026</p>
  <nav class="toc" aria-label="Apps">
    <a href="#cycle-timers">Cycle Timers</a><a href="#tempo">Tempo</a><a href="#drip">Drip</a><a href="#anchor">Anchor</a><a href="#kover">Kover</a><a href="#tandem">Tandem</a><a href="#meso">Meso</a><a href="#grain">Grain</a><a href="#gaminghub">GamingHub</a><a href="#atino">Atino</a><a href="#overbit">Overbit</a>
  </nav>

  <p><strong>La versión corta:</strong> las apps de Seize están hechas para funcionar sin tus datos. No tenemos cuentas de usuario, no usamos SDK de analítica ni de publicidad, y no vendemos ni compartimos nada. Lo que metes en una app se queda en tu dispositivo y en tu propio iCloud, salvo que la sección de esa app diga otra cosa (véase <a href="#gaminghub">GamingHub</a>, <a href="#atino">Atino</a> y <a href="#overbit">Overbit</a>).</p>

  <p><strong>Garum es la excepción:</strong> tiene cuentas, un servidor en la UE y contenido de usuarios, así que tiene <a href="../garum/privacidad/">su propia política de privacidad</a> y <a href="../garum/condiciones/">condiciones de uso</a>.</p>

  <p><strong>Atino es otra excepción:</strong> tu CV, redactado en tu iPhone, se envía a servicios de ordenación de terceros a través de una pasarela de Seize cuando lo permites, y su suscripción se comunica a RevenueCat para analítica de compras, así que tiene <a href="../atino/privacidad/">su propia política de privacidad</a>.</p>

  <p><strong>Overbit es otra excepción:</strong> para enviarte alertas registra un identificador de instalación aleatorio y tu token de notificaciones push en un servidor de Seize, así que lee <a href="#overbit">su sección más abajo</a>.</p>

  <h2>Quiénes somos</h2>
  <p>Seize Apps es un estudio independiente de aplicaciones que llevan <strong>Izotz Cristobal Mota</strong> y <strong>Sendoa Sola</strong> desde el País Vasco (España) («nosotros»). Esta política cubre todas las apps de Seize distribuidas a través de la App Store de Apple y TestFlight: actualmente <a href="#cycle-timers">Cycle Timers</a>, <a href="#tempo">Tempo</a>, <a href="#drip">Drip</a>, <a href="#anchor">Anchor</a>, <a href="#kover">Kover</a>, <a href="#tandem">Tandem</a>, <a href="#meso">Meso</a>, <a href="#grain">Grain</a>, <a href="#gaminghub">GamingHub</a>, <a href="#atino">Atino</a> y <a href="#overbit">Overbit</a>. Cada app la publica en la App Store uno de los dos: el vendedor que figura en su ficha es el responsable del tratamiento de esa app, y se nombra en su sección. Si una app difiere en algo, su sección es la que manda.</p>

  <h2>Qué recogemos</h2>
  <p><strong>Nada, por defecto.</strong> Nuestras apps no requieren cuenta, no incluyen SDK de terceros de analítica, publicidad o seguimiento, y no nos transmiten el contenido que creas. No podemos ver tus temporizadores, sesiones de trabajo, gastos, tickets, rutinas ni ningún otro contenido que crees en una app de Seize.</p>
  <p>Las compras las procesa íntegramente Apple. Cuando una app vende un desbloqueo «Pro» de pago único, la app comprueba esa compra con StoreKit de Apple en tu dispositivo y solo recuerda si está activa; nosotros nunca vemos quién la compró. Recibimos de App Store Connect estadísticas agregadas y anónimas de ventas y fallos (por ejemplo, el número de descargas por país). Esas estadísticas no contienen identificadores personales.</p>

  <h2>Dónde viven tus datos</h2>
  <ul>
    <li><strong>En tu dispositivo.</strong> El contenido de la app se guarda en local, en el contenedor privado de la app (y, en las apps con widgets, en un contenedor de App Group compartido que solo pueden leer la app y su propio widget).</li>
    <li><strong>En tu iCloud.</strong> Nuestras apps sincronizan a través de tu cuenta personal de iCloud, bajo las condiciones de Apple, salvo que lo desactives en Ajustes o que la sección de esa app diga otra cosa; nosotros nunca tenemos acceso.</li>
  </ul>

  <h2>Detalle por app</h2>

  <section id="cycle-timers">
  <h3>Cycle Timers</h3>
  <p>Cycle Timers <strong>no recoge ningún dato</strong>. Tus temporizadores se guardan en el dispositivo, en un contenedor de App Group privado compartido solo con los widgets de inicio y pantalla de bloqueo de la propia app. Las notificaciones se programan en local. La app no hace conexiones de red, no tiene sistema de cuentas y no incluye código de terceros que reciba tus datos.</p>
  <p><em>Publicada en la App Store por Izotz Cristobal Mota.</em></p>
  </section>

  <section id="tempo">
  <h3>Tempo</h3>
  <p>Tempo guarda en tu dispositivo las sesiones de trabajo, los horarios, las preferencias de días laborables, las zonas de trabajo y el historial de correcciones. Un grupo de apps local comparte la información necesaria con los propios widgets de Tempo. Tempo no tiene cuentas, SDK de publicidad, SDK de analítica ni un servicio del desarrollador que reciba tus registros de trabajo o tu historial de ubicación.</p>
  <p><strong>Almacenamiento y copias de seguridad.</strong> Esta versión de Tempo no implementa sincronización propia mediante iCloud. Las copias del dispositivo y los servicios del sistema pueden depender de tu cuenta de Apple y de los ajustes del dispositivo; son distintos de una sincronización implementada por Tempo.</p>
  <p><strong>Ubicación y mapas.</strong> Puedes usar el seguimiento manual sin conceder permiso de ubicación. Al activar el seguimiento automático, Tempo utiliza Core Location de Apple y señales locales para evaluar entradas, salidas y rutinas de trabajo en casa. Controlas los permisos de ubicación en los ajustes de iOS. La búsqueda de lugares, los mapas y las estimaciones de rutas utilizan Apple MapKit; Apple puede procesar solicitudes y coordenadas relevantes de acuerdo con sus condiciones. Que el desarrollador no recopile tu ubicación no significa que los servicios de Apple nunca la procesen.</p>
  <p><strong>Compras.</strong> Apple gestiona las compras de Tempo Pro y las renovaciones de las suscripciones. Tempo determina el acceso en el dispositivo mediante transacciones verificadas de StoreKit. El desarrollador no recibe los datos de tu tarjeta de pago a través de Tempo.</p>
  <p><strong>Exportaciones y tarjetas de resumen.</strong> Puedes exportar tus registros o crear una imagen de resumen. Revisa las exportaciones antes de compartirlas, ya que los archivos de registros y diagnóstico pueden contener información sensible de trabajo o ubicación. Las imágenes de resumen se componen a partir de datos limitados, sin coordenadas precisas, nombres de lugares de trabajo ni horas precisas de inicio y fin; los totales se muestran por defecto y el reparto por categorías generales de ubicación es opcional. Compartir y Copiar no requieren acceso a Fotos. Guardar solicita permiso solo para añadir a Fotos cuando es necesario. El destino elegido, el portapapeles, la imagen guardada o una copia externa tienen sus propias condiciones de conservación y tratamiento; borrar los datos locales de Tempo no elimina las copias que ya has exportado o compartido.</p>
  <p><strong>Tus controles.</strong> Puedes editar o eliminar lugares, corregir registros, exportar datos y borrar los datos locales de Tempo desde la app. También puedes revocar los permisos de ubicación, notificaciones o Fotos en los ajustes de iOS. Restringir un permiso puede limitar la automatización o el guardado, pero el seguimiento manual y las correcciones siguen disponibles.</p>
  <p><em>Publicada por Izotz Cristobal Mota. Para consultas sobre el tratamiento de datos de Tempo, escribe a <a href="mailto:izotz@seizeapps.com">izotz@seizeapps.com</a>.</em></p>
  </section>

  <section id="drip">
  <h3>Drip</h3>
  <p>Drip guarda los servicios que registras —nombre, coste, ciclo de cobro, fechas de pago, categoría, etiquetas, notas y etiqueta del método de pago— <strong>en tu dispositivo</strong>, en un contenedor de App Group privado compartido solo con los widgets de inicio y pantalla de bloqueo de Drip y sus atajos de Siri. Drip no tiene sistema de cuentas, ni analítica, ni código de terceros que reciba tus datos. Tiene dos compras opcionales: un desbloqueo «Drip Pro» de pago único que abre las funciones extra de la app (Apple comprueba el derecho en tu dispositivo, incluido En familia; la app solo guarda si está activo) y un bote de propinas de compras sueltas que no desbloquean nada ni cambian nada de la app. Las procesa Apple las dos; nosotros no vemos tus datos de pago y no guardamos nada de ellas más allá de esa marca local y una cuenta local de cuántas veces has dejado propina.</p>
  <p><strong>La sincronización con iCloud</strong> viene activada: tus servicios se sincronizan entre tus dispositivos a través de tu cuenta personal de iCloud, bajo las condiciones de Apple; nosotros nunca tenemos acceso. Si la desactivas en Ajustes, tus datos se quedan solo en el dispositivo. Los recordatorios de pago y el resumen semanal son notificaciones locales, programadas en tu dispositivo.</p>
  <p><em>Publicada en la App Store por Sendoa Sola.</em></p>
  </section>

  <section id="anchor">
  <h3>Anchor</h3>
  <p>Anchor es una herramienta de apoyo diario para personas que se recuperan de un trastorno de la conducta alimentaria, pensada para acompañar al tratamiento profesional. Todo lo que introduces —bloques de rutina y sus confirmaciones, registros emocionales y sus notas opcionales, sesiones de surf del impulso y de respiración, uso de estrategias, tu plan de seguridad (contactos, estrategias, señales de alarma) y planes para días difíciles— se guarda <strong>en tu dispositivo</strong>, en el contenedor privado de la app. La Actividad en Directo del surf del impulso solo enseña su tiempo en la pantalla de bloqueo; se dibuja en el dispositivo y no lleva nada de lo que introduces. Anchor no tiene sistema de cuentas, ni analítica, ni publicidad, ni chat de IA, ni código de terceros que reciba tus datos. Sí tiene un bote de propinas opcional: compras sueltas que no cambian ninguna herramienta de la app — ninguna función de Anchor está nunca detrás de un pago. Como agradecimiento, cualquier propina abre además tres temas de color opcionales. Las compras las procesa Apple; nosotros no vemos tus datos de pago. Para saber si has dejado propina, Anchor lee en tu dispositivo, con StoreKit de Apple, sus propias propinas en tu historial de compras del App Store, y solo guarda ese hecho y una cuenta local de cuántas veces has dejado propina; no se nos envía nada de ello. El nombre que puedes escribir en «Sobre ti» se usa solo en mensajes dentro del dispositivo.</p>
  <p><strong>Datos de salud.</strong> Anchor puede leer, opcionalmente, el análisis de sueño, la variabilidad de la frecuencia cardíaca, los pasos y el tiempo de ejercicio de Apple Salud, solo después de que concedas el permiso (Ajustes › Datos de salud; desactivado por defecto). Anchor lee esos datos para enseñarte contexto cualitativo sobre descanso y movimiento; nunca escribe en Salud, nunca lee peso, masa corporal, grasa corporal ni nutrición, nunca sube datos de salud a ningún sitio y nunca los usa con fines publicitarios ni los comparte con terceros. Los datos de salud se quedan en tu dispositivo y quedan fuera de la sincronización con iCloud.</p>
  <p><strong>La sincronización con iCloud</strong> viene activada para que tus rutinas, registros y planes te sigan entre tus dispositivos a través de tu cuenta personal de iCloud (la base de datos privada de CloudKit de Apple), bajo las condiciones de Apple; nosotros nunca tenemos acceso. Puedes desactivarla en Ajustes; tus datos se quedan entonces solo en el dispositivo. Los recordatorios de rutinas, el recordatorio del registro diario y las Live Activities se programan y se muestran en local. Los números de emergencia del plan de seguridad son teléfonos de ayuda públicos de tu región; tocar uno hace una llamada normal.</p>
  <p>Anchor no es un producto sanitario y no sustituye al tratamiento profesional. A propósito, no contiene ningún registro de calorías, peso ni medidas corporales.</p>
  <p><em>Publicada en la App Store por Sendoa Sola.</em></p>
  </section>

  <section id="kover">
  <h3>Kover</h3>
  <p>Kover guarda los productos que añades —nombre, categoría, tienda, fecha e importe de compra, país, fechas de garantía, número de serie, contacto de soporte, notas y la foto del ticket— <strong>en tu dispositivo</strong>, en el contenedor privado de la app. Kover no tiene sistema de cuentas, ni analítica, ni código de terceros que reciba tus datos. Tiene dos compras opcionales: un desbloqueo «Kover Pro» de pago único que abre las funciones extra de la app (Apple comprueba el derecho en tu dispositivo, incluido En familia; la app solo guarda si está activo) y un bote de propinas de compras sueltas que no desbloquean nada ni cambian nada de la app. Las procesa Apple las dos; nosotros no vemos tus datos de pago y no guardamos nada de ellas más allá de esa marca local y una cuenta local de cuántas veces has dejado propina.</p>
  <p><strong>Tickets y cámara.</strong> Cuando escaneas un ticket, Kover usa la cámara (o una foto o un PDF que tú eliges) y lee el texto con el framework Vision de Apple, en el propio dispositivo. La imagen y el texto reconocido nunca salen del teléfono; la foto se conserva solo porque es tu justificante de compra. El acceso a la cámara y a la fototeca se pide únicamente cuando usas esas funciones.</p>
  <p><strong>La sincronización con iCloud</strong> viene activada para que tus productos y las fotos de los tickets te sigan entre tus dispositivos a través de tu cuenta personal de iCloud, bajo las condiciones de Apple; nosotros nunca tenemos acceso. Si la desactivas en Ajustes, tus datos se quedan solo en el dispositivo. Los avisos de garantía son notificaciones locales, programadas en tu dispositivo. La exportación CSV y el PDF por producto son archivos que creas y compartes tú.</p>
  <p><em>Publicada en la App Store por Sendoa Sola.</em></p>
  </section>

  <section id="tandem">
  <h3>Tandem</h3>
  <p>Tandem guarda los nombres de las dos personas, sus ingresos mensuales, cada gasto compartido (importe, categoría, fecha, quién pagó, cómo se repartió, nombre opcional) y cada liquidación <strong>en tu dispositivo</strong>, en un contenedor de App Group privado compartido solo con los widgets de la propia app. Tandem no tiene sistema de cuentas, ni analítica, ni código de terceros que reciba tus datos. Tiene dos compras opcionales: un desbloqueo «Tandem Pro» de pago único que abre las funciones extra de la app (Apple comprueba el derecho en tu dispositivo, incluido En familia; la app solo guarda si está activo) y un bote de propinas de compras sueltas que no desbloquean nada ni cambian nada de la app. Las procesa Apple las dos; nosotros no vemos tus datos de pago y no guardamos nada de ellas más allá de esa marca local y una cuenta local de cuántas veces has dejado propina. Un solo móvil lleva las cuentas de los dos; no se envía nada al dispositivo de la otra persona ni a nadie más.</p>
  <p><strong>La sincronización con iCloud</strong> viene activada para que tus gastos te sigan entre tus propios dispositivos a través de tu cuenta personal de iCloud, bajo las condiciones de Apple; nosotros nunca tenemos acceso. Si la desactivas en Ajustes, tus datos se quedan solo en el dispositivo. Los recordatorios semanal y de fin de mes son notificaciones locales.</p>
  <p><em>Publicada en la App Store por Sendoa Sola.</em></p>
  </section>

  <section id="meso">
  <h3>Meso</h3>
  <p>Meso guarda tus programas de entrenamiento (bloques, sesiones, ejercicios y sus prescripciones), cada sesión registrada (cargas, repeticiones, repeticiones en reserva, notas, el gimnasio que usaste) y tus propios ejercicios y gimnasios <strong>en tu dispositivo</strong>, en el contenedor privado de la app. Meso no tiene sistema de cuentas, ni analítica, ni código de terceros que reciba tus datos. Tiene dos compras opcionales: un desbloqueo «Meso Pro» de pago único que abre las funciones extra de la app (Apple comprueba el derecho en tu dispositivo, incluido En familia; la app solo guarda si está activo) y un bote de propinas de compras sueltas que no desbloquean nada ni cambian nada de la app. Las procesa Apple las dos; nosotros no vemos tus datos de pago y no guardamos nada de ellas más allá de esa marca local y una cuenta local de cuántas veces has dejado propina.</p>
  <p><strong>Apple Salud.</strong> Apagado por defecto. Si lo activas en Ajustes, cada sesión terminada se escribe en Salud como un entrenamiento de fuerza (inicio, fin y nombre) para que cuente en tu actividad. Meso nunca lee nada de Salud ni sube datos de Salud a ningún sitio; el permiso y la preferencia viven solo en ese dispositivo.</p>
  <p><strong>La sincronización con iCloud</strong> viene activada para que tus programas y sesiones te sigan entre tus dispositivos a través de tu cuenta personal de iCloud, bajo las condiciones de Apple; nosotros nunca tenemos acceso. Si la desactivas en Ajustes, tus datos se quedan solo en el dispositivo. Meso no tiene temporizador de descanso ni envía notificaciones. Mientras hay una sesión abierta, una Actividad en Directo muestra el ejercicio en curso y la siguiente serie en la pantalla de bloqueo; se dibuja en el dispositivo con lo que le pasa la app y termina con la sesión. El texto de la semana y el CSV del bloque que envías a un entrenador son archivos que creas y compartes tú.</p>
  <p><em>Publicada en la App Store por Sendoa Sola.</em></p>
  </section>

  <section id="grain">
  <h3>Grain</h3>
  <p>Grain guarda lo que anotas —cada alimento con su comida, día, gramos y los valores nutricionales copiados de su fuente—, tus metas diarias, y los alimentos y recetas que creas, corriges o escaneas <strong>en tu dispositivo</strong>, en el contenedor privado de la app y en un contenedor de App Group privado compartido solo con los widgets de la propia app. Grain no tiene sistema de cuentas, ni analítica, ni código de terceros que reciba tus datos. Tiene compras opcionales: un desbloqueo «Grain Pro» de pago único que abre las funciones extra de la app, con una prueba gratis de 30 días que se puede hacer una vez por Apple ID (Apple comprueba el derecho en tu dispositivo, incluido En familia; la app solo guarda si está activo y, durante la prueba, cuándo termina), y un bote de propinas de compras sueltas que no desbloquean nada ni cambian nada de la app. Las procesa Apple; nosotros no vemos tus datos de pago y no guardamos nada de ellas más allá de esa marca local y una cuenta local de cuántas veces has dejado propina.</p>
  <p><strong>Códigos de barras y Open Food Facts.</strong> El catálogo de alimentos (CIQUAL y BEDCA) va dentro de la app y se busca en el dispositivo. Cuando escaneas o escribes un código de barras que no está entre tus alimentos, Grain envía solo ese número a Open Food Facts (openfoodfacts.org, una base de datos de alimentos abierta y sin ánimo de lucro) para buscar el producto; la petición nombra la app, no a ti, y no se envía nada de tu diario. Open Food Facts trata esa petición según sus propias condiciones.</p>
  <p><strong>Enviar un producto a Open Food Facts.</strong> Solo si marcas «Enviar también a Open Food Facts» al guardar un alimento con código de barras, Grain envía ese producto —el código y sus valores por 100 g, y además su nombre y marca si es nuevo para Open Food Facts— a través de la cuenta de Grain en Open Food Facts, con un identificador aleatorio creado para esta instalación para que sus moderadores puedan distinguir las aportaciones. No se envía nada de tu diario, de tus metas ni de tu cuenta de Apple. Lo que envías se publica allí con la licencia Open Database License, para que cualquiera lo use, y Grain no puede retirarlo; Open Food Facts lo trata según sus propias condiciones.</p>
  <p><strong>Cámara, etiquetas y texto.</strong> La cámara solo se usa mientras escaneas un código de barras o fotografías una etiqueta nutricional, y no se graba nada. Las etiquetas, de la cámara o de una foto que eliges, se leen con el framework Vision de Apple en el propio dispositivo; una comida que describes con palabras se interpreta en el iPhone (con Apple Intelligence donde está disponible). Ni la imagen ni el texto salen del teléfono.</p>
  <p><strong>Apple Salud.</strong> Apagado por defecto. Si lo activas en Ajustes, cada anotación se escribe en Salud como comida (energía, proteína, hidratos y grasa), y se cambia o se borra allí cuando la editas o la borras en Grain. Grain nunca lee nada de Salud ni sube datos de Salud a ningún sitio; el permiso y la preferencia viven solo en ese dispositivo.</p>
  <p><strong>La sincronización con iCloud</strong> viene activada para que tu diario, tus metas y tus alimentos te sigan entre tus dispositivos a través de tu cuenta personal de iCloud, bajo las condiciones de Apple; nosotros nunca tenemos acceso. Si la desactivas en Ajustes, tus datos se quedan solo en el dispositivo. Grain no envía notificaciones.</p>
  <p><em>Publicada en la App Store por Sendoa Sola.</em></p>
  </section>

  <section id="gaminghub">
  <h3>GamingHub</h3>
  <p>GamingHub es una app de juegos para jugar en una sala con otras personas. No tiene cuenta, ni correo, ni contraseña.</p>
  <p>Para que una sala funcione, la app guarda el nombre que eliges, un avatar y un identificador anónimo creado en tu dispositivo. Esos datos, y el estado de la partida, se envían a nuestro servidor (Supabase) y se muestran a los demás jugadores de esa sala. Lo que escribes para el juego — pistas, papeles, canciones y cosas parecidas — forma parte de ese estado y se muestra a los demás jugadores. Los datos secretos de la partida (tu rol, la palabra o las cartas) se envían solo a tu dispositivo.</p>
  <p>Las salas se borran cuando se vacían y, en cualquier caso, se purgan a las 12 horas. No guardamos un historial de partidas.</p>
  <p>Esta versión no tiene publicidad, ni analítica, ni seguimiento. No vendemos tus datos.</p>
  <p>Las compras las procesa Apple. Solo sabemos qué juegos ha desbloqueado este dispositivo, nunca tus datos de pago.</p>
  <p>Si denuncias un problema o a un jugador, la app abre un mensaje a <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>. Esa denuncia es un correo que envías tú; no se guarda en el servidor del juego.</p>
  <p>Borrar la app elimina el identificador anónimo y los datos que estaban en el dispositivo. Las salas en las que jugaste desaparecen cuando caducan.</p>
  <p><em>Publicada en el App Store por Izotz Cristobal Mota.</em></p>
  </section>

  <section id="atino">
  <h3>Atino</h3>
  <p>Atino ordena ofertas de empleo según tu CV. Tu CV se queda en tu iPhone: Atino nunca sube el PDF y quita tu nombre y tus datos de contacto en el teléfono antes de que salga ningún texto. Solo después de que lo permitas, el texto redactado se envía a través de la pasarela de Seize a Command Code y TypeSafe AI (Jev) para ordenar las ofertas y explicar el encaje; pueden conservarlo según sus propias condiciones. La pasarela, que funciona en Supabase en la UE (Fráncfort, Alemania), guarda un registro pequeño por instalación —un identificador aleatorio, una clave de App Attest y los contadores de búsquedas del día— y lo borra a los 60 días sin actividad. No hay cuenta, ni publicidad, ni seguimiento. Apple procesa la suscripción; nosotros nunca vemos tus datos de pago. Atino comunica además tu suscripción a RevenueCat para analítica de compras (un identificador anónimo, tus compras en el App Store y la última vez que usaste la app); RevenueCat actúa siguiendo nuestras instrucciones y no recibe ningún texto del CV.</p>
  <p>Los detalles completos —qué se envía, quién lo recibe, cuánto tiempo se conserva y cómo retirar el permiso— están en <a href="../atino/privacidad/">la política de privacidad de Atino</a>.</p>
  <p><em>Publicada en la App Store por Izotz Cristobal Mota.</em></p>
  </section>

  <section id="overbit">
  <h3>Overbit</h3>
  <p>Overbit es una app de alertas del RSI de Bitcoin. No tiene cuenta, ni inicio de sesión, ni contraseña, y no opera ni custodia nada por ti.</p>
  <p><strong>Qué envía la app a nuestro servidor.</strong> Overbit usa un servidor de Seize (Supabase, Fráncfort, Alemania) para enviarte una alerta cuando el RSI cruza un nivel. Cada vez que la app está abierta y se actualiza, registra esta instalación con un identificador aleatorio creado en tu dispositivo, el idioma y la región de tu dispositivo y si Overbit Pro está desbloqueado en esa instalación. Mientras el interruptor de Notificaciones de Ajustes está activado y iOS permite que Overbit te notifique, el registro lleva además tu token de notificaciones push de Apple y los marcos temporales, la longitud del RSI y los niveles que elegiste. Si desactivas el interruptor, ese registro se sustituye al instante por otro sin token ni marcos temporales, y si desactivas las notificaciones de Overbit en iOS ocurre lo mismo la próxima vez que abras Overbit, de modo que el servidor deja de enviarte pushes. Después de usar Borrar mis datos (véase Tus datos más abajo), la app no vuelve a registrar este iPhone hasta que actives las alertas. El servidor guarda un registro por instalación y no lo borra cuando se borra la app, solo cuando usas Borrar mis datos; cuando Apple informa de que un token ya no es válido, el servidor lo borra. El registro de alertas ya enviadas se elimina a los 90 días.</p>
  <p><strong>Precios.</strong> El precio y las velas de la app salen de nuestro propio servidor, no de un exchange ni de ningún servicio al que te conectes tú. La app se los pide a nuestro proyecto de Supabase. Como cualquier servidor, recibe tu dirección IP con cada petición; la petición no lleva ningún identificador, nuestro código no lee ni guarda la dirección y Supabase, como nuestro proveedor de alojamiento, puede conservar registros de peticiones normales según sus propias condiciones. El propio servidor lee datos públicos de precio en la cadena (fondos de PancakeSwap y Aerodrome en Base, fondos de Uniswap en Ethereum) a través de proveedores de nodos, Alchemy y PublicNode. Esos proveedores solo ven las peticiones del servidor de datos públicos de la cadena de bloques; no reciben nada de tu teléfono ni nada sobre ti.</p>
  <p><strong>Comentarios (Overbit Pro).</strong> Si usas el buzón de comentarios, el mensaje que escribes se envía al mismo proyecto de Supabase junto con un correo de respuesta (solo si lo escribes), la versión y la compilación de la app, la versión de iOS, el modelo del dispositivo, el idioma y la región de tu dispositivo, el identificador aleatorio de arriba, el indicador de Pro y los marcos temporales que tenías activos. Lo leemos para darte soporte; no se publica. Lo conservamos hasta que nos pidas borrarlo.</p>
  <p><strong>Compras.</strong> Overbit Pro es una compra única que procesa Apple y que la app lee de StoreKit en tu dispositivo. El servidor solo guarda un indicador de sí o no de Pro junto al identificador de la instalación, para aplicar los límites de Pro a las alertas y a los comentarios; nunca vemos tu nombre ni tus datos de pago. La app incluye la biblioteca de RevenueCat para analítica de compras, pero en esta versión está desactivada, así que no se envía nada a RevenueCat.</p>
  <p>Esta versión no tiene publicidad, ni analítica, ni seguimiento, y no vendemos tus datos. Tus ajustes, el historial de alertas que ves en la app y el identificador aleatorio se guardan también en tu dispositivo.</p>
  <p><strong>Tus datos.</strong> El registro del servidor está ligado a un identificador aleatorio, no a tu nombre, tu correo ni una cuenta. En Overbit, Ajustes › Tus datos › Borrar mis datos elimina al instante el registro de esta instalación en el servidor (registro, marcos temporales e historial de alertas) y los comentarios que hayas enviado desde ella, y desactiva las alertas. Tus ajustes en el iPhone se quedan, y la app no vuelve a registrar este iPhone hasta que actives las alertas (sigue leyendo los precios del servidor, y los comentarios que envíes siguen llegándole). Borrar solo la app no elimina el registro del servidor, así que usa antes Borrar mis datos. Si ya borraste la app, escríbenos a <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>: solo podemos identificar un registro por un comentario que enviaste desde la app, que lleva el identificador, y borraremos lo que podamos identificar. Puedes dejar de recibir pushes cuando quieras con el interruptor de Notificaciones de los Ajustes de Overbit o en Ajustes de iOS › Notificaciones.</p>
  <p><em>Publicada en la App Store por Izotz Cristobal Mota.</em></p>
  </section>

  <h2>Notificaciones</h2>
  <p>Las apps que te recuerdan cosas usan notificaciones locales, programadas y entregadas en tu dispositivo. No operamos servidores de notificaciones push para estas funciones. <a href="#overbit">Overbit</a> es la excepción: se registra en un servidor de Seize para que este envíe sus alertas.</p>

  <h2>Tus derechos</h2>
  <p>Como tus datos viven en tu dispositivo, ejerces tus derechos directamente: borrar contenido en una app lo borra; borrar la app borra su contenedor; desactivar la sincronización con iCloud y borrar la app lo elimina también de iCloud (o gestiónalo en Ajustes › Cuenta de Apple › iCloud). Con arreglo al RGPD tienes además derechos de acceso, rectificación, supresión y portabilidad; como no tenemos datos personales tuyos, normalmente no hay nada que podamos entregarte, pero siempre puedes escribirnos con preguntas o solicitudes a <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>. La excepción es <a href="#overbit">Overbit</a>, que guarda en nuestro servidor un registro con un identificador aleatorio: bórralo en la app (Ajustes › Tus datos › Borrar mis datos) o pídenoslo ahí.</p>

  <h2>Menores</h2>
  <p>Nuestras apps son utilidades para público general y no recogen a sabiendas información personal de nadie, tampoco de menores.</p>

  <h2>Cambios</h2>
  <p>Si una app o función futura cambia algo de lo anterior (por ejemplo, una app que añada un servicio en línea), actualizaremos esta política y la etiqueta de privacidad de la app en la App Store antes de que esa función salga.</p>

  <h2>Contacto</h2>
  <p>Seize Apps · Izotz Cristobal Mota y Sendoa Sola<br><a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a></p>
'''

TERMS_ES='''
  <p class="eyebrow">Legal</p>
  <h1>Condiciones de uso</h1>
  <p class="effective">En vigor desde el 4 de octubre de 2026</p>

  <h2>1. Acuerdo</h2>
  <p>Estas condiciones regulan el uso de las apps publicadas bajo el nombre Seize Apps por Izotz Cristobal Mota y Sendoa Sola (País Vasco, España; «nosotros»). El vendedor de cada app es el desarrollador que figura en su ficha de la App Store. Las apps se distribuyen a través de la App Store de Apple y TestFlight. Al descargar o usar una app de Seize aceptas estas condiciones y el <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">Contrato de licencia de usuario final de aplicaciones</a> estándar de Apple, que se aplica en todo lo que estas condiciones no cubran. Garum tiene cuentas y contenido de usuarios, así que tiene <a href="../garum/condiciones/">sus propias condiciones de uso</a>, que se le aplican en lugar de estas.</p>

  <h2>2. Licencia</h2>
  <p>Te concedemos una licencia personal, no exclusiva e intransferible para usar nuestras apps en dispositivos Apple que poseas o controles, según permiten las condiciones de la App Store. Las apps, su diseño y su código siguen siendo nuestros.</p>

  <h2>3. Compras</h2>
  <p>Las apps de pago y las compras dentro de la app las factura Apple al precio que se muestra en la App Store antes de confirmar. Las suscripciones se renuevan solas al final de cada periodo, al mismo precio, salvo que las canceles al menos 24 horas antes en los ajustes de tu cuenta de Apple, donde puedes gestionarlas cuando quieras. Los reembolsos los gestiona Apple según las políticas de reembolso de la App Store; nosotros no podemos emitirlos directamente.</p>

  <h2>4. Tu contenido es tuyo</h2>
  <p>Todo lo que creas en una app de Seize (temporizadores, registros de trabajo, gastos, rutinas, tickets, registros de entrenamiento, diarios de comida) es tuyo. Como se describe en nuestra <a href="privacy.html">Política de privacidad</a>, se guarda en tu dispositivo y en tu propio iCloud y no tenemos acceso a ello, lo que también significa que <strong>las copias de seguridad son cosa tuya</strong>. La única excepción es un producto que decidas enviar a Open Food Facts desde Grain, que se publica allí con la licencia Open Database License. Borrar una app borra sus datos en ese dispositivo; lo que haya en tu iCloud se queda hasta que lo borres allí.</p>

  <h2>5. No es asesoramiento profesional</h2>
  <p>Nuestras apps son herramientas de organización. No son asesoramiento médico, nutricional, psicológico, financiero ni legal. Cualquier app nuestra que toque el bienestar es un acompañamiento y <strong>no sustituye al tratamiento profesional</strong>; si lo estás pasando mal, busca ayuda cualificada. Los plazos de garantía que muestra Kover son valores orientativos por defecto; tus derechos dependen de la ley y de las condiciones del vendedor que apliquen a cada compra.</p>

  <h2>6. Uso aceptable</h2>
  <p>No hagas ingeniería inversa, no revendas ni hagas un mal uso de las apps, y no las uses de ninguna forma que infrinja la ley o las condiciones de Apple.</p>

  <h2>7. Garantía y responsabilidad</h2>
  <p>Las apps se ofrecen «tal cual», sin garantías de ningún tipo. En la máxima medida que permite la ley, no respondemos de daños indirectos o consecuentes derivados del uso de las apps; nuestra responsabilidad total se limita al importe que hayas pagado por la app en los doce meses anteriores a la reclamación. Nada de estas condiciones limita los derechos que la legislación de consumo te concede y a los que no se puede renunciar.</p>

  <h2>8. Cambios</h2>
  <p>Podemos actualizar estas condiciones a medida que las apps evolucionen; la versión vigente vive siempre en esta dirección con su fecha de entrada en vigor arriba. Seguir usando las apps tras un cambio supone aceptar las condiciones actualizadas.</p>

  <h2>9. Ley aplicable</h2>
  <p>Estas condiciones se rigen por la legislación española. Los consumidores de la UE conservan además las protecciones de su país de residencia.</p>

  <h2>Contacto</h2>
  <p><a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a></p>
'''
