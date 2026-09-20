# WAF_ Introduction

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `wafintroduction` | https://tryhackme.com/room/wafintroduction | 01 Level Easy | TryHackMe | WAF, ModSecurity, libinjection, detección por firmas, virtual patching, defensa en profundidad | Comprensión y operación de un Web Application Firewall y sus modos de detección y despliegue |

---

**Contexto:** Introducción a los Web Application Firewalls (WAF): qué son, cómo se despliegan, sus modos de funcionamiento, métodos de detección y el papel que juegan dentro de la defensa en profundidad. Incluye un laboratorio con ModSecurity donde se crea una regla para bloquear un path traversal. El resumen original conserva únicamente las respuestas posicionales, sin los enunciados de las preguntas.

> **ES:** Aprende qué es un WAF, sus opciones de despliegue y detección, y configura una regla ModSecurity que bloquea un path traversal.
> **EN:** Learn what a WAF is, its deployment and detection options, and set up a ModSecurity rule that blocks a path traversal.

## Solucionario

### Task 1: Definición / Definition

**Explicación:** Tarea conceptual: se define qué es un Web Application Firewall.

```
1. Web Application Firewall
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `Web Application Firewall` |

### Task 2: Opciones de despliegue / Deployment Options

**Explicación:** Se revisan las distintas formas de desplegar y posicionar un WAF en la arquitectura. No requiere respuesta.

```
2. 1. No answer needed
   2. No answer needed
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `No answer needed` |
| 2 | *(Pregunta 2 no especificada en el original)* | `No answer needed` |

### Task 3: Modos de funcionamiento / Working Modes

**Explicación:** Se estudian los modos de operación del WAF: el paquete `ACK` y el modo `Stateful`.

```
3. 1. ACK
   2. Stateful
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `ACK` |
| 2 | *(Pregunta 2 no especificada en el original)* | `Stateful` |

### Task 4: Capas de aplicación / Application Layers

**Explicación:** Se profundiza en la protección a nivel de aplicación: `Layer 7`, el concepto de `Virtual patching` y el código de estado `403 Forbidden` que devuelve el WAF al bloquear.

```
4. 1. Layer 7
   2. Virtual patching
   3. 403 Forbidden
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `Layer 7` |
| 2 | *(Pregunta 2 no especificada en el original)* | `Virtual patching` |
| 3 | *(Pregunta 3 no especificada en el original)* | `403 Forbidden` |

### Task 5: Métodos de detección / Detection Methods

**Explicación:** Se comparan los métodos de detección: la detección `Signature-based` y su punto ciego, los ataques `Zero-day`.

```
5. 1. Signature-based
   2. Zero-day
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `Signature-based` |
| 2 | *(Pregunta 2 no especificada en el original)* | `Zero-day` |

### Task 6: ModSecurity: reglas y laboratorio / ModSecurity: Rules and Lab

**Explicación:** Laboratorio ModSecurity: la librería `libinjection` detecta SQLi, la transformación `urlDecodeUni` normaliza la entrada, el `Anomaly score` acumula la puntuación de las reglas y la petición `/?parameter=../../../etc/passwd` se bloquea por path traversal.

```
6. 1. libinjection
   2. urlDecodeUni
   3. Anomaly score
   4. /?parameter=../../../etc/passwd
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `libinjection` |
| 2 | *(Pregunta 2 no especificada en el original)* | `urlDecodeUni` |
| 3 | *(Pregunta 3 no especificada en el original)* | `Anomaly score` |
| 4 | *(Pregunta 4 no especificada en el original)* | `/?parameter=../../../etc/passwd` |

### Task 7: WebSockets y cifrado / Encryption

**Explicación:** Se aborda la protección del tráfico y el papel de la `Encryption` en el contexto del WAF.

```
7. Encryption
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `Encryption` |

### Task 8: Recomendaciones de despliegue / Deployment Recommendations

**Explicación:** Tarea final: cómo integrar el WAF dentro de una estrategia de seguridad global. La respuesta es `Defence in depth`.

```
8. Defence in depth
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `Defence in depth` |

---

**Metodología:** Conceptos de WAF → opciones de despliegue → modos de funcionamiento → capas de detección → métodos (firmas vs zero-day) → laboratorio ModSecurity (reglas, transformaciones, scoring) → cifrado y recomendaciones de infraestructura.

### Cadena de ataque / Attack Chain

```text
WAF (definición y despliegue) -> modo Stateful / capa 7 -> virtual patching -> detección por firmas -> ModSecurity: libinjection + urlDecodeUni + anomaly score -> bloqueo de /?parameter=../../../etc/passwd (403) -> cifrado -> defence in depth
```

**Learning chain:** Definición → despliegue → modos → capas → detección → ModSecurity → cifrado → defensa en profundidad

**Lección:** *Un Web Application Firewall basado en firmas detiene ataques conocidos mediante virtual patching, pero los ataques zero-day y su correcta integración en una estrategia de defensa en profundidad determinan su efectividad real.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1083 (File and Directory Discovery), T1059 (Command and Scripting Interpreter)

**Fuente:** [TryHackMe - WAF_ Introduction](https://tryhackme.com/room/wafintroduction)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.