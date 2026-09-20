# MalBuster

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Malware / Análisis estático | malbuster | https://tryhackme.com/room/malbuster | 02 Level Medium | TryHackMe | Análisis estático de malware, PE, hashing, Detect It Easy, AV | Identificación y clasificación de una muestra troyana |

---

**Contexto:** La sala **MalBuster** es un laboratorio de **análisis estático de malware** en el que se examina una muestra ejecutable sin ejecutarla, usando inspección de cabeceras PE, generación de hashes, detección multi-antivirus, análisis de importaciones y strings. El objetivo es clasificar la muestra por familia y variante (TrickBot/Zloader), recuperar las flags repartidas por la máquina y relacionar el hallazgo con técnicas de MITRE ATT&CK.

## Solucionario

### Task 1: Configuración inicial
**Explicación:**

Presentación de la sala y despliegue de la máquina del laboratorio. No se requiere una respuesta concreta.

Respuesta: `No answer needed`

### Task 2: Análisis de la muestra
**Explicación:**

Se analiza la muestra maliciosa `7JYpE.exe` con herramientas estáticas. Se determina que el binario está compilado para **32-bit**, su hash **MD5** es `4348da65e4aeae6472c7f97d6dd8ad8f`, y las detecciones de antivirus lo clasifican como `trojan.zbot/razy` y `HEUR/AGEN.1306860`. La muestra importa `mscoree.dll`, su nombre de archivo original es `7JYpE.exe`, pertenece a la familia `TrickBot` y al loader `Zloader`. El stub DOS conserva el mensaje `!This Salfram cannot be run in DOS mode.`, se importa `shell32.dll`, el ejecutable tiene `3` secciones, la técnica MITRE asociada es `T1083` (File and Directory Discovery) y la recogida de flags entrega `malbuster_1`, `malbuster_2` y `malbuster_3`.

1. `32-bit`
2. `4348da65e4aeae6472c7f97d6dd8ad8f`
3. `trojan.zbot/razy`
4. `HEUR/AGEN.1306860`
5. `mscoree.dll`
6. `7JYpE.exe`
7. `TrickBot`
8. `Zloader`
9. `!This Salfram cannot be run in DOS mode.`
10. `shell32.dll`
11. `3`
12. `malbuster_3`
13. `T1083`
14. `malbuster_2`
15. `malbuster_1`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Configuración inicial del laboratorio | `No answer needed` |
| 2.1 | Arquitectura del binario | `32-bit` |
| 2.2 | Hash MD5 de la muestra | `4348da65e4aeae6472c7f97d6dd8ad8f` |
| 2.3 | Detección del primer antivirus | `trojan.zbot/razy` |
| 2.4 | Detección del segundo antivirus | `HEUR/AGEN.1306860` |
| 2.5 | DLL importada por la muestra | `mscoree.dll` |
| 2.6 | Nombre de archivo original | `7JYpE.exe` |
| 2.7 | Familia de malware | `TrickBot` |
| 2.8 | Variante / loader | `Zloader` |
| 2.9 | Mensaje del stub DOS | `!This Salfram cannot be run in DOS mode.` |
| 2.10 | DLL de shell importada | `shell32.dll` |
| 2.11 | Número de secciones del PE | `3` |
| 2.12 | Flag de root de la máquina | `malbuster_3` |
| 2.13 | Técnica MITRE ATT&CK del hallazgo | `T1083` |
| 2.14 | Flag de usuario de la máquina | `malbuster_2` |
| 2.15 | Primera flag de la máquina | `malbuster_1` |

---

**Metodología:** Análisis estático del binario: hash MD5, inspección de cabeceras PE, detección multi-AV, análisis de importaciones y strings, empaquetado y mapeo a MITRE ATT&CK.

**Learning chain:** Aprovisionamiento → hashing → fingerprint del binario → clasificación de familia/variante → recovery de flags → correlación MITRE.

**Lección:** *El análisis estático basta para clasificar una muestra troyana (bitness, hash, imports, detecciones) antes de ejecutarla; la recogida de flags del lab refuerza la gestión de evidencias.*

**MITRE ATT&CK:** T1083 File and Directory Discovery.

**Fuente:** [TryHackMe - MalBuster](https://tryhackme.com/room/malbuster)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.