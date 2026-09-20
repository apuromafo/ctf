# Enumeration & Brute Force

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `enumerationbruteforce` | [TryHackMe](https://tryhackme.com/room/enumerationbruteforce) | 01 Level Easy | TryHackMe | enumeración de usuarios / errores verbose / password reset / HTTP Basic Auth / Burp Suite / Hydra / OSINT | Enumerar usuarios legítimos y explotar lógica de autenticación débil para comprometer cuentas. |

> **Objeto:** Practicar la enumeración de usuarios válidos y el brute force en una aplicación web (enum.thm): aprovechar mensajes de error verbose, explotar una lógica de reset de contraseña predecible y forzar la autenticación HTTP Basic con Burp Suite y Hydra.

---

**Contexto:** La aplicación del laboratorio (http://enum.thm) revela o no revela información según cómo se gestionen los errores. Los mensajes de error verbose (verborrágicos) confirman qué usuarios existen, algo que un atacante aprovecha; un reset de contraseña con lógica predecible y una autenticación HTTP Basic débil completan el camino hacia el compromiso de la cuenta objetivo.

> **ES:** Room práctica sobre enum.thm. Se estudia cómo los errores verbose confirman usuarios válidos; se enumeran correos legítimos hasta dar con canderson@gmail.com, se explota la lógica del reset de contraseña (flag THM{50_pr3d1ct4BL333!!}) y se fuerza la autenticación HTTP Basic: primero con Burp Suite (flag THM{b4$$1C_AuTTHHH}) y luego con Hydra para automatizar el brute force. Cierran la room una tarea de OSINT y la conclusión, ambas sin respuesta.
> **EN:** Hands-on room on enum.thm. Verbose errors confirm valid users; legitimate emails are enumerated until canderson@gmail.com is found, the predictable password-reset logic is exploited (flag THM{50_pr3d1ct4BL333!!}) and HTTP Basic Auth is brute-forced: first with Burp Suite (flag THM{b4$$1C_AuTTHHH}) and then with Hydra to automate the attack. The room ends with an OSINT task and a conclusion, both with no answers.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:** Se despliega la máquina y se accede a la aplicación web del laboratorio en http://enum.thm (se recomienda usar el AttackBox). Tarea introductoria sin respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | After 3 minutes, visit http://enum.thm to access the machine. We recommend using the AttackBox for this room. / Tras 3 minutos, visita http://enum.thm para acceder al laboratorio. Se recomienda el AttackBox. | `No answer needed` |

### Task 2: Enumeración de autenticación / Authentication Enumeration
**Explicación:** Se estudia qué tipo de mensajes de error pueden confirmar usuarios válidos sin necesidad de brute force: los errores verbose (verborrágicos) son la pista. Si el sistema distingue entre "usuario no existe" y "contraseña incorrecta", el atacante ya tiene un oráculo de validación de usuarios.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What type of error messages can unintentionally provide attackers with confirmation of valid usernames? / ¿Qué tipo de mensajes de error pueden confirmar involuntariamente usuarios válidos? | `Verbose errors` |

### Task 3: Enumerar usuarios con errores verbose / Enumerating Users via Verbose Errors
**Explicación:** Se prueban los correos de una lista contra el formulario de la aplicación. La respuesta verbose revela cuál de los candidatos es una cuenta existente.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the valid email address from the list? / ¿Cuál es el email válido de la lista? | `canderson@gmail.com` |

### Task 4: Explotar una lógica de reset vulnerable / Exploiting Vulnerable Password Reset Logic
**Explicación:** El formulario de recuperación de contraseña genera un token predecible; se regenera repetidamente el código hasta descubrir su patrón y se restablece la contraseña de canderson@gmail.com. Al iniciar sesión con la nueva credencial aparece la flag del reset.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag? / ¿Cuál es la flag? | `THM{50_pr3d1ct4BL333!!}` |

### Task 5: Explotar HTTP Basic Authentication / Exploiting HTTP Basic Authentication
**Explicación:** Una ruta protegida con HTTP Basic Auth se fuerza primero con Burp Suite (intrusión manual con el conjunto de contraseñas del diccionario) hasta obtener la flag, y después se automatiza el ataque con Hydra contra el formulario para confirmar la vulnerabilidad.

```bash
hydra -l canderson@gmail.com -P /usr/share/wordlists/rockyou.txt enum.thm http-get /protected -t 4
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag? / ¿Cuál es la flag? | `THM{b4$$1C_AuTTHHH}` |
| 2 | Try using Hydra instead of Burp to brute force the password. / Intenta usar Hydra en lugar de Burp para forzar la contraseña. | `No answer needed` |

### Task 6: OSINT / OSINT
**Explicación:** Tarea introductoria de investigación OSINT que enlaza con la siguiente parte del curso (recopilación de información pasiva).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Click me to proceed to the next task. / Haz clic para pasar a la siguiente tarea. | `No answer needed` |

### Task 7: Conclusión / Conclusion
**Explicación:** Resumen de lo aprendido: cómo los errores verbose, la lógica de reset predecible y la autenticación básica débil permiten comprometer cuentas, y por qué conviene automatizar (Hydra/Burp).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Ensure you fully understand the section before moving on. / Asegúrate de entender bien la sección antes de continuar. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What type of error messages can unintentionally provide attackers with confirmation of valid usernames? | `Verbose errors` |
| 2 | What is the valid email address from the list? | `canderson@gmail.com` |
| 3 | What is the flag? | `THM{50_pr3d1ct4BL333!!}` |
| 4 | What is the flag? | `THM{b4$$1C_AuTTHHH}` |
| 5 | Try using Hydra instead of Burp to brute force the password. | `No answer needed` |

---

**Metodología:** Se despliega el laboratorio y se abre http://enum.thm. Primero se analizan los mensajes de error del formulario para confirmar la existencia de un usuario (errores verbose). Con el email válido se explota la lógica del reset de contraseña (token predecible) y se inicia sesión para obtener la primera flag. Después se fuerza la ruta protegida por HTTP Basic Auth con Burp Suite y, para automatizar, con Hydra, obteniendo la segunda flag. Cierran la room las tareas de OSINT y conclusión.

### Cadena de ataque / Attack Chain

```text
http://enum.thm -> análisis de errores verbose -> confirmación de usuario (canderson@gmail.com) -> reset predecible -> login -> flag THM{50_pr3d1ct4BL333!!} -> HTTP Basic Auth -> Burp Intruder -> flag THM{b4$$1C_AuTTHHH} -> Hydra (automatización)
```

**Learning chain:** Introduction → Authentication Enumeration (verbose errors) → Enumerating Users → Vulnerable Password Reset → HTTP Basic Authentication (Burp + Hydra) → OSINT → Conclusion.

**Lección:** *Los mensajes de error verbose convierten una web en un oráculo de usuarios válidos; una lógica de reset predecible y una HTTP Basic Auth débil permiten comprometer la cuenta sin vulnerabilidades "complicadas". Para el defensor: nunca diferenciar en público "usuario inválido" de "contraseña incorrecta", usar tokens aleatorios y forzar MFA.*

**MITRE ATT&CK:** T1589.001 (Gather Victim Identity Information: Credentials), T1110.003 (Brute Force: Password Spraying), T1110.001 (Brute Force: Password Guessing), T1078 (Valid Accounts)

**Fuente:** [TryHackMe - Enumeration & Brute Force](https://tryhackme.com/room/enumerationbruteforce)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.