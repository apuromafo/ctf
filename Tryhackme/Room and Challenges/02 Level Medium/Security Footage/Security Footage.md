# Security Footage

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF (Forense de red / Blue Team) | securityfootage | https://tryhackme.com/room/securityfootage | 02 Level Medium | TryHackMe | Análisis de tráfico (Wireshark/tshark), flujo MJPEG, extracción de imágenes JPEG (carving), reconstrucción de vídeo con ffmpeg, automatización con Python, OCR (opcional) | Recuperación de la grabación de una cámara de seguridad difundida por HTTP y extracción del flag contenido en los fotogramas |

---

**Contexto:** La sala **Security Footage** es un CTF de **Blue Team** centrado en análisis de tráfico. Alguien entró en una oficina la noche anterior y destruyó los discos duros con las grabaciones de las cámaras; solo queda una captura de red (`security-footage-1648933966395.pcap`). En ella se observa una única conversación HTTP entre dos equipos (`192.168.1.100` y `10.0.2.15`) que transmite un **flujo MJPEG**: decenas de fotogramas JPEG (más de 500) que una cámara envía por HTTP sin cifrar. La tarea es extraer esas imágenes del pcap, convertirlas en un vídeo (o revisarlas) y localizar el fotograma donde se muestra el flag. Se fomenta la **automatización**: escribir scripts para el *carving* y el ensamblado del vídeo con `ffmpeg`.

## Solucionario

### Task 1: Recuperar la grabación y obtener el flag / Recover the footage and get the flag
**Explicación:** Se abre el pcap en Wireshark y se identifica la conversación HTTP única que contiene el flujo MJPEG (los paquetes con `frame.len > 10000` contienen imágenes JPEG completas, detectadas por sus magic bytes `FF D8 FF`). Hay dos caminos: exportar el stream TCP en bruto y partir las imágenes usando el BoundaryString multipart, o bien procesar el pcap por paquetes con un script. Con las imágenes extraídas se genera un vídeo con `ffmpeg` (o se revisan los fotogramas) y el flag aparece sobre una pantalla/letrero de uno de los fotogramas.

```python
# extractor.py: filtra los frames con imagen JPEG completa y los guarda a disco
import re, struct, os
import pyshark  # o scapy

def extract_images(filename):
    with open(filename, "rb") as f:
        content = f.read()
    parts = content.split(b"BOUNDARY")   # BoundaryString del flujo multipart
    n = 0
    for part in parts:
        if b"Content-type: image/jpeg" in part:
            m = re.search(b"Content-Length:\s*(\d+)", part)
            if not m: continue
            length = int(m.group(1))
            header_end = part.find(b"\r\n\r\n")
            img = part[header_end+4:header_end+4+length]
            if len(img) == length:
                with open(f"image_{n:03}.jpg", "wb") as out:
                    out.write(img)
                n += 1
extract_images("stream.raw")
```

```bash
# Convertir el flujo de imágenes a un vídeo
cat images/* | ffmpeg -framerate 30 -f image2pipe -i - -c:v libx264 -r 30 -pix_fmt yuv420p output.mp4
# Repasar el vídeo/fotogramas y leer el letrero -> flag
```

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | What is the flag? (Recover the footage) | `flag{5ebf457ea66b2877fdbca2de9ec86f31}` |

### Tabla unificada / Unified table

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag? (Recover the footage) | `flag{5ebf457ea66b2877fdbca2de9ec86f31}` |

---

**Metodología:** Análisis del pcap en Wireshark → identificación de la conversación HTTP con el flujo MJPEG → exportación del stream en bruto → extracción/carving de los fotogramas JPEG (script Python, binwalk o filtros por tamaño de frame) → ensamblado del vídeo con `ffmpeg` → revisión de los fotogramas y lectura del flag.

**Learning chain:** Reconocimiento del tráfico (conversación única, magic bytes JFIF) → exportación de objetos/streams en Wireshark → automatización del carving de imágenes → reconstrucción de vídeo → extracción del dato visible.

**Lección:** *Un flujo MJPEG o cualquier objeto transmitido por HTTP en claro puede extraerse y reconstruirse por completo: en incidentes, automatizar el volcado y ensamblado de artefactos (scripts + ffmpeg) permite recuperar la evidencia oculta en cientos de fotogramas.*

**MITRE ATT&CK:** T1071.001 Application Layer Protocol (HTTP) · T1039 Data from Network Shared Drive / T1105 Ingress Tool Transfer · T1557 Adversary-in-the-Middle (captura del stream) · T1027.012 Obfuscated Files or Information (dato embebido en el flujo).

**Fuente:** [TryHackMe - Security Footage](https://tryhackme.com/room/securityfootage)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.