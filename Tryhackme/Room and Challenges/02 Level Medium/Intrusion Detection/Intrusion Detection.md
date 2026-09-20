# Intrusion Detection

| **Dificultad** | MEDIUM | **Tipo** | Free | **Slug** | `intrusiondetection` |
| **Link** | [TryHackMe](https://tryhackme.com/room/intrusiondetection) | **Sección** | 02 Level Medium | **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | IDS / Detección basada en firmas / NMAP / Suricata / Grafana / Shodan / Dorks OSINT / CVE-2021-43798 / Docker | **Impacto** | Detecta actividad intrusiva real sobre un host Grafana vulnerable (CVE-2021-43798): reconocimiento, detección por firmas, servicios web/HTTP, monitorización de reglas y captura de la flag final |

---

**Contexto:** Sala de detección de intrusos: se analiza un lab donde un objetivo Grafana versión `8.2.5` se ve comprometido vía CVE-2021-43798. La tarea cubre la detección basada en firmas (`signature-based detection`), la identificación de protocolos (`TLS`) y servicios (`web`, `docker`), escaneos con nmap, la monitorización en Grafana (identificador `GraphingTheWorld32`, reglas de Suricata), búsquedas OSINT con Shodan y dorks como `site:example.com filetype:pdf`, hasta obtener la flag `{SNEAK_ATTACK_CRITICAL}`.

## Solucionario

### Task 1: Introducción a la Detección de Intrusos

**Explicación:** Conceptos de detección de intrusiones y encuadre del laboratorio. No se requiere respuesta:

1. No answer needed

### Task 2: Tipos de Detección

**Explicación:** El tipo de detección empleado por el IDS de la sala, basado en patrones/reglas conocidas:

2. signature-based detection

### Task 3: Reconocimiento del Servicio

**Explicación:** Protocolo identificado en el escaneo y confirmación de respuesta:

3. 1. TLS
   2. No answer needed

### Task 4: Intervalos Observados

**Explicación:** Rangos/intervalos detectados durante la monitorización:

4. 1. 1-3
   2. 3

### Task 5: Endpoints y Reglas Detectadas

**Explicación:** Ruta identificada en el análisis, número de reglas y categorías de la firma:

5. 1. /login
   2. 6
   3. 6,A,B

### Task 6: Footprinting del Objetivo

**Explicación:** Datos de versión, vulnerabilidad asociada y técnicas de recopilación:

6. 1. 8.2.5
   2. CVE-2021-43798
   3. shodan
   4. site:example.com filetype:pdf

### Task 7: Monitorización del Dashboard (Grafana)

**Explicación:** Identificación del dashboard/identificador del lab, confirmación (yay) y motor de detección:

7. 1. GraphingTheWorld32
   2. yay
   3. Suricata

### Task 8: Servicios Expuestos

**Explicación:** Tipo de servicio expuesto y confirmación de la respuesta:

8. 1. web
   2. No answer needed

### Task 9: Contenedor del Objetivo

**Explicación:** Tecnología de contenedorización del servicio y número relacionado:

9. 1. docker
   2. 5

### Task 10: Flag Final

**Explicación:** Se obtiene la flag del detective al correlacionar la alerta con el panel del lab:

10. {SNEAK_ATTACK_CRITICAL}

### Task 11: Revisión 1

**Explicación:** Apartado de repaso. No se requiere respuesta:

11. No answer needed

### Task 12: Revisión 2

**Explicación:** Apartado final de cierre. No se requiere respuesta:

12. No answer needed

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué tipo de detección usa patrones/firmas de ataques conocidos? | `signature-based detection` |
| 2 | ¿Qué protocolo cifrado identificó el escaneo? | `TLS` |
| 3 | Primer intervalo observado en la monitorización | `1-3` |
| 4 | Segundo intervalo observado | `3` |
| 5 | ¿Qué ruta/endpoint se detecta en el análisis? | `/login` |
| 6 | ¿Cuántas reglas coinciden con la firma? | `6` |
| 7 | ¿Qué categorías/sets de reglas intervienen? | `6,A,B` |
| 8 | ¿Qué versión tiene el Grafana objetivo? | `8.2.5` |
| 9 | ¿Qué CVE afecta al objetivo? | `CVE-2021-43798` |
| 10 | ¿Qué servicio OSINT se usa para buscar dispositivos expuestos? | `shodan` |
| 11 | ¿Qué dork de búsqueda se usa para encontrar PDFs en un dominio? | `site:example.com filetype:pdf` |
| 12 | ¿Qué identificador/dashboard se observa en Grafana? | `GraphingTheWorld32` |
| 13 | Pregunta de confirmación (yay = sí) | `yay` |
| 14 | ¿Qué motor IDS genera las reglas de detección? | `Suricata` |
| 15 | ¿Qué tipo de servicio/publicación se expone en el objetivo? | `web` |
| 16 | ¿Qué tecnología de contenedores usa el servicio? | `docker` |
| 17 | Número relacionado con el contenedor del servicio | `5` |
| 18 | Flag final de la sala | `{SNEAK_ATTACK_CRITICAL}` |

---

**Metodología:**
1. Reconocimiento del objetivo: nmap, protocolos (TLS) y versión del servicio.
2. Identificar la vulnerabilidad asociada (CVE-2021-43798) y su versión (8.2.5).
3. Recopilar intel con Shodan y dorks (site/filetype).
4. Correlacionar las reglas de Suricata detectadas.
5. Validar el evento en el dashboard Grafana (GraphingTheWorld32).
6. Extraer la flag final `{SNEAK_ATTACK_CRITICAL}`.

**Learning chain:** signature-based detection → TLS → 1-3/3 → /login → 6 reglas → 6,A,B → 8.2.5 → CVE-2021-43798 → shodan → dork filetype:pdf → GraphingTheWorld32 → yay → Suricata → web → docker/5 → `{SNEAK_ATTACK_CRITICAL}`

**Lección:** *La detección de intrusos eficaz es una cadena: firmas sólidas que disparan alertas, correlación de esa alerta con la superficie real del objetivo (versión, CVE, tecnología) y confirmación visual en el dashboard. Solo cuando las tres piezas encajan la alerta se convierte en evidencia crítica.*

**MITRE ATT&CK:** T1190 - Exploit Public-Facing Application (CVE-2021-43798); T1046 - Network Service Discovery (nmap); T1018 - Remote System Discovery; T1110 - Brute Force; T1071.001 - Application Layer Protocol: Web Protocols; T1590.002 - Gather Victim Network Information: DNS (OSINT/shodan)

**Fuente:** [TryHackMe - Intrusion Detection](https://tryhackme.com/room/intrusiondetection)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.