# Sweettooth Inc [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM
* **Tipo / Type:** CTF (Free)
* **Slug:** `sweettoothinc`
* **Link:** https://tryhackme.com/room/sweettoothinc
* **Sección / Section:** Web / CTF
* **Fuente / Source:** (thmrevenant)

---

## Solucionario de Tareas / Task Solutions

> **ES:** CTF orientado a la explotación de una infraestructura de automatización industrial (ICS). Incluye escaneo de puertos, acceso a una base de datos InfluxDB sin autenticación, consultas de datos de sensores (temperatura, RPM) y obtención de flags de usuario y root a través de credenciales y bases de datos internas.
> **EN:** CTF oriented to exploiting an industrial automation (ICS) infrastructure. It includes port scanning, unauthenticated access to an InfluxDB database, sensor data queries (temperature, RPM) and obtaining user and root flags through credentials and internal databases.

---

### Task 1 — Enumeración y Base de Datos / Enumeration and Database

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Do a TCP portscan. What is the name of the database software running on one of these ports? | `influxdb` |
| What is the database user you find? | `o5yY6yya` |

---

### Task 2 — Datos de Sensores ICS / ICS Sensor Data

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What was the temperature of the water tank at 1621346400 (UTC Unix Timestamp)? | `22.5` |
| What is the highest rpm the motor of the mixer reached? | `4875` |
| What username do you find in one of the databases? | `uzJk6Ry98d8C` |

---

### Task 3 — Flags / Flags

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| user.txt | `THM{V4w4FhBmtp4RFDti}` |
| /root/root.txt | `THM{5qsDivHdCi2oabwp}` |
| The second /root/root.txt | `THM{nY2ZahyFABAmjrnx}` |

---

## Metodología / Methodology

1. **Paso / Step:** Realizar un escaneo TCP de puertos para descubrir los servicios expuestos; entre los puertos abiertos se identifica una base de datos InfluxDB desplegada en la máquina. / Perform a TCP port scan to discover the exposed services; among the open ports an InfluxDB database deployed on the machine is identified.
2. **Paso / Step:** Conectarse a InfluxDB sin credenciales (o con las descubiertas) y enumerar sus bases de datos y usuarios, obteniendo el usuario de base de datos `o5yY6yya`. / Connect to InfluxDB without credentials (or with the discovered ones) and enumerate its databases and users, obtaining the database user `o5yY6yya`.
3. **Paso / Step:** Consultar las series temporales almacenadas en las bases de datos ICS: obtener la temperatura del tanque de agua en el timestamp 1621346400 (22.5) y las RPM máximas alcanzadas por el motor del mezclador (4875). / Query the time series stored in the ICS databases: obtain the water tank temperature at timestamp 1621346400 (22.5) and the maximum RPM reached by the mixer motor (4875).
4. **Paso / Step:** Extraer credenciales o usuarios almacenados en las bases de datos (usuario `uzJk6Ry98d8C`) para acceder a la máquina y leer `user.txt`. / Extract credentials or users stored in the databases (user `uzJk6Ry98d8C`) to access the machine and read `user.txt`.
5. **Paso / Step:** Escalar privilegios localmente y localizar las dos variantes de `/root/root.txt`, capturando ambas flags de root. / Escalate privileges locally and locate the two variants of `/root/root.txt`, capturing both root flags.

### Cadena de ataque / Attack Chain

```
nmap (TCP ports) -> InfluxDB expuesta (sin auth)
  -> enum DBs/users: o5yY6yya, uzJk6Ry98d8C
  -> consultas Flux: water tank temp @1621346400 = 22.5
  -> mixer max rpm = 4875
  -> credenciales/usuario en DB -> acceso al host
  -> user.txt  = THM{V4w4FhBmtp4RFDti}
  -> privesc  -> /root/root.txt = THM{5qsDivHdCi2oabwp}
  -> flag root secundaria  = THM{nY2ZahyFABAmjrnx}
```

**Lección:** Las bases de datos de series temporales (InfluxDB) en entornos ICS suelen quedar expuestas sin autenticación; los datos operacionales y credenciales embebidas son una vía directa para comprometer el host y escalar a root.

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.