/* 7 Espigas: tienda de Amazon según el navegador (sin cookies ni IP) y aparición suave de bloques. */
(function(){
  var tiendas={de:["amazon.de","Alemania"],au:["amazon.com.au","Australia"],be:["amazon.com.be","Bélgica"],ca:["amazon.ca","Canadá"],es:["amazon.es","España"],com:["amazon.com","Estados Unidos"],fr:["amazon.fr","Francia"],ie:["amazon.ie","Irlanda"],it:["amazon.it","Italia"],jp:["amazon.co.jp","Japón"],nl:["amazon.nl","Países Bajos"],pl:["amazon.pl","Polonia"],uk:["amazon.co.uk","Reino Unido"],se:["amazon.se","Suecia"]};
  function elegir(){
    var idioma=(navigator.language||"es-ES").toLowerCase(), zona="";
    try{zona=Intl.DateTimeFormat().resolvedOptions().timeZone||"";}catch(e){}
    if(zona==="Europe/Madrid"||zona==="Atlantic/Canary"||zona==="Africa/Ceuta"||idioma==="es-es") return "es";
    if(idioma.indexOf("es")===0) return zona.indexOf("America/")===0?"com":"es";
    var porZona={"Europe/London":"uk","Europe/Dublin":"ie","Europe/Berlin":"de","Europe/Vienna":"de","Europe/Zurich":"de","Europe/Paris":"fr","Europe/Rome":"it","Europe/Amsterdam":"nl","Europe/Brussels":"be","Europe/Warsaw":"pl","Europe/Stockholm":"se","Asia/Tokyo":"jp","America/Toronto":"ca","America/Vancouver":"ca","America/Montreal":"ca"};
    if(porZona[zona]) return porZona[zona];
    if(zona.indexOf("Australia/")===0) return "au";
    var porIdioma={de:"de",fr:"fr",it:"it",nl:"nl",pl:"pl",sv:"se",ja:"jp"};
    if(idioma==="en-gb") return "uk"; if(idioma==="en-ie") return "ie"; if(idioma==="en-ca") return "ca"; if(idioma==="en-au") return "au";
    return porIdioma[idioma.slice(0,2)]||"com";
  }
  var activas=(document.body.getAttribute("data-tiendas")||"es,com").split(",");
  var clave=elegir(); if(activas.indexOf(clave)<0) clave=activas.indexOf("com")>=0&&clave!=="es"?"com":"es";
  function url(k,asin){return "https://www."+tiendas[k][0]+"/dp/"+asin;}
  document.querySelectorAll("[data-asin]").forEach(function(caja){
    var asin=caja.getAttribute("data-asin"), boton=caja.querySelector(".comprar"), paises=caja.querySelector(".paises");
    if(boton){boton.href=url(clave,asin); boton.textContent="Comprar en Amazon"+tiendas[clave][0].slice(6); boton.setAttribute("title","Tienda de Amazon de "+tiendas[clave][1]);}
    if(paises){var html=[];activas.forEach(function(k){if(k!==clave&&tiendas[k])html.push('<li><a href="'+url(k,asin)+'" rel="noopener">'+tiendas[k][1]+'</a></li>');});
      if(html.length){paises.querySelector("ul").innerHTML=html.join("");paises.hidden=false;
        if(location.hash==="#paises"){paises.open=true;var ajustar=function(){var fin=paises.getBoundingClientRect().bottom+window.pageYOffset;window.scrollTo(0,Math.max(0,fin-window.innerHeight+40));};ajustar();window.addEventListener("load",function(){setTimeout(ajustar,0);});}}}
  });
  if("IntersectionObserver" in window && !window.matchMedia("(prefers-reduced-motion: reduce)").matches){
    var obs=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add("visible");obs.unobserve(e.target);}});},{threshold:.12});
    document.querySelectorAll(".aparece").forEach(function(el){obs.observe(el);});
  } else { document.querySelectorAll(".aparece").forEach(function(el){el.classList.add("visible");}); }
})();
/* Boletín: envío a Kit sin salir de la página (sin JavaScript, el formulario va a Kit directamente). */
(function(){
  document.querySelectorAll("form.boletin").forEach(function(f){
    f.addEventListener("submit",function(ev){
      if(!window.fetch||!window.FormData) return;
      ev.preventDefault();
      var r=f.querySelector(".respuesta"), b=f.querySelector("button");
      b.disabled=true;
      fetch(f.action,{method:"POST",body:new FormData(f),headers:{Accept:"application/json"}})
        .then(function(res){return res.json().catch(function(){return {};}).then(function(d){return {ok:res.ok,d:d};});})
        .then(function(x){
          if(x.ok&&(!x.d.status||x.d.status==="success")){r.textContent="Gracias. Te hemos enviado un correo: confirma tu suscripción desde él.";f.querySelector(".fila").hidden=true;}
          else{r.textContent="No se ha podido completar la suscripción. Revisa la dirección e inténtalo de nuevo.";b.disabled=false;}
          r.hidden=false;
        })
        .catch(function(){r.textContent="No se ha podido conectar. Inténtalo de nuevo en unos minutos.";r.hidden=false;b.disabled=false;});
    });
  });
})();
/* Cabecera fija (solo ordenador): se oculta al bajar y reaparece en cuanto se sube un poco. */
(function(){
  var cab=document.querySelector(".cabecera"); if(!cab) return;
  var ultima=window.pageYOffset, pendiente=false;
  function revisar(){
    var y=window.pageYOffset;
    if(y<120||y<ultima-6) cab.classList.remove("oculta");
    else if(y>ultima+6) cab.classList.add("oculta");
    if(Math.abs(y-ultima)>6) ultima=y;
    pendiente=false;
  }
  window.addEventListener("scroll",function(){if(!pendiente){pendiente=true;window.requestAnimationFrame(revisar);}},{passive:true});
  cab.addEventListener("focusin",function(){cab.classList.remove("oculta");});
})();
