# Stealth

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Ofensivo / Post-explotación | stealth | https://tryhackme.com/room/stealth | 02 Level Medium | TryHackMe | Evasión, Linux, Post-explotación, Usuario local, Admin | Ocultación de la actividad post-explotación y compromiso total (user + admin) |

---

**Contexto:** La sala **Stealth** es una máquina Linux enfocada en la **evasión**: aplicar técnicas de post-explotación que dificultan la detección del atacante mientras se recorre la cadena de compromiso. Se obtienen dos flags que marcan la evolución del ataque: la primera corresponde al entorno de **usuario local** y la segunda al nivel de **administrador**, confirmando la escalada y el control total del sistema.

## Solucionario

### Task 1: Flags de evasión
**Explicación:**

Completada la cadena de evasión como usuario local y tras escalar a administrador, se recogen las dos flags que acreditan el compromiso sigiloso de la máquina.

1. `THM{1010_EVASION_LOCAL_USER}`
2. `THM{101011_ADMIN_ACCESS}`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1.1 | Flag de evasión nivel usuario local | `THM{1010_EVASION_LOCAL_USER}` |
| 1.2 | Flag de evasión nivel administrador | `THM{101011_ADMIN_ACCESS}` |

---

**Metodología:** Post-explotación en Linux con enfoque en evasión de defensas, ocultación de artefactos y comportamiento, escalada de privilegios y captura de flags de usuario y administrador.

**Learning chain:** Acceso inicial → evasión de detección local → escalada de privilegios → evasión en nivel admin → flags.

**Lección:** *La evasión no es solo borrar logs: cada artefacto, conexión y proceso del atacante debe diseñarse para no destacar en un entorno vigilado.*

**MITRE ATT&CK:** T1564 Hide Artifacts · T1070 Indicator Removal on Host · T1068 Exploitation for Privilege Escalation · T1055 Process Injection.

**Fuente:** [TryHackMe - Stealth](https://tryhackme.com/room/stealth)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.