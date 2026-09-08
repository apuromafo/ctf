# REmux The Tmux

| **Dificultad** | Info |
| **Tipo** | Walkthrough |
| **Slug** | `tmuxremux` |
| **Link** | [TryHackMe](https://tryhackme.com/room/tmuxremux) |
| **Sección** | 00 Level Info |
| **Fuente** | TryHackMe |
| **Componentes** | tmux / terminal multiplexer / shell |
| **Impacto** | Guia completa de uso de tmux: sesiones, paneles, ventanas, copy mode y personalizacion |

---

**Contexto:** Guia actualizada de como usar tmux, el multiplexor de terminal mas utilizado en Linux. Cubre desde la creacion de sesiones y el manejo del prefijo por defecto, hasta la administracion de paneles, ventanas, modo de copia y configuracion avanzada con oh-my-tmux.

## Solucionario

### Task 1: Tmux practice machine

**Explicación:** La sala despliega una máquina de prácticas. Para hacer los ejercicios basta con conectarse por SSH a la máquina y abrir una sesión de tmux; el resto de tareas se resuelven dentro de tmux, de modo que conviene tener una segunda terminal o un panel aparte para emitir los comandos de control sin perder la vista de la sesión que se está manejando.

```bash
ssh thm@<IP>
tmux
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Start the VM if you need it and ssh in. | No answer needed |

### Task 2: Starting tmux "Sessions" and default tmux "prefix"

**Explicación:** tmux gestiona **sesiones** (sesión), cada una con su propio estado. El prefijo por defecto es `ctrl b`: se pulsa y se suelta, y después se teclea el comando (no hace falta mantenerlo pulsado; por eso la primera respuesta es `nay`). Comandos esenciales para el control de sesiones:

```bash
tmux new -s thm          # nueva sesión llamada "thm"
tmux ls                  # listar sesiones
tmux a -t thm            # reattacher a la sesión "thm" (detach previo con ctrl b d)
tmux new -s kali -d      # crear sesión "kali" en segundo plano (-d)
tmux kill-session -t thm # matar forzosamente la sesión "thm"
tmux kill-session -t notes -a   # matar todas menos la actual ("notes")
```

Dentro de la sesión: `ctrl b shift $` renombra la sesión, `ctrl b d` la desprende (detach, la deja corriendo), `ctrl b s` permite cambiar de sesión sin desacoplarse y `ctrl b shift :` abre el prompt de comandos de tmux (donde escribes sobre la línea de comandos, con tabulación, comandos como `attach -c /opt` para que las nuevas ventanas arranquen en `/opt`). En sesiones anidadas (una tmux dentro de otra) hay que pulsar el prefijo dos veces: `ctrl b ctrl b`. tmux es sensible a mayúsculas (caps lock sí rompe los atajos), el prompt se puede salir de varias formas y existen varias vías de salida, así que las respuestas relevantes son `yea`/`yea`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Do the ctrl and b keys need to be held down the whole time with every commands to work? yea/nay | `nay` |
| 2 | How to start tmux with the session with the name "thm"? | `tmux new -s thm` |
| 3 | How to change the current tmux session name? | `ctrl b shift $` |
| 4 | How to quit a tmux session without closing the session? To attach back later. | `ctrl b d` |
| 5 | How to list all tmux sessions? | `tmux ls` |
| 6 | How to reattach to a detached tmux session with the session name of "thm" | `tmux a -t thm` |
| 7 | How to create a new tmux session from your current tmux session with the name kali? | `tmux new -s kali -d` |
| 8 | How to switch between two or more tmux sessions without detaching from the current tmux session? | `ctrl b s` |
| 9 | How do you force kill the tmux session named "thm" if it's not responsive from a new terminal window or tmux session? | `tmux kill-session -t thm` |
| 10 | Within a nested tmux session. A second tmux session within the first one. How to change the session name of the second/internal tmux session? | `ctrl b ctrl b shift $` |
| 11 | How to get into a tmux prompt to run/type tmux commands? | `ctrl b shift :` |
| 12 | Are there than one way to exit a tmux prompt? yea/nay | `yea` |
| 13 | Is tmux case sensitive. Will hitting the caps lock break tmux? yea/nay | `yea` |
| 14 | Within tmux prompt or command mode how would you change the tmux directory? Where a new window or pane will start from the changed directory of /opt. | `attach -c /opt` |
| 15 | How to kill all tmux sessions except the one currently in use? With the name "notes". | `tmux kill-session -t notes -a` |

### Task 3: Manage tmux "Panes"

**Explicación:** Los **paneles** dividen la ventana en áreas. Se crean con `ctrl b shift "` (división horizontal) y `ctrl b shift %` (vertical). Para cerrarlos: `exit` (como una sesión ssh) o `ctrl b x` y confirmar con `y` si el panel se ha congelado. Para moverse, se puede usar `ctrl b q` (ver el número de cada panel) y luego las flechas (`yea`, se pueden usar), y atajos como `ctrl b ;` para saltar entre los dos últimos paneles más usados. La disposición se cambia con `ctrl b esc` + número de layout (del 1 en adelante), o de una en una con `ctrl b spacebar`. Reordenar paneles: `ctrl b shift {` mueve el panel actual en sentido horario y `ctrl b shift }` en sentido antihorario. Intercambiar posiciones se hace desde el prompt de tmux con `swap-pane`:

```bash
# dentro del prompt de tmux (ctrl b shift :)
swap-pane -s 3 -t 1   # mover el panel 3 a la posición 1 (y viajar con él)
swap-pane -t 4 -s 1   # intercambiar 1 <-> 4 sin cambiar tu posición actual
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | How to create a new pane split horizontally? | `ctrl b shift "` |
| 2 | How to close a tmux pane like closing a ssh session? | `exit` |
| 3 | How to create a new pane split vertically? | `ctrl b shift %` |
| 4 | How to cycle between tmux pre built layout options? Starting with the number 1. | `ctrl b esc 1` |
| 5 | How to cycle/toggle between tmux layouts, one at a time? | `ctrl b spacebar` |
| 6 | How to force quit a frozen, crashed or borked pane? | `ctrl b x y` |
| 7 | How to move between the two most used tmux panes for the current tmux window? | `ctrl b ;` |
| 8 | Can you use the arrow to move to the desired pane? yea/nay | `yea` |
| 9 | How to move the currently selected pane clockwise? | `ctrl b shift {` |
| 10 | How to move the currently selected pane counter-clockwise? | `ctrl b shift }` |
| 11 | Before using swap-pane. How to check for which pane has what number? | `ctrl b q` |
| 12 | How to swap two panes and move with the swapped pane? Within tmux prompt mode. 1 -> 3 location | `swap-pane -s 3 -t 1` |
| 13 | How to swap two panes without changing the currently selected pane location? Within tmux prompt mode. 1 -> 4 pane number | `swap-pane -t 4 -s 1` |

### Task 4: Manage tmux "Windows"

**Explicación:** Las **ventanas** son pestañas dentro de la sesión. `ctrl b c` crea una ventana nueva; `ctrl b ,` la renombra. `ctrl b shift !` lleva el panel seleccionado a su propia ventana. Desde el prompt de tmux, `join-pane` fusiona ventanas/paneles: `join-pane -s bash` trae el contenido de la ventana "bash", `join-pane -t sudo` lo envía hacia la ventana "sudo"; con `-v` la fusión es vertical y con `-h` horizontal (y se puede usar el número de ventana en vez del nombre, `yea`). `ctrl b shift &` mata la ventana entera (avisando con confirmación), `ctrl b w` escoge entre ventanas sin desacoplarte y `ctrl b p` / `ctrl b n` saltan a la ventana anterior/siguiente.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | How to create a new empty tmux window? | `ctrl b c` |
| 2 | How to change the currently select window's name? | `ctrl b ,` |
| 3 | How to move the currently selected pane to it's own tmux window? | `ctrl b shift !` |
| 4 | How to fuse two panes together with the "source" window of "bash"? After entering a tmux prompt? | `join-pane -s bash` |
| 5 | How to fuse two panes together with the "destination" window of "sudo"? After entering a tmux prompt? | `join-pane -t sudo` |
| 6 | What option can added with question 4 and 5 to fuse together vertically? | `-v` |
| 7 | What option can added with question 4 and 5 to fuse together horizontally? | `-h` |
| 8 | With join-pane can you use the window number instead of the window's name? yea/nay | `yea` |
| 9 | How to kill or completely close a window. Including all the panes open on that window. If it's unresponsive? | `ctrl b shift &` |
| 10 | How to view and cycle between all the tmux windows for the current tmux session without detaching from the current session? | `ctrl b w` |
| 11 | How to move back to the previous tmux window? | `ctrl b p` |
| 12 | How to move up to the next tmux window? | `ctrl b n` |

### Task 5: Tmux "copy" mode

**Explicación:** El modo de copia permite navegar y seleccionar texto del historial de la pantalla como si fuera un paginador. Se entra con `ctrl b [`. Dentro: `ctrl r` busca hacia atrás, `ctrl s` hacia delante, `esc` sale de la búsqueda, `q` sale del modo de copia, `ctrl spacebar` inicia la selección y `alt w` copia la selección. Para pegar: `ctrl b ]`. `ctrl b shift #` alterna el pane marcado (marked pane), útil para operaciones que implican dos paneles.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | How to enter copy mode in tmux? | `ctrl b [` |
| 2 | How to search backwards in copy mode? | `ctrl r` |
| 3 | How to search forwards in copy mode? | `ctrl s` |
| 4 | How to exit search in copy mode? | `esc` |
| 5 | How to quit copy mode? | `q` |
| 6 | How to start selection in copy mode? | `ctrl spacebar` |
| 7 | How to copy the selection in copy mode? | `alt w` |
| 8 | How to paste in tmux? | `ctrl b ]` |
| 9 | How to toggle the marked pane? | `ctrl b shift #` |

### Task 6: Oh My Tmux and beyond

**Explicación:** Más allá del uso básico, tmux se puede configurar y ampliar. No viene preinstalado en Kali (`nay`); la documentación está en `/usr/share/doc/tmux`; tmux es un comando POSIX (`yea`) y `home` te lleva al inicio de la línea. Para configurarlo: `source-file ~/.tmux.conf` recarga la configuración, `tmux kill-server` mata todo el servidor tmux, `bind` asigna teclas, `set -g prefix C-a` cambia el prefijo a `ctrl a`, los plugins se cargan con `set -g @plugin` (sí es posible escribir plugins: `yea`) y `run-shell` ejecuta un comando de shell desde la configuración.

```bash
tmux kill-server
source-file ~/.tmux.conf
set -g prefix C-a
set -g @plugin 'tmux-plugins/tpm'
run-shell 'cmd'
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Does the oh-my-tmux plugin come pre-installed on Kali Linux? (yea/nay) | `nay` |
| 2 | What is the location of the tmux documentation folder? | `/usr/share/doc/tmux` |
| 3 | Is tmux a POSIX command? (yea/nay) | `yea` |
| 4 | What key can you press to go to the start of the line in a tmux session? | `home` |
| 5 | How to reload the tmux configuration? | `source-file ~/.tmux.conf` |
| 6 | How to kill the tmux server? | `tmux kill-server` |
| 7 | What is the command to bind a key in tmux? | `bind` |
| 8 | What is the command to change the tmux prefix to ctrl a? | `set -g prefix C-a` |
| 9 | Is it possible to create a tmux plugin? (yea/nay) | `yea` |
| 10 | What is the command to load a tmux plugin? | `set -g @plugin` |
| 11 | What is the tmux command to run a shell command from the tmux configuration? | `run-shell` |

### Task 7: Oreo's open-source .tmux.conf file

**Explicación:** La sala cierra mostrando un `.tmux.conf` de código abierto (el de Oreo) como referencia real de configuración: recoge en un solo archivo todas las ideas vistas (prefijo, bindings, layouts, plugins de oh-my-tmux). Oír/ver el archivo sirve como hoja de ruta práctica para personalizar tu propio entorno.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Read the above. | No answer needed |

---

**Metodologia:**

1. Comenzar una sesion de tmux con `tmux` y comprender el prefijo por defecto `ctrl b` para ejecutar comandos.
2. Crear, renombrar, listar, cambiar y eliminar sesiones con comandos de gestion de sesiones.
3. Dividir ventanas en paneles horizontal y verticalmente, y gestionar su disposicion con layouts integrados.
4. Mover, intercambiar y cerrar paneles, incluyendo el uso de `swap-pane` desde el prompt de tmux.
5. Administrar ventanas: crear, renombrar, cerrar, fusionar con `join-pane` y navegar entre ellas.
6. Usar el modo de copia para seleccionar, copiar y pegar texto del historial del terminal.
7. Explorar configuracion avanzada: cambiar prefijo, documentacion, recargar configuracion y plugins con oh-my-tmux.

**Learning chain:** Sesion tmux -> Prefijo ctrl b -> Paneles (split/swap/kill) -> Ventanas (create/rename/join) -> Copy mode (select/copy/paste) -> Configuracion avanzada (prefix change, plugins)

**MITRE ATT&CK:** N/A (herramienta de productividad, no ofensiva)

**Fuente:** [TryHackMe - REmux The Tmux](https://tryhackme.com/room/tmuxremux)