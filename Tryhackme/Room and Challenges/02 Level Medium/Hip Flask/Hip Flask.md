# Hip Flask

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Room | hipflask | https://tryhackme.com/room/hipflask | 02 Level Medium | TryHackMe | Pentest metodológico, DNS/zone transfer, Flask, source disclosure, cookie forgery, Jinja2 SSTI, RCE, Linux privesc | Compromiso total (root) de un servidor expuesto |

---

**Contexto:** **Hip Flask** es un walkthrough de pentesting completo contra un servidor expuesto (Hip Flasks Ltd). El alcance es un único target con SSH (22), DNS (53, banner modificado) y HTTP(S) (80/443). Se empieza con pasivo (OSINT) y activo (nmap/rustscan, Nessus de solo puertos conocidos), se aprende el dominio `hipflasks.thm`, se hace un zone transfer (`dig axfr`) que revela el subdominio `hipper`, y sobre la web se encadenan: source disclosure, robo del secret key de Flask, forja de cookies de sesión y una SSTI en Jinja2 que deriva en RCE. La escalada termina leyendo el hash del usuario root (`/etc/shadow`, sha512crypt `$6$`).

## Solucionario

### Task 1

**Explicación:** Presentación del alcance (target único, clon de producción, todo en scope, cliente Hip Flasks Ltd). Sin respuesta textual.

Respuestas de la tarea:

1. `No answer needed`

### Task 2

**Explicación:** Reconocimiento pasivo (OSINT: emails públicos, empleados, subdominios, repos) y escaneo de puertos activo con rustscan/nmap. Se confirman SSH (22), DNS (53 TCP/UDP con banner modificado) y HTTP(S) (80/443).

```bash
rustscan -a <IP> -- -sT -Pn
nmap -Pn -sT -vv <IP> -oN Initial-SYN-Scan
nmap -sV -p 22,53,80,443 <IP>
```

Respuestas de la tarea:

1. `No answer needed`

### Task 3

**Explicación:** Business/scope: la parte de red del target es externa (Internet pública). Es la respuesta que captura la nota.

Respuestas de la tarea:

1. `External`

### Task 4

**Explicación:** Escaneo de vulnerabilidades con Nessus (Advanced Scan, sin ping, solo los puertos ya confirmados). Resultados: 2 medium, 1 low y 42 information disclosures (certificado self-signed, cipher CBC débil en SSH). Nada explotable directamente.

Respuestas de la tarea:

1. `No answer needed`

### Task 5

**Explicación:** Valoración de los hallazgos de Nessus para el informe al cliente.

Respuestas de la tarea:

1. `No answer needed`

### Task 6

**Explicación:** Primeras impresiones de la web: el servidor responde "Host not found" y confirma que sirve sitios del dominio `hipflasks.thm`.

Respuestas de la tarea:

1. `No answer needed`

### Task 7

**Explicación:** Reconocimiento DNS del dominio; se identifica que el servidor espera un server name concreto.

Respuestas de la tarea:

1. `No answer needed`

### Task 8

**Explicación:** Se lanza una transferencia de zona (AXFR) contra `hipflasks.thm`; revela los subdominios, incluido `hipper`.

```bash
dig axfr hipflasks.thm @<IP>
```

Respuestas de la tarea:

1. `No answer needed`

### Task 9

**Explicación:** El zone transfer muestra los registros A; el subdominio que aloja la webapp es `hipper` (sin `www`).

Respuestas de la tarea:

1. `hipper`

### Task 10

**Explicación:** Enumeración de la web en `https://hipper.hipflasks.thm` (añadir a hosts): Wappalyzer/Burp muestran header `waitress` (reverso a Flask/Django). La cookie de sesión se crea sin el flag `Secure`.

Respuestas de la tarea:

1. `No answer needed`

### Task 11

**Explicación:** Nikto y Feroxbuster en paralelo; el certificado es válido aunque el cipher se consideró corriente; Nikto marca BREACH (falso positivo).

Respuestas de la tarea:

1. `No answer needed`

### Task 12

**Explicación:** Source disclosure: se consigue cURLear `main.py` del webroot (y `modules/__init__.py`, `libs/auth.py`). Se obtiene el código de la app y su secret key de Flask — la base de todo lo siguiente.

```bash
curl -k https://hipper.hipflasks.thm/main.py
curl -k https://hipper.hipflasks.thm/modules/__init__.py
curl -k https://hipper.hipflasks.thm/libs/auth.py
```

Respuestas de la tarea:

1. `No answer needed`

### Task 13

**Explicación:** Entender la vulnerabilidad: sesiones de Flask client-side firmadas con el secret key; quien tenga la clave puede forjar cualquier cookie (`session["auth"]="True"`, `username` a voluntad).

Respuestas de la tarea:

1. `No answer needed`

### Task 14

**Explicación:** Forjar la cookie firmada para acceder al panel de admin con los valores deseados.

Respuestas de la tarea:

1. `No answer needed`

### Task 15

**Explicación:** SSTI + RCE: el valor de `session["username"]` se inyecta en la plantilla Jinja2 antes de renderizarla; un payload Jinja2 dentro del username (en la cookie forjada) se evalúa como código → RCE en el servidor.

```jinja
{{ ... passthrough a RCE ... }}
# cookie forjada con username = payload Jinja2 + secret key
```

Respuestas de la tarea:

1. `No answer needed`

### Task 16

**Explicación:** Estabilizar la shell obtenida.

Respuestas de la tarea:

1. `No answer needed`

### Task 17

**Explicación:** Escalada de privilegios local tras la shell (enumeración y privesc hacia root).

Respuestas de la tarea:

1. `No answer needed`

### Task 18

**Explicación:** Lectura de `/etc/shadow` preparando el crackeo del hash de root.

Respuestas de la tarea:

1. `No answer needed`

### Task 19

**Explicación:** Se extrae el hash sha512crypt (`$6$...`) del usuario root; el formato sha512crypt es el de Linux por defecto.

Respuestas de la tarea:

1. `$6$./Fh3mWMsk8X29kq$6CvaDzV7zlXKn1MMQjXtO.abB4/7ecNKBFkQvEWsLkgM8raAZeuSHZurnXG01pqZ4BY2ubk/WgIbo4ee.wnaP0`
2. `No answer needed`

### Task 20

**Explicación:** Redacción final del informe/report al cliente (entregable del pentest).

Respuestas de la tarea:

1. `No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1.1 | Pregunta 1 (scope) | `No answer needed` |
| 2.1 | Pregunta 1 (recon/port scan) | `No answer needed` |
| 3.1 | Is the network portion internal or external? | `External` |
| 4.1 | Pregunta 1 (Nessus scan) | `No answer needed` |
| 5.1 | Pregunta 1 (hallazgos) | `No answer needed` |
| 6.1 | Pregunta 1 (initial thoughts web) | `No answer needed` |
| 7.1 | Pregunta 1 (DNS recon) | `No answer needed` |
| 8.1 | Pregunta 1 (zone transfer) | `No answer needed` |
| 9.1 | What subdomain hosts the webapp we're looking for? | `hipper` |
| 10.1 | Pregunta 1 (web enumeración) | `No answer needed` |
| 11.1 | Pregunta 1 (Nikto/Feroxbuster) | `No answer needed` |
| 12.1 | Pregunta 1 (source disclosure) | `No answer needed` |
| 13.1 | Pregunta 1 (entender la vuln) | `No answer needed` |
| 14.1 | Pregunta 1 (cookie forgery) | `No answer needed` |
| 15.1 | Pregunta 1 (SSTI + RCE) | `No answer needed` |
| 16.1 | Pregunta 1 (shell stabilize) | `No answer needed` |
| 17.1 | Pregunta 1 (privesc) | `No answer needed` |
| 18.1 | Pregunta 1 (/etc/shadow) | `No answer needed` |
| 19.1 | What is the root user's password hash? | `$6$./Fh3mWMsk8X29kq$6CvaDzV7zlXKn1MMQjXtO.abB4/7ecNKBFkQvEWsLkgM8raAZeuSHZurnXG01pqZ4BY2ubk/WgIbo4ee.wnaP0` |
| 19.2 | Pregunta 2 (crack el hash) | `No answer needed` |
| 20.1 | Pregunta 1 (informe) | `No answer needed` |

---

**Metodología:** Metodología de pentest completa (PTES/OSSTMM): alcance, recon pasivo/activo (OSINT, rustscan/nmap), escaneo de vulnerabilidades (Nessus solo puertos conocidos), footprinting DNS (zone transfer), enumeración web (Wappalyzer/Burp/Feroxbuster/Nikto), source disclosure (main.py + secret key), forja de cookies Flask, SSTI en Jinja2 → RCE, estabilización de shell y escalada leyendo `/etc/shadow`, cerrando con el informe al cliente.

**Learning chain:** scope único → OSINT + rustscan/nmap → Nessus (2M/1L/42info) → dominio hipflasks.thm → dig axfr → hipper → waitress/Flask → source disclosure → secret key → cookie forge (role admin) → SSTI Jinja2 → RCE → shell → privesc → /etc/shadow → hash root $6$ → informe.

**Lección:** *Un pentest "aburrido" (todo No answer needed hasta la tarea 9) se gana con metodología: el zone transfer y la disclosure del código con la secret key son los dos pivotes que convierten la enumeración en compromiso total.*

**MITRE ATT&CK:** T1596.002 DNS (zone transfer) · T1083 File and Directory Discovery · T1082 System Information Discovery · T1213.002 (NO) · T1550.004 Web Session Cookie · T1600 Weaken Encryption/Weakened Cryptography (cookie forgery) · T1190 Exploit Public-Facing Application (SSTI → RCE) · T1068 Exploitation for Privilege Escalation.

**Fuente:** [TryHackMe - Hip Flask](https://tryhackme.com/room/hipflask)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.