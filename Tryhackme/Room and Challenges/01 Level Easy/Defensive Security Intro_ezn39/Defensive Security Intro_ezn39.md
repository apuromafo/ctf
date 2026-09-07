# Defensive Security Intro

| **Dificultad** | Easy |
| **Tipo** | walkthrough |
| **Slug** | `defensivesecurityintroezn39` |
| **Link** | [TryHackMe](https://tryhackme.com/r/room/defensivesecurityintroezn39) |
| **Sección** | Cyber Defense |
| **Fuente** | THM |
| **Componentes** | Network analysis, Firewall rules, Static-site |
| **Impacto** | Fundamentos defensivos |

---

**Contexto:** Introducción a la seguridad defensiva: objetivos del blue team, análisis de tráfico de red, identificación de IPs maliciosas y bloqueo con reglas de firewall. Laboratorio práctico con sitio web FakeBank.

## Solucionario

### T1 - Think like a Defender

| Pregunta | Respuesta |
|----------|-----------|
| ¿Cuál es el objetivo principal de la seguridad defensiva? | Detect and respond to attacks |

### T2 - Detect Suspicious Activity

| Pregunta | Respuesta |
|----------|-----------|
| Dirección IP fuente del tráfico sospechoso | 32.122.195.63 |

### T3 - Identify the Attack

| Pregunta | Respuesta |
|----------|-----------|
| URL más reciente que el atacante intentó encontrar | https://fakebank.com/admin |

### T4 - Stop the Attack

| Pregunta | Respuesta |
|----------|-----------|
| Copiar el flag tras bloquear el ataque | THM{FAKEBANK-SECURED} |

---

**Metodología:** Identificar tráfico anómalo en el analizador → extraer la IP origen → rastrear las URLs consultadas → bloquear con regla de firewall → obtener el flag de confirmación.

**Learning chain:** Detección de anomalías → análisis de IPs → correlación de requests HTTP → contención mediante firewall → verificación.

**MITRE ATT&CK:** TA0001 Initial Access, TA0005 Defense Evasion, TA0009 Collection.

**Fuente:** https://github.com/Cajac/TryHackMe-Writeups/blob/main/Walkthroughs/Info/Defensive_Security_Intro.md