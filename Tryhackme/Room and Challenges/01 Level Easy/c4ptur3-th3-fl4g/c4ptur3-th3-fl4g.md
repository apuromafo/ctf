# c4ptur3-th3-fl4g

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `c4ptur3th3fl4g` | [TryHackMe](https://tryhackme.com/room/c4ptur3th3fl4g) | 01 Level Easy | THM | Decodificación (leet, binario, base32, base64, hex, ROT13, ROT47, Morse, BCD), espectrogramas, esteganografía | Introductorio |

---

**Contexto:** Room introductoria de criptografía y decodificación tipo CTF. A lo largo de 4 tareas se practican la traducción y el descifrado de mensajes codificados (leet, binario, base32, base64, hexadecimal, ROT13, ROT47, código Morse, BCD y un encadenado de técnicas), el análisis de espectrogramas de audio, la esteganografía básica y la extracción de archivos ocultos basada en la seguridad por oscuridad.

> **ES:** 4 tareas y 15 flags consistentes en frases en claro: descifrar cadenas codificadas (leet, binario, base32, base64, hex, ROT13, ROT47, Morse, BCD y multicapa), localizar el texto en el espectrograma de un .wav, aplicar esteganografía y extraer archivos ocultos de un binario con binwalk, strings y herramientas online.

> **EN:** 4 tasks and 15 flags that are plaintext phrases: decode encoded strings (leet, binary, base32, base64, hex, ROT13, ROT47, Morse, BCD and multi-layer), find the text in the spectrogram of a .wav, use steganography and extract hidden files from a binary with binwalk, strings and online tools.

## Solucionario

### Task 1: Translation & Shifting / Traducción y Desplazamiento

**Explicación:** La tarea propone 10 mensajes codificados con técnicas distintas (leet, binario, base32, base64, hexadecimal, ROT13, ROT47, código Morse, BCD y una cadena multicapa). Con herramientas como CyberChef se descifran capa a capa hasta obtener las frases en claro finales.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Decodifica el mensaje en leet speak | `can you capture the flag?` |
| 2 | Decodifica el mensaje en binario | `lets try some binary out!` |
| 3 | Decodifica el mensaje en base32 | `base32 is super common in CTF's` |
| 4 | Decodifica el mensaje en base64 | `Each Base64 digit represents exactly 6 bits of data.` |
| 5 | Decodifica el mensaje hexadecimal (base16) | `hexadecimal or base16?` |
| 6 | Aplica ROT13 al mensaje | `Rotate me 13 places!` |
| 7 | Aplica ROT47 al mensaje | `You spin me right round baby right round (47 times)` |
| 8 | Decodifica el mensaje en código Morse | `telecommunication encoding` |
| 9 | Decodifica el mensaje en BCD | `Unpack this BCD` |
| 10 | Decodifica la cadena multicapa | `Let's make this a bit trickier...` |

### Task 2: Spectrograms / Espectrogramas

**Explicación:** Se proporciona un archivo de audio (.wav) cuyo texto oculto se hace visible analizando su espectrograma con una herramienta de análisis espectral.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | ¿Qué mensaje revela el espectrograma del archivo de audio? / What is the flag in the spectrogram? | `Super Secret Message` |

### Task 3: Steganography / Esteganografía

**Explicación:** Tarea centrada en recuperar el dato oculto mediante técnicas de esteganografía aplicadas sobre el archivo aportado en la room.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | ¿Qué mensaje se recupera con la esteganografía? / What is the hidden message? | `SpaghettiSteg` |

### Task 4: Security Through Obscurity / Seguridad por oscuridad

**Explicación:** Un archivo descargado esconde en su interior (magic bytes) un contenido extraíble con binwalk. Tras abrir el .7z se obtiene hackerchat.png y, inspeccionando el archivo e investigando su sección PCRT (Pareto Check & Repair Tool), se descubre el texto oculto.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Descarga el archivo y entra en él. ¿Cuál es el primer nombre de archivo y su extensión? | `hackerchat.png` |
| 2 | Entra en el archivo e inspecciónalo con cuidado. Encuentra el texto oculto. | `AHH_YOU_FOUND_ME!` |

---

**Metodología:** Identificación del tipo de encoding por su apariencia → decodificación con CyberChef (leet, binario, base32, base64, hex, ROT13, ROT47, Morse, BCD y multicapa) → análisis del espectrograma del .wav → esteganografía → binwalk sobre el archivo → extracción del contenido → strings/PCRT → recuperación del texto oculto.

### Cadena de ataque / Attack Chain

Descifrado de cadenas codificadas → espectrograma del audio → esteganografía → extracción del contenido del binario → obtención de los 15 flags.

**Learning chain:** Leet speak → binario → base32 → base64 → hexadecimal → ROT13 → ROT47 → Morse → BCD → encadenado de técnicas → espectrogramas → esteganografía → binwalk/PCRT → la oscuridad como ocultación.

**Lección:** *Los mensajes "ocultos" casi nunca están realmente ocultos: una cadena legible de caracteres, un audio y un binario esconden la información en capas que se identifican por su firma y se decodifican con las herramientas adecuadas.*

**MITRE ATT&CK:** T1132 (Data Encoding), T1027 (Obfuscated Files or Information) — contexto académico/CTF.

**Fuente:** [TryHackMe - c4ptur3-th3-fl4g](https://tryhackme.com/room/c4ptur3th3fl4g)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.