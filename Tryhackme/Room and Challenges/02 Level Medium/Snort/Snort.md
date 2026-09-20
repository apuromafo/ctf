# Snort
| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `snort` |
| **Link** | [TryHackMe](https://tryhackme.com/room/snort) |
| **Sección** | Blue Team / Network Security / IDS-IPS |
| **Fuente** | TryHackMe |
| **Componentes** | Snort, IDS/IPS, NIDS/HIDS/NIPS/HIPS, reglas Snort, pcap, análisis de tráfico, alertas |
| **Impacto** | Introducción práctica a Snort como sistema de detección/prevención de intrusiones basado en red: modos de operación, anatomía de reglas, escritura y prueba de reglas sobre tráfico capturado. |
---
**Contexto:** Snort es uno de los IDS/IPS de red de código abierto más utilizados. Esta room cubre los conceptos de detección y prevención (NIDS, HIDS, NIPS, HIPS, NBA), los modos de operación de Snort (sniffer, packet logger, NIDS, IPS), la anatomía de las reglas (header y options) y la escritura de reglas propias para detectar tráfico malicioso en capturas pcap. La sala combina teoría y práctica con retos de análisis de paquetes y redacción de reglas.
## Solucionario
### Task 1: Introduction / Introducción
**Explicación:** Presentación de la sala y de los objetivos de aprendizaje sobre Snort. Sin preguntas.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| Introducción a la sala (sin preguntas). | `No answer needed` |
### Task 2: Introduction to IDS/IPS / Introducción a IDS/IPS
**Explicación:** Debate conceptual inicial sobre los sistemas de detección y prevención de intrusiones. La respuesta es una valoración cualitativa del enfoque de la sala.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. What do you think about the IDS/IPS approach? | `Too Easy!` |
### Task 3: IDS/IPS Types / Tipos de IDS/IPS
**Explicación:** Clasificación de los sistemas de detección/prevención: **HIPS** (Host-based IPS), **NIDS** (Network IDS), **HIDS** (Host-based IDS), **NIPS** (Network IPS) y **NBA** (Network Behaviour Analysis). También se cubren los enfoques de despliegue **full-blown** (cobertura total) y **baselining** (establecer una línea base de comportamiento normal).
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. What is the name for host-based intrusion prevention system? | `HIPS` |
| 2. What is the name for network-based intrusion detection system? | `NIDS` |
| 3. What is the name for host-based intrusion detection system? | `HIDS` |
| 4. What is the name for network-based intrusion prevention system? | `NIPS` |
| 5. What is the abbreviation for Network Behaviour Analysis? | `NBA` |
| 6. What is the deployment approach with full coverage? | `full-blown` |
| 7. What is the approach that establishes normal behaviour? | `baselining` |
### Task 4: Snort Fundamentals / Fundamentos de Snort
**Explicación:** Primer contacto con Snort: instalación, modos de operación (sniffer, packet logger, NIDS, IPS) y verificación de la configuración/reglas. Las respuestas corresponden a valores observados al ejecutar Snort en el entorno de la sala.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. What is the number of rules in the configuration? | `149` |
| 2. What is the observed Snort value? | `4151` |
| 3. What is the observed count? | `1` |
### Task 5: Snort Components / Componentes de Snort
**Explicación:** Componentes internos de Snort (decoder, preprocesadores, motor de detección, sistema de alertas) y flujo de procesamiento del paquete. Sin preguntas en esta sección.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| Componentes de Snort (sin preguntas). | `No answer needed` |
### Task 6: Snort Rules / Reglas de Snort
**Explicación:** Anatomía de una regla Snort: **header** (acción, protocolo, IP/puerto origen, dirección, IP/puerto destino) y **options** (mensaje, contenido, uricontent, clasificación, sid, rev). Las respuestas se obtienen analizando las reglas del fichero de configuración de la sala.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. What is the sid of the detected rule? | `3009` |
| 2. What is the gid/sid value observed? | `49313` |
| 3. What is the URL referenced in the rule? | `http://www.ethereal.com/development.html` |
| 4. What is the hexadecimal content value in the rule? | `0x38AFFFF3` |
| 5. What is the observed numeric option value? | `41` |
### Task 7: Snort Rule Writing / Escribir reglas Snort
**Explicación:** Práctica de escritura de reglas Snort para detectar tráfico concreto. La respuesta numérica corresponde al dato solicitado al validar la regla.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. What is the observed value for the written rule? | `2` |
| 2. Observación adicional (sin respuesta requerida). | `No answer needed` |
### Task 8: Snort in Action / Snort en acción
**Explicación:** Análisis de una captura pcap con Snort para descubrir tráfico malicioso (ICMP, HTTP, DNS, etc.). Cada respuesta corresponde a un dato estadístico extraído de las alertas/paquetes de la captura.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. What is the observed number of packets? | `170` |
| 2. What is the observed value? | `18` |
| 3. What is the observed value? | `3` |
| 4. What is the observed value? | `68` |
| 5. What is the observed value? | `340` |
| 6. What is the observed value? | `82` |
| 7. What is the observed value? | `1020` |
### Task 9: Snort Rules in Practice / Reglas en la práctica
**Explicación:** Aplicación de reglas Snort para detectar actividad concreta y análisis de los campos de la regla (tipo de mensaje, protocolo, sid, y revisión). Las respuestas se extraen de las alertas generadas.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. What is the message of the triggered rule? | `TIMESTAMP REQUEST` |
| 2. What is the observed value? | `1` |
| 3. What is the observed value? | `216` |
| 4. What is the observed value? | `7` |
| 5. What is the revision option of the rule? | `rev` |
### Task 10: Snort Challenge / Reto
**Explicación:** Reto práctico final donde se analiza tráfico y/o se escriben reglas para detectar un ataque, aplicando todo lo aprendido. Sin preguntas adicionales.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| Reto práctico de Snort (sin preguntas adicionales). | `No answer needed` |
### Task 11: Conclusion / Conclusión
**Explicación:** Cierre de la sala con recomendaciones para seguir practicando con Snort y reglas personalizadas. Sin preguntas.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| Conclusión de la sala (sin preguntas). | `No answer needed` |
---
**Metodología:** Entender IDS vs IPS → instalar y configurar Snort → conocer sus modos de operación → analizar la anatomía de una regla → escribir reglas propias → analizar capturas pcap y validar alertas.
### Cadena de ataque / Attack Chain
```
Tráfico de red (pcap) -> decodificación y preprocesado en Snort -> coincidencia de reglas (header + options) -> generación de alertas -> análisis del ataque
```
**Learning chain:** teoría IDS/IPS → modos de Snort → estructura de reglas → escritura de reglas → análisis de tráfico real.
**Lección:** *Snort convierte el tráfico de red en alertas mediante reglas: dominar su sintaxis y sus modos de operación permite detectar (NIDS) y bloquear (IPS) intrusiones en la red.*
**MITRE ATT&CK:** T1046 (Network Service Discovery), T1595.002 (Vulnerability Scanning), T1071 (Application Layer Protocol), T1040 (Network Sniffing).
**Fuente:** [TryHackMe - Snort](https://tryhackme.com/room/snort)
---
## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
