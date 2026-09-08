# Sweettooth Inc

| **Dificultad** | Medium |
| **Tipo** | CTF |
| **Slug** | `sweettoothinc` |
| **Link** | [TryHackMe](https://tryhackme.com/room/sweettoothinc) |
| **Sección** | 02 Level Medium |
| **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | InfluxDB / ICS / time series / sensor data / credential exposure / privesc |
| **Impacto** | Explotar una base de datos InfluxDB sin autenticación en un entorno ICS para leer datos de sensores, extraer credenciales y obtener flags |

---

**Contexto:** CTF orientado a la explotación de una infraestructura de automatización industrial (ICS). Incluye escaneo de puertos, acceso a una base de datos InfluxDB sin autenticación, consultas de datos de sensores (temperatura, RPM) y obtención de flags de usuario y root a través de credenciales y bases de datos internas.

## Solucionario

### Task 1: Enumeración y Base de Datos / Enumeration and Database

**Explicación:**

Un escaneo TCP de puertos revela el software de base de datos que corre en uno de los puertos abiertos: **influxdb**. Al enumerar la base de datos (sin credenciales o con las descubiertas) se obtiene el usuario de base de datos **o5yY6yya**.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Do a TCP portscan. What is the name of the database software running on one of these ports? | `influxdb` |
| 2 | What is the database user you find? | `o5yY6yya` |

### Task 2: Datos de Sensores ICS / ICS Sensor Data

**Explicación:**

Consultando las series temporales de las bases de datos ICS (InfluxDB, lenguaje Flux) se obtienen los valores operativos: la temperatura del tanque de agua en el timestamp Unix 1621346400 era **22.5**; las RPM máximas alcanzadas por el motor del mezclador fueron **4875**. En una de las bases de datos aparece además el usuario **uzJk6Ry98d8C**.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What was the temperature of the water tank at 1621346400 (UTC Unix Timestamp)? | `22.5` |
| 2 | What is the highest rpm the motor of the mixer reached? | `4875` |
| 3 | What username do you find in one of the databases? | `uzJk6Ry98d8C` |

### Task 3: Flags / Flags

**Explicación:**

Con las credenciales/usuarios extraídos de las bases de datos se accede por SSH y se lee `user.txt`. Tras escalar privilegios localmente se localizan dos variantes de `/root/root.txt`, capturando ambas flags de root: `THM{V4w4FhBmtp4RFDti}` (user.txt), `THM{5qsDivHdCi2oabwp}` (primera /root/root.txt) y `THM{nY2ZahyFABAmjrnx}` (segunda /root/root.txt).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | user.txt | `THM{V4w4FhBmtp4RFDti}` |
| 2 | /root/root.txt | `THM{5qsDivHdCi2oabwp}` |
| 3 | The second /root/root.txt | `THM{nY2ZahyFABAmjrnx}` |

---

**Metodología:**

1. Realizar un escaneo TCP de puertos para descubrir los servicios expuestos; entre los puertos abiertos se identifica una base de datos InfluxDB desplegada en la máquina.
2. Conectarse a InfluxDB sin credenciales (o con las descubiertas) y enumerar sus bases de datos y usuarios, obteniendo el usuario de base de datos `o5yY6yya`.
3. Consultar las series temporales almacenadas en las bases de datos ICS: obtener la temperatura del tanque de agua en el timestamp 1621346400 (22.5) y las RPM máximas alcanzadas por el motor del mezclador (4875).
4. Extraer credenciales o usuarios almacenados en las bases de datos (usuario `uzJk6Ry98d8C`) para acceder a la máquina y leer `user.txt`.
5. Escalar privilegios localmente y localizar las dos variantes de `/root/root.txt`, capturando ambas flags de root.

**Learning chain:** nmap -> InfluxDB expuesto -> enumerar DBs/usuarios -> consultas Flux (temp/RPM) -> credenciales -> user.txt -> privesc -> dos root.txt

**Lección:** *Las bases de datos de series temporales (InfluxDB) en entornos ICS suelen quedar expuestas sin autenticación; los datos operacionales y credenciales embebidas son una vía directa para comprometer el host y escalar a root.*

**MITRE ATT&CK:** T1005 (Data from Local System) · T1078 (Valid Accounts) · T0812 (Remote System Information Discovery, ICS) · CWE-287 (Improper Authentication)

**Fuente:** [TryHackMe - Sweettooth Inc](https://tryhackme.com/room/sweettoothinc)
