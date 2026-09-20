# Sea Surfer

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Hard | CTF | `seasurfer` | https://tryhackme.com/room/seasurfer | 03 Level Hard | TryHackMe | SSRF / LFI / RCE / sudo / tokens / flags | Reto CTF de explotación web: cadena SSRF hacia LFI y RCE, y robo de tokens de sudo para elevar privilegios, con dos flags que validan cada fase. |

---

**Contexto:** Sala de reto CTF de explotación web encadenada: un SSRF permite convertir el acceso en LFI y de ahí a RCE, y después se roban los tokens de sudo para completar la escalada. El contenido original recogido es únicamente el par de flags del reto.

> **ES:** "Explota la cadena SSRF -> LFI -> RCE y roba los tokens de sudo para obtener las dos flags."
> **EN:** "Exploit the SSRF -> LFI -> RCE chain and steal the sudo tokens to obtain the two flags."

## Solucionario

### Task 1: Flags del reto / Challenge flags

**Explicación:** Las dos flags del reto: la primera tras la cadena SSRF/LFI/RCE y la segunda tras el robo de tokens de sudo. Contenido original de la tarea:

```text
1. 1. THM{SSRFING_TO_LFI_TO_RCE}
   2. THM{STEALING_SUDO_TOKENS}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag de la cadena SSRF -> LFI -> RCE. | `THM{SSRFING_TO_LFI_TO_RCE}` |
| 2 | Flag del robo de tokens de sudo. | `THM{STEALING_SUDO_TOKENS}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag de la cadena SSRF -> LFI -> RCE. | `THM{SSRFING_TO_LFI_TO_RCE}` |
| 2 | Flag del robo de tokens de sudo. | `THM{STEALING_SUDO_TOKENS}` |

---

**Metodología:**
1. Enumerar la aplicación web y localizar el punto vulnerable a SSRF.
2. Encadenar el SSRF hacia LFI para leer archivos locales.
3. Convertir el LFI en RCE.
4. Robar los tokens de sudo del sistema comprometido.
5. Escalar privilegios y recoger las dos flags.

### Cadena de ataque / Attack Chain

```text
Web recon -> SSRF -> LFI -> RCE -> robo de sudo tokens -> THM{SSRFING_TO_LFI_TO_RCE} -> THM{STEALING_SUDO_TOKENS}
```

**Learning chain:** `SSRF -> LFI -> RCE -> sudo tokens -> escalada -> flags`

**Lección:** *Una sola vulnerabilidad mal mitigada (SSRF) puede convertirse en LFI y luego en RCE; el robo de tokens de sudo muestra cómo una sesión comprometida se eleva hasta el control total.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1005 (Data from Local System), T1105 (Ingress Tool Transfer), T1068 (Exploitation for Privilege Escalation), T1548 (Abuse Elevation Control Mechanism)

**Fuente:** [TryHackMe - Sea Surfer](https://tryhackme.com/room/seasurfer)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.