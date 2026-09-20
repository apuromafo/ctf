# Web Application Security

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `webapplicationsecurity` | https://tryhackme.com/room/webapplicationsecurity | 01 Level Easy | TryHackMe | OWASP Top 10 (2021), IDOR, seguridad de aplicaciones web | Comprensión de las principales vulnerabilidades web (OWASP Top 10) y explotación de un IDOR |

---

**Contexto:** Sala introductoria a la seguridad de aplicaciones web: se revisan los conceptos clave del OWASP Top 10 (2021), se responden preguntas sobre los riesgos más comunes (Identification and Authentication Failure, Cryptographic Failures) y se completa un laboratorio que explota un IDOR. El resumen original conserva únicamente las respuestas posicionales, sin los enunciados de las preguntas.

> **ES:** Repasa los conceptos del OWASP Top 10 (2021) y explota un IDOR para obtener la flag del laboratorio.
> **EN:** Review OWASP Top 10 (2021) concepts and exploit an IDOR to capture the lab flag.

## Solucionario

### Task 1: Conceptos básicos / Basic Concepts

**Explicación:** Tarea conceptual: se introduce qué se ejecuta del lado del cliente y cómo interactúa el usuario con la aplicación web. La respuesta es `Browser`.

```
1. Browser
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `Browser` |

### Task 2: OWASP Top 10 (2021) / OWASP Top 10 (2021)

**Explicación:** Se trabajan los riesgos del OWASP Top 10: `Identification and Authentication Failure` (A07) y `Cryptographic Failures` (A02), que representan fallos de autenticación y de criptografía respectivamente.

```
2. 1. Identification and Authentication Failure
   2. Cryptographic Failures
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `Identification and Authentication Failure` |
| 2 | *(Pregunta 2 no especificada en el original)* | `Cryptographic Failures` |

### Task 3: IDOR / Insecure Direct Object Reference

**Explicación:** Laboratorio práctico: manipulando la referencia directa a objetos en las peticiones se accede a recursos ajenos, obteniendo la flag `THM{IDOR_EXPLORED}`.

```
3. THM{IDOR_EXPLORED}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `THM{IDOR_EXPLORED}` |

---

**Metodología:** Revisión de conceptos del OWASP Top 10 → identificación de riesgos de autenticación y criptografía → laboratorio web → manipulación de identificadores en peticiones (IDOR) → acceso a recursos ajenos → obtención de la flag.

### Cadena de ataque / Attack Chain

```text
Entender el OWASP Top 10 (A07 auth failure, A02 crypto failures) -> análisis de la app web -> detectar referencias directas a objetos (IDOR) -> modificar el identificador en la petición -> acceso a recurso de otro usuario -> THM{IDOR_EXPLORED}
```

**Learning chain:** OWASP Top 10 → riesgos de autenticación y criptografía → IDOR → manipulación de parámetros → flag

**Lección:** *Confiar en identificadores directamente referenciados (IDOR) sin verificar la propiedad del recurso permite acceder a datos de otros usuarios con una simple modificación de la petición.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1530 (Data from Cloud Storage Object), T1213 (Data from Information Repositories)

**Fuente:** [TryHackMe - Web Application Security](https://tryhackme.com/room/webapplicationsecurity)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.