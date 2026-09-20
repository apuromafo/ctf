# Ra 2

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|------|------|------|---------|--------|-------------|---------|
| Hard | CTF | `ra2` | [TryHackMe](https://tryhackme.com/room/ra2) | 03 Level Hard | Web (API THM `api/v2/rooms/tasks?roomCode=ra2` + websearch de walkthroughs) | DNS (TXT/enumeración) / nsupdate (dynamic updates) / Certificados (crackpkcs12 / cert.pfx) / Responder (NetNTLMv2) / PowerShell Web Access (PSWA) / SeImpersonatePrivilege (PrintSpoofer/SweetPotato) | Enumeración DNS de recursos, envenenamiento DNS con nsupdate (actualizaciones dinámicas inseguras), robo de certificado pfx, captura de NetNTLMv2 con Responder, acceso a PowerShell Web Access y escalada local por SeImpersonatePrivilege. |

---

**Contexto:**

> **ES:** **Ra 2** es la continuación del CTF AD **Ra** (ambientado en `windcorp.thm`). La primera flag se encuentra en un **registro DNS TXT** y, además, sirve como hint: "Allowing nonsecure dynamic updates is a significant security vulnerability because updates can be accepted from untrusted sources". Con `crackpkcs12`\`/`openssl` se abre el `cert.pfx` robado de `selfservice.dev.windcorp.thm/backup` (contraseña crackeada), y con el par clave/cert y **nsupdate** se realizan actualizaciones dinámicas DNS para apuntar `selfservice.windcorp.thm` a la máquina del atacante. Cuando el usuario `edwardle` se conecta al portal se captura su **NetNTLMv2** con **Responder**; crackeado ese hash se accede a **PowerShell Web Access (PSWA)** y, contando la cuenta con **SeImpersonatePrivilege**, se escala a SYSTEM con PrintSpoofer/alternativas para leer el flag final.
> **EN:** **Ra 2** is the sequel to the **Ra** AD CTF (set in `windcorp.thm`). The first flag sits in a **DNS TXT record** and, at the same time, works as a hint: "Allowing nonsecure dynamic updates is a significant security vulnerability because updates can be accepted from untrusted sources". With `crackpkcs12`/`openssl` the stolen `cert.pfx` from `selfservice.dev.windcorp.thm/backup` is opened (cracked password), and with the key/cert pair, **nsupdate** performs dynamic DNS updates to point `selfservice.windcorp.thm` at the attacker's machine. When user `edwardle` connects to the portal, his **NetNTLMv2** hash is captured with **Responder**; once cracked, access is gained to **PowerShell Web Access (PSWA)** and, since the account holds **SeImpersonatePrivilege**, escalation to SYSTEM is achieved with PrintSpoofer/alternatives to read the final flag.

---

## Solucionario

### Task 1: Obtener las banderas / Get the flags

**Explicación:**
La cadena completa (TXT DNS → robo de cert.pfx → nsupdate/DNS poisoning → Responder NetNTLMv2 de edwardle → crack → PSWA → SeImpersonatePrivilege → SYSTEM) desemboca en las tres flags. La flag 1 es una frase literal almacenada en el TXT, por lo que se debe copiar con sus mayúsculas y espacios exactos.

1. 1. THM{Allowing nonsecure dynamic updates is a significant security vulnerability because updates can be accepted from untrusted sources}
   2. THM{8a1d460dfe345f8edd09d45ae00e5c1c14d12c89}
   3. THM{9a8b9f4f3af2bce68885106c1c8473ab85e0eda0}

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | 1. What is flag 1? | `THM{Allowing nonsecure dynamic updates is a significant security vulnerability because updates can be accepted from untrusted sources}` |
| 1 | 2. What is flag 2? | `THM{8a1d460dfe345f8edd09d45ae00e5c1c14d12c89}` |
| 1 | 3. What is flag 3? | `THM{9a8b9f4f3af2bce68885106c1c8473ab85e0eda0}` |

---

**Metodología:**

1. Reconocimiento: `nmap` → DC `windcorp.thm` (`fire.windcorp.thm`) con DNS, HTTP, SMB, LDAP, RDP, WinRM... Se añaden los FQDN a `/etc/hosts`.
2. Flag 1 (DNS TXT): enumeración de registros TXT con `dig`/`host -t TXT` sobre el dominio → el TXT contiene la flag 1 (frase literal, con mayúsculas y espacios).
3. Enumeración web/backup: en `selfservice.dev.windcorp.thm/backup` se encuentra un fichero de certificado **`cert.pfx`** (probablemente el certificado de un usuario del dominio).
4. Crack del pfx: `crackpkcs12` (o `john` sobre el pfx) recupera la contraseña del certificado → se extraen la clave privada y el certificado (openssl pkcs12).
5. DNS poisoning con nsupdate: el hint del TXT (actualizaciones dinámicas no seguras) indica que el DNS permite actualizaciones sin firma. Con **nsupdate** y el par clave/cert (o la cuenta del certificado) se crea actualiza `selfservice.windcorp.thm` → apuntando a la IP del atacante.
6. Captura NetNTLMv2: se levanta **Responder** (`responder -I tun0`) en la máquina del atacante. Cuando `edwardle` se autentica contra el portal `selfservice.windcorp.thm` (ahora dirigido al atacante), Responder captura su **NetNTLMv2**.
7. Crack del hash: `hashcat -m 5600` (o john) → password de `edwardle`.
8. PowerShell Web Access (PSWA): con las credenciales se entra en `https://<IP>/pswa` (interfaz web de PowerShell) y se abre una sesión remota.
9. SeImpersonatePrivilege → SYSTEM → flag 3: comprobado que la cuenta tiene **SeImpersonatePrivilege** (`whoami /priv`), se sube/ejecuta **PrintSpoofer** (o SeImpersonate/alternativas) para conseguir una shell como SYSTEM → leer `flag 3` (root.txt / flag del administrador).

### Cadena de ataque / Attack Chain

`nmap → windcorp.thm (DC) → dig TXT → flag 1 (sentence hint) → selfservice.dev.windcorp.thm/backup → cert.pfx → crackpkcs12 → clave + cert → nsupdate (dynamic update) → selfservice.windcorp.thm → IP atacante → Responder → NetNTLMv2 de edwardle → hashcat -m 5600 → PSWA (https://<IP>/pswa) → sesión PowerShell → SeImpersonatePrivilege → PrintSpoofer → SYSTEM → flag 3`

**Learning chain:**

Enumeración DNS (TXT) → Descubrimiento de secretos en servidores de aplicaciones (backup) → Cracking de contenedores PKCS#12 (cert.pfx) → DNS dynamic updates (nsupdate) como vector de red → Redirección de hostname al atacante → Captura de autenticación con Responder (NetNTLMv2) → Cracking de NTLMv2 → Acceso vía PowerShell Web Access → Reconocimiento de privilegios (whoami /priv) → Abuso de SeImpersonatePrivilege (PrintSpoofer) → SYSTEM.

*Lección:* Un simple registro DNS TXT puede regalar el primer flag y, a la vez, la filosofía del reto: los **dynamic updates DNS no seguros** (apuntando un hostname al atacante) dejan de ser un "detalle" y se convierten en el vector de suplantación que alimenta a Responder. Después, el bucle se cierra con la misma moraleja de Ra: credenciales crackeadas + un privilegio de impresión mal otorgado (SeImpersonate) = SYSTEM en la máquina.

**MITRE ATT&CK:**

T1596.002 (Search Open Technical Databases: DNS/Passive DNS), T1552.001 (Unsecured Credentials: Credentials In Files), T1187 (Forced Authentication), T1040 (Network Sniffing), T1078 (Valid Accounts), T1059.001 (PowerShell), T1134 (Access Token Manipulation), T1068 (Exploitation for Privilege Escalation)

**Fuente:** [TryHackMe - Ra 2](https://tryhackme.com/room/ra2)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.