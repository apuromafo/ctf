# Neighbour

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough (CTF) | `neighbour` | https://tryhackme.com/room/neighbour | 01 Level Easy | TryHackMe | Análisis forense / OSINT / flag | Reto CTF de nivel Easy: investigar el objetivo "Neighbour" y recuperar la flag final. |

---

**Contexto:** Sala tipo CTF del catálogo de TryHackMe. El objetivo de la investigación es rastrear un escenario relacionado con un vecino ("Neighbour") combinando análisis y enumeración hasta encontrar el dato que cierra la sala. El registro de esta migración conserva únicamente la flag final (`flag{66be95c478473d91a5358f2440c7af1f}`).

> **ES:** Investigar el escenario Neighbour y extraer la flag final del reto.
> **EN:** Investigate the Neighbour scenario and extract the final flag of the challenge.

## Solucionario

### Task 1: La flag de la sala / Room flag

**Explicación:** Tras completar la investigación del escenario, se localiza y valida la flag en formato `flag{...}`.

Contenido original de la tarea / Original task content:

```text
1. flag{66be95c478473d91a5358f2440c7af1f}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag de la sala / Room flag | `flag{66be95c478473d91a5358f2440c7af1f}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag de la sala / Room flag | `flag{66be95c478473d91a5358f2440c7af1f}` |

---

**Metodología:** Seguir la pista del escenario Neighbour con técnicas de análisis/OSINT hasta dar con el dato final, validarlo y confirmar la flag obtenida.

### Cadena de ataque / Attack Chain

```text
Escenario Neighbour -> análisis/enumeración -> dato clave -> flag{66be95c478473d91a5358f2440c7af1f}
```

**Learning chain:** Investigación del caso -> análisis de pistas -> extracción de la flag.

**Lección:** *Las pistas de un reto están conectadas entre sí: documentar lo que se encuentra permite encadenar los descubrimientos hasta la flag final.* 

**MITRE ATT&CK:** T1553 (Subvert Trust Controls), T1133 (External Remote Services)

**Fuente:** [TryHackMe - Neighbour](https://tryhackme.com/room/neighbour)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.