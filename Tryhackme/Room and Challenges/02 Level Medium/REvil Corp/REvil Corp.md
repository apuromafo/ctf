# REvil Corp

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF / DFIR (Ransomware) | revilcorp | https://tryhackme.com/room/revilcorp | 02 Level Medium | TryHackMe | Mandiant Redline, análisis forense de una imagen de host Windows, ransomware REvil/Sodinokibi, indicadores de compromiso (IoC), reconstrucción de línea de tiempo | Compromiso total de una estación de trabajo Windows por ransomware: cifrado de 48 archivos, modificación del escritorio, nota de rescate y contacto con el portal de descifrado del atacante |

---

**Contexto:** La sala **REvil Corp** es un ejercicio de **respuesta a incidentes basado en forense**: se dispone de una imagen forense de una estación de trabajo Windows comprometida y se analiza con **Mandiant Redline** para reconstruir la cadena completa del ataque del ransomware **REvil/Sodinokibi**. Siguiendo las pestañas de Redline (información del sistema, historial de descargas, sistema de archivos, proceso de establecimiento de artefactos) se identifican el empleado afectado, el sistema operativo, el binario malicioso (`WinRAR2021.exe`) y su URL de origen. Después se determinan los efectos del cifrado: extensión de los archivos renombrados, número de archivos afectados, wallpaper reemplazado, nota de rescate, carpeta de enlaces modificada y archivo oculto de 0 bytes. Finalmente se recogen los indicadores de compromiso: hash MD5 del binario y del descargador, la URL de descifrado y los tres nombres asociados a la familia del malware.

## Solucionario

### Task 1: Investigación del host infectado / Investigating the infected host
**Explicación:** La investigación sigue el flujo de un triaje forense con Redline sobre la imagen del host comprometido. En `System Information` se obtiene el usuario logueado (`John Coleman`) y la versión completa del sistema operativo. En la pestaña de descargas del navegador se encuentra el binario que actuó como payload inicial (`WinRAR2021.exe`) y la URL completa de descarga. Consultando la pestaña `File System` se calcula el hash MD5 del binario y su tamaño, la extensión con la que se renombraron los archivos (`.t48s39la`), el número de archivos cifrados, la ruta del wallpaper reemplazado por el atacante, la nota de rescate del escritorio, el archivo dejado en la carpeta "Links for United States" y el archivo oculto de 0 bytes (`d60dff40.lock`). Después se identifica el descargador que el usuario ejecutó intentando recuperar sus datos y su hash MD5. Por último, la nota de rescate apunta a la URL de descifrado gratuito y permite atribuir el incidente a la familia **REvil (Sodinokibi)** con sus tres nombres asociados.

```text
Infección: John Coleman descarga WinRAR2021.exe desde http://192.168.75.129:4748/Documents/WinRAR2021.exe
    -> ejecución del payload -> cifrado de 48 archivos con extensión .t48s39la
    -> cambio de wallpaper (hk8.bmp), nota de rescate (t48s39la-readme.txt) y archivos ocultos (.lock)
    -> la víctima descarga un "decryptor" (hash f617af8c0d276682fdf528bb3e72560b) desde http://decryptor.top/644E7C8EFA02FBB7
    -> atribución: REvil / Sodin / Sodinokibi
```

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | What is the compromised employee's full name? | `John Coleman` |
| 2 | What is the operating system of the compromised host? | `Windows 7 Home Premium 7601 Service Pack 1` |
| 3 | What is the name of the malicious executable that the user opened? | `WinRAR2021.exe` |
| 4 | What is the full URL that the user visited to download the malicious binary? (include the binary as well) | `http://192.168.75.129:4748/Documents/WinRAR2021.exe` |
| 5 | What is the MD5 hash of the binary? | `890a58f200dfff23165df9e1b088e58f` |
| 6 | What is the size of the binary in kilobytes? | `164` |
| 7 | What is the extension to which the user's files got renamed? | `.t48s39la` |
| 8 | What is the number of files that got renamed and changed to that extension? | `48` |
| 9 | What is the full path to the wallpaper that got changed by an attacker, including the image name? | `C:\Users\John Coleman\AppData\Local\Temp\hk8.bmp` |
| 10 | The attacker left a note for the user on the Desktop; provide the name of the note with the extension. | `t48s39la-readme.txt` |
| 11 | The attacker created a folder "Links for United States" under C:\Users\John Coleman\Favorites\ and left a file there. Provide the name of the file. | `GobiernoUSA.gov.url.t48s39la` |
| 12 | There is a hidden file that was created on the user's Desktop that has 0 bytes. Provide the name of the hidden file. | `d60dff40.lock` |
| 13 | The user downloaded a decryptor hoping to decrypt all the files, but he failed. Provide the MD5 hash of the decryptor file. | `f617af8c0d276682fdf528bb3e72560b` |
| 14 | In the ransomware note, the attacker provided a URL that is accessible through the normal browser in order to decrypt one of the encrypted files for free. The user attempted to visit it. Provide the full URL path. | `http://decryptor.top/644E7C8EFA02FBB7` |
| 15 | What are some three names associated with the malware which infected this host? (enter the names in alphabetical order) | `REvil,Sodin,Sodinokibi` |

### Tabla unificada / Unified table

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the compromised employee's full name? | `John Coleman` |
| 2 | What is the operating system of the compromised host? | `Windows 7 Home Premium 7601 Service Pack 1` |
| 3 | What is the name of the malicious executable that the user opened? | `WinRAR2021.exe` |
| 4 | What is the full URL that the user visited to download the malicious binary? (include the binary as well) | `http://192.168.75.129:4748/Documents/WinRAR2021.exe` |
| 5 | What is the MD5 hash of the binary? | `890a58f200dfff23165df9e1b088e58f` |
| 6 | What is the size of the binary in kilobytes? | `164` |
| 7 | What is the extension to which the user's files got renamed? | `.t48s39la` |
| 8 | What is the number of files that got renamed and changed to that extension? | `48` |
| 9 | What is the full path to the wallpaper that got changed by an attacker, including the image name? | `C:\Users\John Coleman\AppData\Local\Temp\hk8.bmp` |
| 10 | The attacker left a note for the user on the Desktop; provide the name of the note with the extension. | `t48s39la-readme.txt` |
| 11 | The attacker created a folder "Links for United States" under C:\Users\John Coleman\Favorites\ and left a file there. Provide the name of the file. | `GobiernoUSA.gov.url.t48s39la` |
| 12 | There is a hidden file that was created on the user's Desktop that has 0 bytes. Provide the name of the hidden file. | `d60dff40.lock` |
| 13 | The user downloaded a decryptor hoping to decrypt all the files, but he failed. Provide the MD5 hash of the decryptor file. | `f617af8c0d276682fdf528bb3e72560b` |
| 14 | In the ransomware note, the attacker provided a URL that is accessible through the normal browser in order to decrypt one of the encrypted files for free. The user attempted to visit it. Provide the full URL path. | `http://decryptor.top/644E7C8EFA02FBB7` |
| 15 | What are some three names associated with the malware which infected this host? (enter the names in alphabetical order) | `REvil,Sodin,Sodinokibi` |

---

**Metodología:** Triage forense con Mandiant Redline sobre la imagen de un host Windows: extracción de la información del sistema y del usuario, análisis del historial de descargas del navegador, revisión del sistema de archivos para localizar artefactos, cálculo de hashes MD5, identificación de la nota de rescate y de la URL de descifrado, y atribución final de la familia de ransomware.

**Learning chain:** Recolección de evidencia (imagen forense) → perfilado del host y del usuario → identificación del payload y su vector de entrega → efectos del ransomware (cifrado/escritorio/nota) → artefactos de persistencia y ocultamiento → descargador del atacante y portal de rescate → atribución a REvil/Sodinokibi.

**Lección:** *La reconstrucción de un incidente de ransomware se apoya en artefactos del sistema y del navegador: el payload, su origen, los efectos del cifrado y la nota de rescate forman una línea de tiempo que permite atribuir el ataque a una familia concreta.*

**MITRE ATT&CK:** T1204.001 User Execution (Malicious Link) · T1059.003 Command and Scripting Interpreter (Windows Command Shell) · T1486 Data Encrypted for Impact · T1491.001 Defacement (Internal) · T1565.001 Data Manipulation (Stored) · T1185 Browser Session Hijacking/artefactos de navegador.

**Fuente:** [TryHackMe - REvil Corp](https://tryhackme.com/room/revilcorp)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.