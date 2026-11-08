# 7espigas-web

Web de 7 Espigas (7espigas.com): libros de economía y finanzas de José Ignacio del Castillo.

## Cómo se genera

- `data/libros.json`: los libros (título, subtítulo, ASIN de Amazon).
- `docs/textos-web.md`: todos los textos de la web.
- `src/`: estilos, script, imágenes, fuentes y archivos de marca.
- `python3 build.py` genera la web en `_site/`. Al subir cambios a `main`, GitHub la publica sola.
