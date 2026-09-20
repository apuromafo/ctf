# Fixit

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Blue Team / Splunk (SIEM) | fixit | https://tryhackme.com/room/fixit | 02 Level Medium | TryHackMe | Splunk, props.conf, transforms.conf, fields.conf, SPL | Reparación del pipeline de ingestion y extracción de campos en Splunk |

---

**Contexto:** **Fixit** es una sala práctica de Splunk para SOC (nivel 2). Hay que reparar el parsing de logs de la app **Fixit**: definir los límites de eventos multilínea con `props.conf` (stanza `BREAK_ONLY_BEFORE` y regex `\[Network-log\]`), extraer campos personalizados con `transforms.conf`/`fields.conf` y, después, analizar los datos con SPL para extraer estadísticas (dominio, países, departamentos, usuarios, IPs) e identificar quién accedió al documento `secret-document.pdf`. La app vive en `/opt/splunk/etc/apps/fixit` y el script de ingesta en `bin/network-logs`.

## Solucionario

### Task 1: Reparación del pipeline Splunk (resolución completa)
**Explicación:**

La sala se divide en tres niveles. **Nivel 1 (event boundaries):** crear `props.conf` en `/opt/splunk/etc/apps/fixit/default` con la stanza `BREAK_ONLY_BEFORE` y el regex `\[Network-log\]` para delimitar eventos multilínea. **Nivel 2 (campos personalizados):** crear `transforms.conf` (regex + `FORMAT`) y `fields.conf` (campos indexados), y enlazar el transform en `props.conf` (`TRANSFORM-network = network_custom_fields`); reiniciar con `/opt/splunk/bin/splunk restart`. **Nivel 3 (análisis):** con comandos SPL como `stats dc()` y `top` se extraen las estadísticas: dominio `Cybertees.THM`, 12 países, 6 departamentos, 28 usuarios y 52 IPs; los dos top países de Robert son Canada y United States, y quien accedió a `secret-document.pdf` es Sarah Hall.

Respuestas del lab (contenido original):

```
1. /opt/splunk/etc/apps/fixit
2. BREAK_ONLY_BEFORE
3. /opt/splunk/etc/apps/fixit/bin/network-logs
4. \[Network-log\]
5. Cybertees.THM
6. 12
7. 6
8. 28
9. 52
10. fields.conf, props.conf, transforms.conf
11. Canada, United States
12. Sarah Hall
```

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la ruta completa del directorio de la app FIXIT? | `/opt/splunk/etc/apps/fixit` |
| 2 | ¿Qué stanza se usa para definir los límites de evento en este caso multilínea? | `BREAK_ONLY_BEFORE` |
| 3 | En inputs.conf, ¿cuál es la ruta completa del script network-logs? | `/opt/splunk/etc/apps/fixit/bin/network-logs` |
| 4 | ¿Qué regex define el inicio del evento? | `\[Network-log\]` |
| 5 | ¿Qué dominio se captura en los logs? | `Cybertees.THM` |
| 6 | ¿Cuántos países se capturaron? | `12` |
| 7 | ¿Cuántos departamentos se capturaron? | `6` |
| 8 | ¿Cuántos usuarios se capturaron? | `28` |
| 9 | ¿Cuántas IPs de origen se capturaron? | `52` |
| 10 | ¿Qué archivos de configuración se usaron para arreglarlo? (orden alfabético) | `fields.conf, props.conf, transforms.conf` |
| 11 | ¿Cuáles son los dos top países desde los que Robert accedió al dominio? | `Canada, United States` |
| 12 | ¿Qué usuario accedió a secret-document.pdf? | `Sarah Hall` |

---

**Metodología:** Revisión de la estructura de la app Splunk (`inputs.conf`), creación de `props.conf` con `BREAK_ONLY_BEFORE` y regex para límites de eventos, definición de regex y `FORMAT` en `transforms.conf`, declaración de campos en `fields.conf`, reinicio de Splunk y análisis con SPL (filtros, `stats dc()`, `top`) para responder las estadísticas.

**Learning chain:** Contexto → Nivel 1 (event boundaries con props.conf) → Nivel 2 (extracción de campos con transforms/fields) → Nivel 3 (análisis de datos y estadísticas con SPL).

**Lección:** *Un pipeline de ingesta roto convierte logs útiles en basura: dominar `BREAK_ONLY_BEFORE`, los regex de `transforms.conf` y los campos indexados en `fields.conf` es el primer paso para que un SIEM devuelva visibilidad real, y luego el análisis con `stats`/`top` aísla rápidamente a los responsables.*

**MITRE ATT&CK:** T1005 Data from Local System · T1560 Archive Collected Data · T1078 Valid Accounts · T1083 File and Directory Discovery.

**Fuente:** [TryHackMe - Fixit](https://tryhackme.com/room/fixit)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.