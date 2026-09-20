# Scripting

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF / Scripting (Premium) | scripting | https://tryhackme.com/room/scripting | 02 Level Medium | TryHackMe | Bash y Python, base64 (decodificación en bucle), sockets TCP (port hopping con operaciones aritméticas), UDP, descifrado AES-GCM, hashes (checksum) | Un CTF de scripting en 3 niveles que ejercita automatización: decodificar texto ofuscado, resolver una cadena de cálculos en múltiples puertos y extraer un flag descifrando mensajes cifrados |

---

**Contexto:** La sala **Scripting** (del learning path hace parte del contenido Premium) enseña scripting con **Bash y Python** resolviendo tres retos. El primero (Easy - Base64) entrega un archivo codificado en base64 50 veces; hay que escribir un script que lo decodifique reiteradamente hasta obtener la cadena final. El segundo (Medium - Gotta Catch em All) pide conectarse a un servidor web en un puerto, realizar una operación aritmética sobre un número y saltar al siguiente puerto hasta llegar a un puerto final. El tercero (Hard - Encrypted Server Chit Chat) requiere comunicarse con un servidor UDP, descifrar los mensajes cifrados con **AES-GCM**, comparar el checksum de cada candidato y quedarse con el que coincide para obtener el flag final.

## Solucionario

### Task 1: [Fácil] Base64 / [Easy] Base64
**Explicación:** El archivo viene codificado en base64 50 veces. Solución en Bash y en Python: leer el contenido, aplicar la decodificación en un bucle de 50 iteraciones (usando una función) e imprimir el resultado final.

```bash
# Bash
b64decode() { echo -n "$1" | base64 -d; }
content=$(cat b64_1550406728131.txt)
for i in {1..50}; do content=$(b64decode "$content"); done
echo "$content"
```

```python
# Python
import base64
f = open("b64_1550406728131.txt")
read = f.read()
for i in range(50):
    read = base64.b64decode(read)
print(read.decode())
```

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | What is the final string? (Base64) | `HackBack2019=` |

### Task 2: [Medio] Gotta Catch em All / [Medium] Gotta Catch em All
**Explicación:** Hay que conectarse a un puerto (inicialmente 1337): si no responde, repetir hasta que esté vivo. Al obtener datos de la forma *operación, número, siguiente puerto* (formato legible con regex), se aplica la operación aritmética al número y se pasa al siguiente puerto. El proceso continúa hasta alcanzar el puerto final (~9867), momento en el que se muestra la respuesta acumulada.

```python
# Python (con sockets + regex)
import socket, re
op_re = re.compile(r'([a-z]{3,})\s(-?[0-9]+\.?[0-9]*)\s([0-9]+)')
answer = 0
port = 1337
while port != 9867:
    try:
        s = socket.create_connection(("10.10.x.x", port), timeout=3)
        data = s.recv(1024).decode()
        op, num, nxt = op_re.search(data).groups()
        num = float(num); answer = answer op num   # aplicar +,-,*,/
        port = int(nxt)
        s.close()
    except Exception:
        pass
print(answer)
```

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | What is the final answer after completing the arithmetic chain? | `344769.12` |

### Task 3: [Difícil] Servidor cifrado / [Hard] Encrypted Server Chit Chat
**Explicación:** Se conecta por **UDP** al puerto 4000 y se envía "hello". El servidor responde con la clave (key), el IV y el checksum objetivo. Después se reciben textos cifrados y *tags* de **AES-GCM**: para cada candidato se descifra, se calcula el hash del texto plano y se compara con el checksum dado; se repite hasta encontrar la bandera cuyo hash coincide.

```python
# Esquema: UDP -> recoger key/IV/checksum -> descifrar AES-GCM -> comparar digest
import socket, hashlib
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(2)
s.sendto(b"hello", ("10.10.x.x", 4000))
key, iv = ..., ...            # proporcionados por el servidor
target = "checksum_dado"
aes = AESGCM(key)
while True:
    data, _ = s.recvfrom(4096)
    plain = aes.decrypt(iv, data, None)
    if hashlib.sha256(plain).hexdigest() == target:
        print(plain.decode()); break
```

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | What is the flag? (Encrypted Server Chit Chat) | `THM{eW-sCrIpTiNg-AnD-cRyPtO}` |

### Tabla unificada / Unified table

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the final string? (Base64) | `HackBack2019=` |
| 2 | What is the final answer after completing the arithmetic chain? | `344769.12` |
| 3 | What is the flag? (Encrypted Server Chit Chat) | `THM{eW-sCrIpTiNg-AnD-cRyPtO}` |

---

**Metodología:** Reto 1: decodificación iterativa de base64 con funciones y bucles en Bash/Python. Reto 2: automatización con sockets TCP, regex para extraer operación/número/puerto y salto de puertos hasta el destino. Reto 3: comunicación UDP, extracción de key/IV/checksum, descifrado AES-GCM de cada mensaje y comparación de hashes para identificar el flag correcto.

**Learning chain:** Manipulación de archivos y funciones en Bash/Python → descodificación en bucle → programación de sockets (TCP) con reintentos → parsing con regex → operaciones aritméticas encadenadas entre puertos → sockets UDP → criptografía (AES-GCM) y validación por checksum → flag.

**Lección:** *Automatizar tareas repetitivas (decodificar, conectar puerto a puerto, descifrar candidatos) es una habilidad esencial en ciberseguridad: un bucle bien diseñado resuelve en segundos lo que a mano llevaría horas.*

**MITRE ATT&CK:** T1059.004 Command and Scripting Interpreter (Unix Shell) · T1059.006 Command and Scripting Interpreter (Python) · T1140 Deobfuscate/Decode Files or Information · T1027 Obfuscated Files or Information (doble codificación) · T1105 Ingress Tool Transfer / exfiltración de datos a través de múltiples canales.

**Fuente:** [TryHackMe - Scripting](https://tryhackme.com/room/scripting)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.