# El Bandito

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Hard | CTF | `elbandito` | https://tryhackme.com/room/elbandito | 03 Level Hard | TryHackMe | OSINT / coordenadas astronómicas / declinación / ascensión recta / image metadata / EXIF | Reto CTF de OSINT: localizar la posición del bandido mediante coordenadas astronómicas. Las dos flags contienen la declinación y la ascensión recta del objetivo. |

---

**Contexto:** La sala El Bandito es un reto tipo CTF que mezcla OSINT y coordenadas astronómicas. Hay que geolocalizar/identificar un objeto celeste o punto del cielo y entregar sus dos coordenadas como flags: la declinación (con su signo, grados, minutos y segundos de arco) y la ascensión recta (horas y minutos) con su característica envoltura THM. Ambas flags incluyen caracteres especiales (`°`, `'`, `''`, `¡!¡`, `:::`).

> **ES:** "Reto OSINT: resuelve la localización del bandido y entrega la declinación y la ascensión recta como flags."
> **EN:** "OSINT challenge: solve the bandit's location and submit declination and right ascension as flags."

## Solucionario

### Task 1: Coordenadas celestiales / Celestial coordinates

**Explicación:** Las dos flags del reto: la declinación y la ascensión recta del objetivo. Se conservan exactamente, incluidos los caracteres `°`, `'`, `''` y la envoltura `:::`/`¡!¡` con su envoltura THM. Contenido original de la tarea:

```text
1. 1. THM{:::MY_DECLINATION:+62°_14'_31.4'':::}
   2. THM{¡!¡RIGHT_ASCENSION_12h_36m_25.46s!¡!}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag 1: declinación del objetivo. | `THM{:::MY_DECLINATION:+62°_14'_31.4'':::}` |
| 2 | Flag 2: ascensión recta del objetivo. | `THM{¡!¡RIGHT_ASCENSION_12h_36m_25.46s!¡!}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag 1: declinación del objetivo. | `THM{:::MY_DECLINATION:+62°_14'_31.4'':::}` |
| 2 | Flag 2: ascensión recta del objetivo. | `THM{¡!¡RIGHT_ASCENSION_12h_36m_25.46s!¡!}` |

---

**Metodología:**
1. Analizar los datos proporcionados por el reto (imágenes, metadatos o pistas del sitio).
2. Identificar las coordenadas astronómicas del objetivo: declinación y ascensión recta.
3. Formatear cada coordenada con su envoltura THM y entregarla tal cual.

### Cadena de ataque / Attack Chain

```text
OSINT -> localizar objetivo -> coordenadas astronómicas -> declinación +62°14'31.4'' -> THM{:::MY_DECLINATION:+62°_14'_31.4'':::} -> ascensión recta 12h36m25.46s -> THM{¡!¡RIGHT_ASCENSION_12h_36m_25.46s!¡!}
```

**Learning chain:** `OSINT -> geolocalización -> coordenadas -> declinación -> ascensión recta -> flags`

**Lección:** *Los retos de OSINT esconden la respuesta en coordenadas bien formateadas; el detalle está en no alterar símbolos como `°`, comillas simples o la envoltura `:::`/`¡!¡` al copiar la flag.*

**MITRE ATT&CK:** T1595 (Active Scanning), T1596.003 (Search Open Technical Databases), T1059 (Command and Scripting Interpreter)

**Fuente:** [TryHackMe - El Bandito](https://tryhackme.com/room/elbandito)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.