# Bypass
| **Dificultad** | Medium |
| **Tipo** | CTF |
| **Slug** | `bypass` |
| **Link** | [TryHackMe](https://tryhackme.com/room/bypass) |
| **Sección** | Web / CTF |
| **Fuente** | Research de thmrevenant (GitHub) y writeups de la comunidad |
| **Componentes** | Web, IDOR en fpassword.php (?id=), panel CCTV, concatenación de flags, virtual host cctv.thm, entorno Linux (lsb_release), credenciales por defecto, bandera final tras login |
| **Impacto** | Sala Medium estilo CTF: enumerar flags vía manipulación de parámetro (`id`) en un endpoint de "forgot password", concatenar los valores obtenidos como primera capa de seguridad, identificar el sistema (20.04), entrar al panel CCTV y capturar la bandera de compromiso. |
---
**Contexto:** La sala plantea un reto tipo CTF sobre un panel de CCTV. La cadena comienza recorriendo los valores de `id` del endpoint `fpassword.php` (vulnerabilidad de acceso a objetos, IDOR) para recolectar cinco banderas; el resultado es la "contraseña" que protege el panel. Con las comprobaciones de entorno y una credencial sencilla (`bypass`) se accede al panel y se obtiene la bandera final de compromiso de la vídeo-vigilancia.
*EN: The room poses a CCTV panel CTF-style challenge. The chain starts by walking the `id` values of the `fpassword.php` endpoint (broken object access / IDOR) to collect five flags; their concatenation is the "password" protecting the panel. With environment checks and a trivial credential (`bypass`) the panel is entered and the final CCTV compromise flag is obtained.*
## Solucionario
### Task 1 — Enumeración de Flags (cctv.thm/fpassword.php)
**Explicación:** Configurar el virtual host `cctv.thm` (por ejemplo con `/etc/hosts` o navegando con ese Host) y recorrer el endpoint `fpassword.php?id=1..5`. Cada valor de `id` devuelve una bandera distinta; el parámetro no valida correctamente qué ficha se consulta (IDOR).
*EN: Set up the virtual host `cctv.thm` (for example via `/etc/hosts` or browsing with that Host header) and walk the `fpassword.php?id=1..5` endpoint. Each `id` value returns a different flag; the parameter does not properly validate which entry is fetched (IDOR).*

```bash
# Añadir virtual host
echo "10.10.x.x cctv.thm" | sudo tee -a /etc/hosts
# Enumerar banderas
for i in 1 2 3 4 5; do curl -s "http://cctv.thm/fpassword.php?id=$i"; done
```
### Task 2 — Primera Capa de Seguridad (CCTV)
**Explicación:** La primera capa de seguridad del panel se resuelve concatenando las cinco banderas obtenidas en el paso anterior (en orden), formando la "contraseña" de entrada para el siguiente nivel.
*EN: The panel's first security layer is solved by concatenating the five flags obtained in the previous step (in order), forming the entry "password" for the next level.*
### Task 3 — Environment
**Explicación:** Comprobación del entorno del sistema comprometido. Ejecutar `lsb_release -r -s` en la máquina asociada devuelve la versión de la distribución (Ubuntu Focal Fossa 20.04).
*EN: Environment check of the compromised system. Running `lsb_release -r -s` on the attached machine returns the distribution version (Ubuntu Focal Fossa 20.04).*

```bash
ssh <user>@<target>   # o shell previa
lsb_release -r -s
# 20.04
```
### Task 4 — Acceso al Panel (CCTV)
**Explicación:** Con la capa de seguridad superada, se identifican credenciales de acceso al panel CCTV: el usuario es `bypass`. Tras iniciar sesión en el panel, se muestra la bandera final que confirma el compromiso de la videovigilancia.
*EN: With the first security layer passed, the CCTV panel access credentials are identified: the username is `bypass`. After logging into the panel, the final flag confirming the video-surveillance compromise is displayed.*
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag value after accessing the endpoint cctv.thm/fpassword.php?id=1? | `THM{10001}` |
| 2 | What is the flag value after accessing the endpoint cctv.thm/fpassword.php?id=2? | `THM{10125}` |
| 3 | What is the flag value after accessing the endpoint cctv.thm/fpassword.php?id=3? | `THM{13231}` |
| 4 | What is the flag value after accessing the endpoint cctv.thm/fpassword.php?id=4? | `THM{33120}` |
| 5 | What is the flag value after accessing the endpoint cctv.thm/fpassword.php?id=5? | `THM{12319}` |
| 6 | What is the password value for the first layer of security for the CCTV web panel? | `THM{10001}THM{10125}THM{13231}THM{33120}THM{12319}` |
| 7 | What is the lsb_release -r -s command output from the attached machine? | `20.04` |
| 8 | What is the username for the CCTV web panel? | `bypass` |
| 9 | What is the flag value after logging into the CCTV web panel? | `THM{CCTV_HACKED_1011110}` |
---
**Metodología:** Configurar virtual host cctv.thm → enumerar `fpassword.php?id=N` (IDOR) → recopilar 5 banderas → concatenarlas como contraseña (capa 1) → comprobar sistema con `lsb_release -r -s` → autenticarse en el panel con `bypass` → bandera final.
**Learning chain:** virtual host + IDOR → obtención de credenciales fragmentadas → concatenación como clave → identificación del sistema → acceso de panel → compromiso final.
**Lección:** *Los endpoints que exponen objetos por un `id` secuencial sin autorización (IDOR) filtran tanto como una API mal diseñada; si además las credenciales derivan de valores concatenados del propio sistema, el "candado" es solo decorativo.*
**MITRE ATT&CK:** T1592.002 (Gather Victim Host Information - OS), T1110 (Brute Force), T1110.001 (Password Guessing), T1078 (Valid Accounts), T1021, T1499.
**Fuente:** [TryHackMe - Bypass](https://tryhackme.com/room/bypass)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.