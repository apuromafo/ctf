# PrintNightmare, again!

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | ctf | `printnightmareagain` | [TryHackMe](https://tryhackme.com/room/printnightmareagain) | 01 Level Easy | THM | PrintNightmare CVE-2021-1675, Cola de impresión, DLL maliciosa, Registro de Windows, Limpieza | Explotación de la vulnerabilidad PrintNightmare |

---

**Contexto:** Laboratorio casi real que reproduce la explotación de PrintNightmare (CVE-2021-1675): se descarga el PoC (levelup.zip), se configura el listener, se ejecuta el exploit que sube una DLL maliciosa (nightmare.dll) a la cola de impresión, se crea el driver en el registro de Windows y se establece una conexión de retorno para acceder a la máquina como el usuario comprometido. Finalmente, se realiza la limpieza de los artefactos.

> **ES:** Explota la vulnerabilidad PrintNightmare (CVE-2021-1675) en Windows: sube una DLL maliciosa a la cola de impresión, crea el driver en el registro y obtiene una conexión de retorno a la víctima.
> **EN:** Exploit the PrintNightmare vulnerability (CVE-2021-1675) on Windows: upload a malicious DLL to the print spooler, create the driver in the registry and get a callback to the victim.

## Solucionario

### Task 1: Explotación de PrintNightmare / PrintNightmare Exploitation

**Explicación:** Reproduce el ataque PrintNightmare: descarga del PoC oficial (levelup.zip), ejecución del script CVE-2021-1675.ps1 que sube la DLL maliciosa nightmare.dll a la cola de impresión (C:\Users\bmurphy\AppData\Local\Temp\3\nightmare.dll), instalación final en System32 (C:\Windows\system32\spool\DRIVERS\x64\3\nightmare.dll), creación de la clave de registro THMPrinter en la rama de drivers de impresión, conexión del callback en el puerto 2600 y acceso con el usuario backup. Al terminar se ejecutan los comandos de limpieza (rmdir/del) para borrar los artefactos.

1. 1. levelup.zip
   2. C:\Users\bmurphy\Downloads\CVE-2021-1675-main\CVE-2021-1675.ps1
   3. C:\Users\bmurphy\AppData\Local\Temp\3\nightmare.dll
   4. C:\Windows\system32\spool\DRIVERS\x64\3\nightmare.dll
   5. HKLM\System\CurrentControlSet\Control\Print\Environments\Windows x64\Drivers\Version-3\THMPrinter\
   6. 2600
   7. backup
   8. ucGGDMyFHkqMRWwHtQ
   9. rmdir .\CVE-2021-1675-main\,del .\levelup.zip

| Pregunta | Respuesta |
|---|---|
| ¿Cuál es el archivo ZIP que se descarga con el PoC? | `levelup.zip` |
| ¿Cuál es la ruta del script CVE-2021-1675.ps1 descargado? | `C:\Users\bmurphy\Downloads\CVE-2021-1675-main\CVE-2021-1675.ps1` |
| ¿Cuál es la ruta temporal donde se sube la DLL nightmare.dll? | `C:\Users\bmurphy\AppData\Local\Temp\3\nightmare.dll` |
| ¿Cuál es la ruta final de la DLL en System32? | `C:\Windows\system32\spool\DRIVERS\x64\3\nightmare.dll` |
| ¿Qué clave de registro crea el driver de impresión THMPrinter? | `HKLM\System\CurrentControlSet\Control\Print\Environments\Windows x64\Drivers\Version-3\THMPrinter\` |
| ¿Qué puerto de escucha (LPORT) usa el callback? | `2600` |
| ¿Con qué usuario se accede a la máquina? | `backup` |
| ¿Cuál es la contraseña de la cuenta backup? | `ucGGDMyFHkqMRWwHtQ` |
| ¿Qué comandos limpian los archivos del PoC? | `rmdir .\CVE-2021-1675-main\,del .\levelup.zip` |

---

**Metodología:** Descarga del PoC públicamente disponible (CVE-2021-1675), preparación de la DLL maliciosa y del listener, ejecución del exploit contra la cola de impresión de Windows, verificación de la DLL instalada y de la clave de registro del driver, conexión del callback y limpieza de artefactos.

### Cadena de ataque / Attack Chain
Descarga del PoC (levelup.zip) -> Ejecución del script CVE-2021-1675.ps1 -> Subida de la DLL maliciosa a la cola de impresión (Temp) -> Instalación de la DLL en System32\spool\DRIVERS -> Creación del driver THMPrinter en el registro -> Petición del callback al puerto 2600 -> Acceso a la máquina con el usuario backup -> Limpieza de artefactos (rmdir y del).

**Learning chain:** Vulnerabilidad PrintNightmare (CVE-2021-1675), puntos de subida del spooler de impresión, claves de registro de drivers de impresión y buenas prácticas de limpieza tras un test.

**Lección:** *Un spooler de impresión no actualizado permite ejecutar DLLs arbitrarias en el host vía el directorio de drivers: la gestión de parches y el endurecimiento de la cola de impresión son imprescindibles.*

**MITRE ATT&CK:** T1543.003 Create or Modify System Process (Windows Service), T1569.002 System Services (Service Execution), T1134 Access Token Manipulation, T1505 Server Software Component (DLL), y la técnica afín T1211 Exploitation for Defense Evasion; CVE-2021-1675 (LPE/RCE) mapea también a T1068 Exploitation for Privilege Escalation.

**Fuente:** [TryHackMe - PrintNightmare, again!](https://tryhackme.com/room/printnightmareagain)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.