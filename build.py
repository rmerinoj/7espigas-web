#!/usr/bin/env python3
"""Genera la web estática de 7 Espigas en _site/.

Fuentes: data/libros.json (libros), docs/textos-web.md (textos), src/ (estilos, script, imágenes, fuentes, marca).
Uso: python3 build.py
"""
import html
import json
import math
import re
import hashlib
import shutil
from pathlib import Path

RAIZ = Path(__file__).parent
SALIDA = RAIZ / "_site"
DOMINIO = "https://7espigas.com"
TIENDAS = "de,au,be,ca,es,com,fr,ie,it,jp,nl,pl,uk,se"  # tiendas de Amazon con tapa blanda de KDP, en orden alfabético del país (comprobar antes del lanzamiento)
KIT_FORMULARIO = "10161891"  # formulario «Web 7espigas.com» de Kit (con confirmación por correo)

libros = sorted(json.loads((RAIZ / "data/libros.json").read_text(encoding="utf-8")), key=lambda l: l["orden"])


# ---------- textos ----------
def secciones(md):
    out, actual = {}, None
    for linea in md.splitlines():
        if linea.startswith("## "):
            actual = linea[3:].strip()
            out[actual] = []
        elif actual is not None:
            out[actual].append(linea)
    return out


S = secciones((RAIZ / "docs/textos-web.md").read_text(encoding="utf-8"))


def campos(nombre):
    d = {}
    for l in S[nombre]:
        m = re.match(r"- ([^:]+): (.+)", l)
        if m:
            d[m.group(1).strip()] = m.group(2).strip()
    return d


def parrafos(nombre):
    texto = "\n".join(l for l in S[nombre] if not l.startswith("- ") and not l.startswith("Enlace:"))
    return [p.strip().replace("\n", " ") for p in texto.split("\n\n") if p.strip()]


def enlace(nombre):
    for l in S[nombre]:
        if l.startswith("Enlace:"):
            return l[len("Enlace:"):].strip()
    return ""


def version(ruta):
    """Huella corta del archivo, para que el navegador no use una copia antigua del CSS o del JS."""
    return hashlib.sha1((RAIZ / "src" / ruta).read_bytes()).hexdigest()[:8]


def esc(t):
    return html.escape(t, quote=True)


def cursivas(t):
    """Convierte *texto* en <em> tras escapar."""
    return re.sub(r"\*([^*]+)\*", r"<em>\1</em>", esc(t))


portada = campos("Portada · cabecera")
boletin = campos("Boletín")


# ---------- piezas ----------
def circulo():
    W, c, R, sw = 680, 340, 150, 34
    oro, noche = "#C4A464", "#1E2D47"
    s = [f'<svg viewBox="0 0 {W} {W}" role="img" aria-label="La colección como un círculo: 1, qué (La riqueza); 2, cómo (Matar al mensajero); 3, dónde (El coste de la distancia); 4, cuándo (Las cuatro estaciones del dinero)">',
         f'<circle cx="{c}" cy="{c}" r="{R + 62}" fill="#26375A"/>']
    for i in range(4):
        a0 = math.radians(-90 + i * 90 - 45 + 8)
        a1 = math.radians(-90 + i * 90 + 45 - 8)
        s.append(f'<path d="M{c + R * math.cos(a0):.1f},{c + R * math.sin(a0):.1f} A{R},{R} 0 0 1 {c + R * math.cos(a1):.1f},{c + R * math.sin(a1):.1f}" fill="none" stroke="{oro}" stroke-width="{sw}" stroke-linecap="round"/>')
    s.append(f'<text x="{c}" y="{c - 6}" text-anchor="middle" font-family="Archivo Narrow, Arial Narrow, sans-serif" font-weight="700" font-size="28" fill="#F6F1E7">Economía</text>')
    s.append(f'<text x="{c}" y="{c + 25}" text-anchor="middle" font-family="Archivo Narrow, Arial Narrow, sans-serif" font-weight="700" font-size="28" fill="#F6F1E7">para todos</text>')
    pos = [(c, c - R), (c + R, c), (c, c + R), (c - R, c)]
    tit = [(c, c - R - 80, "middle", ["La riqueza"]), (c + R + 72, c - 8, "start", ["Matar al", "mensajero"]),
           (c, c + R + 92, "middle", ["El coste de la distancia"]), (c - R - 72, c - 16, "end", ["Las cuatro", "estaciones", "del dinero"])]
    for i, (x, y) in enumerate(pos):
        l = libros[i]
        s.append(f'<a href="/libros/{l["id"]}/"><rect x="{x - 50}" y="{y - 16}" width="100" height="32" rx="16" fill="{noche}" stroke="{oro}" stroke-width="2"/>'
                 f'<text x="{x}" y="{y + 5}" text-anchor="middle" font-family="Inter, sans-serif" font-weight="600" font-size="13" letter-spacing="1.4" fill="#F6F1E7">{i + 1} · {l["pregunta"].upper()}</text>')
        tx, ty, anc, ls = tit[i]
        for j, linea in enumerate(ls):
            s.append(f'<text x="{tx}" y="{ty + j * 20}" text-anchor="{anc}" class="titulo-libro" font-family="Source Serif 4, Georgia, serif" font-style="italic" font-size="18" fill="#E2C98F">{esc(linea)}</text>')
        s.append("</a>")
    s.append("</svg>")
    return "".join(s)


def compra(l, ver=True, paises=False):
    """Botón de compra; en la portada, debajo, «Comprar en otros países» y después «Más detalles»."""
    if paises:
        otros = '<details class="paises" hidden><summary>Comprar en otros países</summary><ul></ul></details>'
    elif ver:
        otros = f'<p class="otras"><a href="/libros/{l["id"]}/#paises">Comprar en otros países</a></p>'
    else:
        otros = ""
    v = f'<p class="detalles"><a class="ver" href="/libros/{l["id"]}/">Más detalles</a></p>' if ver else ""
    return (f'<div class="compra" data-asin="{l["asin"]}"><div class="acciones">'
            f'<a class="boton noche comprar" href="{l["amazon_es"]}" rel="noopener">Comprar en Amazon.es</a></div>'
            f'{otros}{v}</div>')


def tarjeta(l):
    return f'''<article class="tarjeta aparece">
<a href="/libros/{l["id"]}/" tabindex="-1" aria-hidden="true"><picture><source srcset="/img/{l["id"]}.webp" type="image/webp"><img class="cubierta" src="/img/{l["id"]}.jpg" width="600" height="900" alt="" loading="lazy"></picture></a>
<div><div class="etiquetas"><span class="pildora">{l["orden"]} · {esc(l["pregunta"])}</span><span class="pildora neutra">Libro</span></div>
<h3><a href="/libros/{l["id"]}/">{esc(l["titulo"])}</a></h3>
<p class="subtitulo">{esc(l["subtitulo"])}</p>
{compra(l)}</div></article>'''


def pagina(titulo, descripcion, cuerpo, ruta):
    t = f"{titulo} · 7 Espigas" if titulo != "7 Espigas" else "7 Espigas · Economía para todos"
    return f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(t)}</title>
<meta name="description" content="{esc(descripcion)}">
<link rel="canonical" href="{DOMINIO}{ruta}">
<link rel="icon" href="/marca/favicon.svg" type="image/svg+xml">
<link rel="preload" href="/fonts/archivo-narrow-latin-700-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/estilo.css?v={version("estilo.css")}">
<meta property="og:title" content="{esc(t)}">
<meta property="og:description" content="{esc(descripcion)}">
<meta property="og:locale" content="es_ES">
<script>document.documentElement.className="js"</script>
</head>
<body data-tiendas="{TIENDAS}">
<a class="salto" href="#contenido">Saltar al contenido</a>
<header class="cabecera"><div class="envoltorio">
<a href="/" aria-label="7 Espigas, inicio"><img src="/marca/7espigas-logotipo-sobre-oscuro.svg" alt="7 Espigas" width="189" height="52"></a>
<nav aria-label="Principal"><a href="/#libros">Libros</a><a href="/como-nace/">Cómo nace<span class="largo"> 7 Espigas</span></a><a href="/autor/">El autor</a><a href="/#boletin">Boletín</a></nav>
</div></header>
<main id="contenido">
{cuerpo}
</main>
<footer class="pie"><div class="envoltorio">
<img src="/marca/7espigas-firma-web-sobre-claro.svg" alt="7espigas.com" width="104" height="26">
<nav aria-label="Legal"><a href="/aviso-legal/">Aviso legal</a><a href="/privacidad/">Privacidad</a><a href="/cookies/">Cookies</a></nav>
</div></footer>
<script src="/web.js?v={version("web.js")}" defer></script>
</body>
</html>
'''


def bloque_boletin():
    return f'''<section id="boletin" style="padding-top:0"><div class="envoltorio"><div class="bloque noche aparece">
<div><span class="pildora neutra">{esc(boletin["Etiqueta"])}</span><h2>{esc(boletin["Titular"])}</h2>
<p style="margin-top:16px">{esc(boletin["Texto"])}</p></div>
<form class="formulario boletin" action="https://app.kit.com/forms/{KIT_FORMULARIO}/subscriptions" method="post">
<label for="correo">Correo electrónico</label>
<div class="fila"><input id="correo" type="email" name="email_address" placeholder="nombre@ejemplo.com" autocomplete="email" required><button class="boton oro" type="submit">Suscribirme</button></div>
<p class="nota">{esc(boletin["Nota bajo el formulario"])} Al suscribirte aceptas la <a href="/privacidad/">política de privacidad</a>.</p>
<p class="respuesta" role="status" aria-live="polite" hidden></p>
</form></div></div></section>'''


# ---------- páginas ----------
def inicio():
    corta = parrafos("Portada · Cómo nace 7 Espigas (versión corta)")
    cuerpo = f'''<section class="portada"><div class="envoltorio">
<div><span class="pildora">{esc(portada["Antetítulo"])}</span>
<h1>{esc(portada["Titular"])}</h1>
<p>{esc(portada["Entradilla"])}</p>
<a class="boton oro" href="#libros">{esc(portada["Botón"])}</a></div>
<div class="circulo">{circulo()}</div>
</div></section>
<section id="libros"><div class="envoltorio">
<div class="encabezado-seccion"><h2>Los libros</h2><p>{esc(" ".join(parrafos("Portada · los libros")))}</p></div>
<div class="libros">{"".join(tarjeta(l) for l in libros)}</div>
</div></section>
<section style="padding-top:0"><div class="envoltorio"><div class="bloque oro aparece">
<div><span class="pildora">7 Espigas</span><h2>Cómo nace 7 Espigas</h2></div>
<div>{"".join(f"<p>{esc(p)}</p>" for p in corta)}<a class="enlace" href="/como-nace/">Leer la historia completa →</a></div>
</div></div></section>
<section style="padding-top:0"><div class="envoltorio"><div class="bloque linea aparece">
<div><span class="pildora neutra">El autor</span><h2>José Ignacio del Castillo</h2></div>
<div>{"".join(f"<p>{esc(p)}</p>" for p in parrafos("Portada · El autor (bloque breve)"))}<a class="enlace" href="/autor/">{esc(enlace("Portada · El autor (bloque breve)"))}</a></div>
</div></div></section>
{bloque_boletin()}'''
    return pagina("7 Espigas", portada["Entradilla"], cuerpo, "/")


def pagina_libro(l):
    nombre = f"Libro · {l['titulo']}"
    desc = parrafos(nombre) if nombre in S else []
    otros = "".join(f'<li><a href="/libros/{o["id"]}/">{o["orden"]} · {esc(o["pregunta"])}: <em>{esc(o["titulo"])}</em></a></li>' for o in libros if o is not l)
    texto = "".join(f"<p>{esc(p)}</p>" for p in desc) or f'<p>{esc(l["subtitulo"])}.</p>'
    cuerpo = f'''<section><div class="envoltorio">
<p class="miga"><a href="/">Inicio</a> · <a href="/#libros">Libros</a></p>
<div class="ficha" style="margin-top:28px">
<picture><source srcset="/img/{l["id"]}.webp" type="image/webp"><img class="cubierta" src="/img/{l["id"]}.jpg" width="600" height="900" alt="Cubierta de {esc(l["titulo"])}"></picture>
<div><div class="etiquetas" style="display:flex;gap:6px"><span class="pildora">{l["orden"]} · {esc(l["pregunta"])}</span><span class="pildora neutra">Libro</span></div>
<h1>{esc(l["titulo"])}</h1>
<p class="subtitulo">{esc(l["subtitulo"])}</p>
<p class="autor-libro"><a href="/autor/">{esc(l["autor"])}</a></p>
{compra(l, ver=False, paises=True)}
<div class="texto" style="margin-top:36px">{texto}</div>
<h2 style="font-size:28px;margin:40px 0 12px">Los otros libros de la colección</h2>
<ul style="padding-left:20px;margin:0">{otros}</ul>
</div></div></div></section>'''
    return pagina(l["titulo"], f'{l["titulo"]}. {l["subtitulo"]}. Colección Economía para todos.', cuerpo, f'/libros/{l["id"]}/')


def pagina_texto(titulo, etiqueta, parrs, ruta, descripcion, imagen=""):
    """Páginas interiores con la misma rejilla que la ficha de un libro: columna estrecha a la izquierda
    (la imagen, si la hay; si no, la etiqueta y el título) y el texto siempre en la columna derecha."""
    cabeza = f'<span class="pildora">{esc(etiqueta)}</span><h1>{esc(titulo)}</h1>'
    texto = "".join(f"<p>{esc(p)}</p>" for p in parrs)
    if imagen:
        izquierda, derecha = imagen, cabeza + texto
    else:
        izquierda, derecha = f'<div class="titulo-lateral">{cabeza}</div>', texto
    cuerpo = f'''<section><div class="envoltorio"><div class="ficha interior">
<div class="lateral">{izquierda}</div>
<div class="texto">{derecha}</div>
</div></div></section>'''
    return pagina(titulo, descripcion, cuerpo, ruta)


def escribir(ruta, contenido):
    destino = SALIDA / ruta.strip("/") / "index.html" if ruta != "/" else SALIDA / "index.html"
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(contenido, encoding="utf-8")


def main():
    if SALIDA.exists():
        shutil.rmtree(SALIDA)
    shutil.copytree(RAIZ / "src", SALIDA)
    escribir("/", inicio())
    for l in libros:
        escribir(f"/libros/{l['id']}/", pagina_libro(l))
    escribir("/como-nace/", pagina_texto("Cómo nace 7 Espigas", "7 Espigas", parrafos("Página interior · Cómo nace 7 Espigas (versión larga)"), "/como-nace/", "El sueño del faraón, las siete espigas y la idea de la que nace 7 Espigas.",
        '<figure class="ilustracion"><img src="/img/sueno-espigas-vertical.svg" width="540" height="700" alt="Una espiga llena y dorada junto a otra seca y doblada por el viento, con granos caídos a sus pies."></figure>'))
    escribir("/autor/", pagina_texto("José Ignacio del Castillo", "El autor", parrafos("El autor"), "/autor/", "José Ignacio del Castillo, autor de la colección Economía para todos."))
    escribir("/aviso-legal/", pagina_texto("Aviso legal", "Legal", parrafos("Aviso legal"), "/aviso-legal/", "Aviso legal de 7espigas.com."))
    escribir("/privacidad/", pagina_texto("Privacidad", "Legal", parrafos("Privacidad"), "/privacidad/", "Política de privacidad de 7espigas.com."))
    escribir("/cookies/", pagina_texto("Cookies", "Legal", parrafos("Cookies"), "/cookies/", "Política de cookies de 7espigas.com."))
    (SALIDA / "CNAME").write_text("7espigas.com\n")
    (SALIDA / ".nojekyll").write_text("")
    print("Web generada en", SALIDA)


if __name__ == "__main__":
    main()
