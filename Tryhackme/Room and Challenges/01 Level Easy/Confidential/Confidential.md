# Confidential

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | reto de OSINT/estego | `confidential` | https://tryhackme.com/room/confidential | 01 Level Easy | TryHackMe | PDF / páginas de texto / QR code / docx / estego (información oculta) | Descubrir la flag oculta detrás de una imagen que cubre un código QR dentro de un documento PDF. |

---

**Contexto:** Reto que mezcla OSINT/estego: se descarga un fichero de la tarea que hay que analizar, identificando información oculta (metadatos, descriptores DeletedText, etc.) para dar con un PDF que contiene una imagen cuadrada "sospechosa" sobre un documento, y detrás de ella un código QR. Escaneando el QR se obtiene la flag.

> **ES:** Traduce una frase sobre el propio reto (que empieza con un carácter Unicode oculto tipo `\u200b`), analiza el documento y localiza el PDF con un QR oculto detrás de una imagen; escanéalo para obtener la flag.
> **EN:** Translate a sentence about the challenge itself (which starts with a hidden Unicode character), analyze the document and find the PDF with a QR code hidden behind an image; scan it to obtain the flag.

## Solucionario

### Task 1: Descubre la flag / Discover the flag

**Explicación:** En la descripción de la tarea hay una frase que empieza con un carácter Unicode invisible (`\u200b`); al traducirla, la frase es el propio texto de la tarea. En el fichero `Confidential.docx` se encuentra una frase (una pista) y la referencia "Microsoft.github.io", que enlaza con un PDF. Dentro del PDF hay una imagen cuadrada sospechosa puesta encima del documento; se extrae con una herramienta de dibujo o `pdfimages` (por ejemplo, abriendo el PDF con LibreOffice Draw y borrando la imagen o arrastrándola) y debajo aparece un código QR. Al escanearlo se obtiene la flag `flag{e08e6ce2f077a1b420cfd4a5d1a57a8d}`.

```bash
unzip Confidential.docx                 # explorar document.xml, word/media, etc.
strings -e l Confidential.docx          # notar textos ocultos/pistas
# Encontrar la referencia al PDF (Microsoft.github.io) y descargarlo
pdfimages -png Confidential.pdf qr      # extraer las imágenes -> qr-000.png
# o abrir el PDF con LibreOffice Draw y apartar la imagen cuadrada
# Escanear el QR -> flag
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Descubre y escanea el QR para obtener la flag. / Uncover and scan the QR code to retrieve the flag. | `flag{e08e6ce2f077a1b420cfd4a5d1a57a8d}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Descubre y escanea el QR para obtener la flag. / Uncover and scan the QR code to retrieve the flag. | `flag{e08e6ce2f077a1b420cfd4a5d1a57a8d}` |

---

**Metodología:** Analizar los ficheros del paquete docx (sus contenidos y pistas), seguir las referencias hasta el PDF, extraer las imágenes incrustadas (`pdfimages` o LibreOffice Draw), apartar la imagen que cubre el documento y escanear el código QR resultante para obtener la flag.

### Cadena de ataque / Attack Chain

```text
Confidential.docx -> pistas en descriptores/textos -> referencia PDF (Microsoft.github.io) -> QR oculto detrás de una imagen -> extraer imágenes -> escanear QR -> flag
```

**Learning chain:** Reconocimiento de tipos de fichero -> docx/internals -> OSINT/referencias -> PDF -> pdfimages/LibreOffice Draw -> decodificación QR.

**Lección:** *La información sensible puede esconderse en los tipos de documento más comunes (docx, PDF) aprovechando artefactos simples como imágenes superpuestas o textos invisibles; siempre merece la pena inspeccionar los ficheros de un documento y extraer sus imágenes.*

**MITRE ATT&CK:** N/A (reto OSINT/estego con documentación pública)

**Fuente:** [TryHackMe - Confidential](https://tryhackme.com/room/confidential)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.