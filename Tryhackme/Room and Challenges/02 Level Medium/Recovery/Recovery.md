# Recovery

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF / Forense y recuperación | recovery | https://tryhackme.com/room/recovery | 02 Level Medium | TryHackMe | Recuperación de datos, pasos del proceso, prácticas guiadas | Verificación de cada fase del proceso de recuperación |

> **Objeto:** Ejecutar y validar paso a paso un proceso de recuperación guiado, confirmando cada una de las fases del laboratorio mediante la captura de las seis flags que acreditan el correcto avance por el flujo de trabajo planteado.

---

**Contexto:** La sala **Recovery** es un laboratorio guiado de tipo desafío en el que se practica un proceso de recuperación estructurado. Las preguntas del laboratorio se responden de forma secuencial y entregan una flag por cada fase del proceso completada. Aunque el enunciado es una hoja de respuestas directa, la resolución exige seguir el procedimiento de recuperación indicado en las instrucciones de la sala y validar cada etapa con su flag correspondiente.

## Solucionario

### Task 1: Flags del proceso de recuperación / Recovery process flags
**Explicación:**

Cada fase del proceso de recuperación del laboratorio entrega una flag que confirma que el paso ha sido completado correctamente. Las seis respuestas son las flags recogidas a lo largo del proceso:

1. `THM{d8b5c89061ed767547a782e0f9b0b0fe}`
2. `THM{4c3e355694574cb182ca3057a685509d}`
3. `THM{72f8fe5fd968b5817f67acecdc701e52}`
4. `THM{70f7de17bb4e08686977a061205f3bf0}`
5. `THM{b0757f8fb8fe8dac584e80c6ac151d7d}`
6. `THM{088a36245afc7cb935f19f030c4c28b2}`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag de la fase 1 | `THM{d8b5c89061ed767547a782e0f9b0b0fe}` |
| 2 | Flag de la fase 2 | `THM{4c3e355694574cb182ca3057a685509d}` |
| 3 | Flag de la fase 3 | `THM{72f8fe5fd968b5817f67acecdc701e52}` |
| 4 | Flag de la fase 4 | `THM{70f7de17bb4e08686977a061205f3bf0}` |
| 5 | Flag de la fase 5 | `THM{b0757f8fb8fe8dac584e80c6ac151d7d}` |
| 6 | Flag de la fase 6 | `THM{088a36245afc7cb935f19f030c4c28b2}` |

---

**Metodología:** Seguimiento del flujo de recuperación guiado, ejecución de cada fase, validación de la fase completada y anotación de la flag correspondiente hasta finalizar las seis etapas del laboratorio.

**Learning chain:** Fase 1 → Fase 2 → Fase 3 → Fase 4 → Fase 5 → Fase 6, validando cada etapa con su flag hasta completar el proceso de recuperación.

**Lección:** *Documentar cada fase de un proceso de recuperación permite certificar que el flujo se completó íntegramente y que no se omitió ningún paso intermedio.*

**MITRE ATT&CK:** T1030 Data Transfer Size Limits · TA0009 Collection · T1565 Data Manipulation.

**Fuente:** [TryHackMe - Recovery](https://tryhackme.com/room/recovery)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.