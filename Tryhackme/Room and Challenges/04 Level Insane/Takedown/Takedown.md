# Takedown

| **Dificultad** | Insane |
| **Tipo** | CTF |
| **Slug** | `takedown` |
| **Link** | [TryHackMe](https://tryhackme.com/room/takedown) |
| **Sección** | 04 Level Insane |
| **Fuente** | TryHackMe official room, GitHub (jesusgavancho/TryHackMe_and_HackTheBox), Medium writeup by Firat Demir, YouTube walkthrough by Jacob Taylor, Medium writeup by Hassan Mughal |
| **Componentes** | nmap/gobuster/nim/malware/c2-api/privilege-escalation/docker |
| **Impacto** | Desmontaje del teamserver de RISOTTO GROUP combinando análisis estático de malware Nim con el abuso de una C2 API mal asegurada hasta obtener root en el contenedor Docker. |

---

**Contexto:** Takedown es un CTF de nivel Insane donde un servidor web corporativo ha sido comprometido por el grupo RISOTTO. La misión es encontrar su teamserver y tomarlo control. Involucra análisis estático de malware Nim, interpretación de C2 API, y explotación de un endpoint de ejecución remota para obtener root.

## Solucionario

### Task 1: Mission Brief (OPERATION: OVERCOOKED RISOTTO)

Leer el documento de inteligencia adjunto (OPORDOVERCOOKEDRISOTTO.pdf). El brief contiene información crítica sobre el grupo RISOTTO, incluyendo su uso de keying ambiental, agentes Nim, y un User-Agent predefinido para autenticación.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Ready! | `Completed` |

### Task 2: Start VM

Iniciar la máquina virtual y agregar la IP a `/etc/hosts` como `takedown.thm.local`. Ejecutar un escaneo Nmap básico para confirmar puertos 22 (SSH) y 80 (HTTP/nginx 1.23.1) abiertos.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | VM Started | `Completed` |

### Task 3: User.txt

Obtener la bandera user.txt. La cadena de explotación completa requiere: enumeración web con Gobuster, análisis estático de `favicon.ico` (PE64 compilado con Nim que contiene un agente C2), descubrimiento del User-Agent key (`z.5.x.2.l.8.y.5`), uso de la API del C2 para leer archivos del servidor, y obtención de reverse shell a través de `/api/server/exec`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Enter the value of user.txt | `THM{c2_servers_have_vulnerabilities_t00}` |

### Task 4: Root.txt

Obtener la bandera root.txt. Tras obtener shell como `webadmin-lowpriv` a través del agente C2, se puede explotar el endpoint `/api/server/exec` que ejecuta comandos como root en el container Docker `c2-shrike-1`. Usar bash reverse shell codificado en base64 para obtener root.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Enter the value of root.txt | `THM{th3_r00t_of_the_pr0blem}` |

---

**Metodología:**
1. **Enumeración web:** Agregar `takedown.thm.local` a `/etc/hosts`. Ejecutar Nmap para identificar puertos 22 y 80. Usar Gobuster para descubrir `/api/`, `/readme.txt`, `/robots.txt`, y directorios ocultos.
2. **Análisis estático del `favicon.ico`:** Descargar `favicon.ico` y verificar con `file` que es un ejecutable PE64 (no un ICO real). Usar `strings` para descubrir la URL del C2 (`http://takedown.thm.local/`), los endpoints de la API (`/api/agents/`, `/api/agents/register`), y el username keyeado (`c.oberst`).
3. **Análisis del `shutterbug.jpg.bak`:** Descargar `shutterbug.jpg.bak` y verificar que es un ELF 64-bit compilado con Nim. Ejecutarlo con `-v` para ver al agente intentando registrarse. Crear usuario local `c.oberst` para que el keying ambiental funcione.
4. **Interacción con la API C2:** Descubrir el User-Agent key (`z.5.x.2.l.8.y.5`) en los strings del binario. Usar curl con este User-Agent para acceder a `/api/agents` y listar agentes activos. Leer `app.py` del servidor vía `/api/agents/<uid>/upload` para entender la arquitectura Flask del C2.
5. **Reverse shell al servidor web:** Crear un script de reverse shell Python, subirlo al servidor vía `/api/agents/<uid>/download`, y ejecutarlo vía `/api/agents/<uid>/exec` para obtener shell como `webadmin-lowpriv`. Leer `user.txt` → `THM{c2_servers_have_vulnerabilities_t00}`.
6. **Escalada a root:** Usar `/api/server/exec` que ejecuta comandos como root dentro del container Docker. Enviar un bash reverse shell codificado en base64 para obtener root en `c2-shrike-1`.
7. **Captura de flags:** Recolectar las banderas `user.txt` y `root.txt` desde las ubicaciones correspondientes del sistema de ficheros; `root.txt` → `THM{th3_r00t_of_the_pr0blem}`.

**Learning chain:** gobuster → `favicon.ico` (PE64 Nim C2 agent) → strings (C2 URL, endpoints API, username `c.oberst`, User-Agent key) → `shutterbug.jpg.bak` (ELF Nim C2 agent) → usuario `c.oberst` (keying ambiental) → `/api/agents` (lista de agentes) → `app.py` (fuente Flask del C2) → `/api/agents/<uid>/download` y `/exec` → reverse shell → `webadmin-lowpriv` → `user.txt` → `/api/server/exec` (root en Docker) → reverse shell base64 → `root.txt`.

**MITRE ATT&CK:** T1046 (Network Service Discovery), T1036 (Masquerading), T1203 (Execution via Client Software), T1071 (Application Layer Protocol), T1105 (Ingress Tool Transfer), T1219 (Remote Access Software), T1068 (Privilege Escalation)

**Fuente:** [TryHackMe - Takedown](https://tryhackme.com/room/takedown)