# The Game v2

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|------------|------|------|------|---------|--------|--------------|---------|
| Easy | challenge | `thegamev2` | [TryHackMe](https://tryhackme.com/room/thegamev2) | 01 Level Easy | THM | Análisis de memoria (RAM dump), Volatility | Extracción de flag desde memoria |

---

**Contexto:**

> **ES:** Sala de nivel fácil centrada en el análisis de una imagen de memoria (volcado de RAM) con herramientas de memory forensics para localizar información sensible y la bandera del laboratorio.
> **EN:** Easy room focused on analyzing a memory image (RAM dump) with memory forensics tools to locate sensitive information and the lab flag.

## Solucionario

### Task 1: Análisis de memoria / Memory analysis

**Explicación:**

La lista de respuestas del room original contiene un único valor que corresponde a la flag del laboratorio. Se conserva de forma literal:

1. THM{MEMORY_CAN_CHANGE_4R34L$-$}

### Tabla Unificada de Preguntas y Respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el valor del flag? | `THM{MEMORY_CAN_CHANGE_4R34L$-$}` |

---

**Metodología:** Obtención del volcado de memoria → identificación de procesos y artefactos → búsqueda de cadenas o contenido sensible en la imagen → extracción del flag.

### Cadena de ataque / Attack Chain

- Adquisición/análisis del volcado de memoria
- Enumeración de procesos y artefactos del sistema
- Búsqueda de strings, credenciales o contenido de interés
- Captura de la flag

**Learning chain:** Memory forensics → Análisis de procesos → Búsqueda de datos fragmentados → Captura de flag

**Lección:** *La memoria volátil guarda mucha más información de la que parece: las banderas y credenciales suelen quedar en el RAM sin borrar, y el análisis metódico las hace recuperables.*

**MITRE ATT&CK:** N/A (Memory forensics/CTF)

**Fuente:** [TryHackMe - The Game v2](https://tryhackme.com/room/thegamev2)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.