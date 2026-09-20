# Insekube

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `insekube` | [TryHackMe](https://tryhackme.com/room/insekube) | 01 Level Easy | THM | Kubernetes, Grafana 8.3.0-beta2, CVE-2021-43798, directory traversal | Lectura de archivos arbitrarios en Grafana y compromiso de los recursos de la app |

> **Objeto:** Reconocer e explotar una instancia de Grafana 8.3.0-beta2 mediante el path traversal CVE-2021-43798 para leer archivos arbitrarios, credenciales y banderas dentro del entorno Kubernetes.

---

**Contexto:** Sala de TryHackMe donde se audita un entorno con Kubernetes y una instancia insegura de Grafana 8.3.0-beta2. La versión instalada es vulnerable a CVE-2021-43798, un directory traversal que permite leer archivos arbitrarios del sistema (como credenciales de la base de datos). Con esa información se enumeran los recursos y se descubren las banderas de la sala.

> **ES:** Un reto de explotación de Grafana: el path traversal CVE-2021-43798 permite leer archivos arbitrarios, obtener credenciales de la base de datos y recorrer el entorno para recuperar todas las banderas.
> **EN:** A Grafana exploitation challenge: the path traversal CVE-2021-43798 allows reading arbitrary files, grabbing database credentials, and roaming the environment to collect every flag.

## Solucionario

### Task 1: Reconocimiento / Recon

**Explicación:** Escaneo de puertos de la máquina objetivo para descubrir los servicios expuestos.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué puertos están abiertos? / Which ports are open? | `22,80` |

### Task 2: Bandera 1 / Flag 1

**Explicación:** Tras el acceso inicial se localiza y lee la primera bandera del entorno.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 2 | Obtenga la primera bandera / Get the first flag | `flag{5e7cc6165f6c2058b11710a26691bb6b}` |

### Task 3: Configuración / Setup

**Explicación:** Apartado de preparación donde solo se confirma la instalación de herramientas o el acceso al entorno.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 3 | ¿Hay algo que responder en este apartado? / Is there anything to answer here? | `No answer needed` |

### Task 4: Bandera 2 / Flag 2

**Explicación:** Se continúa con la enumeración y se obtiene la segunda bandera.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 4 | Obtenga la segunda bandera / Get the second flag | `flag{df2a636de15108a4dc41135d930d8ec1}` |

### Task 5: Vulnerabilidad / Vulnerability

**Explicación:** Se identifica la versión exacta de Grafana instalada y su CVE asociado (path traversal).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 5.1 | ¿Cuál es la versión de Grafana? / Which Grafana version is installed? | `8.3.0-beta2` |
| 5.2 | ¿Qué CVE afecta a esta versión? / Which CVE affects this version? | `CVE-2021-43798` |

### Task 6: Explotación / Exploitation

**Explicación:** Se explota el directory traversal para leer archivos del sistema, se obtienen credenciales y se accede al panel de administración, recuperando una nueva bandera.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 6.1 | ¿Qué usuario se descubre? / Which user is discovered? | `developer` |
| 6.2 | Valor del recuento descubierto / Discovered count value | `2` |
| 6.3 | Obtenga la bandera / Get the flag | `flag{288232b2f03b1ec422c5dae50f14061f}` |

### Task 7: Bandera 3 / Flag 3

**Explicación:** Con los datos extraídos se completa la explotación y se recupera la bandera final de la sala.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 7 | Obtenga la tercera bandera / Get the third flag | `flag{30180a273e7da821a7fe4af22ffd1701}` |

---

**Metodología:** Se escaneó la máquina y se descubrieron los puertos 22 y 80, donde se alojaba Grafana 8.3.0-beta2. Se explotó el path traversal CVE-2021-43798 para leer archivos arbitrarios y extraer credenciales de la base de datos, identificando la cuenta `developer`. Con ese acceso se enumeraron los recursos del entorno y se recuperaron las banderas `flag{df2a636de15108a4dc41135d930d8ec1}`, `flag{288232b2f03b1ec422c5dae50f14061f}` y `flag{30180a273e7da821a7fe4af22ffd1701}` además de la primera `flag{5e7cc6165f6c2058b11710a26691bb6b}`.

### Cadena de ataque / Attack Chain

Escaneo de puertos → detección de Grafana 8.3.0-beta2 → explotación de CVE-2021-43798 (directory traversal) → lectura de archivos arbitrarios → extracción de credenciales (developer) → acceso a la base de datos → enumeración de recursos → recuperación de banderas.

**Learning chain:** Reconocimiento → fingerprinting Grafana → CVE-2021-43798 path traversal → lectura de archivos → credenciales → acceso a datos → recolección de banderas.

**Lección:** *Un directory traversal en una aplicación expuesta (Grafana CVE-2021-43798) permite leer archivos en un solo paso; además, el secreto de la base de datos en texto plano amplifica el compromiso. Actualizar la versión y sellar los secretos son los controles mínimos en entornos Kubernetes.*

**MITRE ATT&CK:** T1046 (Network Service Scanning), T1190 (Exploit Public-Facing Application), T1005 (Data from Local System), T1552 (Unsecured Credentials), T1083 (File and Directory Discovery).

**Fuente:** [TryHackMe - Insekube](https://tryhackme.com/room/insekube)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.