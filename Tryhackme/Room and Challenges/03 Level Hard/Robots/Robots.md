# Robots

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Hard | CTF | `robots` | https://tryhackme.com/room/robots | 03 Level Hard | TryHackMe | CTF / robots.txt / enumeración web / flags | Reto CTF centrado en el fichero robots.txt: dos flags que se obtienen a partir del análisis web de la sala. |

---

**Contexto:** Sala de reto CTF cuya temática gira en torno a robots.txt y la enumeración web. El contenido original recogido es únicamente el par de flags del reto.

> **ES:** "Enumera la web, analiza robots.txt y entrega las dos flags."
> **EN:** "Enumerate the web, analyze robots.txt and submit the two flags."

## Solucionario

### Task 1: Flags del reto / Challenge flags

**Explicación:** Las dos flags del reto, obtenidas tras el análisis de robots.txt y la enumeración web. Contenido original de la tarea:

```text
1. 1. THM{9b17d3c3e86c944c868c57b5a7fa07d8}
   2. THM{2a279561f5eea907f7617df3982cee24}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag 1 del reto. | `THM{9b17d3c3e86c944c868c57b5a7fa07d8}` |
| 2 | Flag 2 del reto. | `THM{2a279561f5eea907f7617df3982cee24}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag 1 del reto. | `THM{9b17d3c3e86c944c868c57b5a7fa07d8}` |
| 2 | Flag 2 del reto. | `THM{2a279561f5eea907f7617df3982cee24}` |

---

**Metodología:**
1. Acceder a la web del reto y revisar el fichero robots.txt.
2. Enumerar las rutas o pistas que ese fichero deja expuestas.
3. Recorrer esa cadena para obtener la primera flag.
4. Completar el recorrido y recoger la segunda flag.

### Cadena de ataque / Attack Chain

```text
Web -> robots.txt -> rutas ocultas -> THM{9b17d3c3e86c944c868c57b5a7fa07d8} -> THM{2a279561f5eea907f7617df3982cee24}
```

**Learning chain:** `Enumeración web -> robots.txt -> rutas -> flags`

**Lección:** *El fichero robots.txt sigue siendo una fuente de enumeración de primer orden: las rutas que oculta suelen abrir la cadena hacia las flags del reto.*

**MITRE ATT&CK:** T1595 (Active Scanning), T1083 (File and Directory Discovery), T1190 (Exploit Public-Facing Application)

**Fuente:** [TryHackMe - Robots](https://tryhackme.com/room/robots)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.