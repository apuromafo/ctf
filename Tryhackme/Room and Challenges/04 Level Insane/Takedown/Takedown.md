# Takedown [INSANE]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** Insane
* **Tipo / Type:** CTF (Offensive)
* **Slug:** `takedown`
* **Link:** https://tryhackme.com/room/takedown
* **Sección / Section:** 03 Level Hard
* **Fuente / Source:** TryHackMe official room, GitHub (jesusgavancho/TryHackMe_and_HackTheBox), Medium writeup by Firat Demir, YouTube walkthrough by Jacob Taylor, Medium writeup by Hassan Mughal

## Solucionario de Tareas / Task Solutions

> **ES:** Takedown es un CTF de nivel Insane donde un servidor web corporativo ha sido comprometido por el grupo RISOTTO. La misión es encontrar su teamserver y tomarlo control. Involucra análisis estático de malware Nim, interpretación de C2 API, y explotación de un endpoint de ejecución remota para obtener root.
> **EN:** Takedown is an Insane CTF where a corporate webserver has been compromised by RISOTTO GROUP. The mission is to find their teamserver and take it down. Involves static analysis of Nim malware, C2 API interpretation, and exploitation of a remote execution endpoint to gain root.

### Task 1 - Mission Brief (OPERATION: OVERCOOKED RISOTTO)

> **ES:** Leer el documento de inteligencia adjunto (OPORDOVERCOOKEDRISOTTO.pdf). El brief contiene información crítica sobre el grupo RISOTTO, incluyendo su uso de keying ambiental, agentes Nim, y un User-Agent predefinido para autenticación.
> **EN:** Read the attached intelligence brief (OPORDOVERCOOKEDRISOTTO.pdf). The brief contains critical intelligence about RISOTTO GROUP, including their use of environmental keying, Nim agents, and a preset User-Agent for authentication.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Ready! | `Completed` |

### Task 2 - Start VM

> **ES:** Iniciar la máquina virtual y agregar la IP a `/etc/hosts` como `takedown.thm.local`. Ejecutar un escaneo Nmap básico para confirmar puertos 22 (SSH) y 80 (HTTP/nginx 1.23.1) abiertos.
> **EN:** Start the VM and add the IP to `/etc/hosts` as `takedown.thm.local`. Run a basic Nmap scan to confirm ports 22 (SSH) and 80 (HTTP/nginx 1.23.1) are open.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| VM Started | `Completed` |

### Task 3 - User.txt

> **ES:** Obtener la bandera user.txt. La cadena de explotación completa requiere: enumeración web con Gobuster, análisis estático de `favicon.ico` (PE64 compilado con Nim que contiene un agente C2), descubrimiento del User-Agent key (`z.5.x.2.l.8.y.5`), uso de la API del C2 para leer archivos del servidor, y obtención de reverse shell a través de `/api/server/exec`.
> **EN:** Obtain the user.txt flag. The full exploitation chain requires: web enumeration with Gobuster, static analysis of `favicon.ico` (PE64 compiled with Nim containing a C2 agent), discovery of the User-Agent key (`z.5.x.2.l.8.y.5`), using the C2 API to read server files, and obtaining a reverse shell via `/api/server/exec`.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Enter the value of user.txt | `THM{...redacted...}` |

### Task 4 - Root.txt

> **ES:** Obtener la bandera root.txt. Tras obtener shell como `webadmin-lowpriv` a través del agente C2, se puede explotar el endpoint `/api/server/exec` que ejecuta comandos como root en el container Docker `c2-shrike-1`. Usar bash reverse shell codificado en base64 para obtener root.
> **EN:** Obtain the root.txt flag. After getting a shell as `webadmin-lowpriv` through the C2 agent, exploit the `/api/server/exec` endpoint which executes commands as root on the Docker container `c2-shrike-1`. Use a base64-encoded bash reverse shell to obtain root.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Enter the value of root.txt | `THM{...redacted...}` |

## Metodología / Methodology

1. **Paso 1 - Enumeración web / Web Enumeration:** Agregar `takedown.thm.local` a `/etc/hosts`. Ejecutar Nmap para identificar puertos 22 y 80. Usar Gobuster para descubrir `/api/`, `/readme.txt`, `/robots.txt`, y directorios ocultos.
2. **Paso 2 - Análisis estático del favicon.ico / Favicon.ico Static Analysis:** Descargar `favicon.ico` y verificar con `file` que es un ejecutable PE64 (no un ICO real). Usar `strings` para descubrir la URL del C2 (`http://takedown.thm.local/`), endpoints de la API (`/api/agents/`, `/api/agents/register`), y el username keyeado (`c.oberst`).
3. **Paso 3 - Análisis del shutterbug.jpg.bak / Shutterbug.jpg.bak Analysis:** Descargar `shutterbug.jpg.bak` y verificar que es un ELF 64-bit compilado con Nim. Ejecutar con `-v` para ver el agente intentando registrarse. Crear usuario local `c.oberst` para que el keying ambiental funcione.
4. **Paso 4 - Interacción con la API C2 / C2 API Interaction:** Descubrir el User-Agent key (`z.5.x.2.l.8.y.5`) en los strings del binario. Usar curl con este User-Agent para acceder a `/api/agents` y listar agentes activos. Leer `app.py` del servidor vía `/api/agents/<uid>/upload` para entender la arquitectura Flask del C2.
5. **Paso 5 - Reverse Shell al servidor web / Reverse Shell to Web Server:** Crear un script de reverse shell Python, subirlo al servidor vía `/api/agents/<uid>/download`, y ejecutarlo vía `/api/agents/<uid>/exec` para obtener shell como `webadmin-lowpriv`.
6. **Paso 6 - Escalada a root / Privilege Escalation to Root:** Usar `/api/server/exec` que ejecuta comandos como root dentro del container Docker. Enviar un bash reverse shell codificado en base64 para obtener root en `c2-shrike-1`.
7. **Paso 7 - Captura de banderas / Flag Capture:** Leer `user.txt` y `root.txt` desde las ubicaciones correspondientes del sistema de archivos.

### Cadena de ataque / Attack Chain

```
Enumeracion web (Gobuster)
    --> favicon.ico = PE64 Nim C2 Agent
        --> strings revela: User-Agent key, endpoints API, username c.oberst
            --> shutterbug.jpg.bak = ELF Nim C2 Agent
                --> Crear usuario c.oberst para keying ambiental
                    --> Interactuar con API Flask del C2
                        --> Leer app.py = fuente completa del servidor
                            --> Subir reverse shell via /download
                                --> Ejecutar via /exec --> shell webadmin-lowpriv
                                    --> /api/server/exec = root en Docker
                                        --> Reverse shell base64 --> ROOT
```

**Lección:** La ofuscación débil de agentes C2 (nombres de archivo inusuales, strings sin cifrar) expone toda la infraestructura. Un endpoint de ejecución remota sin autenticación adecuada en el C2 permite escalada directa a root.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
