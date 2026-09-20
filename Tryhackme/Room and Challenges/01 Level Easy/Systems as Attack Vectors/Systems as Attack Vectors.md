# Systems as Attack Vectors

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `systemsasattackvectors` | https://tryhackme.com/room/systemsasattackvectors | 01 Level Easy | TryHackMe | SOC / vulnerabilidades / CVE / misconfiguraciones / supply chain / parche (patch) / pentesting / sistemas | Cómo los sistemas (endpoints, servidores, apps) se convierten en vectores de ataque, y cómo un analista SOC responde ante vulnerabilidades, misconfiguraciones y compromisos, con dos laboratorios prácticos. |

---

**Contexto:** Room de la ruta SOC Level 1 (Blue Team Intro) centrada en los sistemas como vectores de ataque. Explica la definición de "sistema", cómo los atacantes explotan vulnerabilidades, fallos humanos y ataques de cadena de suministro, y cómo responder: un CVE se trata con un parche (`CVE-2025-53770` ToolShell en SharePoint), las misconfiguraciones no se corrigen con un update sino reconfigurando, y el pentest es la actividad autorizada para detectarlas. Cierra con dos retos prácticos ("Systems at Risk" y "Remediation Plan") que entregan las flags.

> **ES:** Comprender qué sistemas atacan los grupos de amenazas y cómo protegerlos como SOC: vulnerabilidades (CVE -> Patch), misconfiguraciones (reconfigurar, no parchear), cadena de suministro, y dos desafíos prácticos que entregan `THM{patch_or_reconfigure?}` y `THM{best_systems_defender!}`.
> **EN:** Understand which systems threat groups attack and how to protect them as a SOC: vulnerabilities (CVE -> Patch), misconfigurations (reconfigure, not patch), supply chain, and two hands-on challenges awarding `THM{patch_or_reconfigure?}` and `THM{best_systems_defender!}`.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Presentación de la room: continuar explorando el rol del analista SOC, ahora enfocado en sistemas como vectores de ataque. Objetivos: aprender el rol de un sistema, explorar ataques reales y practicar en dos escenarios. Sin respuesta que rellenar.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Completa la introducción. / Complete the introduction. | `No answer needed` |

### Task 2: Definición de sistema / Definition of System

**Explicación:** Un sistema abarca endpoints (estaciones, portátiles), servidores (correo, web, bases de datos) y plataformas cloud; comprometer un servidor de correo afecta a miles de buzones. Dos preguntas tipo Y/N sobre el alcance del impacto.

**Respuestas originales verbatim:**
```text
2. 1. Yea
   2. Yea
```

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Can cyber attacks happen without victim intervention (Yea/Nay)? / ¿Pueden ocurrir ciberataques sin intervención de la víctima (Yea/Nay)? | `Yea` |
| 2 | Can a breach of just a single system lead to disastrous consequences (Yea/Nay)? / ¿Puede la brecha de un solo sistema llevar a consecuencias desastrosas (Yea/Nay)? | `Yea` |

### Task 3: Ataques a sistemas / Attacks on Systems

**Explicación:** Casi toda campaña grave comienza tratando de obtener acceso al sistema objetivo. Se revisan los tres caminos más comunes: usuarios (contraseñas débiles/robadas), vulnerabilidades de software y ataques de cadena de suministro (malware que llega desde una app o librería de confianza, como SolarWinds o 3CX).

**Respuestas originales verbatim:**
```text
3. 1. Vulnerability
   2. Supply Chain
```

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | What is the term for a security flaw that can be exploited to breach a system? / ¿Cuál es el término para una falla de seguridad explotable para vulnerar un sistema? | `Vulnerability` |
| 2 | What is the name of the attack when malware comes from a trusted app or library? / ¿Cómo se llama el ataque cuando el malware proviene de una app o librería de confianza? | `Supply Chain` |

### Task 4: Vulnerabilidades / Vulnerabilities

**Explicación:** Se explica la carrera CVE: desde el descubrimiento (incluso como zero-day) hasta el parche. La respuesta ante una vulnerabilidad detectada siempre es aplicar el parche del proveedor. Como ejemplo se menciona el CVE crítico de SharePoint bautizado "ToolShell".

**Respuestas originales verbatim:**
```text
4. 1. CVE-2025-53770
   2. Patch
```

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | What is the CVE for the critical SharePoint vulnerability dubbed "ToolShell"? / ¿Cuál es el CVE de la vulnerabilidad crítica de SharePoint apodada "ToolShell"? | `CVE-2025-53770` |
| 2 | How would you respond to a detected vulnerability on your system? / ¿Cómo responderías ante una vulnerabilidad detectada en tu sistema? | `Patch` |

### Task 5: Misconfiguraciones / Misconfigurations

**Explicación:** Una misconfiguración no es un bug del software sino un error de configuración del equipo de TI (contraseñas débiles como "1111" o "123456", cloud mal configurado, firewalls deshabilitados). No se corrige con un parche: requiere un mejor setup. Como actividades de detección proactiva destacan el pentesting (ataque autorizado), los escaneos de vulnerabilidad y las auditorías de configuración.

**Respuestas originales verbatim:**
```text
5. 1. Nay
   2. Penetration Testing
```

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Can a system patch or software update fix the misconfigurations (Yea/Nay)? / ¿Puede un parche o actualización de software corregir las misconfiguraciones (Yea/Nay)? | `Nay` |
| 2 | Which activity involves an authorized cyber attack to detect the misconfigurations? / ¿Qué actividad implica un ciberataque autorizado para detectar misconfiguraciones? | `Penetration Testing` |

### Task 6: Práctica / Practice

**Explicación:** Continuando la analogía de la fortaleza, se combinan Mitigation y Detection. Se realiza el laboratorio en el dashboard de TryHackMe: el desafío "Systems at Risk" entrega la primera flag y el "Remediation Plan" la segunda, tras decidir las mejores medidas (patch management, políticas de contraseña seguras, restricción de exposición, entrenamiento de TI) para los sistemas a proteger.

**Respuestas originales verbatim:**
```text
6. 1. THM{patch_or_reconfigure?}
   2. THM{best_systems_defender!}
```

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | What flag did you receive after completing the "Systems at Risk" challenge? / ¿Qué flag recibiste tras completar el desafío "Systems at Risk"? | `THM{patch_or_reconfigure?}` |
| 2 | What flag did you receive after completing the "Remediation Plan" challenge? / ¿Qué flag recibiste tras completar el desafío "Remediation Plan"? | `THM{best_systems_defender!}` |

### Task 7: Conclusión / Conclusion

**Explicación:** Cierre: los atacantes buscan el camino más fácil, ya sea un fallo del software o manipular a una persona; un SOC debe proteger sistemas y humanos por igual. Sin respuesta que rellenar.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Completa la conclusión. / Complete the conclusion. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Completa la introducción. / Complete the introduction. | `No answer needed` |
| 2 | Can cyber attacks happen without victim intervention (Yea/Nay)? | `Yea` |
| 3 | Can a breach of just a single system lead to disastrous consequences (Yea/Nay)? | `Yea` |
| 4 | What is the term for a security flaw that can be exploited to breach a system? | `Vulnerability` |
| 5 | What is the name of the attack when malware comes from a trusted app or library? | `Supply Chain` |
| 6 | What is the CVE for the critical SharePoint vulnerability dubbed "ToolShell"? | `CVE-2025-53770` |
| 7 | How would you respond to a detected vulnerability on your system? | `Patch` |
| 8 | Can a system patch or software update fix the misconfigurations (Yea/Nay)? | `Nay` |
| 9 | Which activity involves an authorized cyber attack to detect the misconfigurations? | `Penetration Testing` |
| 10 | What flag did you receive after completing the "Systems at Risk" challenge? | `THM{patch_or_reconfigure?}` |
| 11 | What flag did you receive after completing the "Remediation Plan" challenge? | `THM{best_systems_defender!}` |
| 12 | Completa la conclusión. / Complete the conclusion. | `No answer needed` |

---

**Metodología:** Leer los conceptos de sistema y ejemplos de alto impacto -> responder los Y/N de definición -> repasar los vectores (usuarios, vulnerabilidades, supply chain) -> identificar el CVE ToolShell y la respuesta correcta (Patch) -> entender que las misconfiguraciones no se parchean (Nay) y que el pentest es el ataque autorizado para detectarlas -> completar el laboratorio "Systems at Risk" y "Remediation Plan" en el dashboard -> recoger las dos flags -> concluir.

### Cadena de ataque / Attack Chain

```text
Sistema comprometido -> vulnerabilidad (CVE-2025-53770, ToolShell) -> Patch -> misconfiguración -> no se parchea -> reconfigure -> pentesting (ataque autorizado) -> Systems at Risk -> THM{patch_or_reconfigure?} -> Remediation Plan -> THM{best_systems_defender!}
```

**Learning chain:** SOC -> sistemas -> endpoints/servidores/cloud -> usuarios -> vulnerabilidades -> CVE -> Patch -> misconfiguraciones -> reconfiguración -> pentesting -> mitigación y detección -> flags.

**Lección:** *No toda brecha se corrige con un parche: las vulnerabilidades se parchean, pero las misconfiguraciones requieren reconfiguración, y el pentesting es la forma autorizada de descubrirlas antes de que lo haga un atacante.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1195.002 (Supply Chain Compromise: Compromise Software Supply Chain), T1078 (Valid Accounts).

**Fuente:** [TryHackMe - Systems as Attack Vectors](https://tryhackme.com/room/systemsasattackvectors)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.

**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.

**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).

**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.