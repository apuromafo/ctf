# Logstash Data Processing Unit

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Teoría / Laboratorio | logstashdataprocessingunit | https://tryhackme.com/room/logstashdataprocessingunit | 02 Level Medium | TryHackMe | Elasticsearch, Logstash, Kibana, pipeline, plugins (input/filter/output), grok, CSV | Ingesta, transformación y centralización de datos con el stack ELK |

---

**Contexto:** La sala **Logstash Data Processing Unit** enseña el componente Logstash del stack ELK (Elasticsearch, Logstash, Kibana). A lo largo de sus tareas se despliega Elasticsearch y Logstash, se comprueban servicios, se diseñan pipelines con plugins de input, filter y output (stdin, csv, grok, mutate, drop, prune, rename, stdout, tcp, elasticsearch) y se ejecutan con el comando `logstash -f logstash.conf`.

## Solucionario

### Task 1: Introducción
**Explicación:**

Presenta la sala y el rol de Logstash dentro del stack ELK como unidad de procesamiento de datos.

1. `No answer needed`

### Task 2: ¿Qué es Logstash? / What is Logstash?
**Explicación:**

Se introduce el concepto de Logstash: un pipeline de ingesta que recibe, transforma y envía datos (input → filter → output).

1. `No answer needed`

### Task 3: Despliegue de Elasticsearch
**Explicación:**

Se despliega Elasticsearch y se verifican los datos del servicio: puerto por defecto, versión, comando de estado y host de escucha.

1. `9200`
2. `8.8.1`
3. `systemctl status elasticsearch.service`
4. `192.168.0.1`

### Task 4: Pipeline no. 1
**Explicación:**

Se ejecuta el primer pipeline y se anota la versión junto con el tiempo de procesamiento arrojado por la salida.

1. `3s`
2. `8.8.1`

### Task 5: Kibana
**Explicación:**

Se configura y comprueba Kibana, el front-end de visualización del stack ELK: puerto por defecto y número de ítems de configuración indicado.

1. `5601`
2. `3`
3. `No answer needed`

### Task 6: Plugins de Filter
**Explicación:**

Se trabajan los plugins de filtro de Logstash: `Mutate` (manipular campos), `drop` (descartar eventos) y `grok` (parsear con patrones).

1. `Mutate`
2. `drop`
3. `grok`

### Task 7: Plugins de Input
**Explicación:**

Se exploran los plugins de entrada (input), incluyendo opciones de configuración como el archivo a leer, el formato de las columnas y el destino de salida de Elasticsearch.

1. `nay`
2. `path`
3. `columns`
4. `elasticsearch`

### Task 8: Plugins de Output
**Explicación:**

Se examinan los plugins de salida (output), como la conexión por `tcp` y el parseo de datos en formato `csv`.

1. `tcp`
2. `csv`

### Task 9: Opciones de Configuración
**Explicación:**

Se aplican opciones de configuración avanzadas de los filtros: `prune` (recortar campos), `mutate` (modificar) y un `rename` que renombra el campo `src_ip` a `source_ip`.

1. `prune`
2. `mutate`
3. `rename => { "src_ip" => "source_ip" }`

### Task 10: Comportamiento de plugins
**Explicación:**

Se verifica el comportamiento de los plugins: una pregunta sí/no sobre el filtrado aplicado, la salida a `stdout` y los campos que se conservan en el pipeline (`syslog,host,port`).

1. `yay`
2. `stdout`
3. `syslog,host,port`

### Task 11: Ejecución del pipeline
**Explicación:**

Se ejecuta el pipeline completo: el comando para lanzarlo con el archivo de configuración y los plugins implicados en la cadena input → filter → output.

1. `logstash -f logstash.conf`
2. `stdin,csv,stdout`

### Task 12: Cierre
**Explicación:**

Se finaliza la práctica y se consolida el funcionamiento de Logstash como data processing unit del stack ELK.

1. `No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Tarea de introducción | `No answer needed` |
| 2 | Concepto de Logstash / pipeline | `No answer needed` |
| 3.1 | Puerto por defecto de Elasticsearch | `9200` |
| 3.2 | Versión de Elasticsearch | `8.8.1` |
| 3.3 | Comando para ver el estado del servicio | `systemctl status elasticsearch.service` |
| 3.4 | Host de escucha de Elasticsearch | `192.168.0.1` |
| 4.1 | Tiempo de procesamiento del pipeline | `3s` |
| 4.2 | Versión de Logstash | `8.8.1` |
| 5.1 | Puerto por defecto de Kibana | `5601` |
| 5.2 | Número de ítems / configuración de Kibana | `3` |
| 5.3 | Ítem adicional de configuración | `No answer needed` |
| 6.1 | Plugin de filter para manipular campos | `Mutate` |
| 6.2 | Plugin de filter para descartar eventos | `drop` |
| 6.3 | Plugin de filter para parsear con patrones | `grok` |
| 7.1 | ¿Hay configuración adicional en el input? | `nay` |
| 7.2 | Opción del archivo a leer en el input | `path` |
| 7.3 | Formato de las columnas en el input | `columns` |
| 7.4 | Destino de salida hacia Elasticsearch | `elasticsearch` |
| 8.1 | Plugin de output para conexión por socket | `tcp` |
| 8.2 | Formato de datos parseado en el output | `csv` |
| 9.1 | Plugin para recortar campos | `prune` |
| 9.2 | Plugin para modificar campos | `mutate` |
| 9.3 | Configuración para renombrar `src_ip` | `rename => { "src_ip" => "source_ip" }` |
| 10.1 | ¿El filtro se aplicó correctamente? | `yay` |
| 10.2 | Salida visible del pipeline | `stdout` |
| 10.3 | Campos conservados en el pipeline | `syslog,host,port` |
| 11.1 | Comando para ejecutar el pipeline con Logstash | `logstash -f logstash.conf` |
| 11.2 | Plugins de la cadena input → filter → output | `stdin,csv,stdout` |
| 12 | Tarea final de cierre | `No answer needed` |

---

**Metodología:** Configuración y uso práctico de Logstash dentro del stack ELK: despliegue de Elasticsearch y verificación de servicios, diseño de pipelines con plugins de input (stdin, tcp, csv), filter (mutate, grok, drop, prune, rename) y output (stdout, elasticsearch), y ejecución con `logstash -f logstash.conf` hasta confirmar el flujo completo de datos.

**Learning chain:** Introducción a Logstash → despliegue de Elasticsearch y Kibana → primeros pipelines (tiempo y versión) → plugins de filter → plugins de input → plugins de output → opciones de configuración avanzada → ejecución y cierre.

**Lección:** *Un pipeline de Logstash es una tubería simple input → filter → output: la potencia está en combinar plugins de transformación (mutate, grok, rename) con un buen destino de indexación en Elasticsearch.*

**MITRE ATT&CK:** T1005 Data from Local System (centralización de logs) · T1110 Brute Force · T1190 Exploit Public-Facing Application (detección vía pipelines Logstash) · T1078 Valid Accounts.

**Fuente:** [TryHackMe - Logstash Data Processing Unit](https://tryhackme.com/room/logstashdataprocessingunit)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.