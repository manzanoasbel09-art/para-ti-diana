from flask import Flask, send_from_directory, abort
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ARCHIVOS_PERMITIDOS = {
    "portada.png",
    "portada2.png",
    "portada3.png",
    "portada4.png",
    "portada5.png",
    "portada6.png",
    "portada7.jpg",
    "portada8.png",
    "portada9.png",
    "portada10.png",
    "portada11.png",
    "cancion.mp3",
    "cancion2.mp3",
    "cancion3.mp3",
    "canción4.mp3",
    "cancion4.mp3",
    "canción5.mp3",
    "cancion5.mp3",
    "cancion6.mp3",
}


@app.route("/<path:filename>")
def archivos_raiz(filename):
    if filename in ARCHIVOS_PERMITIDOS:
        ruta_raiz = os.path.join(BASE_DIR, filename)
        if os.path.isfile(ruta_raiz):
            return send_from_directory(BASE_DIR, filename)

        ruta_static = os.path.join(BASE_DIR, "static", filename)
        if os.path.isfile(ruta_static):
            return send_from_directory(os.path.join(BASE_DIR, "static"), filename)

    abort(404)


@app.route("/")
def inicio():
    return """
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>PARA TI DIANA🌹</title>
<script>
  function abrirRegalo() {
    var pantalla = document.getElementById("pantalla-regalo");
    if (pantalla) {
      pantalla.style.display = "none";
      pantalla.style.visibility = "hidden";
      pantalla.style.opacity = "0";
      pantalla.style.pointerEvents = "none";
    }
    try {
      if (typeof window.iniciarAudioRegalo === "function") {
        window.iniciarAudioRegalo();
      }
    } catch (err) {}
  }
</script>
<style>
  * {
    box-sizing: border-box;
    scroll-behavior: smooth;
  }

  body {
    margin: 0;
    font-family: Georgia, "Times New Roman", serif;
    background: radial-gradient(circle at 50% 15%, #341527 0%, #160911 55%, #090408 100%);
    color: #f9eaf0;
    overflow-x: hidden;
    position: relative;
  }

  /* PANTALLA INICIAL DE REGALO */
  #pantalla-regalo {
    position: fixed;
    inset: 0;
    background: radial-gradient(circle at center, #2d1221 0%, #0d060b 85%);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    z-index: 99999;
    text-align: center;
    padding: 20px;
    cursor: pointer;
    touch-action: manipulation;
  }

  .caja-regalo {
    font-size: 74px;
    filter: drop-shadow(0 0 24px rgba(255, 130, 185, 0.55));
    animation: rebotarCaja 2.2s ease-in-out infinite;
    user-select: none;
    pointer-events: none;
  }

  @keyframes rebotarCaja {
    0%, 100% { transform: translateY(0) scale(1); }
    50% { transform: translateY(-10px) scale(1.06); }
  }

  .texto-regalo {
    margin-top: 16px;
    font-size: 13px;
    letter-spacing: 1.5px;
    color: #e6b4c8;
    font-family: Arial, sans-serif;
    user-select: none;
    pointer-events: none;
  }

  /* REPRODUCTOR FLOTANTE */
  .reproductor-card {
    --escala-marco: 1;
    position: fixed;
    left: 18px;
    bottom: 20px;
    width: calc(235px * var(--escala-marco));
    min-width: 175px;
    max-width: 360px;
    background: rgba(20, 11, 17, 0.95);
    border: 1px solid rgba(255, 185, 212, 0.28);
    border-radius: 18px;
    padding: 12px;
    box-shadow: 0 16px 38px rgba(0, 0, 0, 0.75);
    backdrop-filter: blur(10px);
    z-index: 60;
    text-align: left;
    font-family: Arial, sans-serif;
    touch-action: none;
    user-select: none;
    cursor: grab;
  }

  .reproductor-card:active {
    cursor: grabbing;
  }

  .cabecera-marco {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 6px;
    margin-bottom: 8px;
  }

  .barra-arrastre {
    flex: 1;
    height: 4px;
    background: rgba(255, 185, 212, 0.35);
    border-radius: 999px;
    margin-left: 24px;
  }

  .btn-esquina-min {
    width: 24px;
    height: 24px;
    border-radius: 8px;
    border: 1px solid rgba(255, 185, 212, 0.35);
    background: rgba(255, 158, 198, 0.16);
    color: #fff;
    font-size: 13px;
    line-height: 1;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    flex-shrink: 0;
    touch-action: manipulation;
  }

  .btn-esquina-min:hover {
    background: rgba(255, 158, 198, 0.32);
  }

  .reproductor-card img {
    width: 100%;
    aspect-ratio: 1 / 1;
    height: auto;
    object-fit: cover;
    border-radius: 12px;
    display: block;
    margin-bottom: 10px;
    pointer-events: none;
  }

  .cancion-titulo {
    font-size: calc(13px * var(--escala-marco));
    font-weight: bold;
    color: #fff;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  .barra-tiempo {
    width: 100%;
    height: 4px;
    background: rgba(255, 255, 255, 0.16);
    border-radius: 999px;
    margin: 9px 0 5px;
    overflow: hidden;
    cursor: pointer;
    touch-action: manipulation;
  }

  .barra-relleno {
    width: 0%;
    height: 100%;
    background: #ff9ec6;
  }

  .marcas-tiempo {
    display: flex;
    justify-content: space-between;
    font-size: calc(10px * var(--escala-marco));
    color: #b595a3;
  }

  .controles-audio {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 14px;
    margin-top: 8px;
  }

  .btn-icono {
    background: transparent;
    border: none;
    color: #f9eaf0;
    font-size: calc(14px * var(--escala-marco));
    cursor: pointer;
    padding: 4px 6px;
    touch-action: manipulation;
  }

  .btn-play-pausa {
    width: calc(34px * var(--escala-marco));
    height: calc(34px * var(--escala-marco));
    border-radius: 50%;
    border: 1px solid rgba(255, 158, 198, 0.45);
    background: rgba(255, 158, 198, 0.24);
    color: #fff;
    font-size: calc(13px * var(--escala-marco));
    cursor: pointer;
    touch-action: manipulation;
  }

  .tirador-esquina {
    position: absolute;
    right: 4px;
    bottom: 4px;
    width: 18px;
    height: 18px;
    border-radius: 6px;
    background: rgba(255, 158, 198, 0.22);
    border: 1px solid rgba(255, 185, 212, 0.4);
    color: #ffe3ef;
    font-size: 11px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: nwse-resize;
    touch-action: none;
  }

  .reproductor-card.minimizado {
    width: auto;
    min-width: 165px;
    max-width: 260px;
    padding: 8px 10px;
    border-radius: 16px;
  }

  .reproductor-card.minimizado .cabecera-marco {
    margin-bottom: 6px;
  }

  .reproductor-card.minimizado #portadaActual,
  .reproductor-card.minimizado .barra-tiempo,
  .reproductor-card.minimizado .marcas-tiempo,
  .reproductor-card.minimizado .tirador-esquina {
    display: none;
  }

  .reproductor-card.minimizado .controles-audio {
    margin-top: 6px;
    gap: 8px;
  }

  /* CONTENIDO PRINCIPAL */
  .contenedor-principal {
    max-width: 980px;
    margin: 0 auto;
    padding: 40px 24px 120px 270px;
    text-align: center;
    position: relative;
    z-index: 2;
  }

  @media (max-width: 720px) {
    .contenedor-principal {
      padding: 35px 18px 260px 18px;
    }
    .reproductor-card {
      left: 14px;
      bottom: 14px;
      width: calc(205px * var(--escala-marco));
      min-width: 165px;
    }
  }

  .etiqueta-cursiva {
    font-style: italic;
    font-size: 17px;
    color: #e4a5be;
    margin-bottom: 10px;
  }

  .hero {
    min-height: auto;
    padding-bottom: 20px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }

  h1 {
    font-size: clamp(36px, 6vw, 60px);
    font-weight: 500;
    line-height: 1.15;
    margin: 0 0 14px;
    color: #fff3f7;
  }

  .subtexto {
    max-width: 470px;
    font-size: 14px;
    line-height: 1.65;
    color: #d6b6c4;
    margin: 0 auto 24px;
  }

  .flor-hero {
    font-size: 56px;
    color: #ff9ec6;
    filter: drop-shadow(0 0 22px rgba(255, 130, 185, 0.85));
    animation: flotarFlor 3.2s ease-in-out infinite;
    margin: 10px 0 20px;
  }

  @keyframes flotarFlor {
    0%, 100% { transform: translateY(0) rotate(0deg); }
    50% { transform: translateY(-9px) rotate(12deg); }
  }

  .scroll-guia {
    font-size: 11px;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: rgba(249, 234, 240, 0.55);
  }

  .seccion {
    margin-top: 45px;
  }

  h2 {
    font-size: clamp(28px, 4.5vw, 42px);
    font-weight: 500;
    margin: 6px 0 24px;
    color: #fff2f6;
  }

  /* CARTA */
  .tarjeta-carta {
    background: rgba(28, 13, 22, 0.78);
    border: 1px solid rgba(255, 175, 208, 0.16);
    border-radius: 22px;
    padding: 36px 28px;
    text-align: left;
    box-shadow: 0 20px 50px rgba(0, 0, 0, 0.45);
  }

  .tarjeta-carta h3 {
    text-align: center;
    font-size: clamp(24px, 4vw, 34px);
    font-weight: 500;
    margin: 0 0 24px;
    line-height: 1.25;
  }

  .tarjeta-carta p {
    font-size: 14px;
    line-height: 1.8;
    color: #e6ccd7;
    margin-bottom: 16px;
  }

  .firma {
    text-align: center;
    font-style: italic;
    color: #f3b5ce;
    margin-top: 24px;
    font-size: 16px;
  }

  /* GRID DE RAZONES */
  .grid-razones {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
    gap: 16px;
    margin-top: 24px;
  }

  .card-razon {
    background: rgba(28, 13, 22, 0.72);
    border: 1px solid rgba(255, 175, 208, 0.14);
    border-radius: 16px;
    padding: 20px;
  }

  .card-razon .icono {
    font-size: 24px;
    margin-bottom: 8px;
  }

  .card-razon h4 {
    margin: 0 0 8px;
    font-size: 16px;
    color: #ffd6e7;
  }

  .card-razon p {
    margin: 0;
    font-size: 12.5px;
    line-height: 1.6;
    color: #cfb0bd;
  }

  /* JARDÍN INTERACTIVO */
  .flores-fila {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 18px;
    margin: 24px 0 18px;
  }

  .flor-boton {
    background: rgba(255, 158, 198, 0.1);
    border: 1px solid rgba(255, 158, 198, 0.25);
    border-radius: 14px;
    padding: 12px 14px;
    font-size: 28px;
    cursor: pointer;
    transition: transform 0.2s ease, background 0.2s ease;
  }

  .flor-boton:hover {
    transform: translateY(-4px) scale(1.08);
    background: rgba(255, 158, 198, 0.22);
  }

  .mensaje-flor {
    min-height: 44px;
    font-style: italic;
    color: #f6bdd4;
    font-size: 15px;
    padding: 10px 16px;
  }

  /* GALERÍA DE FOTOS */
  .grid-fotos {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 26px;
    margin-top: 28px;
  }

  @media (max-width: 640px) {
    .grid-fotos {
      grid-template-columns: 1fr;
    }
  }

  .marco-foto {
    background: rgba(26, 12, 20, 0.84);
    border: 1.5px solid rgba(255, 175, 208, 0.26);
    border-radius: 22px;
    padding: 18px;
    box-shadow: 0 18px 40px rgba(0, 0, 0, 0.5);
    transition: transform 0.25s ease, border-color 0.25s ease;
  }

  .marco-foto:hover {
    transform: translateY(-5px);
    border-color: rgba(255, 158, 198, 0.5);
  }

  .marco-foto img {
    width: 100%;
    height: 340px;
    object-fit: cover;
    border-radius: 16px;
    filter: grayscale(25%) contrast(1.06);
    display: block;
  }

  @media (max-width: 640px) {
    .marco-foto {
      padding: 15px;
    }
    .marco-foto img {
      height: 270px;
    }
  }

  .pie-foto {
    margin-top: 14px;
    font-style: italic;
    font-size: 16px;
    color: #ecc2d4;
  }

  .dedicatoria-final {
    margin-top: 10px;
    font-style: italic;
    font-size: 16px;
    color: #f3b5ce;
    line-height: 1.7;
  }

  /* PÉTALOS */
  .petalo {
    position: fixed;
    top: -24px;
    color: #ff9ec6;
    pointer-events: none;
    z-index: 1;
    animation: caer linear forwards;
  }

  @keyframes caer {
    0% {
      transform: translateY(-20px) translateX(0) rotate(0deg);
      opacity: 0.9;
    }
    100% {
      transform: translateY(105vh) translateX(30px) rotate(360deg);
      opacity: 0;
    }
  }
</style>
</head>
<body>

  <!-- PANTALLA INICIAL DE REGALO -->
  <div id="pantalla-regalo" onclick="abrirRegalo()">
    <div class="caja-regalo">🎁</div>
    <div class="texto-regalo">HECHO CON MUCHO CARIÑO PARA TI🌹</div>
  </div>

  <!-- REPRODUCTOR FLOTANTE -->
  <aside class="reproductor-card" id="reproductorMovil">
    <div class="cabecera-marco">
      <div class="barra-arrastre" title="Arrastra para mover"></div>
      <button type="button" class="btn-esquina-min" id="btnMinimizar" title="Minimizar / Expandir">−</button>
    </div>

    <img id="portadaActual" src="/portada5.png" alt="Portada de la canción" onerror="this.style.display='none'">
    <div class="cancion-titulo" id="tituloCancion">Con mucho amor para ti</div>

    <audio id="audioPrincipal" preload="auto" playsinline webkit-playsinline></audio>

    <div class="barra-tiempo" onclick="buscarTiempo(event)">
      <div class="barra-relleno" id="barraRelleno"></div>
    </div>
    <div class="marcas-tiempo">
      <span id="actualSeg">0:00</span>
      <span id="totalSeg">0:00</span>
    </div>

    <div class="controles-audio">
      <button type="button" class="btn-icono" id="btnAnterior" title="Anterior">⏮</button>
      <button type="button" class="btn-play-pausa" id="botonPlay" title="Reproducir / Pausar">▶</button>
      <button type="button" class="btn-icono" id="btnSiguiente" title="Siguiente">⏭</button>
    </div>

    <div class="tirador-esquina" id="tiradorEsquina" title="Arrastra para ajustar tamaño">⤡</div>
  </aside>

  <!-- CONTENIDO PRINCIPAL -->
  <main class="contenedor-principal">

    <!-- PORTADA -->
    <section class="hero">
      <div class="etiqueta-cursiva">Con mucho amor</div>
      <h1>PARA TI DIANA🌹</h1>
      <p class="subtexto">Cada pétalo guarda un susurro de lo mucho que significas para mí</p>
      <div class="flor-hero">❀</div>
      <div class="scroll-guia">desliza para descubrir<br>↓</div>
    </section>

    <!-- CARTA -->
    <section class="seccion">
      <div class="etiqueta-cursiva">desde mi corazón</div>
      <div class="tarjeta-carta">
        <h3>Eres mi<br>sueño más bonito<br>hecho realidad.</h3>
        <p>
          En un mundo lleno de momentos comunes, tú eres lo extraordinario. La forma en que ríes,
          cómo cuidas y cómo simplemente existes llena cada rincón de mi mundo con algo que
          nunca supe que necesitaba.
        </p>
        <p>
          Estas flores no son suficientes, y ninguna palabra lo sería. Pero llevan cada sentimiento
          que guardo por ti, como pequeñas cartas de amor esperando ser descubiertas entre sus pétalos.
        </p>
        <div class="firma">— Siempre tuyo 🌹</div>
      </div>
    </section>

    <!-- RAZONES -->
    <section class="seccion">
      <div class="etiqueta-cursiva">mil razones más</div>
      <h2>Por qué te amo</h2>
      <div class="grid-razones">
        <div class="card-razon">
          <div class="icono">🌹</div>
          <h4>Tu sonrisa</h4>
          <p>Ilumina hasta los días más pesados y hace que todo parezca posible.</p>
        </div>
        <div class="card-razon">
          <div class="icono">✨</div>
          <h4>Tu alma</h4>
          <p>Única, sincera y más hermosa que cualquier flor que haya existido.</p>
        </div>
        <div class="card-razon">
          <div class="icono">🌸</div>
          <h4>Tu ternura</h4>
          <p>La forma en que quieres al mundo me inspira a ser mejor cada día.</p>
        </div>
        <div class="card-razon">
          <div class="icono">🌷</div>
          <h4>Tu risa</h4>
          <p>Mi sonido favorito en todo el universo.</p>
        </div>
        <div class="card-razon">
          <div class="icono">🌺</div>
          <h4>Tu fuerza</h4>
          <p>Llevas todo con tanta gracia que te admiro sin medida.</p>
        </div>
        <div class="card-razon">
          <div class="icono">💖</div>
          <h4>Simplemente tú</h4>
          <p>Cada momento a tu lado es un recuerdo que atesoro para siempre.</p>
        </div>
      </div>
    </section>

    <!-- JARDÍN INTERACTIVO -->
    <section class="seccion">
      <div class="etiqueta-cursiva">nuestro jardín secreto</div>
      <h2>Un jardín creado<br>solo para ti</h2>
      <div class="flores-fila">
        <button class="flor-boton" onclick="mostrarFlor('Una rosa roja por cada latido que me haces sentir.')">🌹</button>
        <button class="flor-boton" onclick="mostrarFlor('Una flor de cerezo por la paz que me das.')">🌸</button>
        <button class="flor-boton" onclick="mostrarFlor('Un loto por lo único y especial que eres.')">🪷</button>
        <button class="flor-boton" onclick="mostrarFlor('Una flor suave por cada sonrisa compartida.')">🌼</button>
        <button class="flor-boton" onclick="mostrarFlor('Un tulipán por todo lo que sueño contigo.')">🌷</button>
        <button class="flor-boton" onclick="mostrarFlor('Un girasol porque iluminas mis días.')">🌻</button>
      </div>
      <div class="mensaje-flor" id="mensajeFlor">Toca cada flor para descubrir su significado</div>
    </section>

    <!-- FOTOS -->
    <section class="seccion">
      <div class="etiqueta-cursiva">Te quiero mucho</div>
      <h2>Ten tus florecitas que no te pude dar este año :3</h2>
      <div class="grid-fotos">
        <div class="marco-foto">
          <img src="/portada7.jpg" alt="Foto 1" onerror="this.style.background='#281320'">
          <div class="pie-foto">Feliz día de las flores amarillas 21 de septiembre</div>
        </div>
        <div class="marco-foto">
          <img src="/portada8.png" alt="Foto 2" onerror="this.style.background='#281320'">
          <div class="pie-foto">Feliz día de las flores moradas 9 de octubre</div>
        </div>
        <div class="marco-foto">
          <img src="/portada9.png" alt="Foto 3" onerror="this.style.background='#281320'">
          <div class="pie-foto">Feliz día de las flores rojas 14 de febrero</div>
        </div>
        <div class="marco-foto">
          <img src="/portada10.png" alt="Foto 4" onerror="this.style.background='#281320'">
          <div class="pie-foto">Feliz día de los tulipanes 13 de diciembre</div>
        </div>
        <div class="marco-foto">
          <img src="/portada11.png" alt="Foto 5" onerror="this.style.background='#281320'">
          <div class="pie-foto">Feliz día de las flores rosadas 31 de octubre</div>
        </div>
      </div>
    </section>

    <!-- CIERRE -->
    <section class="seccion">
      <div class="etiqueta-cursiva">hoy y siempre</div>
      <h2>Te amo más allá<br>de las palabras</h2>
      <p class="subtexto">
        Sin importar a dónde nos lleve la vida, sabe que en algún lugar del universo hay un jardín
        floreciendo con cada sentimiento que guardo por ti. Te mereces el mundo entero, todas las
        flores y todo lo bonito.
      </p>
      <div style="font-size: 28px; margin-top: 14px;">💖</div>
      <div class="etiqueta-cursiva" style="margin-top: 22px;">Hecho con cariño, solo para ti 🌸</div>
      <div class="dedicatoria-final">De: Pibble</div>
      <div class="dedicatoria-final">Para:Diana</div>
    </section>

  </main>

<script>
  const playlist = [
    {
      titulo: "Con mucho amor para ti",
      audio: "/canción5.mp3",
      portada: "/portada5.png"
    },
    {
      titulo: "Hecha Pa' Mí",
      audio: "/cancion.mp3",
      portada: "/portada.png"
    },
    {
      titulo: "Kid Krow",
      audio: "/cancion2.mp3",
      portada: "/portada2.png"
    },
    {
      titulo: "Am I Sinking or Am I Swimming?",
      audio: "/cancion3.mp3",
      portada: "/portada3.png"
    },
    {
      titulo: "Wannabewithu",
      audio: "/canción4.mp3",
      portada: "/portada4.png"
    },
    {
      titulo: "Amor de siempre",
      audio: "/cancion6.mp3",
      portada: "/portada6.png"
    }
  ];

  let indiceActual = 0;

  const audio = document.getElementById("audioPrincipal");
  const botonPlay = document.getElementById("botonPlay");
  const btnAnterior = document.getElementById("btnAnterior");
  const btnSiguiente = document.getElementById("btnSiguiente");
  const barraRelleno = document.getElementById("barraRelleno");
  const actualSeg = document.getElementById("actualSeg");
  const totalSeg = document.getElementById("totalSeg");
  const portadaImg = document.getElementById("portadaActual");
  const tituloCancion = document.getElementById("tituloCancion");
  const reproductor = document.getElementById("reproductorMovil");
  const btnMinimizar = document.getElementById("btnMinimizar");
  const tiradorEsquina = document.getElementById("tiradorEsquina");

  function formatearTiempo(seg) {
    if (!isFinite(seg) || seg < 0) return "0:00";
    const minutos = Math.floor(seg / 60);
    const segundos = Math.floor(seg % 60);
    return minutos + ":" + (segundos < 10 ? "0" : "") + segundos;
  }

  function cargarCancion(indice, reproducir) {
    if (indice < 0) indice = playlist.length - 1;
    if (indice >= playlist.length) indice = 0;
    indiceActual = indice;

    const tema = playlist[indiceActual];
    tituloCancion.textContent = tema.titulo;
    portadaImg.style.display = "block";
    portadaImg.src = tema.portada;
    audio.src = tema.audio;
    barraRelleno.style.width = "0%";
    actualSeg.textContent = "0:00";
    totalSeg.textContent = "0:00";

    if (reproducir) {
      audio.play().catch(function () {});
    }
  }

  window.iniciarAudioRegalo = function () {
    if (!audio.src) {
      cargarCancion(0, true);
      return;
    }
    audio.play().catch(function () {});
  };

  function sincronizarBotonPlay() {
    botonPlay.textContent = audio.paused ? "▶" : "❚❚";
  }

  audio.addEventListener("play", sincronizarBotonPlay);
  audio.addEventListener("pause", sincronizarBotonPlay);

  botonPlay.addEventListener("click", function () {
    if (!audio.src) {
      cargarCancion(0, true);
      return;
    }
    if (audio.paused) {
      audio.play().catch(function () {});
    } else {
      audio.pause();
    }
  });

  btnAnterior.addEventListener("click", function () {
    cargarCancion(indiceActual - 1, !audio.paused);
  });

  btnSiguiente.addEventListener("click", function () {
    cargarCancion(indiceActual + 1, !audio.paused);
  });

  audio.addEventListener("loadedmetadata", function () {
    totalSeg.textContent = formatearTiempo(audio.duration);
  });

  audio.addEventListener("timeupdate", function () {
    actualSeg.textContent = formatearTiempo(audio.currentTime);
    if (audio.duration > 0) {
      barraRelleno.style.width = ((audio.currentTime / audio.duration) * 100) + "%";
    }
  });

  audio.addEventListener("ended", function () {
    cargarCancion(indiceActual + 1, true);
  });

  function buscarTiempo(evento) {
    if (!audio.duration) return;
    const rect = evento.currentTarget.getBoundingClientRect();
    const ratio = Math.min(Math.max((evento.clientX - rect.left) / rect.width, 0), 1);
    audio.currentTime = ratio * audio.duration;
  }

  if (btnMinimizar && reproductor) {
    btnMinimizar.addEventListener("click", function (e) {
      e.stopPropagation();
      reproductor.classList.toggle("minimizado");
      btnMinimizar.textContent = reproductor.classList.contains("minimizado") ? "+" : "−";
    });
  }

  let arrastrando = false;
  let offsetX = 0;
  let offsetY = 0;

  if (reproductor) {
    reproductor.addEventListener("pointerdown", function (e) {
      if (e.target.closest("button, .tirador-esquina, .barra-tiempo")) return;
      arrastrando = true;
      const rect = reproductor.getBoundingClientRect();
      offsetX = e.clientX - rect.left;
      offsetY = e.clientY - rect.top;
      reproductor.style.left = rect.left + "px";
      reproductor.style.top = rect.top + "px";
      reproductor.style.bottom = "auto";
      reproductor.style.right = "auto";
      reproductor.setPointerCapture(e.pointerId);
    });

    reproductor.addEventListener("pointermove", function (e) {
      if (!arrastrando) return;
      const maxX = Math.max(0, window.innerWidth - reproductor.offsetWidth);
      const maxY = Math.max(0, window.innerHeight - reproductor.offsetHeight);
      const nuevaX = Math.min(Math.max(0, e.clientX - offsetX), maxX);
      const nuevaY = Math.min(Math.max(0, e.clientY - offsetY), maxY);
      reproductor.style.left = nuevaX + "px";
      reproductor.style.top = nuevaY + "px";
    });

    reproductor.addEventListener("pointerup", function () {
      arrastrando = false;
    });
  }

  let escalando = false;
  let inicioX = 0;
  let escalaInicial = 1;

  if (tiradorEsquina && reproductor) {
    tiradorEsquina.addEventListener("pointerdown", function (e) {
      e.stopPropagation();
      escalando = true;
      inicioX = e.clientX;
      escalaInicial = parseFloat(getComputedStyle(reproductor).getPropertyValue("--escala-marco")) || 1;
      tiradorEsquina.setPointerCapture(e.pointerId);
    });

    tiradorEsquina.addEventListener("pointermove", function (e) {
      if (!escalando) return;
      const delta = (e.clientX - inicioX) / 160;
      const nuevaEscala = Math.min(Math.max(0.75, escalaInicial + delta), 1.45);
      reproductor.style.setProperty("--escala-marco", nuevaEscala.toFixed(2));
    });

    tiradorEsquina.addEventListener("pointerup", function () {
      escalando = false;
    });
  }

  function mostrarFlor(texto) {
    document.getElementById("mensajeFlor").textContent = texto;
  }

  setInterval(() => {
    const petalo = document.createElement("div");
    petalo.className = "petalo";
    petalo.textContent = Math.random() > 0.5 ? "🌸" : "❀";
    petalo.style.left = (Math.random() * 100) + "vw";
    petalo.style.fontSize = (14 + Math.random() * 14) + "px";
    const duracion = 5 + Math.random() * 5;
    petalo.style.animationDuration = duracion + "s";
    document.body.appendChild(petalo);

    setTimeout(() => {
      petalo.remove();
    }, duracion * 1000);
  }, 550);

  cargarCancion(0, false);
</script>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=True)
