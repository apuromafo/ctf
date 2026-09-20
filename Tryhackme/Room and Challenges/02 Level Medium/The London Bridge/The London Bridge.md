# The London Bridge
| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Challenge / Boot2Root | thelondonbridge | https://tryhackme.com/room/thelondonbridge | 02 Level Medium | TryHackMe | Linux, enumeración web, parámetros olvidados, fuerza bruta con listas comunes, escalada de privilegios | Compromiso completo del host boot2root y recuperación de las tres respuestas (user, root y contraseña de charles) |

> **Objeto:** Capturar todas las flags de un reto boot2root clásico y tomar el control del host.

---
**Contexto:** **The London Bridge** es una sala tipo boot2root de dificultad Media, de estilo CTF clásico, ambientada en "el puente de Londres cayéndose". El atacante debe enumerar el servicio web expuesto, descubrir un parámetro dejado atrás durante el desarrollo y abusar de él probando listas comunes para obtener acceso. Una vez dentro, hay que escalar privilegios hasta root y extraer las tres respuestas: la flag de usuario, la flag de root y la contraseña del usuario *charles*. La propia sala advierte que el arranque tarda hasta 5 minutos y pide usar limitadores de tasa al hacer fuerza bruta.
> **ES:** El puente de Londres se está cayendo.
> **EN:** The London Bridge is falling down.

## Solucionario
### Task 1: Capturar la flag / Capture the Flag
**Explicación:** Se enumera la máquina y se localiza el servicio web. Revisando los parámetros de la aplicación se encuentra uno remanente de la fase de desarrollo; si una lista no funciona, se prueba otra lista común hasta dar con el valor válido (la pista apunta a este enfoque). Con el acceso obtenido se escala a root y se recuperan las flags de usuario y root, además de la contraseña del usuario *charles*.

Descripción original de la tarea:

> This is a classic boot2root CTF-style room. Make sure to get all the flags.
> *This room will take upto 5 minutes to fully boot , please be patient.*
> *Please use rate limiters while brute-forcing.*

| Pregunta / Question | Respuesta / Answer |
|---------------------|--------------------|
| What is the user flag? | `THM{l0n6_l1v3_7h3_qu33n}` |
| What is the root flag? | `THM{l0nd0n_br1d63_p47ch3d}` |
| What is the password of charles? | `thekingofengland` |

### Tabla de preguntas y respuestas
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the user flag? | `THM{l0n6_l1v3_7h3_qu33n}` |
| 2 | What is the root flag? | `THM{l0nd0n_br1d63_p47ch3d}` |
| 3 | What is the password of charles? | `thekingofengland` |

---
**Metodología:** Enumeración de servicios → análisis de la aplicación web → descubrimiento de parámetros dejados en desarrollo → fuerza bruta con listas comunes (rate-limited) → acceso inicial → escalada de privilegios a root → captura de flags y de la contraseña de charles.

### Cadena de ataque / Attack Chain
```
Enumeración (nmap + web) -> parámetro remanente de desarrollo -> probar listas comunes
-> fuerza bruta controlada -> acceso inicial -> escalada a root
-> user flag + root flag + password de charles
```
**Learning chain:** Enumeración → análisis de parámetros → fuerza bruta → acceso → escalada → extracción de credenciales y flags.
**Lección:** *Los parámetros y funciones que se dejan durante el desarrollo, combinados con listas de valores comunes, son un vector clásico de acceso en un boot2root.*
**MITRE ATT&CK:** T1595 (Active Scanning), T1190 (Exploit Public-Facing Application), T1110 (Brute Force), T1068 (Exploitation for Privilege Escalation), T1005 (Data from Local System).
**Fuente:** [TryHackMe - The London Bridge](https://tryhackme.com/room/thelondonbridge)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
