# HeartBleed

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `heartbleed` | [TryHackMe](https://tryhackme.com/room/heartbleed) | 01 Level Easy | THM | Heartbleed, TLS, SSL, Vulnerabilidad | Comprensión de la vulnerabilidad Heartbleed en TLS |

---

**Contexto:** Sala sobre la vulnerabilidad Heartbleed (CVE-2014-0160) y la protección de los datos en tránsito: explica qué es SSL/TLS, por qué es crítico proteger el tráfico de red y cómo Heartbleed expuso memoria del servidor.

> **ES:** Comprender TLS/SSL, la protección de datos en tránsito y el fallo Heartbleed.
> **EN:** Understand TLS/SSL, the protection of data in transit and the Heartbleed flaw.

## Solucionario

### Task 1: Información de fondo / Background Information

**Explicación:** Presentación de la sala y del contexto de la vulnerabilidad Heartbleed.

No answer needed

### Task 2: Protegiendo los datos en tránsito / Protecting Data In Transit

**Explicación:** Se revisan los fundamentos de TLS para proteger el tráfico y se recupera la bandera del apartado.

- `THM{sSl-Is-BaD}`

### Tabla unificada de preguntas y respuestas

| Task | Pregunta | Respuesta |
|------|----------|-----------|
| 1 | — | `No answer needed` |
| 2 | Bandera del apartado | `THM{sSl-Is-BaD}` |

---

**Metodología:** Revisión teórica del contexto de Heartbleed, repaso del papel de TLS/SSL en la protección de datos en tránsito y resolución del apartado final.

### Cadena de ataque / Attack Chain

```text
Contexto de Heartbleed -> TLS/SSL (datos en tránsito) -> flag
```

**Learning chain:** Heartbleed context → TLS/SSL fundamentals → Flag

**Lección:** *El cifrado en tránsito es la primera barrera contra la interceptación: un fallo a nivel de extensión TLS (como Heartbleed) puede filtrar memoria con datos sensibles sin que el atacante rompa el cifrado en sí.*

**MITRE ATT&CK:** N/A (Room de vulnerabilidades/TLS)

**Fuente:** [TryHackMe - HeartBleed](https://tryhackme.com/room/heartbleed)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.