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
- **Solo tapa blanda** en Amazon por ahora; tiendas activas en la web: España y Estados Unidos (revisar en el lanzamiento).
- **Foto del autor:** más adelante; la página de autor funciona sin ella.
- **No se publica en 7espigas.com** hasta tener los textos legales y el formulario de Kit conectado.

- **Vista previa privada:** https://claude.ai/artifact/37w3EZaX6i4RKnYYtJNmvp, generada con `python3 preview.py` (rutas relativas). Se actualiza a mano tras cada cambio.
- **Texto de El coste de la distancia en la web**, adaptado: plural inclusivo en lugar del usted de la contracubierta.
- **Correo:** hola@7espigas.com (plan Mini de DonDominio), contacto y remitente del boletín.
- **Dominios secundarios** (7espigas.es, sieteespigas.com, sieteespigas.es): redirección permanente a 7espigas.com.
- **Datos legales:** pendientes; el aviso legal llevará huecos que Raquel rellenará antes de publicar.

## Bocetos

- 7 nov: primeras direcciones A (colección) y B (novedad destacada). Descartado el enfoque personalista de ambas; pendiente rehacerlas con el sello en primer plano.

## Pendiente

- Texto de «Por qué 7 Espigas».
- Nombre o gancho del boletín.
- Frase de la colección.
