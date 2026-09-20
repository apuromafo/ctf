# CSRF

| Campo | Valor |
|-------|-------|
| **Dificultad** | Medium |
| **Tipo** | CTF / Web |
| **Slug** | csrf |
| **Link** | https://tryhackme.com/room/csrfV2 |
| **Sección** | 02 Level Medium |
| **Fuente** | TryHackMe |
| **Componentes** | CSRF, Web Security, Token Validation, Session Management |
| **Impacto** | Alto — Suplantación de acciones de usuario autenticado mediante solicitudes forjadas |

---

**Contexto:** Esta sala cubre Cross-Site Request Forgery (CSRF), una vulnerabilidad web que permite a un atacante inducir a un usuario autenticado a realizar acciones no deseadas. Se exploran técnicas de protección como tokens CSRF, políticas same-origin y verificación de referer, así como ataques que las evaden.

## Solucionario

### Task 1: Conceptos básicos de CSRF

**Explicación:** Se presentan los fundamentos de CSRF y se introduce la primera pregunta sobre la sala.

1. No answer needed

### Task 2: Tipos de ataques CSRF

**Explicación:** Se analizan diferentes tipos de ataques CSRF y sus vectores de entrega.

1. No answer needed
2. 1. d
   2. yea

### Task 3: Uso de herramientas

**Explicación:** Se describe el uso de herramientas y formatos de payload para CSRF.

3. 1. .swf
   2. Asynchronous

### Task 4: Explotación práctica

**Explicación:** Se realizan ataques CSRF prácticos contra la aplicación de la sala, obteniendo flags que validan el éxito del ataque.

4. 1. THM{SUCCESSFUL_ATTACK}
   2. THM{INVALID_CSRF_TOKEN}
   3. nay

### Task 5: Protección con tokens

**Explicación:** Se implementan y prueban mecanismos de protección con tokens CSRF, verificando su correcto funcionamiento.

5. 1. GB82MYBANK5699
   2. GB82MYBANK5697
   3. THM{SECURED_CSRF}
   4. csrf_token
   5. yea

### Task 6: Ataques avanzados y tokens

**Explicación:** Se explotan debilidades en la implementación de tokens y gestión de sesiones.

6. 1. 7kRt2x9LpQyW
   2. THM{LOGGED_OUT}
   3. THM{ATTACK_DETECTED}
   4. THM{USER_IS_B@NNED}

### Task 7: Defensas contra CSRF

**Explicación:** Se examinan las defensas estándar contra CSRF y su efectividad.

7. 1. same-origin policy
   2. yea
   3. referer

### Task 8: Escenarios avanzados

**Explicación:** Se presentan escenarios complejos de CSRF que combinan múltiples técnicas.

8. nay

### Task 9: Cierre

**Explicación:** Pregunta final de cierre de la sala.

9. No answer needed

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Conceptos básicos | `No answer needed` |
| 2.1 | Tipo de ataque | `d` |
| 2.2 | Confirmación | `yea` |
| 3.1 | Formato de archivo | `.swf` |
| 3.2 | Tipo de carga | `Asynchronous` |
| 4.1 | Flag de ataque exitoso | `THM{SUCCESSFUL_ATTACK}` |
| 4.2 | Token inválido | `THM{INVALID_CSRF_TOKEN}` |
| 4.3 | Confirmación | `nay` |
| 5.1 | Número de cuenta | `GB82MYBANK5699` |
| 5.2 | Cuenta alternativa | `GB82MYBANK5697` |
| 5.3 | Flag CSRF seguro | `THM{SECURED_CSRF}` |
| 5.4 | Nombre del token | `csrf_token` |
| 5.5 | Confirmación | `yea` |
| 6.1 | Token expuesto | `7kRt2x9LpQyW` |
| 6.2 | Flag logout | `THM{LOGGED_OUT}` |
| 6.3 | Flag ataque detectado | `THM{ATTACK_DETECTED}` |
| 6.4 | Flag baneado | `THM{USER_IS_B@NNED}` |
| 7.1 | Política de seguridad | `same-origin policy` |
| 7.2 | Confirmación | `yea` |
| 7.3 | Cabecera de verificación | `referer` |
| 8 | Escenario avanzado | `nay` |
| 9 | Cierre | `No answer needed` |

---

**Metodología:** Análisis de formulario y parámetros → Generación de payload CSRF → Inyección en página controlada por el atacante → Ejecución forzada en víctima autenticada → Validación con flags.

**Learning chain:** Enumeración de endpoints → Construcción de PoC → Manipulación de tokens → Bypass de defensas → Obtención de flags

**Lección:** *Un token CSRF válido por sí solo no garantiza seguridad; la implementación debe validar integridad, unicidad y caducidad.*

**MITRE ATT&CK:**
- T1189 — Drive-by Compromise
- T1534 — Internal Spearphishing

**Fuente:** [TryHackMe - CSRF](https://tryhackme.com/room/csrfV2)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.