# Windows Forensics 1

| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `windowsforensics1` |
| **Link** | [TryHackMe](https://tryhackme.com/room/windowsforensics1) |
| **Sección** | 02 Level Medium |
| **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | Windows forensics / Registry / Amcache / AppCompatCache / BAM/DAM / USB / Prefetch |
| **Impacto** | Analizar artefactos de Windows (Registry hives, Amcache, USB, Prefetch) para reconstruir actividad del sistema |

---

**Contexto:** Sala de forense de Windows 1: conocer el sistema operativo, los hives del registro, Amcache, AppCompatCache, BAM/DAM, dispositivo USB y Prefetch para reconstruir la actividad (instalación, ejecución, conexión de USBs).

## Solucionario

### Task 1: (SO / Operating System)

**Explicación:**

El sistema operativo del volcado/artefacto es `Microsoft Windows`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (OS) | `1. Microsoft Windows` |

### Task 2: (Hive del registro / Registry Hives)

**Explicación:**

El hive del registro que contiene la información del sistema/computadora es `HKLM` (HKEY_LOCAL_MACHINE).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Hive) | `1. HKLM` |

### Task 3: (Ubicación de hives / Hive Locations)

**Explicación:**

Las ubicaciones por defecto: la carpeta de los hives del sistema es `C:\Windows\System32\Config` y el archivo del hive Amcache es `C:\Windows\AppCompat\Programs\Amcache.hve`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Config folder) | `1. C:\Windows\System32\Config` |
| 2 | (Amcache.hve) | `2. C:\Windows\AppCompat\Programs\Amcache.hve` |

### Task 4: (Simulación / Simulation)

**Explicación:**

Simulación/práctica.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Simulation) | `No answer needed` |

### Task 5: (Simulación 2 / Simulation 2)

**Explicación:**

Simulación/práctica 2.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Simulation 2) | `No answer needed` |

### Task 6: (Imagen del sistema / System Image)

**Explicación:**

Imagen del sistema: el build number es `19044`; la versión de launch es `1`; el hostname es `THM-4n6`; la zona horaria es `Pakistan Standard Time`; la IP es `192.168.100.58`; y el RID del administrador es `501`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Build) | `1. 19044` |
| 2 | (Version) | `2. 1` |
| 3 | (Hostname) | `3. THM-4n6` |
| 4 | (Timezone) | `4. Pakistan Standard Time` |
| 5 | (IP) | `5. 192.168.100.58` |
| 6 | (RID) | `6. 501` |

### Task 7: (Actividad del sistema / System Activity)

**Explicación:**

Actividad del sistema: el primer boot es `2021-12-01 13:00:34`; el último shutdown es `2021-12-01 13:06:47`; la bandera de Ec2Config es `C:\Program Files\Amazon\Ec2ConfigService\Settings`; y el último boot es `2021-11-30 10:56:19`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (First boot) | `1. 2021-12-01 13:00:34` |
| 2 | (Last shutdown) | `2. 2021-12-01 13:06:47` |
| 3 | (Ec2Config flag) | `3. C:\Program Files\Amazon\Ec2ConfigService\Settings` |
| 4 | (Last boot) | `4. 2021-11-30 10:56:19` |

### Task 8: (Artefactos de ejecución / Execution Artifacts)

**Explicación:**

Artefactos de ejecución: el número de artefactos es `26`; los artefactos mencionados son `AppCompatCache`, `AmCache`, `BAM/DAM`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Count) | `1. 26` |
| 2 | (Artifact 1) | `2. AppCompatCache` |
| 3 | (Artifact 2) | `3. AmCache` |
| 4 | (Artifact 3) | `4. BAM/DAM` |

### Task 9: (Dispositivo USB / USB Devices)

**Explicación:**

El dispositivo USB: el ID del dispositivo es `1C6f654E59A3B0C179D366AE&0`; el nombre es `Kingston Data Traveler 2.0 USB Device`; y el tipo de conexión es `USB`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Device ID) | `1. 1C6f654E59A3B0C179D366AE&0` |
| 2 | (Device name) | `2. Kingston Data Traveler 2.0 USB Device` |
| 3 | (Connection type) | `3. USB` |

### Task 10: (Ejecución de archivos / File Execution)

**Explicación:**

Ejecución de archivos: el número de ejecuciones de `python-3.8.2.exe` es `3`; el usuario es `thm-user2`; el artefacto consultado es `count`; la primera ejecución es `2021-11-24 18:18:48`; la ruta es `Z:\setups\python-3.8.2.exe`; y la última ejecución es `2021-11-24 18:40:06`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Count) | `1. 3` |
| 2 | (User) | `2. thm-user2` |
| 3 | (Artifact) | `3. count` |
| 4 | (First exec) | `4. 2021-11-24 18:18:48` |
| 5 | (Path) | `5. Z:\setups\python-3.8.2.exe` |
| 6 | (Last exec) | `6. 2021-11-24 18:40:06` |

### Task 11: (Conclusión)

**Explicación:**

Conclusión.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Conclusión) | `No answer needed` |

---

**Metodología:**

1. Conocer el SO y los hives (HKLM, `C:\Windows\System32\Config`, Amcache.hve).
2. Reconstruir la imagen del sistema (build, hostname, timezone, IP, RID) y la actividad (boots, shutdowns).
3. Analizar artefactos de ejecución (AppCompatCache, AmCache, BAM/DAM) y el dispositivo USB.
4. Verificar la ejecución de archivos (python-3.8.2.exe) por usuario y ruta.

**Learning chain:** SO Microsoft Windows -> HKLM -> hives locations -> imagen (19044, THM-4n6, Pakistan) -> boots/shutdown -> AppCompatCache/AmCache/BAM-DAM -> USB Kingston -> python exec thm-user2

**Lección:** *Los hives del registro y los artefactos de ejecución (Amcache, AppCompatCache, BAM/DAM) junto con los contenedores USB permiten reconstruir la imagen del sistema y la actividad de usuarios sin depender de capturas en vivo.*

**MITRE ATT&CK:** T1082 (System Information Discovery) · T1555 (Credentials from Password Stores) · T1072 (Software Deployment Tools) · CWE-200 (Exposure of Sensitive Information)

**Fuente:** [TryHackMe - Windows Forensics 1](https://tryhackme.com/room/windowsforensics1)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
