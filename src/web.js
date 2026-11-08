/* 7 Espigas: tienda de Amazon según el navegador (sin cookies ni IP) y aparición suave de bloques. */
(function(){
  var tiendas={es:{dominio:"amazon.es",nombre:"España"},com:{dominio:"amazon.com",nombre:"Estados Unidos"},mx:{dominio:"amazon.com.mx",nombre:"México"},uk:{dominio:"amazon.co.uk",nombre:"Reino Unido"},de:{dominio:"amazon.de",nombre:"Alemania"},fr:{dominio:"amazon.fr",nombre:"Francia"},it:{dominio:"amazon.it",nombre:"Italia"}};
  function elegir(){
    var idioma=(navigator.language||"es-ES").toLowerCase(), zona="";
    try{zona=Intl.DateTimeFormat().resolvedOptions().timeZone||"";}catch(e){}
    if(zona==="Europe/Madrid"||zona==="Atlantic/Canary"||zona==="Africa/Ceuta"||idioma==="es-es") return "es";
    if(zona==="America/Mexico_City"||idioma==="es-mx") return "mx";
    if(idioma.indexOf("es")===0) return zona.indexOf("America/")===0?"com":"es";
    if(idioma==="en-gb"||zona==="Europe/London") return "uk";
    if(idioma.indexOf("de")===0) return "de";
    if(idioma.indexOf("fr")===0) return "fr";
    if(idioma.indexOf("it")===0) return "it";
    return "com";
  }
  var activas=(document.body.getAttribute("data-tiendas")||"es,com").split(",");
  var clave=elegir(); if(activas.indexOf(clave)<0) clave=activas.indexOf("com")>=0&&clave!=="es"?"com":"es";
  document.querySelectorAll("[data-asin]").forEach(function(caja){
    var asin=caja.getAttribute("data-asin"), boton=caja.querySelector(".comprar"), otras=caja.querySelector(".otras");
    if(boton){boton.href="https://www."+tiendas[clave].dominio+"/dp/"+asin; boton.setAttribute("title","Comprar en Amazon ("+tiendas[clave].nombre+")");}
    if(otras){var html=[];activas.forEach(function(k){if(k!==clave&&tiendas[k])html.push('<a href="https://www.'+tiendas[k].dominio+'/dp/'+asin+'" rel="noopener">'+tiendas[k].nombre+'</a>');});
      otras.innerHTML=html.length?"También en Amazon "+html.join(" · "):"";}
  });
  if("IntersectionObserver" in window && !window.matchMedia("(prefers-reduced-motion: reduce)").matches){
    var obs=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add("visible");obs.unobserve(e.target);}});},{threshold:.12});
    document.querySelectorAll(".aparece").forEach(function(el){obs.observe(el);});
  } else { document.querySelectorAll(".aparece").forEach(function(el){el.classList.add("visible");}); }
})();
