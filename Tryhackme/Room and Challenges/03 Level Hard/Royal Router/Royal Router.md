# Royal Router

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Hard | CTF | `hfb1royalrouter` | https://tryhackme.com/room/hfb1royalrouter | 03 Level Hard | TryHackMe | router / embebido / explotación / routers MIPS / exfiltración | Reto de explotación de router: comprometer el router MIPS para exfiltrar datos y entregar la flag final. |

---

**Contexto:** Sala de explotación de routers embebidos (función "Royal Router"). El objetivo es comprometer el dispositivo y realizar la exfiltración, y el contenido original recogido es la flag final del reto.

> **ES:** "Compromete el router embebido y exfiltra la información para obtener la flag."
> **EN:** "Compromise the embedded router and exfiltrate the data to obtain the flag."

## Solucionario

### Task 1: Exfiltración del router / Router exfiltration

**Explicación:** Flag final del reto, obtenida tras comprometer el router MIPS y completar la exfiltración. Contenido original de la tarea:

```text
1. THM{EXFILTRATING_A_MIPS_ROUTER}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag de exfiltración del router. | `THM{EXFILTRATING_A_MIPS_ROUTER}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag de exfiltración del router. | `THM{EXFILTRATING_A_MIPS_ROUTER}` |

---

**Metodología:**
1. Enumerar el router embebido y sus servicios expuestos.
2. Identificar la vulnerabilidad o vía de acceso al dispositivo.
3. Comprometer el router MIPS.
4. Exfiltrar la información sensible y capturar la flag final.

### Cadena de ataque / Attack Chain

```text
Recon router -> vector de explotación -> compromiso MIPS -> exfiltración de datos -> THM{EXFILTRATING_A_MIPS_ROUTER}
```

**Learning chain:** `Recon -> explotación de router -> exfiltración -> flag`

**Lección:** *La seguridad de los dispositivos embebidos se descuida a menudo: la enumeración de servicios web del router y la explotación del binario MIPS permiten comprometerlo y exfiltrar sus datos.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1210 (Exploitation of Remote Services), T1041 (Exfiltration Over C2 Channel), T1005 (Data from Local System)

**Fuente:** [TryHackMe - Royal Router](https://tryhackme.com/room/hfb1royalrouter)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.