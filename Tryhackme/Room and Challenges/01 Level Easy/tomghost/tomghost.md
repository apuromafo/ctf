# tomghost

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `tomghost` | [TryHackMe - tomghost](https://tryhackme.com/room/tomghost) | 01 Level Easy | THM | Apache Tomcat, GhostCat, CVE-2020-1938, ZIP | RCE mediante GhostCat y análisis de la flag |

---

**Contexto:** Máquina CTF que explota GhostCat (CVE-2020-1938), la vulnerabilidad de Apache Tomcat que permite leer archivos o ejecutar el JSP vía el protocolo AJP, y finaliza con el análisis de un archivo ZIP protegido.

> **ES:** La máquina se compromete explotando la vulnerabilidad GhostCat (CVE-2020-1938) del protocolo AJP de Tomcat para leer el `WEB-INF/web.xml`, obtener credenciales y culminar con un ZIP con otra flag.
> **EN:** The box is compromised by exploiting Tomcat's GhostCat (CVE-2020-1938) AJP vulnerability to read `WEB-INF/web.xml`, obtain credentials and finally crack a ZIP holding another flag.

## Solucionario

### Task 1: Banderas / Flags

**Explicación:** La primera flag se obtiene tras explotar GhostCat y conseguir acceso; la segunda requiere obtener una credencial de descifrado de un archivo ZIP.

1. 1. THM{GhostCat_1s_so_cr4sy}
   2. THM{Z1P_1S_FAKE}

### Tabla unificada de preguntas / Unified Q&A

| # | Pregunta / Question | Respuesta / Answer |
|---|---|---|
| 1 | User flag | `THM{GhostCat_1s_so_cr4sy}` |
| 2 | Root flag (ZIP) | `THM{Z1P_1S_FAKE}` |

---

**Metodología:** Se enumeró el puerto 8009 (AJP) de Apache Tomcat y se explotó la vulnerabilidad GhostCat (CVE-2020-1938) para leer archivos internos del servidor mediante el protocolo AJP. Con las credenciales obtenidas se accedió al sistema, donde un archivo ZIP protegido contenía la flag final, obtenida tras descifrar su contraseña.

### Cadena de ataque / Attack Chain

1. Enumeración de puertos: detección de AJP en el 8009.
2. Explotación de GhostCat (CVE-2020-1938) para leer archivos del servidor.
3. Extracción de credenciales desde la configuración de Tomcat.
4. Acceso al sistema mediante SSH u otro vector de entrada.
5. Descifrado del ZIP y obtención de la flag final.

**Learning chain:** Enumeration → AJP → GhostCat (CVE-2020-1938) → file read → credentials → ZIP cracking

**Lección:** *Dejar expuesto el puerto AJP (8009) de Tomcat sin la debida restricción permite leer archivos internos mediante GhostCat, incluso sin conocer credenciales HTTP.*

**MITRE ATT&CK:** T1083 - File and Directory Discovery, T1078 - Valid Accounts, T1110.002 - Brute Force: Password Cracking

**Fuente:** [TryHackMe - tomghost](https://tryhackme.com/room/tomghost)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.