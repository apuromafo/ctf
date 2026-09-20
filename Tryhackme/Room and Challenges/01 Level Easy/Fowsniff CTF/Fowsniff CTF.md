# Fowsniff CTF

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | ctf / walkthrough | `fowsniffctf` | https://tryhackme.com/room/fowsniffctf | 01 Level Easy | TryHackMe | nmap / POP3 (110) / SMTP (25) / hydra / pastebin / hashtopolis / John the Ripper / SSH / user flag | Ofensivo: explotar un servidor de correo (POP3) filtrando credenciales de una brecha y un email interno para ganar acceso SSH y leer la flag de usuario. |

---

> **Objeto:** Comprometer la empresa ficticia Fowsniff Corp obteniendo credenciales válidas de POP3 mediante un ataque de fuerza bruta contra el usuario `seina` (password débil de una brecha pública), leyendo un correo interno que revela una contraseña temporal y usándola para acceder por SSH a la máquina `fowsniff`.

**Contexto:** Sala CTF clásica (by mss) sobre una brecha de datos pública. El escaneo revela puertos de correo, y en el sitio web filtrado aparecen correos y pistas (usuario de Twitter `mss`, dump de credenciales `FowsniffCorp` en pastebin). Con el diccionario de contraseñas filtradas, `hydra` encuentra la contraseña de POP3 de `seina`: `scoobydoo2`. Entrando al buzón se lee el correo interno de un compañero donde se comparte una contraseña temporal para SSH (`S1ck3nBluff+secureshell`), con la que se inicia sesión en `10.10.54.116` como `seina` y se lee la flag.

> **ES:** "Fowsniff CTF" — de una brecha pública a POP3 (hydra) y de un email interno a SSH.
> **EN:** From a public breach pasted online, to cracking POP3 (`seina`) with hydra, to reading a colleague's email that leaks the SSH temp password.

## Solucionario

### Task 1: Despliegue / Deployment

**Explicación:** Se inicia la máquina del laboratorio y se lee el escenario de la sala. No hay respuesta que escribir.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Deploy the machine and read the scenario. / Despliega la máquina y lee el escenario. | `No answer needed` |

### Task 2: Reconocimiento / Recon

**Explicación:** Con `nmap` se identifican los servicios expuestos: `POP3` en el puerto `110`, `SMTP` en el `25` y la web en el `80`. En el sitio principal (fowsniffcorp) se encuentra la pista del tweet de burla del usuario `mss` y el enlace a un dump de credenciales filtradas de la empresa publicado como gist (`FowsniffCorp OPSEC Fail`), que contiene usuarios y contraseñas con hash MD5.

```bash
nmap -sV -sC <IP>
# Ver el dump de FowsniffCorp -> 9 usuarios con hash MD5 de contraseñas
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 2 | Identify the leaked credentials. / Identifica las credenciales filtradas. | `No answer needed` |
| 3 | Identify the Twitter user / shaming tweet. / Identifica al usuario de Twitter de la burla. | `No answer needed` |
| 4 | Crack the MD5 hashes. / Descifra los hashes MD5 del dump. | `No answer needed` |
| 5 | Identify the user with the same username on Fowsniff. / Identifica al usuario con el mismo nombre en Fowsniff. | `No answer needed` |

### Task 3: Fuerza bruta sobre POP3 / POP3 Bruteforce

**Explicación:** Entre los hashes del dump destaca el de `seina`, cuyas credenciales filtradas reutiliza en el buzón. Se guardan las contraseñas crackeadas en un diccionario y se lanza `hydra` contra el servicio `pop3` del puerto `110` usando como usuarios la lista del dump, confirmando que `seina` usa `scoobydoo2`.

```bash
hydra -L users.txt -P passwords.txt pop3://<IP> -t 64
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 6 | Brute force the POP3 service. / Lanza fuerza bruta contra POP3. | `No answer needed` |
| 7 | What password did you discover during the bruteforce? / ¿Qué contraseña descubriste en la fuerza bruta? | `scoobydoo2` |

### Task 4: Acceso al buzón / Mailbox Access

**Explicación:** Con las credenciales de `seina` se inicia sesión en POP3 y se descarga el buzón. El primer correo, remitente `stone`, detalla por error que se ha registrado una contraseña temporal del sistema y la comparte sin cifrar: `S1ck3nBluff+secureshell`. Esa misma contraseña sirve para entrar por SSH al servidor.

```bash
nc <IP> 110
USER seina
PASS scoobydoo2
LIST / RETR 1
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 8 | Read the mail from the mailbox. / Lee el correo del buzón. | `No answer needed` |
| 9 | What is the password provided in the email? / ¿Qué contraseña se comparte en el email? | `S1ck3nBluff+secureshell` |

### Task 5: Acceso SSH / SSH Access

**Explicación:** Se usa la contraseña temporal para conectarse por SSH como `seina` a la máquina. Una vez dentro, se localiza la flag de usuario y se exploran los servicios de la internal network según pide la sala.

```bash
ssh seina@<IP>
# contraseña: S1ck3nBluff+secureshell
find / -name "user.txt" 2>/dev/null
cat user.txt
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 10 | SSH into the box. / Entra por SSH a la máquina. | `No answer needed` |
| 11 | Find the user flag. / Encuentra la flag de usuario. | `No answer needed` |
| 12 | Investigate the internal services. / Investiga los servicios internos. | `No answer needed` |
| 13 | Explore the box and record the services. / Explora la máquina y anota sus servicios. | `No answer needed` |
| 14 | Complete the final step. / Completa el paso final. | `No answer needed` |
| 15 | Complete the room. / Completa la sala. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Deploy the machine and read the scenario. | `No answer needed` |
| 2 | Identify the leaked credentials. | `No answer needed` |
| 3 | Identify the Twitter user / shaming tweet. | `No answer needed` |
| 4 | Crack the MD5 hashes. | `No answer needed` |
| 5 | Identify the user with the same username on Fowsniff. | `No answer needed` |
| 6 | Brute force the POP3 service. | `No answer needed` |
| 7 | What password did you discover during the bruteforce? | `scoobydoo2` |
| 8 | Read the mail from the mailbox. | `No answer needed` |
| 9 | What is the password provided in the email? | `S1ck3nBluff+secureshell` |
| 10 | SSH into the box. | `No answer needed` |
| 11 | Find the user flag. | `No answer needed` |
| 12 | Investigate the internal services. | `No answer needed` |
| 13 | Explore the box and record the services. | `No answer needed` |
| 14 | Complete the final step. | `No answer needed` |
| 15 | Complete the room. | `No answer needed` |

---

**Metodología:** Escaneo de puertos (110 POP3, 25 SMTP, 80 HTTP) y OSINT desde la web hasta el dump público de credenciales. Crackeo de los hashes MD5 publicados y fuerza bruta de POP3 con `hydra` para validar la reutilización de contraseñas (`seina`). Acceso al buzón para extraer la contraseña temporal de SSH y, con ella, acceso final a la máquina.

### Cadena de ataque / Attack Chain

```text
nmap (110/25/80) -> web -> tweet de mss -> dump FowsniffCorp en pastebin/gist -> crack de MD5 -> hydra pop3 (seina) -> scoobydoo2 -> mail interno -> S1ck3nBluff+secureshell -> SSH -> flag de usuario
```

**Learning chain:** OSINT leak -> MD5 cracking -> hydra POP3 -> password reuse -> internal email -> SSH access.

**Lección:** *Las brechas públicas de credenciales son el punto de partida: los usuarios reutilizan contraseñas (POP3) y el personal comparte secretos por correo sin cifrar; la fuerza bruta dirigida contra el servicio de correo destapa todo el camino de intrusión.*

**MITRE ATT&CK:** T1078.001 — Valid Accounts: Default Accounts; T1110.003 — Brute Force: Password Spraying; T1021.001 — Remote Services: SSH; T1213 — Data from Information Repositories

**Fuente:** [TryHackMe - Fowsniff CTF](https://tryhackme.com/room/fowsniffctf)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.