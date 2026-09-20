# Command Injection

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough (web) | `commandinjection` | https://tryhackme.com/room/commandinjection | 01 Level Easy | TryHackMe | OS command injection / PHP / Python (Flask) / grep / payloads (`;`, `&&`, `$( )`) / sanitización | Comprender y explotar la inyección de comandos del sistema operativo para ejecutar comandos arbitrarios y leer la flag de la aplicación vulnerable. |

---

**Contexto:** Room de la ruta de pentesting web que explica qué es la inyección de comandos (OS command injection), cómo descubrirla (con el ejemplo de una aplicación que busca canciones con `grep` en PHP y otra en Python/Flask), cómo explotarla inyectando payloads (`whoami`, `ping`, `timeout`) y cómo remediarla mediante la sanitización de entradas. Termina con una práctica en la que se despliega una máquina vulnerable: se ejecutan comandos para descubrir el usuario de la aplicación (`www-data`) y leer la flag en `/home/tryhackme/flag.txt`.

> **ES:** Aprende qué es la inyección de comandos, cómo descubrirla y explotarla con payloads en aplicaciones PHP/Python, y cómo remediarla (sanitización) antes de resolver la práctica donde se extrae la flag.
> **EN:** Learn what command injection is, how to discover and exploit it with payloads in PHP/Python applications, and how to remediate it (sanitisation) before completing the practical where you extract the flag.

## Solucionario

### Task 1: Introducción: ¿Qué es la inyección de comandos? / Introduction (What is Command Injection?)

**Explicación:** Se introduce el concepto de inyección de comandos: cuando una aplicación pasa la entrada del usuario a una llamada del sistema operativo, un atacante puede inyectar comandos adicionales para que el servidor los ejecute. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Leer la introducción de la room. / Read the room's introduction. | `No answer needed` |

### Task 2: Descubriendo la inyección de comandos / Discovering Command Injection

**Explicación:** Se analizan dos snippets vulnerables: una aplicación PHP que guarda la entrada del usuario en `$title` y la pasa al comando `grep` (la entrada se obtiene con `$_GET`, es decir, método `GET`), y una aplicación Python/Flask donde las rutas ejecutan comandos directamente, por lo que el comando `id` se ejecuta visitando `/id`.

```php
$title = $_GET['title'];
$command = "grep $title /path/to/songtitle.txt";
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué variable guarda la entrada del usuario en el snippet PHP? / What variable stores the user's input in the PHP code snippet? | `$title` |
| 2 | ¿Qué método HTTP se usa para recuperar los datos enviados por el usuario? / What HTTP method is used to retrieve data submitted by a user? | `GET` |
| 3 | Si quisieras ejecutar el comando `id` en el snippet de Python, ¿qué ruta visitarías? / If you wanted to execute the `id` command in the Python code snippet, what route would you need to visit? | `/id` |

### Task 3: Explotando la inyección de comandos / Exploiting Command Injection

**Explicación:** Se practican payloads de inyección para interactuar con el sistema: `whoami` revela el usuario con el que corre la aplicación, `ping` comprueba conectividad (muy usado además en inyecciones ciegas basadas en tiempo) y `timeout` lanza un comando con un límite/retardo de tiempo, útil para verificar inyecciones ciegas.

```text
whoami
ping
timeout
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué payload usarías para determinar bajo qué usuario se ejecuta la aplicación? / What payload would you use to determine what user the application is running as? | `whoami` |
| 2 | ¿Qué payload usarías para hacer ping al host local? / What payload would you use to ping the local host? | `ping` |
| 3 | ¿Qué payload usarías para ejecutar un comando aplicando un retardo (timeout)? / What payload would you use to run a command with a timeout delay? | `timeout` |

### Task 4: Remediando la inyección de comandos / Remediating Command Injection

**Explicación:** La defensa principal es limpiar (sanear) la entrada suministrada por el usuario antes de pasarla a la shell, evitando que caracteres como `;`, `&&` o `$()` alteren el comando original.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el término para el proceso de "limpiar" la entrada que se le da a la aplicación? / What is the term for the process of "cleaning" user input that is provided to an application? | `sanitisation` |

### Task 5: Práctica: Inyección de comandos (Desplegar) / Practical: Command Injection (Deploy)

**Explicación:** Se despliega la máquina vulnerable. Tras probar payloads (por ejemplo `127.0.0.1; whoami`), se confirma que la aplicación se ejecuta como `www-data`. Después se abusa de la misma técnica para leer la flag: `127.0.0.1; cat /home/tryhackme/flag.txt`, obteniendo `THM{COMMAND_INJECTION_COMPLETE}`.

```text
127.0.0.1; whoami                       # -> www-data
127.0.0.1; cat /home/tryhackme/flag.txt # -> THM{COMMAND_INJECTION_COMPLETE}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Bajo qué usuario se ejecuta la aplicación? / What user is this application running as? | `www-data` |
| 2 | ¿Cuál es el contenido de la flag en /home/tryhackme/flag.txt? / What are the contents of the flag located in /home/tryhackme/flag.txt? | `THM{COMMAND_INJECTION_COMPLETE}` |

### Task 6: Conclusión / Conclusion

**Explicación:** Cierre de la room recalcando que la inyección de comandos se mitiga saneando las entradas y aplicando el principio de mínimo privilegio. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Leer la conclusión de la room. / Read the room's conclusion. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué variable guarda la entrada del usuario en el snippet PHP? / What variable stores the user's input in the PHP code snippet? | `$title` |
| 2 | ¿Qué método HTTP se usa para recuperar los datos enviados por el usuario? / What HTTP method is used to retrieve data submitted by a user? | `GET` |
| 3 | Si quisieras ejecutar el comando `id` en el snippet de Python, ¿qué ruta visitarías? / If you wanted to execute the `id` command in the Python code snippet, what route would you need to visit? | `/id` |
| 4 | ¿Qué payload usarías para determinar bajo qué usuario se ejecuta la aplicación? / What payload would you use to determine what user the application is running as? | `whoami` |
| 5 | ¿Qué payload usarías para hacer ping al host local? / What payload would you use to ping the local host? | `ping` |
| 6 | ¿Qué payload usarías para ejecutar un comando aplicando un retardo (timeout)? / What payload would you use to run a command with a timeout delay? | `timeout` |
| 7 | ¿Cuál es el término para el proceso de "limpiar" la entrada que se le da a la aplicación? / What is the term for the process of "cleaning" user input that is provided to an application? | `sanitisation` |
| 8 | ¿Bajo qué usuario se ejecuta la aplicación? / What user is this application running as? | `www-data` |
| 9 | ¿Cuál es el contenido de la flag en /home/tryhackme/flag.txt? / What are the contents of the flag located in /home/tryhackme/flag.txt? | `THM{COMMAND_INJECTION_COMPLETE}` |

---

**Metodología:** Se identifica dónde la aplicación pasa la entrada del usuario a una llamada del sistema (grep en PHP, rutas en Flask). Se prueban payloads de inyección (`whoami`, `ping`, `timeout`, `; cat ...`) para confirmar la ejecución de comandos y se explota para descubrir el usuario (`www-data`) y leer la flag. La mitigación se resume en sanitizar la entrada.

### Cadena de ataque / Attack Chain

```text
Localizar input que llega a la shell -> probar separadores (; && $()) -> whoami -> ping/timeout (inyección ciega) -> cat /home/tryhackme/flag.txt -> flag
```

**Learning chain:** Concepto de inyección de comandos -> descubrimiento (PHP/Flask) -> payloads de explotación -> sanitización -> práctica con máquina real.

**Lección:** *Si una aplicación construye comandos con entrada del usuario sin sanitizarla, cualquier separador de shell (`;`, `&&`, `$( )`) convierte esa entrada en ejecución remota de comandos.*

**MITRE ATT&CK:** T1059 - Command and Scripting Interpreter

**Fuente:** [TryHackMe - Command Injection](https://tryhackme.com/room/commandinjection)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.