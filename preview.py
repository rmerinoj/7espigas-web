#!/usr/bin/env python3
"""Genera una copia de _site con rutas relativas (para vistas previas fuera del dominio): _preview/."""
import re, shutil, subprocess
from pathlib import Path
R=Path(__file__).parent; S=R/"_site"; P=R/"_preview"
subprocess.run(["python3",str(R/"build.py")],check=True)
if P.exists(): shutil.rmtree(P)
shutil.copytree(S,P)
for f in P.rglob("*.html"):
    d=len(f.relative_to(P).parts)-1; pre="../"*d or "./"
    s=f.read_text(encoding="utf-8")
    def fix(m):
        attr,url=m.group(1),m.group(2)
        frag=""
        if "#" in url: url,frag=url.split("#",1); frag="#"+frag
        if url=="" : return f'{attr}="{frag}"'
        if url.endswith("/"): url+= "index.html"
        return f'{attr}="{pre}{url.lstrip("/")}{frag}"'
    s=re.sub(r'(href|src|srcset)="(/[^"]*)"',fix,s)
    f.write_text(s,encoding="utf-8")
c=P/"estilo.css"; c.write_text(c.read_text().replace("url(/fonts/","url(fonts/"))
print("Vista previa en",P)
