# tmux

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `tmux` | [TryHackMe - tmux](https://tryhackme.com/room/tmux) | 01 Level Easy | THM | tmux, terminal multiplexer, atajos de teclado | Dominio de tmux para la gestión de sesiones de terminal |

---

**Contexto:** La sala enseña el uso de tmux, un multiplexor de terminal: sesiones, binds, paneles, copiado/pegado y búsqueda, con ejercicios prácticos para fijar los atajos.

> **ES:** Sala práctica de tmux: crear y adjuntar sesiones, gestionar paneles y ventanas, realizar scroll, copiar/pegar y buscar contenido en el buffer.
> **EN:** Hands-on tmux room: create and attach sessions, manage panes and windows, scroll back, copy/paste and search buffer content.

## Solucionario

### Task 1: Ejercicios de tmux / tmux exercises

**Explicación:** Respuestas a los ejercicios de la sala sobre tmux: comandos de sesión, atajos de panel y ventana, navegación, copiado/pegado y búsqueda.

1. 1. No answer needed
   2. tmux
   3. Control
   4. b
   5. d
   6. tmux ls
   7. 0
   8. tmux a -t 0
   9. c
   10. No answer needed
   11. No answer needed
   12. [
   13. g
   14. G
   15. q
   16. %
   17. "
   18. No answer needed
   19. No answer needed
   20. No answer needed
   21. x
   22. exit
   23. tmux new -s neat

### Tabla unificada de preguntas / Unified Q&A

| # | Respuesta / Answer |
|---|---|
| 1 | `No answer needed` / `tmux` / `Control` / `b` / `d` / `tmux ls` / `0` / `tmux a -t 0` |
| 2 | `c` / `No answer needed` / `No answer needed` |
| 3 | `[` / `g` / `G` / `q` |
| 4 | `%` / `"` / `No answer needed` |
| 5 | `No answer needed` / `No answer needed` |
| 6 | `x` / `exit` |
| 7 | `tmux new -s neat` |

---

**Metodología:** Se resolvieron los ejercicios practicando los atajos de tmux: inicio de sesiones (`tmux`, `tmux new -s neat`), detección de la tecla prefix (`Control` + `b`), detach (`d`), listado y adjuntado (`tmux ls`, `tmux a -t 0`), gestión de ventanas y paneles (`c`, `%`, `"`, `x`), copiado/pegado y scroll (`[`, `g`, `G`, `q`) y salida (`exit`).

### Cadena de ataque / Attack Chain

1. Iniciar una nueva sesión de tmux (`tmux`).
2. Familiarizarse con la tecla prefix (`Control` + `b`).
3. Crear y dividir paneles y ventanas (`%`, `"`, `c`).
4. Explorar el buffer de scroll y copia/pegado (`[`, `g`, `G`, `q`).
5. Cerrar paneles y salir de la sesión (`x`, `exit`).
6. Crear una sesión con nombre (`tmux new -s neat`).

**Learning chain:** tmux sessions → prefix key → panes & windows → scroll & copy → session management

**Lección:** *Conocer la tecla prefix y los binds básicos de tmux multiplica la productividad en el manejo de múltiples paneles y ventanas de terminal.*

**MITRE ATT&CK:** T1059.004 - Command and Scripting Interpreter: Unix Shell

**Fuente:** [TryHackMe - tmux](https://tryhackme.com/room/tmux)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.