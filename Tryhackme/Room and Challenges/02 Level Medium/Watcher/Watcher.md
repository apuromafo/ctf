# Watcher

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Medium | Reto / Challenge (Web) | watcher | https://tryhackme.com/room/watcher | 02 Level Medium | TryHackMe | Web exploitation, LFI, FTP, Privilege Escalation | Alta - máquina de práctica |

> **Objeto:** Explotar el sitio web vulnerable (robots.txt, FTP, LFI) y escalar privilegios para capturar las siete flags del reto.

---

**Contexto:** "Watcher" es una máquina de dificultad media enfocada en explotación web y escalada de privilegios. El camino pasa por descubrir `robots.txt`, abusar de credenciales FTP, realizar un Local File Inclusion, explotar scripts con crontab y finalmente obtener acceso al usuario watcher.

> **ES:** Reto web en cadena: descubrimiento, FTP, LFI y privesc con scripts.
> **EN:** Chained web challenge: discovery, FTP, LFI, and script-based privesc.

## Solucionario

### Task 1: Robots.txt / Robots.txt

**Explicación:** Revisar `robots.txt` del sitio para descubrir la primera ruta oculta y su flag.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Cuál es la flag de robots.txt? / What is the robots.txt flag? | FLAG{robots_dot_text_what_is_next} |

### Task 2: Servicio FTP / FTP service

**Explicación:** Conectar por FTP con las credenciales descubiertas y leer la segunda flag.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Cuál es la flag de FTP? / What is the FTP flag? | FLAG{ftp_you_and_me} |

### Task 3: LFI / Local File Inclusion

**Explicación:** Explotar la inclusión local de ficheros para leer recursos del servidor y obtener la siguiente flag.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Cuál es la flag del LFI? / What is the LFI flag? | FLAG{lfi_what_a_guy} |

### Task 4: Código oculto / Hidden code

**Explicación:** Localizar código oculto o directorios mediante fuerza bruta para superar el siguiente obstáculo.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Cuál es la flag del código oculto? / What is the hidden code flag? | FLAG{chad_lifestyle} |

### Task 5: Tarea programada / Scheduled task

**Explicación:** Abusar de la tarea cron del usuario watcher para ejecutar comandos (Living off the Land) y leer la flag.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Cuál es la flag de la tarea? / What is the scheduled task flag? | FLAG{live_by_the_cow_die_by_the_cow} |

### Task 6: Script vulnerable / Vulnerable script

**Explicación:** Explotar el script que se ejecuta con la shell para ejecutar código y obtener la flag del script.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Cuál es la flag del script? / What is the script flag? | FLAG{but_i_thought_my_script_was_secure} |

### Task 7: Usuario watcher / Watcher user

**Explicación:** Acceder como usuario watcher y leer la flag final que revela al "vigilante".

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Cuál es la flag final? / What is the final flag? | FLAG{who_watches_the_watchers} |

---

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | ¿Cuál es la flag de robots.txt? / What is the robots.txt flag? | `FLAG{robots_dot_text_what_is_next}` |
| 2 | ¿Cuál es la flag de FTP? / What is the FTP flag? | `FLAG{ftp_you_and_me}` |
| 3 | ¿Cuál es la flag del LFI? / What is the LFI flag? | `FLAG{lfi_what_a_guy}` |
| 4 | ¿Cuál es la flag del código oculto? / What is the hidden code flag? | `FLAG{chad_lifestyle}` |
| 5 | ¿Cuál es la flag de la tarea? / What is the scheduled task flag? | `FLAG{live_by_the_cow_die_by_the_cow}` |
| 6 | ¿Cuál es la flag del script? / What is the script flag? | `FLAG{but_i_thought_my_script_was_secure}` |
| 7 | ¿Cuál es la flag final? / What is the final flag? | `FLAG{who_watches_the_watchers}` |

---

**Metodología:**

1. Enumeración web y descubrimiento de `robots.txt`.
2. Acceso FTP con credenciales encontradas.
3. Explotación de Local File Inclusion (LFI).
4. Fuerza bruta de directorios y código oculto.
5. Abuso de cron/scripts para escalar y leer las flags.

### Cadena de ataque / Attack Chain

```text
robots.txt -> FTP -> LFI -> código oculto -> cron (cow) -> script -> watcher (flag final)
```

**Learning chain:**

- `robots.txt` es la puerta de entrada al primer paso del reto.
- El LFI conecta con credenciales FTP y código oculto.
- La escalada aprovecha tareas cron y scripts mal protegidos del usuario watcher.

**Lección:** *Cada flag marca un hito; el reto entero es una cadena de descubrimiento y abuso acumulativo.*

**MITRE ATT&CK:**
- T1190 - Exploit Public-Facing Application
- T1005 - Data from Local System
- T1053.003 - Scheduled Task/Job: Cron
- T1059 - Command and Scripting Interpreter

**Fuente:** [TryHackMe - Watcher](https://tryhackme.com/room/watcher)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.