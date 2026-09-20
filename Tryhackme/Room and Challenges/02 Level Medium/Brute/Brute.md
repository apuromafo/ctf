# Brute
| **Dificultad** | Medium |
| **Tipo** | CTF |
| **Slug** | `brute` |
| **Link** | [TryHackMe](https://tryhackme.com/room/brute) |
| **Sección** | Linux / CTF |
| **Fuente** | Research de thmrevenant (GitHub) y writeups de la comunidad |
| **Componentes** | Linux, SSH (22), Apache, hydra (brute force), log poisoning (User-Agent), LFI, command injection, webshell, subida de shell PHP, escalada de privilegios |
| **Impacto** | Máquina Linux Medium: la cadena pasa por el brute force de credenciales SSH con hydra, el envenenamiento de logs de Apache (User-Agent) para conseguir RCE, el user flag y la explotación de una inyección de comandos para obtener el root flag. |
---
**Contexto:** Sala CTF de dificultad media centrada en el ataque de fuerza bruta como punto de entrada. Tras obtener credenciales válidas, el siguiente paso es inyectar un payload en los logs de Apache (log poisoning a través del User-Agent) para convertirlos en una webshell, y finalmente abusar de una inyección de comandos mal filtrada para escalar a root y capturar ambos flags.
*EN: Medium CTF room focused on brute force as the initial entry point. After obtaining valid credentials, the next step is injecting a payload into Apache logs (log poisoning via the User-Agent) to turn them into a webshell, and finally abusing a poorly filtered command injection to escalate to root and capture both flags.*
## Solucionario
### Task 1 — Flags
**Explicación:** El objetivo de la sala es obtener dos flags. Recorrido habitual: `nmap` (22 SSH + 80 Apache) → enumeración (gobuster) → fuerza bruta de SSH con hydra para conseguir credenciales → inspección de la web y de los logs de Apache → log poisoning inyectando código PHP en el `User-Agent` → inclusión/ejecución del log como webshell → user flag → escalada por inyección de comandos en un script/panel con privilegios → root flag.
*EN: The goal is to grab two flags. Typical flow: `nmap` (22 SSH + 80 Apache) → enumeration (gobuster) → SSH brute force with hydra to get credentials → web and Apache log review → log poisoning by injecting PHP code into the `User-Agent` → include/execute the log as a webshell → user flag → privilege escalation via command injection in a privileged script/panel → root flag.*

```bash
nmap -sC -sV <target>
hydra -l <user> -P /usr/share/wordlists/rockyou.txt ssh://<target> -t 4
# Log poisoning vía User-Agent
curl -A "<?php system(\$_GET['cmd']); ?>" http://<target>/
http://<target>/<ruta_al_log>?cmd=id
```
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the user flag? | `THM{PoI$0n_tH@t_L0g}` |
| 2 | What is the root flag? | `THM{C0mm@nD_Inj3cT1on_4_D@_BruT3}` |
---
**Metodología:** Recon (nmap: SSH + Apache) → fuerza bruta con hydra (SSH) → reconocimiento web → log poisoning del User-Agent de Apache → webshell → user flag → inyección de comandos mal filtrada (sin sanitizar) → root flag.
**Learning chain:** brute force → abuso de logs de servidor web (inclusión de código en cabeceras) → RCE → inyección de comandos → compromiso total.
**Lección:** *Un fallo de fuerza bruta no termina en el acceso: los logs de Apache que reflejan cabeceras HTTP pueden convertirse en una webshell si introducimos código PHP, y una inyección de comandos no saneada cierra la cadena hasta root.*
**MITRE ATT&CK:** T1110 (Brute Force), T1505.003 (Web Shell), T1059.001/007 (PowerShell/JavaScript), T1203, T1068, T1105 (Ingress Tool Transfer).
**Fuente:** [TryHackMe - Brute](https://tryhackme.com/room/brute)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.