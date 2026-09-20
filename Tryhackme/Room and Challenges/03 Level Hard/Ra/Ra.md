# Ra

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|------|------|------|---------|--------|-------------|---------|
| Hard | CTF | `ra` | [TryHackMe](https://tryhackme.com/room/ra) | 03 Level Hard | Web (API THM `api/v2/rooms/tasks?roomCode=ra` + websearch de walkthroughs) | Active Directory / SMB / XMPP Spark 2.8.3 (CVE-2020-12772) / XSS img → Responder (NetNTLMv2) / hashcat crack / WinRM / Account Operators / PowerShell scripts | Abuso de un chat XMPP (Spark) con XSS en imágenes para capturar NetNTLMv2 con Responder, crackear la contraseña, entrar por WinRM y escalar en el dominio a través del grupo Account Operators y un script de PowerShell gestionando cuentas de servidores. |

---

**Contexto:**

> **ES:** **Ra** es un CTF Hard de Active Directory ambientado en la empresa ficticia **windcorp** (dominio `windcorp.thm`, DC en `fire.windcorp.thm`). En una primera fase se "resetea el password de la mascota" en el portal de self-service (nombre del perro del usuario) para obtener acceso inicial y, por SMB, la verdadera primera flag. Después el reto es un **XMPP/chat** (Spark 2.8.3) vulnerable al **CVE-2020-12772**: el cliente Spark muestra imágenes de avatares, y en el logout la petición con la URL de la imagen se envía vía `img` sin escaparla → se carga un recurso de tu listener/Responder → captura de un hash NetNTLMv2 del usuario del chat. Se crackea (password del estilo temático de la sala) y mediante **WinRM** se conecta como el usuario; la última flag exige escalar dentro de AD: se abusa del grupo **Account Operators** (que permite administrar cuentas de otros) y del script `checkservers.ps1`/fichero `hosts.txt` con el que el usuario `buse` controla las máquinas. El nombre "Ra" y las credenciales temáticas (dioses egipcios) recorren la sala.
> **EN:** **Ra** is a Hard Active Directory CTF set in the fictional company **windcorp** (domain `windcorp.thm`, DC at `fire.windcorp.thm`). In a first phase the "pet's password" is reset on the self-service portal (the user's dog name) to gain initial access and, via SMB, the true first flag. Afterwards the challenge is an **XMPP/chat** (Spark 2.8.3) vulnerable to **CVE-2020-12772**: the Spark client renders avatar images, and on logout the request with the image URL goes through an `img` tag without escaping → it loads a resource from your listener/Responder → a NetNTLMv2 hash from the chat user is captured. It is cracked (password in the room's thematic style) and access is gained via **WinRM**; the final flag requires escalating inside AD: abusing the **Account Operators** group (which lets you manage other accounts) and the `checkservers.ps1` script / `hosts.txt` file with which the `buse` user controls the machines. The name "Ra" and the Egyptian-god-themed credentials run through the whole room.

---

## Solucionario

### Task 1: Obtener las banderas / Get the flags

**Explicación:**
Se obtienen tres flags encadenando: el reset del password de la mascota y SMB (flag 1), la captura del NetNTLMv2 vía CVE-2020-12772 en el chat Spark + WinRM (flag 2) y la escalada a través de Account Operators / script de administración del DC (flag 3).

1. 1. THM{466d52dc75a277d6c3f6c6fcbc716d6b62420f48}
   2. THM{6f690fc72b9ae8dc25a24a104ed804ad06c7c9b1}
   3. THM{ba3a2bff2e535b514ad760c283890faae54ac2ef}

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | 1. What is flag 1? | `THM{466d52dc75a277d6c3f6c6fcbc716d6b62420f48}` |
| 1 | 2. What is flag 2? | `THM{6f690fc72b9ae8dc25a24a104ed804ad06c7c9b1}` |
| 1 | 3. What is flag 3? | `THM{ba3a2bff2e535b514ad760c283890faae54ac2ef}` |

---

**Metodología:**

1. Reconocimiento: `nmap` sobre `windcorp.thm` (IP del DC `fire.windcorp.thm`) → DNS, HTTP (portal de self-service), SMB, LDAP, RDP, WinRM (5985/5986)... Se añaden todos los FQDN a `/etc/hosts`.
2. Self-service / reset de password: en el portal se resetea la contraseña del usuario objetivo respondiendo a la pregunta de seguridad (la mascota). Se obtienen credenciales válidas iniciales.
3. SMB → flag 1: con las credenciales (`nxc smb` / smbclient) se enumeran los shares y se localiza/lee la flag 1 del share de usuario.
4. Identificar el chat XMPP: hay un servidor/la app de **Spark 2.8.3** sobre XMPP; el cliente renderiza avatares/imágenes.
5. CVE-2020-12772 → NetNTLMv2: se prepara **Responder** en el host atacante (`responder -I tun0`) y desde el chat del usuario se consigue que cargue una imagen apuntando a la IP del atacante en el momento del logout (petición `img` sin escape). Responder captura el **NetNTLMv2** del usuario del chat.
6. Crack del hash: `hashcat -m 5600 netntlm.txt rockyou` (o john) → password (temática egipcia/del reto).
7. WinRM → flag 2: con las credenciales crackeadas se entra vía WinRM (evil-winrm) como el usuario del chat → **flag 2** en su entorno/profesión.
8. Escalada Account Operators → flag 3: se descubre que el usuario está en **Account Operators**; enumerando AD (BloodHound/net users) se ve que puede administrar la cuenta del usuario `buse`. `buse` ejecuta `checkservers.ps1` sobre los servidores listados en `hosts.txt` (delegación de administración). Abusando de esa delegación (restablecer password / añadir a grupo / crear tarea) se consigue acceso a la cuenta de administración del servidor/DC → **flag 3**.

### Cadena de ataque / Attack Chain

`nmap → windcorp.thm / fire.windcorp.thm → Self-service portal (reset de password por pregunta de seguridad) → SMB con credenciales → flag 1 → Chat XMPP Spark 2.8.3 → CVE-2020-12772 (img en logout sin escape) → Responder NetNTLMv2 → hashcat -m 5600 → WinRM (evil-winrm) → flag 2 → Account Operators (usuario del chat) → búsqueda de delegación: checkservers.ps1 + hosts.txt (buse) → Abuso de la delegación → Admin del servidor/DC → flag 3`

**Learning chain:**

Enumeración de servicios Windows AD → Molestia de self-service password reset (pregunta de seguridad) → SMB share → Recon de aplicaciones de chat empresariales → CVE-2020-12772 (XSS/img en Spark) → Captura de credenciales con Responder (NetNTLMv2) → Cracking offline → Acceso WinRM → Enumeración de grupos privilegiados (Account Operators) → Abuso de cuentas delegadas/scripts de administración → Control de máquinas del dominio → flag final.

*Lección:* Un "chat de fotos de gatos" puede ser la puerta del dominio: las URLs no escapadas en el render de imágenes de Spark (CVE-2020-12772) convierten un cliente XMPP en una trampa de NetNTLMv2 para Responder. Después, una contraseña débil crackeada abre WinRM, y el grupo **Account Operators** — diseñado para "administrar un puñado de cuentas" — se convierte en la palanca final para tomar el DC si las cuentas delegadas están mal protegidas.

**MITRE ATT&CK:**

T1110 (Brute Force), T1040 (Network Sniffing), T1187 (Forced Authentication), T1078 (Valid Accounts), T1059.001 (PowerShell), T1068 (Exploitation for Privilege Escalation), T1484 (Domain Policy Modification)

**Fuente:** [TryHackMe - Ra](https://tryhackme.com/room/ra)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.