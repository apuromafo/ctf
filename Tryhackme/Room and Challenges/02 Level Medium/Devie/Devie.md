# Devie

| Campo | Valor |
|-------|-------|
| **Dificultad** | Medium |
| **Tipo** | CTF / Web + Python |
| **Slug** | devie |
| **Link** | https://tryhackme.com/room/devie |
| **Sección** | 02 Level Medium |
| **Fuente** | TryHackMe |
| **Componentes** | Python, eval(), XOR, Web, RCE |
| **Impacto** | Alto — Malas prácticas de codificación que habilitan ejecución remota de código |

---

**Contexto:** Devie es un reto centrado en malas prácticas de programación en Python dentro de una aplicación web: uso inseguro de `eval()`, cifrado XOR débilmente implementado y lógica de juego modificable. El aprendiz explota cada uno de estos fallos para avanzar hasta la flag final.

## Solucionario

### Task 1: Explotación de Devie

**Explicación:** Se explotan los fallos de la aplicación: inyección a través de `eval()`, descifrado por XOR y manipulación de la lógica del juego.

1. 1. THM{Car3ful_witH_3v@l}
   2. THM{X0R_XoR_XOr_xOr}
   3. THM{J0k3r$_Ar3_W1ld}

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1.1 | Flag eval() | `THM{Car3ful_witH_3v@l}` |
| 1.2 | Flag XOR | `THM{X0R_XoR_XOr_xOr}` |
| 1.3 | Flag juego | `THM{J0k3r$_Ar3_W1ld}` |

---

**Metodología:** Revisión del código fuente → Identificación de `eval()` no sanitizado → Explotación de la lógica XOR → Manipulación de la mecánica del juego → Obtención de flags.

**Learning chain:** Source review → eval() injection → XOR analysis → Game logic tampering → Flags

**Lección:** *`eval()` sin saneamiento de entrada es una sentencia de muerte para una aplicación web.*

**MITRE ATT&CK:**
- T1059.006 — Python
- T1190 — Exploit Public-Facing Application

**Fuente:** [TryHackMe - Devie](https://tryhackme.com/room/devie)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.