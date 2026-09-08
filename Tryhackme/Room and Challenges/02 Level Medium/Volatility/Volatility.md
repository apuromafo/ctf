# Volatility

| **Dificultad** | Medium |
| **Tipo** | CTF |
| **Slug** | `volatility` |
| **Link** | [TryHackMe](https://tryhackme.com/room/volatility) |
| **Sección** | 02 Level Medium |
| **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | Volatility / memory forensics / WannaCry / processes / DLLs / mutex / filescan |
| **Impacto** | Analizar un memory dump de una máquina infectada con WannaCry usando Volatility (imagen, procesos, DLL, mutex, archivos) |

---

**Contexto:** Sala de forense de memoria con Volatility 3 sobre un dump infectado: determinar la imagen/versión del sistema, fecha de adquisición, procesos (reader_sl.exe, explorer.exe), DLLs, el mutex de WannaCry, y localizar el ejecutable malicioso.

## Solucionario

### Task 1 a 5: (Acceso y setup)

**Explicación:**

Acceso a la sala y preparación de la máquina virtual.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Task 1) | `No answer needed` |
| 2 | (Task 2) | `No answer needed` |
| 3 | (Task 3) | `No answer needed` |
| 4 | (Task 4) | `No answer needed` |
| 5 | (Task 5) | `No answer needed` |

### Task 6: (Comandos Generales / Volatility 3)

**Explicación:**

Uso de los comandos generales de Volatility 3.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Volatility 3 - 1) | `1. No answer needed` |
| 2 | (Volatility 3 - 2) | `2. No answer needed` |

### Task 7: (Imagen de Perfil / Profile Image)

**Explicación:**

Imagen de perfil (detectar la versión del sistema).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Image info) | `No answer needed` |

### Task 8: (Procesos y DLL / ImageInfo, pslist, dlllist via MD5)

**Explicación:**

Procesos y bibliotecas del volcado. Usando `windows.info`, `windows.pslist` y `windows.dlllist`: la versión de build/SP es `2600.xpsp.080413-2111`; la fecha de adquisición es `2012-07-22 02:45:08`; el proceso `reader_sl.exe` está en la lista; el proceso padre es `explorer.exe`; el PID de reader_sl.exe es `1640`; el PID de explorer.exe es `1484`; el UserAgent (de la metadata) es `Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)`; el valor de "Y" indica un proceso verde/verificación; el mutex de WannaCry es `@WanaDecryptor@`; la ruta completa del ejecutable es `C:\Intel\ivecuqmanpnirkt615\@WanaDecryptor@.exe`; el proceso tasksche.exe tiene PID `1940`; el malware es `Wannacry`; la DLL cargada es `Ws2_32.dll`; el mutex es `MsWinZonesCacheCounterMutexA`; y el plugin para listar archivos es `windows.filescan`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Build version) | `1. 2600.xpsp.080413-2111` |
| 2 | (Acquisition date) | `2. 2012-07-22 02:45:08` |
| 3 | (Process 1) | `3. reader_sl.exe` |
| 4 | (Process 2) | `4. explorer.exe` |
| 5 | (PID 1) | `5. 1640` |
| 6 | (PID 2) | `6. 1484` |
| 7 | (UserAgent) | `7. Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)` |
| 8 | (Y/N) | `8. Y` |
| 9 | (Mutex) | `9. @WanaDecryptor@` |
| 10 | (Executable path) | `10. C:\Intel\ivecuqmanpnirkt615\@WanaDecryptor@.exe` |
| 11 | (Process 3) | `11. tasksche.exe` |
| 12 | (PID 3) | `12. 1940` |
| 13 | (Malware) | `13. Wannacry` |
| 14 | (DLL) | `14. Ws2_32.dll` |
| 15 | (Mutex 2) | `15. MsWinZonesCacheCounterMutexA` |
| 16 | (Filescan plugin) | `16. windows.filescan` |

### Task 9: (Conclusión)

**Explicación:**

Conclusión.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Conclusión) | `No answer needed` |

---

**Metodología:**

1. Usar `windows.info` para conocer la versión de build y la fecha de adquisición del volcado.
2. Usar `windows.pslist` para listar procesos y correlacionar PIDs/padres (reader_sl.exe 1640, explorer.exe 1484, tasksche.exe 1940).
3. Usar `windows.dlllist` para ver las DLL cargadas (Ws2_32.dll).
4. Buscar el mutex de WannaCry (`@WanaDecryptor@`, `MsWinZonesCacheCounterMutexA`) y localizar el ejecutable malicioso con `windows.filescan`.

**Learning chain:** windows.info -> build 2600.xpsp -> fecha 2012-07-22 -> pslist -> reader_sl.exe 1640 -> explorer.exe 1484 -> tasksche.exe 1940 -> dlllist -> Ws2_32.dll -> mutex @WanaDecryptor@ / MsWinZonesCacheCounterMutexA -> filescan -> C:\Intel\...\@WanaDecryptor@.exe -> WannaCry

**Lección:** *Identificar el malware (WannaCry) en un memory dump pasa por correlacionar varios plugins de Volatility: imagen (windows.info), procesos (pslist), DLL (dlllist), mutex y archivos (filescan); el mutex peculiar y la ruta de ejecución delatan el ransomware sin necesidad de YARA.*

**MITRE ATT&CK:** T1486 (Data Encrypted for Impact) · T1059 (Command and Scripting Interpreter) · T1105 (Ingress Tool Transfer) · CWE-829 (Inclusion of Functionality from Untrusted Control Sphere)

**Fuente:** [TryHackMe - Volatility](https://tryhackme.com/room/volatility)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
