# kiba

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `kiba` | https://tryhackme.com/room/kiba | 01 Level Easy | TryHackMe | Kibana 6.5.4 / CVE-2019-7609 / Prototype Pollution / RCE / getcap / capabilities | Máquina Linux: explotar Kibana mediante prototype pollution (CVE-2019-7609) para ejecutar comandos, y escalar a root abusando de las capabilities de Python (getcap). |

---

**Contexto:** Máquina del catálogo de TryHackMe (kiba). El vector inicial es Kibana 6.5.4, vulnerable a **prototype pollution** (CVE-2019-7609), que permite ejecución remota de comandos (RCE) para obtener una shell. La escalada se resuelve revisando las capabilities con `getcap -r /` y abusando de la capacidad `setuid` de Python para ejecutar `/bin/sh` como root.

> **ES:** Máquina explotada vía prototype pollution en Kibana (CVE-2019-7609) con escalada por capabilities de Python.
> **EN:** Box exploited via prototype pollution in Kibana (CVE-2019-7609) with capabilities-based privilege escalation.

## Solucionario

### Task 1: Explotación y escalada / Exploitation and Escalation

**Explicación:** Se identifican la vulnerabilidad **Prototype pollution**, la versión de Kibana `6.5.4` y su CVE `CVE-2019-7609`. Con el exploit se obtiene RCE y la user flag `THM{1s_easy_pwn3d_k1bana_w1th_rce}`. Para escalar se ejecuta `getcap -r /` para listar capabilities y, abusando de la capacidad `setuid` de Python, se obtiene la root flag `THM{pr1v1lege_escalat1on_us1ng_capab1l1t1es}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué vulnerabilidad afecta al servicio? / Which vulnerability affects the service? | `Prototype pollution` |
| 2 | ¿Qué versión de Kibana se está ejecutando? / What version of Kibana is running? | `6.5.4` |
| 3 | ¿Qué CVE corresponde a la vulnerabilidad? / Which CVE matches the vulnerability? | `CVE-2019-7609` |
| 4 | ¿Cuál es la user flag? / What is the user flag? | `THM{1s_easy_pwn3d_k1bana_w1th_rce}` |
| 5 | Paso previo de la escalada. / Previous escalation step. | `No answer needed` |
| 6 | ¿Qué comando lista las capabilities del sistema? / Which command lists the system capabilities? | `getcap -r /` |
| 7 | ¿Cuál es la root flag? / What is the root flag? | `THM{pr1v1lege_escalat1on_us1ng_capab1l1t1es}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué vulnerabilidad afecta al servicio? | `Prototype pollution` |
| 2 | ¿Qué versión de Kibana se está ejecutando? | `6.5.4` |
| 3 | ¿Qué CVE corresponde a la vulnerabilidad? | `CVE-2019-7609` |
| 4 | ¿Cuál es la user flag? | `THM{1s_easy_pwn3d_k1bana_w1th_rce}` |
| 5 | Paso previo de la escalada. | `No answer needed` |
| 6 | ¿Qué comando lista las capabilities del sistema? | `getcap -r /` |
| 7 | ¿Cuál es la root flag? | `THM{pr1v1lege_escalat1on_us1ng_capab1l1t1es}` |

---

**Metodología:** Enumerar el servicio web (Kibana), identificar la versión 6.5.4 y el prototype pollution (CVE-2019-7609), lanzar el exploit para lograr RCE y leer la user flag; después enumerar capabilities con `getcap -r /` y abusar de la capacidad `setuid` de Python para ejecutar una shell como root y leer la root flag.

### Cadena de ataque / Attack Chain

```text
nmap -> identificar Kibana 6.5.4 -> prototype pollution (CVE-2019-7609) -> RCE -> user flag -> getcap -r / -> python3 setuid -> root -> root flag
```

**Learning chain:** Kibana -> versión -> CVE -> prototype pollution -> RCE -> getcap -> capabilities -> root.

**Lección:** *Los servicios de monitorización como Kibana acumulan CVEs de prototype pollution que acaban en RCE; y las capabilities (`getcap`) son un vector de escalada silencioso que se pasa por alto si solo se revisan SUID.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1059 (Command and Scripting Interpreter), T1548.001 (Setuid and Setgid / capabilities)

**Fuente:** [TryHackMe - kiba](https://tryhackme.com/room/kiba)
---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.