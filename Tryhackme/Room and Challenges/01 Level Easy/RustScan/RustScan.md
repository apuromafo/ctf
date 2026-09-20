# RustScan

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `rustscan` | https://tryhackme.com/room/rustscan | 01 Level Easy | TryHackMe | RustScan / escaneo de puertos / config de scripts / opciones CLI / banners / flags | Aprendizaje del escáner de puertos RustScan: instalación, configuración de scripts, ejecución contra un laboratorio, lectura de resultados y uso de sus flags de línea de comandos. |

---

**Contexto:** Sala práctica para aprender a usar RustScan, el escáner de puertos escrito en Rust que combina velocidad con scripts de Nmap. Se cubre la instalación y configuración del archivo `rustscan_scripts.toml`, la ejecución del escáner contra el laboratorio de la DMZ y la interpretación de los resultados (puertos abiertos, versiones de servicios y atributos como `httponly`), terminando con el repaso de las opciones de línea de comandos (`-h`, `-q`, `-r`, `-V`, `-b`, `-t`).

> **ES:** "RustScan" — el escáner de puertos rápido en Rust: instalación, config de scripts, laboratorio DMZ y flags de CLI.
> **EN:** "RustScan" — the fast port scanner in Rust: installation, scripts config, DMZ lab and CLI flags.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Presentación de la sala: qué es RustScan y sus fundamentos como escáner de puertos de alta velocidad. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la sala. / Read the room introduction. | `No answer needed` |

### Task 2: Instalación / Installation

**Explicación:** Se instala y se prepara RustScan en el sistema según las indicaciones de la sala. Las cuestiones de la instalación no requieren respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Paso 1 del proceso de instalación. / Step 1 of the installation process. | `No answer needed` |
| 2 | Paso 2 del proceso de instalación. / Step 2 of the installation process. | `No answer needed` |
| 3 | Paso 3 del proceso de instalación. / Step 3 of the installation process. | `No answer needed` |
| 4 | Paso 4 del proceso de instalación. / Step 4 of the installation process. | `No answer needed` |

### Task 3: Primera ejecución / First Run

**Explicación:** Se ejecuta RustScan por primera vez contra un objetivo para comprobar su funcionamiento. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Ejecuta RustScan por primera vez según las indicaciones. / Run RustScan for the first time as instructed. | `No answer needed` |

### Task 4: Escaneos básicos / Basic Scans

**Explicación:** Se prueban escaneos básicos de RustScan sobre el objetivo del laboratorio. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Realiza el escaneo básico indicado en la sala. / Perform the basic scan indicated in the room. | `No answer needed` |

### Task 5: Configuración de scripts / Scripts Configuration

**Explicación:** RustScan permite configurar scripts adicionales desde el archivo `rustscan_scripts.toml`. Las afirmaciones sobre cómo se activan y personalizan esos scripts se responden con `T` y `F` según corresponda.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cómo se llama el archivo de configuración de scripts de RustScan? / What is the RustScan scripts configuration file called? | `rustscan_scripts.toml` |
| 2 | Afirmación sobre la configuración de scripts (T/F). / Statement about script configuration (T/F). | `T` |
| 3 | Afirmación sobre la configuración de scripts (T/F). / Statement about script configuration (T/F). | `F` |

### Task 6: Laboratorio DMZ / DMZ Lab

**Explicación:** Se despliegan y escanean las máquinas del laboratorio DMZ para poner en práctica lo aprendido. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Escanea la DMZ del laboratorio según las indicaciones. / Scan the lab DMZ as instructed. | `No answer needed` |

### Task 7: Resultados del escaneo / Scan Results

**Explicación:** A partir del escaneo de la DMZ se interpretan los resultados: se encuentran `2` puertos abiertos, se identifica la versión `6.6.1p1` en uno de los servicios y se descubre el atributo `httponly` en el servicio web. El resto de la verificación no requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Ejecuta el escaneo indicado en la sala. / Run the scan indicated in the room. | `No answer needed` |
| 2 | ¿Cuántos puertos abiertos arroja el escaneo? / How many open ports does the scan show? | `2` |
| 3 | ¿Qué versión de servicio se identifica en el puerto abierto? / What service version is identified on the open port? | `6.6.1p1` |
| 4 | ¿Qué atributo adicional se descubre en el servicio web? / What extra attribute is discovered on the web service? | `httponly` |
| 5 | Completa la verificación final de la tarea. / Complete the task's final verification. | `No answer needed` |

### Task 8: Opciones de línea de comandos / Command Line Options

**Explicación:** Repaso de los flags principales de RustScan: `-h` muestra la ayuda, `-q` ejecuta en modo silencioso, `-r` fija un rango de puertos, `-V` muestra la versión, `-b` establece el tamaño de batch y `-t` configura el timeout.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué flag muestra el menú de ayuda de RustScan? / What flag shows the RustScan help menu? | `-h` |
| 2 | ¿Qué flag ejecuta RustScan de forma silenciosa? / What flag runs RustScan quietly? | `-q` |
| 3 | ¿Qué flag permite especificar un rango de puertos? / What flag allows specifying a port range? | `-r` |
| 4 | ¿Qué flag muestra la versión de RustScan? / What flag shows the RustScan version? | `-V` |
| 5 | ¿Qué flag permite especificar el tamaño de batch? / What flag allows specifying the batch size? | `-b` |
| 6 | ¿Qué flag permite especificar el timeout? / What flag allows specifying the timeout? | `-t` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la sala. / Read the room introduction. | `No answer needed` |
| 2 | Paso 1 del proceso de instalación. / Step 1 of the installation process. | `No answer needed` |
| 3 | Paso 2 del proceso de instalación. / Step 2 of the installation process. | `No answer needed` |
| 4 | Paso 3 del proceso de instalación. / Step 3 of the installation process. | `No answer needed` |
| 5 | Paso 4 del proceso de instalación. / Step 4 of the installation process. | `No answer needed` |
| 6 | Ejecuta RustScan por primera vez según las indicaciones. / Run RustScan for the first time as instructed. | `No answer needed` |
| 7 | Realiza el escaneo básico indicado en la sala. / Perform the basic scan indicated in the room. | `No answer needed` |
| 8 | ¿Cómo se llama el archivo de configuración de scripts de RustScan? / What is the RustScan scripts configuration file called? | `rustscan_scripts.toml` |
| 9 | Afirmación sobre la configuración de scripts (T/F). / Statement about script configuration (T/F). | `T` |
| 10 | Afirmación sobre la configuración de scripts (T/F). / Statement about script configuration (T/F). | `F` |
| 11 | Escanea la DMZ del laboratorio según las indicaciones. / Scan the lab DMZ as instructed. | `No answer needed` |
| 12 | Ejecuta el escaneo indicado en la sala. / Run the scan indicated in the room. | `No answer needed` |
| 13 | ¿Cuántos puertos abiertos arroja el escaneo? / How many open ports does the scan show? | `2` |
| 14 | ¿Qué versión de servicio se identifica en el puerto abierto? / What service version is identified on the open port? | `6.6.1p1` |
| 15 | ¿Qué atributo adicional se descubre en el servicio web? / What extra attribute is discovered on the web service? | `httponly` |
| 16 | Completa la verificación final de la tarea. / Complete the task's final verification. | `No answer needed` |
| 17 | ¿Qué flag muestra el menú de ayuda de RustScan? / What flag shows the RustScan help menu? | `-h` |
| 18 | ¿Qué flag ejecuta RustScan de forma silenciosa? / What flag runs RustScan quietly? | `-q` |
| 19 | ¿Qué flag permite especificar un rango de puertos? / What flag allows specifying a port range? | `-r` |
| 20 | ¿Qué flag muestra la versión de RustScan? / What flag shows the RustScan version? | `-V` |
| 21 | ¿Qué flag permite especificar el tamaño de batch? / What flag allows specifying the batch size? | `-b` |
| 22 | ¿Qué flag permite especificar el timeout? / What flag allows specifying the timeout? | `-t` |

---

**Metodología:** Instalar RustScan, configurar el archivo `rustscan_scripts.toml`, ejecutar los primeros escaneos y el del laboratorio DMZ para interpretar puertos abiertos, versiones (`6.6.1p1`) y atributos (`httponly`), y finalizar dominando las opciones de línea de comandos (`-h`, `-q`, `-r`, `-V`, `-b`, `-t`).

### Cadena de ataque / Attack Chain

```text
Instalación -> Config de scripts (rustscan_scripts.toml) -> Escaneo de la DMZ -> Análisis de resultados (2 puertos, 6.6.1p1, httponly) -> Flags de CLI (-h -q -r -V -b -t)
```

**Learning chain:** Instalación -> configuración de scripts -> escaneo DMZ -> interpretación de resultados -> flags de CLI.

**Lección:** *Una herramienta rápida solo sirve si se interpretan bien sus resultados y se domina su configuración: los scripts de Nmap y los flags de RustScan marcan la diferencia entre un escaneo ruidoso y una enumeración quirúrgica.*

**MITRE ATT&CK:** T1595.001 (Active Scanning: Port Scanning), T1046 (Network Service Discovery)

**Fuente:** [TryHackMe - RustScan](https://tryhackme.com/room/rustscan)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.