# Living Off the Land

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Walkthrough | livingofftheland | https://tryhackme.com/room/livingofftheland | Windows / Living Off the Land | TryHackMe | Pktmon.exe (T1127.001), AES/Base64 (OpenSSL), archivos cifrados, enumeración PowerShell | Droppers y ejecución living off the land |

---

**Contexto:** La sala **Living Off the Land** es un laboratorio de Windows centrado en el abuso de herramientas nativas del sistema (LOLBins): se trabaja con **Pktmon.exe** (proxy execution MITRE T1127.001) para ejecutar `.dll`, se crea un archivo cifrado en **AES** con Base64 usando las herramientas de vuelco de la máquina (p. ej. OpenSSL) y se descifra localmente para recuperar la flag, todo sin cargar binarios externos al host.

## Solucionario

### Task 1
**Explicación:**

Acceso inicial a la máquina Windows del laboratorio.

`No answer needed`

### Task 2
**Explicación:**

Preparación del entorno y comprobación de las herramientas nativas disponibles.

`No answer needed`

### Task 3
**Explicación:**

Identificación del binario nativo usado para ejecutar la DLL y de la técnica MITRE asociada; se confirma la acción permitida.

1. `Pktmon.exe`
2. `T1127.001`
3. `Execute`
4. `No answer needed`

### Task 4
**Explicación:**

Se crea el archivo cifrado en AES con Base64 mediante las utilidades del sistema y se recupera la flag al descifrarlo.

1. `enc_thm_0YmFiOG_file.txt`
2. `THM{ea4e2b9f362320d098635d4bab8a568e}`

### Task 5
**Explicación:**

Cuestionario sobre prevención del abuso de herramientas de confianza (least privilege en el sistema).

`No answer needed`

### Task 6
**Explicación:**

Cuestionario sobre detección del uso de binarios living off the land.

`No answer needed`

### Task 7
**Explicación:**

Flag final relacionada con la detección/monitorización de estos abusos.

`THM{23005dc4369a0eef728aa39ff8cc3be2}`

### Task 8
**Explicación:**

Cierre e integración de los conceptos teóricos de la sala.

`No answer needed`

### Task 9
**Explicación:**

Evaluación final de los conocimientos adquiridos.

`No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Task 1 - Respuesta | `No answer needed` |
| 2 | Task 2 - Respuesta | `No answer needed` |
| 3.1 | Task 3 - Respuesta 1 | `Pktmon.exe` |
| 3.2 | Task 3 - Respuesta 2 | `T1127.001` |
| 3.3 | Task 3 - Respuesta 3 | `Execute` |
| 3.4 | Task 3 - Respuesta 4 | `No answer needed` |
| 4.1 | Task 4 - Respuesta 1 | `enc_thm_0YmFiOG_file.txt` |
| 4.2 | Task 4 - Respuesta 2 | `THM{ea4e2b9f362320d098635d4bab8a568e}` |
| 5 | Task 5 - Respuesta | `No answer needed` |
| 6 | Task 6 - Respuesta | `No answer needed` |
| 7 | Task 7 - Respuesta | `THM{23005dc4369a0eef728aa39ff8cc3be2}` |
| 8 | Task 8 - Respuesta | `No answer needed` |
| 9 | Task 9 - Respuesta | `No answer needed` |

---

**Metodología:** Identificación del binario LOLBin (Pktmon.exe) y su técnica MITRE (T1127.001) → creación de un archivo cifrado con AES + Base64 usando utilidades nativas → descifrado local del archivo para obtener la flag → consolidación de detección y mitigación (least privilege, monitorización).

**Learning chain:** Pktmon.exe (T1127.001) → ejecución de DLL → cifrado AES/Base64 del archivo → descifrado y flag → mitigación/detección.

**Lección:** *Los atacantes "viven de la tierra" usando las propias herramientas del sistema (Pktmon) y de compresión/cifrado ya instaladas; defenderse exige observar el comportamiento y no solo el binario, aplicando least privilege y monitorizando la ejecución inusual de utilidades administrativas.*

**MITRE ATT&CK:** T1127.001 Trusted Developer Utilities Proxy Execution · T1036.005 Masquerading: Match Legitimate Name or Location · T1105 Ingress Tool Transfer · T1005 Data from Local System · T1027.004 Obfuscated Files or Information: Compile After Delivery.

**Fuente:** [TryHackMe - Living Off the Land](https://tryhackme.com/room/livingofftheland)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.