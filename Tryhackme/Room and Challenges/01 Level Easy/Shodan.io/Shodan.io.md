# Shodan.io

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | Walkthrough | `shodanio` | https://tryhackme.com/room/shodanio | 01 Level Easy | TryHackMe | Shodan / OSINT / filtros de búsqueda / `vuln:` / `has_screenshot:` / monitor.shodan.io | Formativo: usar Shodan como motor de búsqueda de dispositivos y servicios expuestos, aplicar filtros y monitorizar alertas. |

---

**Contexto:** Sala práctica sobre el motor de búsqueda **Shodan**, que indexa dispositivos y servicios expuestos a internet (servidores, routers, cámaras, IoT...). Explica cómo realizar búsquedas, filtrar por vulnerabilidades con el prefijo `vuln:` (por ejemplo `vuln:ms17-010` para EternalBlue), interpretar los metadatos de un resultado (versión del servidor, ubicación, tipo de servicio, sistema operativo, valor en la sección de puertos, etc.), monitorizar certificados con `monitor.shodan.io` y usar el filtro `has_screenshot:true` para localizar interfaces con capturas, como cámaras de vigilancia.

> **ES:** "Shodan.io" — el buscador de internet de las cosas: consultas por vulnerabilidades, análisis de resultados, monitorización de certificados y filtros de screenshots.
> **EN:** "Shodan.io" — the search engine of the Internet of Things: vulnerability queries, result analysis, certificate monitoring and screenshot filters.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Introducción a Shodan y a lo que se verá en la sala. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Read the room intro. / Lee la introducción de la sala. | `No answer needed` |

### Task 2: Búsquedas básicas / Basic Queries

**Explicación:** Shodan permite buscar directamente por vulnerabilidades conocidas con el prefijo `vuln:`. Para localizar sistemas afectados por EternalBlue (MS17-010) se usa la consulta `vuln:ms17-010`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 2 | Query used to search for MS17-010. / Consulta usada para buscar MS17-010. | `vuln:ms17-010` |

### Task 3: Explorando resultados / Exploring Results

**Explicación:** Al abrir un resultado de Shodan se muestran los metadatos del dispositivo: la versión del servidor (`5.6.40-84.0-log`), la ubicación (`Netherlands`), el tipo de servicio (`Hypertext Transfer Protocol`), la ubicación expandida (`Kansas City`), el sistema operativo (`Debian`) y el valor de puertos/OS que muestra la ficha (`Nay`).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 3 | Server version shown in the result. / Versión del servidor mostrada en el resultado. | `5.6.40-84.0-log` |
| 4 | Location of the device. / Ubicación del dispositivo. | `Netherlands` |
| 5 | Type of service shown. / Tipo de servicio mostrado. | `Hypertext Transfer Protocol` |
| 6 | Expanded location. / Ubicación expandida. | `Kansas City` |
| 7 | Operating system of the device. / Sistema operativo del dispositivo. | `Debian` |
| 8 | Ports-related value shown in the detail. / Valor mostrado en los detalles del resultado. | `Nay` |

### Task 4: Monitorización / Monitoring

**Explicación:** Shodan también permite monitorizar; la sala indica que para estar al tanto de certificados se usa el panel de monitorización de Shodan en `https://monitor.shodan.io/dashboard`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 9 | URL of the monitoring dashboard. / URL del panel de monitorización. | `https://monitor.shodan.io/dashboard` |

### Task 5: Filtros de screenshot / Screenshot Filters

**Explicación:** Para encontrar interfaces capturables que no deberían ser públicas (como cámaras), se combina el filtro de capturas con la búsqueda: `has_screenshot:true encrypted attention`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 10 | Filter to find devices with screenshots. / Filtro para encontrar dispositivos con capturas. | `has_screenshot:true encrypted attention` |

### Task 6: Conclusión / Conclusion

**Explicación:** La sala finaliza invitando a practicar las búsquedas de forma ética y responsable. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 11 | Practice responsibly. / Practica de forma responsable. | `No answer needed` |
| 12 | Complete the room. / Completa la sala. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Read the room intro. | `No answer needed` |
| 2 | Query used to search for MS17-010. | `vuln:ms17-010` |
| 3 | Server version shown in the result. | `5.6.40-84.0-log` |
| 4 | Location of the device. | `Netherlands` |
| 5 | Type of service shown. | `Hypertext Transfer Protocol` |
| 6 | Expanded location. | `Kansas City` |
| 7 | Operating system of the device. | `Debian` |
| 8 | Ports-related value shown in the detail. | `Nay` |
| 9 | URL of the monitoring dashboard. | `https://monitor.shodan.io/dashboard` |
| 10 | Filter to find devices with screenshots. | `has_screenshot:true encrypted attention` |
| 11 | Practice responsibly. | `No answer needed` |
| 12 | Complete the room. | `No answer needed` |

---

**Metodología:** Realizar búsquedas OSINT en Shodan usando prefijos de vulnerabilidad (`vuln:ms17-010`), interpretar los metadatos del resultado (versión, localización, tipo, SO, puertos), usar el monitor de certificados de Shodan y aplicar el filtro `has_screenshot:true` para descubrir Interfaces no diseñadas para ser públicas.

### Cadena de ataque / Attack Chain

```text
búsqueda en Shodan -> vuln:ms17-010 -> análisis del resultado (versión / Netherlands / HTTP / Kansas City / Debian / Nay) -> monitor.shodan.io/dashboard -> has_screenshot:true encrypted attention -> inventario de dispositivos expuestos
```

**Learning chain:** Shodan search engine -> vulnerability filters (`vuln:`) -> result metadata analysis -> certificate monitoring -> screenshot filters (`has_screenshot:true`).

**Lección:** *Shodan convierte la exposición accidental en una base de datos de búsqueda: aprender a filtrar por vulnerabilidades y por capturas permite mapear la superficie de ataque global, por lo que cualquier administrador debe asumir que sus servicios expuestos son públicos y visibles para cualquiera.*

**MITRE ATT&CK:** T1596.005 — Search Open Technical Databases: Search Engines; T1595 — Active Scanning; T1590.005 — Gather Victim Network Information: IP Addresses

**Fuente:** [TryHackMe - Shodan.io](https://tryhackme.com/room/shodanio)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.