# Weaponizing Vulnerabilities

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Conceptos / Explotación | weaponizingvulnerabilities | https://tryhackme.com/room/weaponizingvulnerabilities | 02 Level Medium | TryHackMe | Exploit chaining, 0-day, n-day, Proof of Concept, parches, privilege escalation, persistencia | Compromiso total del sistema mediante la construcción y encadenamiento de exploits |

---

**Contexto:** La sala **Weaponizing Vulnerabilities** aborda el proceso de convertir una vulnerabilidad en una herramienta de ataque funcional ("weaponización"). Se repasan las diferencias entre vulnerabilidades **0-day** y **n-day**, el papel del *Proof of Concept* en el ciclo de vida del exploit y el momento del parche. Finalmente se estudia el **exploit chaining**: encadenar varios fallos para lograr acceso, escalar privilegios y mantener persistencia, con una validación práctica en el laboratorio.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:**

Presentación de la sala y de la metodología de weaponización de vulnerabilidades. No requiere una respuesta concreta.

Respuesta: `No answer needed`

### Task 2: Clasificación del exploit / Exploit classification
**Explicación:**

Se identifican los tipos de exploits según el alcance del compromiso; la respuesta es el tipo de exploit dirigido a comprometer un servicio remoto.

Respuesta: `remote exploit`

### Task 3: Ciclo de vida del exploit / Exploit lifecycle
**Explicación:**

Se enumeran las etapas de la vida de una vulnerabilidad: el estado de desconocimiento inicial (0-day), la demostración funcional de la falla mediante un Proof of Concept y la liberación del parche que la corrige.

1. `0-day`
2. `Proof of concept`
3. `patch`

### Task 4: Vulnerabilidades conocidas / n-day
**Explicación:**

Una vez publicado el parche, el software pasa a considerarse n-day; se confirma si el sistema objetivo está ya actualizado.

1. `yea`
2. `n-day`

### Task 5: Encadenamiento de exploits / Exploit chaining
**Explicación:**

Se repasan los componentes de una cadena de ataque completa: combinar exploits, escalar privilegios y establecer persistencia.

1. `Exploit chaining`
2. `Privilege escalation`
3. `persistence`

### Task 6: Validación en el laboratorio / Lab validation
**Explicación:**

Se ejecuta la validación práctica del encadenamiento en la máquina de laboratorio, recogiendo el usuario, los privilegios alcanzados y la flag final.

1. `undefined`
2. `nt authority\system`
3. `THM{010101_PAWNED}`
4. `2`

### Task 7: Verificación / Verification
**Explicación:**

Confirmación de que el encadenamiento de exploits permitió alcanzar el objetivo.

Respuesta: `yea`

### Task 8: Cierre / Conclusion
**Explicación:**

Recapitulación final de la sala. No requiere respuesta.

Respuesta: `No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Introducción a la sala | `No answer needed` |
| 2 | Tipo de exploit para comprometer un servicio remoto | `remote exploit` |
| 3.1 | Vulnerabilidad desconocida antes del parche | `0-day` |
| 3.2 | Demostración funcional de la vulnerabilidad | `Proof of concept` |
| 3.3 | Corrección oficial de la vulnerabilidad | `patch` |
| 4.1 | ¿El software objetivo está actualizado/parcheado? | `yea` |
| 4.2 | Vulnerabilidad conocida tras el parche | `n-day` |
| 5.1 | Combinación de varias vulnerabilidades para lograr un objetivo | `Exploit chaining` |
| 5.2 | Obtención de mayores privilegios tras el acceso inicial | `Privilege escalation` |
| 5.3 | Mantenimiento del acceso en el tiempo | `persistence` |
| 6.1 | Usuario identificado en el sistema comprometido | `undefined` |
| 6.2 | Autoridad máxima alcanzada en Windows | `nt authority\system` |
| 6.3 | Flag obtenida en el laboratorio | `THM{010101_PAWNED}` |
| 6.4 | Conteo relacionado con la validación | `2` |
| 7 | ¿Se logró el compromiso completo? | `yea` |
| 8 | Reflexión final | `No answer needed` |

---

**Metodología:** Estudio del ciclo de vida del exploit desde la perspectiva ofensiva: identificación de la vulnerabilidad (0-day frente a n-day), desarrollo o uso de un Proof of Concept, seguimiento de la ventana previa al parche y composición de una cadena de ataque (acceso inicial → escalada de privilegios → persistencia), validada en el laboratorio de la sala.

### Cadena de ataque / Attack Chain

```text
Vulnerabilidad (0-day / n-day) → PoC / exploit → acceso remoto → privilege escalation → persistencia → validación (flag)
```

**Learning chain:** Concepto de weaponización → 0-day vs n-day → Proof of Concept → ciclo del parche → exploit chaining → privilege escalation → persistence → validación en laboratorio.

**Lección:** *La distancia entre un PoC y un exploit operativo es mínima: parchear pronto y comprender el encadenamiento de fallos reduce drásticamente la superficie de compromiso.*

**MITRE ATT&CK:** T1190 Exploit Public-Facing Application · T1210 Exploitation of Remote Services · T1068 Exploitation for Privilege Escalation · T1059 Command and Scripting Interpreter · T1547 Boot or Logon Autostart Execution.

**Fuente:** [TryHackMe - Weaponizing Vulnerabilities](https://tryhackme.com/room/weaponizingvulnerabilities)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.