# GameBuzz

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Hard | CTF | gamebuzz | [GameBuzz](https://tryhackme.com/room/gamebuzz) | 03 Level Hard | TryHackMe | Hashes | Alto |

---

**Contexto:**

> **ES:** Room CTF cuyo recorrido entrega dos hashes MD5 como respuestas clave del reto, producto del análisis de los artefactos encontrados durante la resolución.
> **EN:** CTF room whose walkthrough yields two MD5 hashes as key answers, obtained from the analysis of the artifacts found during the resolution.

## Solucionario

### Task 1: Análisis de hashes / Hash analysis

**Explicación:**

El contenido original de la tarea es el siguiente:

1. 1. d14def35ed0bd914c1c5881fa0fa8090
   2. 9dcb607e31348671de36b9eb7446cb59

| Task | Pregunta / Question | Respuesta |
|---|---|---|
| 1 | ¿Cuál es el primer hash MD5 encontrado? / What is the first MD5 hash found? | `d14def35ed0bd914c1c5881fa0fa8090` |
| 1 | ¿Cuál es el segundo hash MD5 encontrado? / What is the second MD5 hash found? | `9dcb607e31348671de36b9eb7446cb59` |

---

**Metodología:**

Enumeración del entorno, identificación de los artefactos objetivo, cálculo de hashes MD5 sobre los mismos y presentación de los valores resultantes como respuestas del reto.

### Cadena de ataque / Attack Chain

1. Reconocimiento del entorno del reto.
2. Localización de los artefactos a analizar.
3. Cálculo de los hashes MD5 correspondientes.
4. Validación de las respuestas entregadas.

**Learning chain:**

`GameBuzz` → entorno → artefactos → MD5 → validación.

**Lección:** *La integridad de un artefacto se mide con su hash: saber calcular y contrastar huellas digitales es la base para verificar qué se captura, qué se modifica y qué se reporta.*

**MITRE ATT&CK:** T1552 Unsecured Credentials, T1005 Data from Local System, T1059 Command and Scripting Interpreter.

**Fuente:** [TryHackMe - GameBuzz](https://tryhackme.com/room/gamebuzz)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.