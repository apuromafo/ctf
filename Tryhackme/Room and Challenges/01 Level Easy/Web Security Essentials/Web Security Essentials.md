# Web Security Essentials

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `websecurityessentials` | https://tryhackme.com/room/websecurityessentials | 01 Level Easy | TryHackMe | Fundamentos de seguridad web, OWASP, gestión de parches, detección host/signature, flags | Comprensión del ecosistema de seguridad de aplicaciones web y servidores con un laboratorio final de flags |

---

**Contexto:** Sala de fundamentos de seguridad para aplicaciones web y servidores: quién es responsable de la seguridad, el flujo de una petición web, la gestión de vulnerabilidades y parches, los sistemas de detección (host-based y signature-based) y un laboratorio final con tres flags. El resumen original conserva únicamente las respuestas posicionales, sin los enunciados de las preguntas.

> **ES:** Fundamentos de seguridad web: responsabilidades, flujo de peticiones, gestión de parches, detección por hosts y firmas, y laboratorio de flags.
> **EN:** Web security essentials: responsibilities, request flow, patch management, host and signature-based detection, and a flag lab.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Tarea introductoria de la sala. No requiere respuesta.

```
1. No answer needed
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `No answer needed` |

### Task 2: Responsabilidad de la seguridad / Security Responsibility

**Explicación:** Se define quién asume la responsabilidad de la seguridad de la aplicación: la respuesta confirma `Yea` y el propietario es `Web App Owner`.

```
2. 1. Yea
   2. Web App Owner
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `Yea` |
| 2 | *(Pregunta 2 no especificada en el original)* | `Web App Owner` |

### Task 3: Flujo de una petición web / Web Request Flow

**Explicación:** Se analiza el recorrido de una petición: el usuario envía una `Request`, el servidor Apache la procesa y el destino final es la `Host Machine`.

```
3. 1. Request
   2. Apache
   3. Host Machine
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `Request` |
| 2 | *(Pregunta 2 no especificada en el original)* | `Apache` |
| 3 | *(Pregunta 3 no especificada en el original)* | `Host Machine` |

### Task 4: Vulnerabilidades y parches / Vulnerabilities and Patch Management

**Explicación:** Se identifican los mecanismos de respuesta a vulnerabilidades: la acción correctiva se llama `Mitigation` y su proceso de aplicación periódica es `Patch Management`.

```
4. 1. Mitigation
   2. Patch Management
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `Mitigation` |
| 2 | *(Pregunta 2 no especificada en el original)* | `Patch Management` |

### Task 5: Sistemas de detección / Detection Systems

**Explicación:** Se repasan los sistemas de detección: los que protegen un equipo individual son `Host-Based` y los que detectan por patrones conocidos son `Signature-Based`.

```
5. 1. Host-Based
   2. Signature-Based
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `Host-Based` |
| 2 | *(Pregunta 2 no especificada en el original)* | `Signature-Based` |

### Task 6: Flags del laboratorio / Lab Flags

**Explicación:** Laboratorio final con las tres flags: `THM{web_app_secured!}`, `THM{server_security_expert!}` y `THM{the_final_security_layer!}`.

```
6. 1. THM{web_app_secured!}
   2. THM{server_security_expert!}
   3. THM{the_final_security_layer!}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `THM{web_app_secured!}` |
| 2 | *(Pregunta 2 no especificada en el original)* | `THM{server_security_expert!}` |
| 3 | *(Pregunta 3 no especificada en el original)* | `THM{the_final_security_layer!}` |

### Task 7: Conclusión / Conclusion

**Explicación:** Tarea de cierre de la sala. No requiere respuesta.

```
7. No answer needed
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `No answer needed` |

---

**Metodología:** Fundamentos del ecosistema web → responsabilidades de seguridad → flujo de peticiones → gestión de parches → modelos de detección → laboratorio con flags.

### Cadena de ataque / Attack Chain

```text
Conceptos de seguridad web -> responsable (Web App Owner) -> Request -> Apache -> Host Machine -> Mitigation y Patch Management -> detección Host-Based y Signature-Based -> flags del laboratorio
```

**Learning chain:** Responsabilidad → flujo de la petición → gestión de vulnerabilidades → sistemas de detección → laboratorio de flags

**Lección:** *La seguridad de una aplicación web se sostiene sobre la combinación de responsabilidad del propietario, gestión de parches y sistemas de detección que combinan modelos basados en hosts y en firmas.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1059 (Command and Scripting Interpreter), T1078 (Valid Accounts)

**Fuente:** [TryHackMe - Web Security Essentials](https://tryhackme.com/room/websecurityessentials)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.