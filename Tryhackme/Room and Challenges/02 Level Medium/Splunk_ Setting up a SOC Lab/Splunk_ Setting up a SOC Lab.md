# Splunk_ Setting up a SOC Lab
| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `splunksettingupasoclab` |
| **Link** | [TryHackMe](https://tryhackme.com/room/splunksettingupasoclab) |
| **Sección** | Blue Team / SIEM / SOC |
| **Fuente** | TryHackMe |
| **Componentes** | Splunk Enterprise, Splunk Universal Forwarder, puertos (8000/8089/9997), inputs, syslog, Windows Event Logs, Linux forwarder |
| **Impacto** | Montaje de un laboratorio SOC con Splunk: instalación de indexer y forwarder, configuración de ingestas (syslog, logs locales de Windows/Linux) y validación de la recolección de eventos. |
---
**Contexto:** Esta room describe cómo construir un laboratorio SOC desde cero usando Splunk. Se instala Splunk Enterprise (el indexer) y el Splunk Universal Forwarder en máquinas Linux/Windows, se configuran los puertos de servicio (Web/UI `8000`, gestión `8089`, recepción de forwarders `9997`), la entrada **syslog** y la recolección de logs locales (Windows Event Logs). Finalmente se valida que los eventos llegan al indexer y se resuelve un reto final con la flag del laboratorio.
## Solucionario
### Task 1: Introduction / Introducción
**Explicación:** Presentación del objetivo: montar un laboratorio SOC con Splunk paso a paso. Sin preguntas.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| Introducción a la sala (sin preguntas). | `No answer needed` |
### Task 2: Splunk Installation / Instalación de Splunk
**Explicación:** Instalación de Splunk Enterprise y arranque del servicio. Se comprueba que la interfaz web queda operativa. Sin preguntas.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| Instalación y arranque de Splunk (sin preguntas). | `No answer needed` |
### Task 3: Splunk Web Port / Puerto web de Splunk
**Explicación:** Splunk Enterprise expone su interfaz web (Splunk Web) en el puerto **8000** por defecto.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. What is the default Splunk Web port? | `8000` |
### Task 4: Search CLI / CLI de búsqueda
**Explicación:** Uso de la CLI de Splunk para ejecutar búsquedas sin la interfaz web: `./bin/splunk search coffely` busca el término `coffely` en los datos indexados. Sin pregunta adicional.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. What is the CLI command used to search for "coffely"? | `./bin/splunk search coffely` |
| 2. Additional observation (no answer required). | `No answer needed` |
### Task 5: Management Port / Puerto de gestión
**Explicación:** El puerto de gestión/administración de Splunk (REST API y comunicación entre componentes) es el **8089**.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. What is the default Splunk management port? | `8089` |
### Task 6: Syslog Input / Entrada syslog
**Explicación:** Configuración de una entrada de datos tipo **syslog** para recibir logs de red (RFC 3164/5424). Se identifica el puerto syslog habitual, el número de tareas/pasos (`6`) y un fichero de sistema relevante (`/etc/group`) observado durante la configuración Linux.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. What is the input type used to receive network logs? | `syslog` |
| 2. What is the observed number of steps/tasks? | `6` |
| 3. What is the Linux file observed? | `/etc/group` |
### Task 7: Indexer Configuration / Configuración del indexer
**Explicación:** Configuración del indexer: puerto web **8000**, número de componentes/pasos observados (`3`) y tipo de datos **Local Event Logs** para la ingesta de logs del sistema local.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. What is the Splunk Web port? | `8000` |
| 2. What is the observed number of components? | `3` |
| 3. What type of data is collected from the local system? | `Local Event Logs` |
### Task 8: Universal Forwarder / Universal Forwarder
**Explicación:** Instalación del **Splunk Universal Forwarder** en Windows. La ruta por defecto de instalación es `C:\Program Files\SplunkUniversalForwarder` y el puerto por defecto de recepción de forwarders en el indexer es **9997**.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. What is the default installation path of the Universal Forwarder? | `C:\Program Files\SplunkUniversalForwarder` |
| 2. What is the default forwarding/receiving port? | `9997` |
### Task 9: Windows Event Logs / Logs de eventos de Windows
**Explicación:** Configuración del forwarder para enviar **Windows Event Logs**. Se identifica un número de eventos observados (`5`) y la descripción del evento correspondiente a un inicio de sesión exitoso: **An account was successfully logged on.**
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. What is the observed number of events? | `5` |
| 2. What is the description of the logon event? | `An account was successfully logged on.` |
### Task 10: Final Challenge / Reto final
**Explicación:** Reto final del laboratorio: localizar una flag en los datos indexados de Splunk tras completar la configuración.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. What is the flag found in Splunk? | `{COffely_Is_Best_iN_TOwn}` |
### Task 11: Conclusion / Conclusión
**Explicación:** Cierre de la sala con recomendaciones para ampliar el laboratorio SOC. Sin preguntas.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| Conclusión de la sala (sin preguntas). | `No answer needed` |
---
**Metodología:** Instalar Splunk Enterprise → verificar la UI en `8000` y la gestión en `8089` → configurar inputs (syslog, logs locales) → instalar el Universal Forwarder y apuntarlo al indexer (`9997`) → validar la llegada de eventos → resolver el reto.
### Cadena de ataque / Attack Chain
```
Fuente de logs (syslog / Windows Event Logs) -> Universal Forwarder (9997) -> Indexer de Splunk -> búsqueda y análisis en Splunk Web (8000)
```
**Learning chain:** instalación de Splunk → puertos y servicios → syslog → Universal Forwarder → validación de datos en el SOC.
**Lección:** *Un laboratorio SOC funcional exige entender el flujo de datos (fuente → forwarder → indexer → búsqueda) y los puertos/conectores que lo hacen posible.*
**MITRE ATT&CK:** (Blue Team) T1078 (Valid Accounts) — eventos de logon; T1562.002 (Impair Defenses: Disable Windows Event Logging) — relevancia de recolectar y proteger los logs.
**Fuente:** [TryHackMe - Splunk: Setting up a SOC Lab](https://tryhackme.com/room/splunksettingupasoclab)
---
## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
