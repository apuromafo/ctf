# SDLC

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `sdlc` | [TryHackMe](https://tryhackme.com/room/sdlc) | `01 Level Easy` | THM | SDLC, DevOps, CALMS, DORA, gestión de cambios | Resolución completa del reto SDLC |

---

**Contexto:** Room centrada en el ciclo de vida del desarrollo de software (SDLC): se repasan sus etapas (definición de requisitos, planificación, diseño, pruebas, despliegue, operaciones y mantenimiento), el modelo CALMS de DevOps (Culture, Automation, Lean, Measurement, Sharing) y las métricas DORA de rendimiento (velocidad/frecuencia de despliegue, tasa de fallos y MTTR).

> **ES:** Repaso del ciclo de vida del desarrollo de software: las fases que componen el SDLC, el modelo CALMS de DevOps y las métricas DORA para medir el rendimiento de la entrega.
> **EN:** Review of the software development lifecycle: the stages that make up the SDLC, the CALMS model of DevOps and the DORA metrics to measure delivery performance.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Tarea de arranque de la room: se solicita desplegar la máquina y continuar, por lo que no requiere una respuesta técnica.

1. No answer needed

### Task 2: Número de etapas / Number of stages

**Explicación:** Se responde el número de etapas que componen el ciclo de vida del desarrollo de software según la room.

2. 6-8

### Task 3: Primeras fases / Early phases

**Explicación:** Las primeras fases del SDLC cubren la definición de requisitos, la planificación y el diseño con prototipado.

1. Requirements Definition
2. Planning Stage
3. Design and Prototyping

### Task 4: Últimas fases / Later phases

**Explicación:** Las fases finales del SDLC corresponden a operaciones y mantenimiento, despliegue y pruebas.

1. Operations and Maintenance
2. Deployment
3. Testing

### Task 5: Modelo CALMS / CALMS model

**Explicación:** El modelo de DevOps se resume en los pilares Culture, Automation, Lean, Measurement y Sharing.

5. Culture, Automation, Lean, Measurement, Sharing

### Task 6: Métricas DORA / DORA metrics

**Explicación:** Las métricas DORA miden la velocidad y frecuencia de despliegue, la tasa de fallos y el MTTR (tiempo medio de reparación).

1. Deployment speed and frequency
2. Failure rate
3. MTTR

### Task 7: Flag final / Final flag

**Explicación:** Tras completar las preguntas de la room se obtiene la flag final del reto.

7. THM{Ruler.of.the.SDLC.Droids}

### Tabla unificada de preguntas y respuestas

| Task | Pregunta | Respuesta |
|---|---|---|
| 1.1 | Despliegue y arranque de la room | `No answer needed` |
| 2.1 | Número de etapas del SDLC | `6-8` |
| 3.1 | Primera fase del SDLC | `Requirements Definition` |
| 3.2 | Segunda fase del SDLC | `Planning Stage` |
| 3.3 | Tercera fase del SDLC | `Design and Prototyping` |
| 4.1 | Fase de operaciones y mantenimiento | `Operations and Maintenance` |
| 4.2 | Fase de despliegue | `Deployment` |
| 4.3 | Fase de pruebas | `Testing` |
| 5.1 | Pilares del modelo CALMS | `Culture, Automation, Lean, Measurement, Sharing` |
| 6.1 | Métrica de velocidad y frecuencia de despliegue | `Deployment speed and frequency` |
| 6.2 | Métrica de tasa de fallos | `Failure rate` |
| 6.3 | Métrica de tiempo medio de reparación | `MTTR` |
| 7.1 | Flag final | `THM{Ruler.of.the.SDLC.Droids}` |

---

**Metodología:** 1) Leer los fundamentos del SDLC. 2) Identificar el número de etapas del ciclo de vida. 3) Ordenar las primeras fases (requisitos, planificación, diseño). 4) Completar las fases finales (operaciones, despliegue, pruebas). 5) Listar los pilares CALMS de DevOps. 6) Reconocer las métricas DORA. 7) Capturar la flag final de la room.

### Cadena de ataque / Attack Chain

```text
Introducción a la room -> número de etapas del SDLC (6-8) -> fases iniciales (Requisitos/Planificación/Diseño) -> fases finales (Operaciones/Despliegue/Pruebas) -> modelo CALMS -> métricas DORA -> THM{Ruler.of.the.SDLC.Droids}
```

**Learning chain:** SDLC fundamentals -> número y orden de fases -> modelo CALMS de DevOps -> métricas DORA (velocidad, fallos, MTTR) -> flag final

**Lección:** *Comprender el SDLC y medirlo con modelos como CALMS y DORA permite estructurar la gestión del ciclo de vida del software y la mejora continua de la entrega.*

**MITRE ATT&CK:** N/A (Requisitos teóricos de gestión del ciclo de vida del software)

**Fuente:** [TryHackMe - SDLC](https://tryhackme.com/room/sdlc)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.