# Decisiones de la web

Registro de decisiones adoptadas sobre 7espigas.com. Las generales del proyecto están en `7ESPIGAS\00 Decisiones 7 Espigas.txt` (Drive de Raquel).

## 7 de noviembre de 2026

- **Alojamiento:** GitHub Pages en este repositorio; el dominio 7espigas.com (DonDominio) apuntará aquí. La mantiene Claude con indicaciones de Raquel.
- **Páginas mínimas** (decidido el 4 nov): Inicio, Libros (una ficha por libro), Por qué 7 Espigas, Autor, Boletín y páginas legales (aviso legal, privacidad, cookies).
- **Enfoque:** la web es del sello 7 Espigas, no del autor. La portada presenta el sello, su lema («Todos lo viven, pocos lo entienden») y su sentido; los libros aparecen con José Ignacio del Castillo como autor. Habrá contenidos de más personas.
- **Marca:** con más presencia en la cabecera que en los primeros bocetos. Al referirse a ella, «7 Espigas», nunca «siete granos».
- **El aro de la colección** debe estar presente de algún modo en la web.
- **Tratamiento:** de tú, con mesura: preferir preguntas impersonales y el plural inclusivo. Nada de imperativos de captación ni promesas.
- ~~Áreas con color~~: sustituido por color por colección (boceto E).
- **Amazon:** botón principal a la tienda que corresponda por idioma y zona horaria del navegador (sin cookies); enlaces fijos a las demás tiendas debajo.
- **Boletín (Kit):** debe ofrecer algo concreto y con valor; nada de «cuando nos apetezca». Promesa pendiente de decidir.

## 8 de noviembre de 2026

- **Colección:** «Economía para todos» (aprobado por José Ignacio). Falta la frase que la acompaña.
- **Boletín:** contenido abierto a propósito: algún análisis cada quince días aproximadamente, capítulos, píldoras y novedades. El texto debe transmitir que es algo vivo frente al libro. Falta el nombre o gancho.
- **Enlaces:** cada ficha de libro de la portada lleva a la página del libro; el autor enlaza a su página desde las fichas de sus libros.
- **Infografía del orden de lectura** en la sección de libros, sin dar a entender que haya que seguirlo.

- **Cabecera de la portada:** sin repetir las cubiertas, que ya aparecen más abajo; en su lugar, un elemento de la colección (el aro) que remita a ellas.
- **Muestrario:** todos los bocetos y versiones se guardan en el Muestrario tipográfico (https://claude.ai/artifact/Ub9WBwkQLpYPzc4S8ynuYF).
- **Logotipo:** espacio antes del «7» reducido (−6); usar los archivos nuevos de 7ESPIGAS\Marca.
- **Infografía de la colección:** circular, cuatro cuadrantes (qué, cómo, dónde, cuándo); concepto en el Drive.

## 8 de noviembre de 2026 (tarde)

- **El lema «Todos lo viven, pocos lo entienden» queda aparcado** como lema propio: resulta pretencioso atribuírnoslo. Solo se usará como cita de Goethe, cuando venga a cuento.
- **Foco de la web: la colección y los libros**, que ya existen y queremos vender. Nada de prometer contenidos o comunidad que todavía no hay; 7 Espigas se presenta como un espacio que irá creciendo alrededor de la temática, con pequeños monográficos cuando los haya.
- **Colección:** «Economía para todos», con la pregunta «¿Qué hay detrás de lo que vivimos cada día?».
- **Boletín:** «Transformaciones económicas en tiempo real».
- **Fichas de libro:** con enlace directo «Comprar en Amazon» en cada una, además de «Ver el libro».

## 8 de noviembre de 2026 (boceto D)

- **Tono visual:** 7 Espigas no es una editorial al uso (Amazon, otros productos y formatos): rigor, pero no seriedad acartonada. Menos crema y más color: bloques con fondo de color, cabecera en azul noche.
- **Formas:** etiquetas en píldora y botones con esquinas redondeadas (unos 6 px); fichas y bloques con radio suave (10–14 px). Las cubiertas, a escuadra. Sistema de diseño ya actualizado.
- ~~Colores por libro (estaciones)~~: descartado; ver boceto E.
- **El círculo:** sobre fondo azul relleno, con trazo grueso; etiquetas qué, cómo, dónde y cuándo en cruz (0°, 90°, 180°, 270°). Dos variantes en estudio: cuatro arcos de color o aro dorado cerrado, como el de los lomos.
- **Fichas de libro:** en horizontal (cuatro en fila), con fondo de su color; no en lista vertical.
- **Textos fijados por Raquel:** antetítulo «Economía para todos»; entradilla «Cada libro es una unidad que puede leerse por separado; juntos forman un círculo económico que responde al qué, al cómo, al dónde y al cuándo»; presentación de los libros sobre el orden de lectura; texto del boletín.
- **Sección del nombre:** «Cómo nace 7 Espigas» (no «Por qué este nombre»).
- **Animaciones:** solo fundidos suaves al entrar los bloques y un leve movimiento de las cubiertas; nada si el usuario pide reducir movimiento.

## 8 de noviembre de 2026 (boceto E): color por colección

- **Sustituye** a las «áreas con color» del 7 nov y a los colores por libro del boceto D.
- **Tres capas:** marca (azul noche, crema, tinta, dorado) en toda la estructura; una familia de color por colección («Economía para todos»: dorado); temas y formatos, etiquetas neutras.
- **En la web:** círculo de cuatro arcos dorados sobre disco azul, con los títulos de los libros; tarjetas de libro con el mismo tinte dorado y píldora de cuadrante + etiqueta neutra «Libro»; boletín en azul noche con etiqueta neutra.
- **Las estaciones**, solo dentro de Las cuatro estaciones del dinero.

- **Textos:** los aprobados viven en `docs/textos-web.md` (8 nov). «Cómo nace 7 Espigas» tendrá versión corta en portada y larga en página propia.

- **Enlaces de Amazon (8 nov):** se guarda el ASIN de cada libro en `data/libros.json`; el enlace se construye como `amazon.<tienda>/dp/<ASIN>`. Tienda principal según idioma y zona horaria del navegador (sin cookies ni IP), con enlaces a las demás debajo. Antes de publicar, comprobar en qué tiendas está disponible cada libro.

## 8 de noviembre de 2026: primera versión construida

- **Técnica:** web estática generada con `build.py` a partir de `data/libros.json` y `docs/textos-web.md`; se publica sola con GitHub Actions al subir cambios a `main`.
- **Fuentes servidas desde la propia web**, no desde Google Fonts, para no enviar datos de los visitantes a terceros.
- **Solo tapa blanda** en Amazon por ahora; tiendas activas en la web: España y Estados Unidos (revisar en el lanzamiento). Ampliado el 8 nov (noche) a todas las de tapa blanda; ver abajo.
- **Foto del autor:** más adelante; la página de autor funciona sin ella.
- **No se publica en 7espigas.com** hasta tener los textos legales y el formulario de Kit conectado.

- **Vista previa privada:** https://claude.ai/artifact/37w3EZaX6i4RKnYYtJNmvp, generada con `python3 preview.py` (rutas relativas). Se actualiza a mano tras cada cambio.
- **Texto de El coste de la distancia en la web**, adaptado: plural inclusivo en lugar del usted de la contracubierta.
- **Correo:** hola@7espigas.com (plan Mini de DonDominio), contacto y remitente del boletín.
- **Dominios secundarios** (7espigas.es, sieteespigas.com, sieteespigas.es): redirección permanente a 7espigas.com.
- **Datos legales:** pendientes; el aviso legal llevará huecos que Raquel rellenará antes de publicar.

- **Boletín conectado a Kit (8 nov):** formulario «Web 7espigas.com» (n.º 10161891), con confirmación por correo; dominio 7espigas.com autenticado en Kit; remitente «7 Espigas» <hola@7espigas.com>. Al confirmar, Kit redirige de momento a su página por defecto; cambiar a 7espigas.com/gracias/ al publicar.

- **Publicación (8 nov):** GitHub Pages con origen «GitHub Actions» y dominio 7espigas.com. DNS en DonDominio: eliminado el ANAME de la raíz (alojamiento de DonDominio); cuatro registros A a GitHub (185.199.108.153, .109.153, .110.153, .111.153); `www` como CNAME a `rmerinoj.github.io`; TXT `_github-pages-challenge-rmerinoj` para verificar el dominio. Los registros del correo y de Kit no se tocan.

## 8 de noviembre de 2026 (noche): ajustes tras revisar la vista previa

- **Autor en la portada:** bloque discreto (solo filete, sin fondo de color) después de «Cómo nace 7 Espigas» y antes del boletín, con dos líneas y enlace a su página; la foto, cuando la haya. No va el nombre en las tarjetas de la portada. Hoy hay una colección y un autor, y quien quiera ubicarse necesita saber quién la escribe; si llegan más autores, el bloque pasará a ser «Autores». Sustituye a lo anotado antes esa misma noche (ni bloque ni nombre).
- **Página de cada libro:** el nombre del autor, sin más, enlaza a su página (se quita «· Sobre el autor»).
- **Enlaces sin subrayado:** se distinguen por color (dorado oscuro en el texto) y peso; el subrayado aparece solo al pasar el ratón.
- **Cabecera fija** en ordenador (más de 980 px); en tableta y móvil, no. Logotipo de la cabecera a 52 px de alto (antes 42): había quedado pequeño frente al resto.
- **Encabezado de «Los libros»:** título y entradilla en una columna (antes, a los lados y alineados por abajo, lo que dejaba el título bajo frente a un texto largo).
- **Amazon:** en la portada, el botón; debajo, un enlace discreto «Comprar en otros países» (y, después, «Más detalles») que lleva a la página del libro con el desplegable ya abierto (antes «También en Estados Unidos»). En la página de cada libro, desplegable «Comprar en otros países» con todas las tiendas en las que KDP vende tapa blanda (Alemania, Australia, Bélgica, Canadá, España, Estados Unidos, Francia, Irlanda, Italia, Japón, Países Bajos, Polonia, Reino Unido y Suecia), menos la del visitante. México no admite tapa blanda de KDP. Antes del lanzamiento, comprobar que los enlaces funcionan.
- **Descripciones de los libros:** propuesta a partir de las contracubiertas, en `docs/textos-web.md`, pendiente de revisión. En Matar al mensajero se usa «fijar alquileres máximos» en lugar de «topar» (corrección pendiente también en el libro).
- **Migas de pan:** solo en las páginas que cuelgan de otra (hoy, las de los libros); las de primer nivel están en el menú.

- **Botón de compra con la tienda a la vista:** «Comprar en Amazon.es» (o .com, .co.uk… según el visitante), para que se distinga de «Comprar en otros países».
- **Subrayados:** no se trata de eliminarlos todos, sino de no abusar; de momento, la solución sin subrayado (salvo al pasar el ratón) se da por buena.
- **Ilustración de «Cómo nace 7 Espigas»:** dibujo plano, en la línea de la gallina de La riqueza: una espiga llena (el grano del símbolo, ampliado) y otra mustia, doblada por el viento, con granos caídos. Va en la página interior; en la portada no hace falta. Archivos: `src/img/sueno-espigas-vertical.svg` (la que se usa) y `sueno-espigas.svg` (apaisada, de reserva).

- **Caché del navegador:** el CSS y el JS se enlazan con una huella de su contenido (`estilo.css?v=…`), para que, tras cada cambio, nadie vea la página nueva con el estilo antiguo.

- **Rejilla única para las páginas interiores (8 nov):** todas usan la de la ficha de libro: columna estrecha a la izquierda (360 px) y texto a la derecha, siempre en la misma posición y con el mismo ancho de lectura (unos 680 px, 70–80 caracteres por línea). A la izquierda va la imagen si la hay (cubierta, ilustración, foto del autor cuando exista); si no, la etiqueta y el título. Así el texto empieza siempre en el mismo sitio y no queda media página vacía. En móvil, una sola columna. Vale también para las páginas nuevas.
- **Pie de página** siempre al fondo de la ventana, aunque la página sea corta. Fondo «oro tinte» (#EEE6D4, el de las tarjetas), firma para fondo claro y enlaces en gris: había exceso de azul noche, sobre todo al final de la portada (boletín y pie seguidos). El azul queda en la cabecera, la portada y el boletín.

- **Cabecera fija que se aparta (8 nov):** en ordenador, la cabecera se oculta al bajar y reaparece en cuanto se sube un poco (y siempre arriba del todo, o si se llega a ella con el teclado). No se usa la reaparición al pasar el ratón: no funciona en pantallas táctiles, nadie sabe que está ahí y salta sin querer al ir a las pestañas del navegador. Sin flecha de «volver arriba» por ahora: las páginas son cortas; se reconsidera si llegan páginas largas (artículos del boletín, por ejemplo).

- **Barra de desplazamiento:** se reserva siempre su hueco (`scrollbar-gutter: stable`), para que las páginas cortas, que no la tienen, no se desplacen unos píxeles a la derecha respecto de las largas.

- **Dominios secundarios (9 nov):** 7espigas.es, sieteespigas.com y sieteespigas.es reenvían a https://7espigas.com, conservando la ruta, mediante un repositorio mínimo de GitHub Pages por dominio (`rmerinoj/7espigas-es`, `rmerinoj/sieteespigas-com`, `rmerinoj/sieteespigas-es`). DNS en DonDominio igual que el principal (cuatro A de GitHub y `www` CNAME a rmerinoj.github.io; borrados el ANAME y el `*` de parking). Se descartó la redirección de DonDominio: no admite https (conexión rechazada) y Chrome tardaba mucho en caer a http.

- **«sieteespigas.com» en el pie (9 nov):** bajo la firma, en texto pequeño y gris: «También en sieteespigas.com». No como segundo logotipo: la marca se escribe con «7» y el logo va una sola vez; la línea solo aclara que la dirección dicha en voz alta también funciona.

## Bocetos

- 7 nov: primeras direcciones A (colección) y B (novedad destacada). Descartado el enfoque personalista de ambas; pendiente rehacerlas con el sello en primer plano.

## Pendiente

- Texto de «Por qué 7 Espigas».
- Nombre o gancho del boletín.
- Frase de la colección.
