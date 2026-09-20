# Mr. Phisher

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough (phishing/defensa) | `mrphisher` | https://tryhackme.com/room/mrphisher | 01 Level Easy | TryHackMe | Análisis de phishing / correo malicioso / flag | Sala de análisis de phishing: examinar el mensaje entregado para recuperar la flag final. |

---

**Contexto:** Sala del catálogo de TryHackMe centrada en el análisis de un correo de phishing (Mr. Phisher). El objetivo es inspeccionar el mensaje sospechoso y extraer la flag que cierra el reto. El registro de esta migración conserva únicamente la flag final (`flag{a39a07a239aacd40c948d852a5c9f8d1}`).

> **ES:** Analizar un correo de phishing y localizar la flag oculta en el mensaje.
> **EN:** Analyze a phishing email and locate the flag hidden in the message.

## Solucionario

### Task 1: La flag de la sala / Room flag

**Explicación:** Tras el análisis del mensaje de phishing entregado por el remitente ("Mr. Phisher"), se localiza y extrae la flag en formato `flag{...}`.

Contenido original de la tarea / Original task content:

```text
1. flag{a39a07a239aacd40c948d852a5c9f8d1}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag de la sala / Room flag | `flag{a39a07a239aacd40c948d852a5c9f8d1}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag de la sala / Room flag | `flag{a39a07a239aacd40c948d852a5c9f8d1}` |

---

**Metodología:** Descargar/abrir el correo de phishing, inspeccionar sus cabeceras y contenido buscando el patrón `flag{...}`, y validar la flag obtenida en la sala.

### Cadena de ataque / Attack Chain

```text
Correo de phishing (Mr. Phisher) -> inspección de cabeceras y cuerpo -> búsqueda del patrón flag{...} -> flag{a39a07a239aacd40c948d852a5c9f8d1}
```

**Learning chain:** Phishing -> análisis de correo (cabeceras/cuerpo) -> extracción de la flag.

**Lección:** *Los correos de phishing son la puerta de entrada habitual de un ataque; saber leer sus cabeceras y sus elementos escondidos permite detectarlos y, en un reto, encontrar la flag.* 

**MITRE ATT&CK:** T1566 (Phishing)

**Fuente:** [TryHackMe - Mr. Phisher](https://tryhackme.com/room/mrphisher)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.