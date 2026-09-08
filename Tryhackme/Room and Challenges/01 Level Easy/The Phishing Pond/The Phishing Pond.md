# The Phishing Pond

| **Dificultad** | Easy |
| **Tipo** | Sala práctica (phishing) |
| **Slug** | `phishingpond` |
| **Link** | [TryHackMe](https://tryhackme.com/room/phishingpond) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | Phishing / clasificación de correos / typosquatting / impersonación / macro / links acortados / análisis de cabeceras |
| **Impacto** | Desafío interactivo donde se actúa como analista de seguridad clasificando 10 correos como phishing o legítimos. Se repasan las tácticas de los atacantes (urgencia, typosquatting, impersonación de nombre visible, adjuntos con macros, cuentas comprometidas, ofertas demasiado buenas) y al superar los 10 niveles se obtiene la flag final. |

---

**Contexto:** "Catch the phish before the phish catches you". El lab presenta un juego de clasificación: por cada correo hay que decidir si es phishing o legítimo. Los 10 niveles combinan fraude de CEO (transferencia urgente), correos internos legítimos, notificaciones de sistema, servicio al cliente auténtico, archivos adjuntos que piden habilitar macros, enlaces a encuestas de terceros, ofertas de premios que piden datos bancarios, portales falsos de cambio de contraseña, dominios typosquatteados que imitan pasarelas de pago y entrega final de malware vía macros. Tras clasificar correctamente los 10 niveles, la flag es `THM{i_phish_you_not}`.

## Solucionario

### Task 1: Introducción

**Explicación:** Se despliega la máquina y se accede a la URL del juego. La pantalla explica la dinámica y los conceptos clave de phishing (urgencia, typosquatting, impersonación del display name, adjuntos maliciosos, cuentas comprometidas y ofertas demasiado buenas).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción y despliega la máquina. | `No answer needed` |

### Task 2: Los 10 niveles de clasificación

**Explicación:** Análisis y clasificación de cada correo: 1) **Phishing** (impersonación de ejecutivo y transferencia urgente); 2) **Legítimo** (comunicación interna); 3) **Legítimo** (notificación de sistema); 4) **Legítimo** (servicio al cliente auténtico); 5) **Phishing** (adjunto que pide habilitar macros); 6) **Phishing** (encuesta externa sospechosa); 7) **Phishing** (premios a cambio de datos bancarios); 8) **Phishing** (redirección a portal falso de credenciales); 9) **Phishing** (dominio typosquatted imitando una pasarela de pago); 10) **Phishing** (macros maliciosas). Técnicas usadas: hovering para ver la URL real, verificación del dominio From y evaluación del contexto.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Clasifica los 10 correos como phishing o legítimos. | `No answer needed` |

### Task 3: Obtención de la flag

**Explicación:** Al completar correctamente todos los niveles, el sistema valida las respuestas y muestra la flag.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag? | `THM{i_phish_you_not}` |

---

**Metodología:** Inspección de hyperlinks (hovering) para detectar la URL real → análisis de cabeceras (dominio From vs dominio corporativo) → evaluación del contexto (peticiones inusuales de credenciales o transferencias) → clasificación phishing/legítimo → captura de la flag.
**Learning chain:** entender las tácticas del phishing → aplicar el análisis de links, headers y contexto → afinar el veredicto en los 10 niveles → conseguir la flag.
**MITRE ATT&CK:** T1566 (Phishing), T1566.002 (Spearphishing Link), T1204.001 (User Execution: Malicious Link), T1204.002 (User Execution: Malicious File), T1036 (Masquerading - Typosquatting)
**Fuente:** [TryHackMe - The Phishing Pond](https://tryhackme.com/room/phishingpond)