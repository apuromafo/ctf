# Splunk 3

| **Dificultad** | Medium |
| **Tipo** | CTF |
| **Slug** | `splunk3zs` |
| **Link** | [TryHackMe](https://tryhackme.com/room/splunk3zs) |
| **Sección** | 02 Level Medium |
| **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | Splunk / SIEM / threat hunting / BOTS / AWS / credential access / discovery |
| **Impacto** | Investigar un incidente cloud y de endpoint con Splunk para reconstruir el robo de credenciales AWS y la exfiltración |

---

**Contexto:** Sala de investigación con Splunk (BOTS): analizar logs de una red y de infraestructura cloud comprometida, identificar el acceso con credenciales AWS, coinminer, exfiltración y movimiento lateral.

## Solucionario

### Task 1: Investigation

**Explicación:**

Introducción a la investigación.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Intro) | `No answer needed` |

### Task 2: Investigation

**Explicación:**

Introducción a la investigación.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Intro) | `No answer needed` |

### Task 3: Access Investigation

**Explicación:**

Los archivos de config (usuarios con acceso) son `bstoll,btun,splunk_access,web_admin`; el atributo de sesión MFA es `userIdentity.sessionContext.attributes.mfaAuthenticated`; el modelo de instancia EC2 es `E5-2676`; el ID de sesión es `ab45689d-69cd-41e7-8705-5350402cf7ac`; el usuario es `bstoll`; la contraseña de la app es `frothlywebcode`; el archivo bucket abierto es `OPEN_BUCKET_PLEASE_FIX.txt`; y el nombre del host es `BSTOLL-L.froth.ly`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Config users) | `1. bstoll,btun,splunk_access,web_admin` |
| 2 | (MFA attribute) | `2. userIdentity.sessionContext.attributes.mfaAuthenticated` |
| 3 | (EC2 instance model) | `3. E5-2676` |
| 4 | (Session ID) | `4. ab45689d-69cd-41e7-8705-5350402cf7ac` |
| 5 | (User) | `5. bstoll` |
| 6 | (App password) | `6. frothlywebcode` |
| 7 | (Open bucket file) | `7. OPEN_BUCKET_PLEASE_FIX.txt` |
| 8 | (Host) | `8. BSTOLL-L.froth.ly` |

### Task 4: Coinminer Investigation

**Explicación:**

Investigación del coinminer: la pestaña de Chrome implicada es `chrome#5`; el host lo compiló es `BSTOLL-L`; el ID de proceso es `30358`; el archivo es `JSCoinminer Download 8`; el nivel de confianza/severity es **Medium**; y el host implicado es `BTUN-L`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Chrome tab) | `1. chrome#5` |
| 2 | (Host) | `2. BSTOLL-L` |
| 3 | (PID) | `3. 30358` |
| 4 | (File) | `4. JSCoinminer Download 8` |
| 5 | (Confidence/severity) | `5. Medium` |
| 6 | (Host) | `6. BTUN-L` |

### Task 5: AWS Investigation

**Explicación:**

Investigación AWS: la AccessKey ID robada es `AKIAJOGCDXJ5NW5PXUPA`; el account ID es `5244329601`; el secret key es `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`; el usuario null web admin es `nullweb_admin`; y el agente de usuario es `ElasticWolf/5.1.6`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (AccessKey ID) | `1. AKIAJOGCDXJ5NW5PXUPA` |
| 2 | (Account ID) | `2. 5244329601` |
| 3 | (Secret key) | `3. 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` |
| 4 | (Null web admin) | `4. nullweb_admin` |
| 5 | (User agent) | `5. ElasticWolf/5.1.6` |

### Task 6: Discovery Investigation

**Explicación:**

Investigación de descubrimiento: el user agent anómalo es `Mozilla/5.0 (X11; U; Linux i686; ko-KP; rv: 19.1br) Gecko/20130508 Fedora/1.9.1-2.5.rs3.0 NaenaraBrowser/3.5b4`; el archivo exfiltrado es `Frothly-Brewery-Financial-Planning-FY2019-Draft.xlsm`; el ejecutable es `HxTsr.exe`; la contraseña de la app es `ilovedavidverve`; el usuario es `svcvnc`; los grupos son `administrators,user`; el PID es `14356`; y el hash es `586ef56f4d8963dd546163ac31c865d7`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Anomalous UA) | `1. Mozilla/5.0 (X11; U; Linux i686; ko-KP; rv: 19.1br) Gecko/20130508 Fedora/1.9.1-2.5.rs3.0 NaenaraBrowser/3.5b4` |
| 2 | (Exfiltrated file) | `2. Frothly-Brewery-Financial-Planning-FY2019-Draft.xlsm` |
| 3 | (Executable) | `3. HxTsr.exe` |
| 4 | (App password) | `4. ilovedavidverve` |
| 5 | (User) | `5. svcvnc` |
| 6 | (Groups) | `6. administrators,user` |
| 7 | (PID) | `7. 14356` |
| 8 | (Hash) | `8. 586ef56f4d8963dd546163ac31c865d7` |

### Task 7: Lateral Movement Investigation

**Explicación:**

Investigación de movimiento lateral: el puerto anómalo es `3333`; el archivo es `logos.png`; los archivos descubiertos son `colonel.c,definitelydontinvestigatethisfile.sh`; el número de conexiones es `8`; el endpoint es `/admin/get.php`; y los hosts implicados son `ABUNGST-L,FYODOR-L`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Anomalous port) | `1. 3333` |
| 2 | (File) | `2. logos.png` |
| 3 | (Discovered files) | `3. colonel.c,definitelydontinvestigatethisfile.sh` |
| 4 | (Connections) | `4. 8` |
| 5 | (Endpoint) | `5. /admin/get.php` |
| 6 | (Hosts) | `6. ABUNGST-L,FYODOR-L` |

### Task 8: Conclusion

**Explicación:**

Cierre de la investigación.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Conclusion) | `No answer needed` |

---

**Metodología:**

1. Investigar el acceso (usuarios de config, MFA, EC2, sesiones) y el origen del compromiso.
2. Rastrear el coinminer (pestañas de Chrome, procesos, hosts).
3. Analizar el acceso AWS con credenciales robadas (AccessKey ID, secret key, user agent ElasticWolf).
4. Correlacionar descubrimiento, exfiltración y movimiento lateral (puertos anómalos, endpoints).

**Learning chain:** access logs -> MFA bypass -> EC2 -> coinminer -> AWS keys stolen -> ElasticWolf -> exfiltration -> lateral movement

**Lección:** *La correlación de logs de acceso, endpoint y cloud en Splunk revela cómo se roban credenciales AWS y se exfiltran datos a través de movimiento lateral.*

**MITRE ATT&CK:** T1078 (Valid Accounts) · T1110 (Brute Force) · T1041 (Exfiltration Over C2) · T1018 (Remote System Discovery) · T1021 (Remote Services)

**Fuente:** [TryHackMe - Splunk 3](https://tryhackme.com/room/splunk3zs)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
