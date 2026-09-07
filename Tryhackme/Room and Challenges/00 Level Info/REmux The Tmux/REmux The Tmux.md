# REmux The Tmux

| **Dificultad** | Info |
| **Tipo** | Walkthrough |
| **Slug** | `tmuxremux` |
| **Link** | [TryHackMe](https://tryhackme.com/room/tmuxremux) |
| **Seccion** | 00 Level Info |
| **Fuente** | TryHackMe |
| **Componentes** | tmux / terminal multiplexer / shell |
| **Impacto** | Guia completa de uso de tmux: sesiones, paneles, ventanas, copy mode y personalizacion |

---

**Contexto:** Guia actualizada de como usar tmux, el multiplexor de terminal mas utilizado en Linux. Cubre desde la creacion de sesiones y el manejo del prefijo por defecto, hasta la administracion de paneles, ventanas, modo de copia y configuracion avanzada con oh-my-tmux.

## Solucionario

### Task 1: Tmux practice machine

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Start the VM if you need it and ssh in. | No answer needed |

### Task 2: Starting tmux "Sessions" and default tmux "prefix"

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
