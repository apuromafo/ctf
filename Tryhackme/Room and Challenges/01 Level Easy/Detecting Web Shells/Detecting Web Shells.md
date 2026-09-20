# Detecting Web Shells

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `detectingwebshells` | https://tryhackme.com/room/detectingwebshells | 01 Level Easy | TryHackMe | Web shells / ATT&CK T1505.003 / Splunk / logs web / Wireshark / análisis forense | Detección de web shells: técnicas de detección en logs y tráfico, análisis de peticiones y laboratorio forense. |

---

**Contexto:** Sala defensiva dedicada a la detección de web shells en servidores web. Se repasa la técnica MITRE ATT&CK T1505.003 (Web Shell), se practica la identificación de shells mediante query strings y nombres de archivo, la búsqueda de shells en el sistema con herramientas como `find`, y la detección en red con filtros de Wireshark (`http.request.method == "PUT"`). Se completa con laboratorios prácticos donde se analizan las peticiones del atacante y se recuperan flags.

> **ES:** Detección de web shells: técnica T1505.003, búsquedas en logs y sistema, filtros de Wireshark y laboratorios prácticos.
> **EN:** Web shell detection: T1505.003 technique, log and filesystem hunting, Wireshark filters and hands-on labs.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Presentación de la sala sobre detección de web shells. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la sala. | `No answer needed` |

### Task 2: Fundamentos de web shells / Web Shell Fundamentals

**Explicación:** Se introduce la web shell como una técnica de persistencia/ejecución remota mapeada como T1505.003 en ATT&CK. Se recuerda que las web shells pueden presentarse en distintos idiomas y extensiones, como `.aspx`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el ID de la técnica ATT&CK para Web Shell? / What is the ATT&CK technique ID for Web Shell? | `T1505.003` |
| 2 | ¿Qué extensión puede tener una web shell en este contexto? / Which extension can a web shell have in this context? | `.aspx` |

### Task 3: Laboratorio práctico 1 / Practical Lab 1

**Explicación:** En el primer laboratorio se analiza un servidor comprometido con una web shell. El servidor web corre como el usuario `www-data` y al completar el informe se obtiene la flag `THM{W3b_Sh3ll_Usag3}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué usuario ejecuta el proceso del servidor web? / Which user runs the web server process? | `www-data` |
| 2 | ¿Cuál es la flag obtenida en el laboratorio? / What is the flag obtained in the lab? | `THM{W3b_Sh3ll_Usag3}` |

### Task 4: Identificación de web shells / Identifying Web Shells

**Explicación:** Se aprenden los indicadores de una web shell en los logs: los parámetros pasados por query strings y los nombres de archivo sospechosos (que empiezan por `creat`).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Dónde se pasan los parámetros que indican una web shell en los logs? / Where are the parameters indicating a web shell passed in the logs? | `query strings` |
| 2 | ¿Con qué texto empieza el nombre del archivo sospechoso? / With which text does the suspicious file name start? | `creat` |

### Task 5: Búsqueda de web shells / Hunting Web Shells

**Explicación:** Se muestran técnicas para buscar web shells: en el sistema mediante `find /var/www/ -type f -name "*.php"` y en el tráfico de red con Wireshark usando el filtro `http.request.method == "PUT"` para detectar subidas.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué comando busca archivos PHP en /var/www? / Which command searches PHP files under /var/www? | `find /var/www/ -type f -name "*.php"` |
| 2 | ¿Qué filtro de Wireshark detecta peticiones PUT? / Which Wireshark filter detects PUT requests? | `http.request.method == "PUT"` |

### Task 6: Laboratorio práctico 2 / Practical Lab 2

**Explicación:** En el segundo laboratorio se analiza el ataque completo: la IP del atacante es `203.0.113.66`, la aplicación objetivo es un WordPress en `/wordpress`, la subida se hace mediante `upload_form.php`, el atacante ejecuta `whoami` y descarga `linpeas.sh`, obteniendo la flag `THM{W3b_Sh3ll_Int3rnals}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la IP del atacante? / What is the attacker IP? | `203.0.113.66` |
| 2 | ¿Qué aplicación se encuentra en /wordpress? / What is the target application found? | `/wordpress` |
| 3 | ¿Qué archivo permite la subida de la web shell? / Which file allows the web shell upload? | `upload_form.php` |
| 4 | ¿Qué comando ejecuta el atacante con la web shell? / Which command does the attacker run with the web shell? | `whoami` |
| 5 | ¿Qué script de enumeración se descarga la víctima? / Which enumeration script is downloaded by the attacker? | `linpeas.sh` |
| 6 | ¿Cuál es la flag obtenida en el laboratorio? / What is the flag obtained in the lab? | `THM{W3b_Sh3ll_Int3rnals}` |

### Task 7: Conclusión / Conclusion

**Explicación:** Cierre de la sala con las técnicas de detección de web shells aprendidas. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la conclusión de la sala. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la sala. | `No answer needed` |
| 2 | ¿Cuál es el ID de la técnica ATT&CK para Web Shell? | `T1505.003` |
| 3 | ¿Qué extensión puede tener una web shell en este contexto? | `.aspx` |
| 4 | ¿Qué usuario ejecuta el proceso del servidor web? | `www-data` |
| 5 | ¿Cuál es la flag obtenida en el laboratorio? | `THM{W3b_Sh3ll_Usag3}` |
| 6 | ¿Dónde se pasan los parámetros que indican una web shell en los logs? | `query strings` |
| 7 | ¿Con qué texto empieza el nombre del archivo sospechoso? | `creat` |
| 8 | ¿Qué comando busca archivos PHP en /var/www? | `find /var/www/ -type f -name "*.php"` |
| 9 | ¿Qué filtro de Wireshark detecta peticiones PUT? | `http.request.method == "PUT"` |
| 10 | ¿Cuál es la IP del atacante? | `203.0.113.66` |
| 11 | ¿Qué aplicación se encuentra en /wordpress? | `/wordpress` |
| 12 | ¿Qué archivo permite la subida de la web shell? | `upload_form.php` |
| 13 | ¿Qué comando ejecuta el atacante con la web shell? | `whoami` |
| 14 | ¿Qué script de enumeración se descarga la víctima? | `linpeas.sh` |
| 15 | ¿Cuál es la flag obtenida en el laboratorio? | `THM{W3b_Sh3ll_Int3rnals}` |
| 16 | Lee la conclusión de la sala. | `No answer needed` |

---

**Metodología:** El room parte de la definición de la web shell como técnica T1505.003 y sus variantes de extensión (`.aspx`). La detección combina tres frentes: análisis de logs (query strings y nombres de archivo como `creat`), caza en el sistema (`find /var/www/ -type f -name "*.php"`) y detección en red con Wireshark (`http.request.method == "PUT"`). Los laboratorios aplican estos conceptos: en el primero se identifica el proceso del servidor web como `www-data` (flag `THM{W3b_Sh3ll_Usag3}`) y en el segundo se reconstruye el ataque completo contra WordPress (IP `203.0.113.66`, `upload_form.php`, `whoami`, `linpeas.sh`, flag `THM{W3b_Sh3ll_Int3rnals}`).

### Cadena de ataque / Attack Chain

```text
Subida de web shell vía upload_form.php (WordPress en /wordpress) -> peticiones con query strings -> ejecución whoami -> descarga linpeas.sh -> detección con find .php + filtro Wireshark PUT + logs web
```

**Learning chain:** T1505.003 → extensiones (.aspx) → indicadores en logs (query strings, nombres) → caza con find → detección en red con Wireshark (PUT) → laboratorio forense completo.

**Lección:** *Las web shells se delatan por sus query strings, sus nombres de archivo y el método PUT de subida: correlacionar logs de acceso, búsquedas en el sistema con find y filtros de Wireshark permite detectarlas antes de que el atacante complete su objetivo.*

**MITRE ATT&CK:** T1505.003 (Web Shell), T1105 (Ingress Tool Transfer), T1059 (Command and Scripting Interpreter)

**Fuente:** [TryHackMe - Detecting Web Shells](https://tryhackme.com/room/detectingwebshells)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.