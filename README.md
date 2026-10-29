# Stellar · Halloween paper theatre

Presentación comunitaria de 18 diapositivas / 30 minutos, servida en:

- http://100.111.32.67:4318/
- Notas: http://100.111.32.67:4318/?notes
- Capturas de revisión: http://100.111.32.67:4318/review/

## Operación

Abre presentación y notas desde cualquier dispositivo con acceso a la red local o Tailscale. Varios controles y pantallas pueden conectarse simultáneamente. Flechas: navegar; espacio: iniciar/pausar; A: avance automático; T: reiniciar; P: notas; F: pantalla completa. El servidor mantiene el estado compartido y el reloj; todos los dispositivos consultan ese estado cada 250 ms. Los comandos concurrentes se serializan. Las notas muestran una página de libreto por diapositiva y los controles quedan anclados arriba en móvil.

El servicio `stellar-pitch.service` ejecuta `server.py` en 0.0.0.0:4318. El estado se conserva mientras el proceso esté activo; reiniciar el servicio reinicia la charla. Estado: `systemctl --user status stellar-pitch.service`. No hay build ni CDN de runtime. Las tipografías, Three.js 0.186.1 y Anime.js 4.5.0 se sirven localmente, con licencias en sus carpetas.

## Implementación actual

Se sustituyeron completamente la composición, los componentes visuales y la transición anterior. Se conservan el contenido de `slides.js` y los controles del presentador.

- Creepster para encabezados Halloween y Nunito para cuerpo legible; IBM Plex Mono solo para código.
- Paleta Stellar: amarillo, negro, blanco, hueso, lavanda, teal y azul.
- Escenario abierto con bosque recortado, colinas de papel y luna creciente. No utiliza el túnel concéntrico del diseño anterior.
- Tres familias de composición: cartel de apertura, laboratorio/grimorio y secuencias horizontales. Lápidas, pergaminos, covens y libros reemplazan las tarjetas rectangulares.
- Muñeca cosida, familiares fantasma-robot con sombrero, calabazas, murciélagos, calderos y libros: geometrías curvas de cartulina extruida en Three.js. Anime.js articula alas, brazos, oscilaciones, burbujas y pagos.
- Transición nueva: dos mallas subdivididas de papel con bordes irregulares, deformación de vértices, pliegues y giro 3D, animadas por Anime.js. No clona canvases ni usa las antiguas mitades HTML.
- Lienzo fijo 1600×900, escalado uniformemente. Siempre 16:9 horizontal, con márgenes en pantallas de distinta proporción. Los controles quedan fuera del lienzo.
- Movimiento reducido muestra componentes estáticos y elimina las transiciones. Se pausa render al ocultar la pestaña; las notas no crean renderers.

## QA headless

Scripts en `scripts/` utilizan Chromium/Playwright instalado en este servidor (ruta explícita en cada script).

- `audit-deck.cjs qa/after --static`: recorre las 18 slides, captura cada una, comprueba ratio y errores; guarda `results.json`.
- `verify-motion.cjs`: verifica layouts, animación mediante diferencia de píxeles, navegación rápida, notas sincronizadas, cronómetro, autoavance, movimiento reducido y cuatro tamaños de viewport.
- `capture-transitions.cjs`: controla el reloj de Chromium, captura cada transición a 400 ms y comprueba que termine sin dejar capas.

Evidencias completas en `qa/`; selección consultable en `dist/review/`. El libreto original permanece intacto y `dist/revision.md` documenta los ajustes técnicos del contenido.
