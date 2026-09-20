# Chaining Vulnerabilities

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `chainingvulnerabilities` | [TryHackMe](https://tryhackme.com/room/chainingvulnerabilities) | 01 Level Easy | THM | Aplicación web, XSS almacenado, CSRF, panel admin, flag | Medio — encadenamiento de XSS y CSRF para el compromiso de una cuenta privilegiada |

---

**Contexto:** Room práctica sobre encadenamiento de vulnerabilidades (vulnerability chaining). Tras varias tareas conceptuales, la Task 4 entrega una aplicación web con credenciales de bajo privilegio (testuser/password123). Se descubre una XSS almacenada en el perfil de usuario que, ejecutada en el navegador del administrador, permite lanzar peticiones same-origin (la app no utiliza tokens CSRF) para cambiar el email y la contraseña del administrador. Con esas credenciales se accede al panel de administración y se captura la flag; la técnica habilitadora es el Cross-site Scripting.

> **ES:** Encadenar vulnerabilidades "low" para lograr un "high" impacto: la XSS almacenada + la ausencia de tokens CSRF permiten cambiar las credenciales del admin, acceder al panel de administración y capturar la flag.

> **EN:** Chain "low" vulnerabilities for a "high" impact: stored XSS plus the absence of CSRF tokens allows changing the admin credentials, reaching the admin panel and capturing the flag.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Tareas de lectura sobre el concepto de vulnerability chaining: cómo dos o más fallos de bajo riesgo se encadenan para lograr un impacto mayor que el de cada eslabón por separado. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Concepto: ¿qué es el encadenamiento de vulnerabilidades? / What is vulnerability chaining? | `No answer needed` |

### Task 2: Teoría / Theory

**Explicación:** Se repasan los tipos de fallos que suelen encadenarse (XSS, CSRF, SQLi, puertos abiertos, credenciales por defecto, permisos mal configurados, escalada de privilegios) y por qué cada eslabón amplifica el siguiente. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Tipos de vulnerabilidades habitualmente encadenadas / Types of vulnerabilities often chained | `No answer needed` |

### Task 3: Teoría / Theory

**Explicación:** Se profundiza en ejemplos de cadenas reales (web flaws: XSS → CSRF → SQLi; network: puertos abiertos → credenciales por defecto → RCE; PE: permisos → servicio vulnerable → root) y en la mentalidad del atacante. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Ejemplos y defensa: cómo encadenar y cómo evitar las cadenas / Examples and defense | `No answer needed` |

### Task 4: Guided Chain / Cadena guiada

**Explicación:** Se entregan las credenciales de bajo privilegio (testuser/password123). El flujo guiado es: login en la aplicación → descubrir la XSS en el perfil de usuario → alojar y servir script.js → inyectar el payload para que se ejecute en el navegador del administrador → aprovechar la ausencia de tokens CSRF para cambiar el email y la contraseña del admin mediante peticiones same-origin → entrar en el panel de administración → capturar la flag. La vulnerabilidad que permite forzar el cambio de contraseña del admin es el Cross-site Scripting.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | What is the flag in the admin panel? | `THM{57648b8e-3382-47bb-abbc-f125e128f8ab}` |
| 2 | What vulnerability enabled the attacker to force a change in the admin user's password? | `Cross-site Scripting` |

### Task 5: Conclusión / Conclusion

**Explicación:** Se recogen las lecciones de la cadena completa, del fallo de menor impacto al compromiso de la cuenta privilegiada. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Repaso de la cadena y medidas correctivas / Review of the chain and fixes | `No answer needed` |

### Task 6: Conclusión / Conclusion

**Explicación:** Cierre de la room: consolidar qué se ha aprendido sobre la combinación de XSS y CSRF y cómo mitigarla. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Cierre de la room / Room wrap-up | `No answer needed` |

---

**Metodología:** Login con credenciales dadas (testuser/password123) → análisis del perfil de usuario → detección de XSS almacenada → hosting del payload (script.js) → inyección del payload → ejecución en el navegador del administrador → peticiones same-origin para cambiar el email y la contraseña (CSRF sin tokens) → acceso al panel de administración → lectura de la flag del panel.

### Cadena de ataque / Attack Chain

XSS almacenada → ejecución de JavaScript en el contexto del administrador → CSRF sin tokens → cambio de credenciales del administrador → acceso al panel de administración → flag.

**Learning chain:** Concepto de chaining → enumeración de la aplicación web → XSS → CSRF → account takeover → acceso privilegiado.

**Lección:** *Una XSS aparentemente de bajo impacto se convierte en una vulnerabilidad alta cuando se encadena con la ausencia de tokens CSRF: bastan unos pocos eslabones para lograr el control de una cuenta privilegiada.*

**MITRE ATT&CK:** T1059.007 (JavaScript), T1078 (Valid Accounts).

**Fuente:** [TryHackMe - Chaining Vulnerabilities](https://tryhackme.com/room/chainingvulnerabilities)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.