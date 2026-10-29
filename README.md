# Agentes en la red Stellar

Presentación estática de 18 diapositivas, 30 minutos. Fuentes en `dist/`; no requiere build.

- Presentación: http://100.111.32.67:4318/
- Notas: http://100.111.32.67:4318/?notes

Abre ambas en el mismo navegador y origen. P abre las notas; flechas navegan; espacio inicia/pausa; A activa avance automático; T reinicia; F pantalla completa. El avance automático requiere iniciar el reloj. Los controles de las notas operan la presentación mediante BroadcastChannel. No sincroniza entre dispositivos. Usa una sola pestaña principal.

Se conserva el libreto completo y se muestran notas originales por sección. `dist/revision.md` documenta las correcciones y fuentes. Los recursos gráficos son locales; Google Fonts es opcional, con fuentes alternativas.

Servicio persistente de usuario: `systemctl --user status stellar-pitch.service`. Reiniciar: `systemctl --user restart stellar-pitch.service`. Escucha en 0.0.0.0:4318 para LAN/Tailscale; no usa Funnel.

Verificación: HTTP 200 mediante IP Tailscale desde el servidor; Chromium verificó las 18 diapositivas, controles sincronizados, reloj, reinicio y ausencia de desbordamiento horizontal en escritorio y móvil. El acceso desde otro equipo depende de las ACL de la tailnet.
# presentacion-stellar-ia-blockchain
