# Bugged

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `bugged` | [TryHackMe](https://tryhackme.com/room/bugged) | 01 Level Easy | TryHackMe | análisis web, enumeración, captura de flags | Localización y extracción de la flag del room mediante análisis del objetivo |

---

**Contexto:** Sala de dificultad fácil en la que se analiza el objetivo para descubrir la vulnerabilidad o el punto de extracción y obtener la flag final. El resumen original conserva únicamente las respuestas posicionales del room, sin los enunciados de las preguntas.

## Solucionario

### Task 1: Análisis del objetivo / Target Analysis

**Explicación:** Se examina el servicio expuesto, se identifica la vulnerabilidad o el fallo que permite acceder al dato buscado y se extrae la flag del room.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `flag{18d44fc0707ac8dc8be45bb83db54013}` |

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `flag{18d44fc0707ac8dc8be45bb83db54013}` |

---

**Metodología:** Reconocimiento del objetivo → análisis de la aplicación o servicio vulnerable → explotación o inspección del fallo → extracción de la flag.

### Cadena de ataque / Attack Chain

```text
Reconocimiento → análisis del servicio → explotación del fallo → extracción de la flag
```

**Learning chain:** Enumeración → análisis de la aplicación vulnerable → explotación → captura de la bandera

**Lección:** *Los retos tipo bug suelen resolverse analizando con paciencia cada respuesta del servicio: el fallo reside a menudo en un detalle aparentemente inocuo de la aplicación.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1059 (Command and Scripting Interpreter)

**Fuente:** [TryHackMe - Bugged](https://tryhackme.com/room/bugged)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.