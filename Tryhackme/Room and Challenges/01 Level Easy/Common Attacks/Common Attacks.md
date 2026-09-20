# Common Attacks

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough (concienciación/awareness) | `commonattacks` | https://tryhackme.com/room/commonattacks | 01 Level Easy | TryHackMe | Ingeniería social / phishing / malware y ransomware / contraseñas y autenticación / MFA / redes públicas (VPN/HTTPS) / backups / parches | Reconocer los ataques más comunes, entender cómo ocurren y mejorar la higiene cibernética para mantenerse más seguro en línea. |

---

**Contexto:** Room de concienciación en ciberseguridad (Common Attacks) con ejercicios prácticos sobre cómo ocurren los ataques más habituales: ingeniería social (caso Stuxnet), phishing (identificar correos falsos), malware y ransomware (WannaCry), contraseñas y autenticación (romper un hash con una lista de contraseñas), MFA, seguridad en redes públicas (VPN + HTTPS), backups y actualizaciones/parches.

> **ES:** Con ejercicios prácticos, descubre cómo ocurren los ataques comunes y mejora tu higiene cibernética para estar más seguro en línea.
> **EN:** With practical exercises see how common attacks occur, and improve your cyber hygiene to stay safer online.

## Solucionario

### Task 1: Introducción de información / Information Introduction

**Explicación:** Presentación de la room: ejercicios prácticos sobre ataques comunes, orientados a mejorar la higiene cibernética. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¡Empecemos! / Let's get started! | `No answer needed` |

### Task 2: Ataques comunes: Ingeniería social / Common Attacks: Social Engineering

**Explicación:** Se explican las bases de la ingeniería social y se estudia el caso real de Stuxnet, gusano que atacó directamente las centrifugadoras de un programa nuclear. Se responde cuál fue su objetivo original.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Leer la información de la tarea y ver los vídeos adjuntos. / Read the task information and watch the attached videos. | `No answer needed` |
| 2 | ¿Cuál fue el objetivo original de Stuxnet? / What was the original target of Stuxnet? | `The Iran Nuclear Programme` |

### Task 3: Ataques comunes: Ingeniería social: Phishing / Common Attacks: Social Engineering: Phishing

**Explicación:** Se muestra una serie de correos y mensajes de texto y hay que identificar cuáles son genuinos y cuáles son intentos de phishing (dominios sospechosos, adjuntos inesperados, remitentes falsos). Al clasificarlos correctamente se obtiene la flag.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Pulsa el botón verde "View Site" arriba de esta tarea si no lo has hecho todavía. / Click the green "View Site" button at the top of this task if you haven't already done so. | `No answer needed` |
| 2 | ¿Cuál es la flag? / What is the flag? | `THM{I_CAUGHT_ALL_THE_PHISH}` |

### Task 4: Ataques comunes: Malware y ransomware / Common Attacks: Malware and Ransomware

**Explicación:** Se repasan malware y ransomware, con WannaCry como ejemplo: los atacantes cifran los datos y piden el rescate en una criptomoneda. La pregunta se resuelve con investigación sobre WannaCry.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | [Investigación] ¿En qué moneda pidieron el pago los atacantes de WannaCry? / [Research] What currency did the WannaCry attackers request payment in? | `Bitcoin` |

### Task 5: Ataques comunes: Contraseñas y autenticación / Common Attacks: Passwords and Authentication

**Explicación:** Se simula un atacante que volcó la base de datos de contraseñas de un servicio en línea y debe romper los hashes. Se copia la lista de contraseñas de la web interactiva en el campo "Password List" del cracker y se pulsa "Go": el cracker encuentra que la contraseña que coincide con el hash objetivo es `TryHackMe123!`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Ponte en la piel de un hacker: has logrado volcar la base de datos de contraseñas de un servicio en línea, ¡pero aún tienes que romper esos hashes! Pulsa el botón verde para desplegar el cracker interactivo de hashes. / Put yourself in the shoes of a malicious hacker... deploy the interactive hash brute-forcer. | `No answer needed` |
| 2 | Copia la lista de contraseñas en el campo "Password List" del cracker y pulsa "Go". / Copy the list of passwords into the "Password List" field of the hash cracker, then click "Go". | `No answer needed` |
| 3 | El cracker debería encontrar muy rápido la contraseña que coincide con el hash objetivo. ¿Cuál es la contraseña? / The hash cracker should find the password that matches the target hash very quickly. What is the password? | `TryHackMe123!` |
| 4 | En la siguiente tarea veremos algunas medidas comunes de protección de cuentas y cómo generar contraseñas seguras. / In the next task we will look at some of the common account protection measures... | `No answer needed` |

### Task 6: Estar seguro: Autenticación multifactor y gestores de contraseñas / Staying Safe: Multi-Factor Authentication and Password Managers

**Explicación:** Se explican los factores de autenticación y los gestores de contraseñas. Entre TOTP basados en SMS y TOTP basados en aplicaciones autenticadoras, la elección recomendada es la aplicación autenticadora, porque el SMS es menos seguro (secuestro de SIM, etc.).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Cuando tengas opción, ¿cuál deberías usar como segundo factor: TOTP basado en SMS o TOTP basado en app autenticadora (SMS o App)? / Where you have the option, which should you use as a second authentication factor between SMS based TOTPs or Authenticator App based TOTPs (SMS or App)? | `App` |

### Task 7: Estar seguro: Seguridad en redes públicas / Staying Safe: Public Network Safety

**Explicación:** Se despliega un contenido interactivo que demuestra lo que puede pasar si se envía información por una red potencialmente insegura con distintos niveles de cifrado (VPN y/o HTTPS). No hay flag, pero se recomienda probar cada escenario. La conclusión: combinar VPN + HTTPS es lo más seguro.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Despliega el contenido interactivo pulsando el botón verde. / Deploy the interactive content by clicking the green button at the top of the task. | `No answer needed` |
| 2 | El contenido interactivo demuestra lo que puede pasar... No hay flag para esta tarea, pero se anima a probar los diferentes escenarios. / The interactive content demonstrates what can happen if information is sent over a potentially unsafe network... There is no flag for this task. | `No answer needed` |

### Task 8: Estar seguro: Copias de seguridad (Backups) / Staying Safe: Backups

**Explicación:** Se presentan las "reglas de oro" de las copias de seguridad: mantener varias copias actualizadas y guardar parte de ellas en otra ubicación.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el número mínimo de copias de seguridad actualizadas que deberías hacer? / What is the minimum number of up-to-date backups you should make? | `3` |
| 2 | De estas, ¿cuántas (como mínimo) deberían almacenarse en otra ubicación? / Of these, how many (at minimum) should be stored in another location? | `1` |

### Task 9: Estar seguro: Actualizaciones y parches / Staying Safe: Updates and Patches

**Explicación:** Se explica la importancia de mantener los sistemas actualizados y parcheados. Opcionalmente se sugiere completar la room Blue de TryHackMe para ver el efecto del exploit EternalBlue contra una máquina sin parchear. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Opcional) Completa la room Blue de TryHackMe para ver los brutales efectos del exploit EternalBlue contra una máquina sin parchear. / (Optional) Complete the Blue room on TryHackMe to see the brutal effects of the Eternal Blue exploit in action against an unpatched machine for yourself. | `No answer needed` |

### Task 10: Conclusión de información / Information Conclusion

**Explicación:** Cierre de la room: repaso de lo aprendido sobre ataques comunes y buenas prácticas de higiene cibernética. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | He completado la room Common Attacks. / I have completed the Common Attacks room. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál fue el objetivo original de Stuxnet? / What was the original target of Stuxnet? | `The Iran Nuclear Programme` |
| 2 | ¿Cuál es la flag? / What is the flag? | `THM{I_CAUGHT_ALL_THE_PHISH}` |
| 3 | [Investigación] ¿En qué moneda pidieron el pago los atacantes de WannaCry? / [Research] What currency did the WannaCry attackers request payment in? | `Bitcoin` |
| 4 | ¿Cuál es la contraseña? / What is the password? | `TryHackMe123!` |
| 5 | ¿Cuál deberías usar como segundo factor: SMS o App? / Which should you use as a second factor: SMS or App? | `App` |
| 6 | ¿Cuál es el número mínimo de copias de seguridad actualizadas que deberías hacer? / What is the minimum number of up-to-date backups you should make? | `3` |
| 7 | De estas, ¿cuántas (como mínimo) deberían almacenarse en otra ubicación? / Of these, how many (at minimum) should be stored in another location? | `1` |

---

**Metodología:** Se recorre cada ataque común por separado: leer la teoría de ingeniería social y el caso Stuxnet, clasificar correos reales/falsos para obtener la flag de phishing, investigar WannaCry (Bitcoin), romper un hash con una lista de contraseñas en el cracker interactivo (`TryHackMe123!`), elegir la app autenticadora para MFA, comprender la relación VPN/HTTPS en redes públicas, aplicar la regla 3-2-1 de backups y mantener los parches al día.

### Cadena de ataque / Attack Chain

```text
Ingeniería social (Stuxnet) -> Phishing (flag) -> Malware/ransomware (WannaCry, Bitcoin) -> Cracking de hashes (TryHackMe123!) -> MFA (App) -> Redes públicas (VPN+HTTPS) -> Backups (3-2-1) -> Parches
```

**Learning chain:** Concienciación -> ingeniería social -> phishing -> malware/ransomware -> contraseñas -> MFA -> redes públicas -> backups -> actualizaciones.

**Lección:** *La mayoría de ataques explotan a las personas y malas prácticas antes que a la tecnología: desconfiar de correos sospechosos, usar MFA con app, contraseñas fuertes y la regla 3-2-1 de backups reduce drásticamente el riesgo.*

**MITRE ATT&CK:** T1566 - Phishing; T1486 - Data Encrypted for Impact; T1110 - Brute Force

**Fuente:** [TryHackMe - Common Attacks](https://tryhackme.com/room/commonattacks)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.