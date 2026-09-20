# LDAP Injection

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `ldapinjection` | [TryHackMe](https://tryhackme.com/room/ldapinjection) | 01 Level Easy | TryHackMe | LDAP, inyección LDAP, filtros LDAP, blind LDAP injection | Comprender y explotar la inyección LDAP (básica y ciega) para autenticarse y extraer información de un directorio LDAP. |

---

**Contexto:** La sala explica qué es LDAP y cómo funciona la autenticación basada en LDAP. Se introduce el concepto de inyección LDAP: cómo manipular los filtros LDAP concatenando operadores y condiciones `(&(condition)(...)` para alterar la consulta del servidor. Se practica la inyección básica (bypass de autenticación) y la inyección ciega (blind LDAP, `*)(|(&` etc.) para verificar condiciones sin ver la salida directa, recuperando distintas flags del directorio.

> **ES:** Aprendizaje y práctica de LDAP injection: bypass de la autenticación de un panel y explotación de consultas LDAP (básica y ciega) para extraer datos.
> **EN:** Learning and practice of LDAP injection: bypassing a panel's authentication and exploiting LDAP queries (basic and blind) to extract data.

## Solucionario

### Task 1: Introducción a LDAP / LDAP intro
**Explicación:** Tarea introductoria sobre qué es LDAP. No requiere respuesta.

```text
1. No answer needed
```

### Task 2: Filtros LDAP / LDAP filters
**Explicación:** Explicación de los filtros LDAP. No requiere respuesta.

```text
2. No answer needed
```

### Task 3: Preparación del entorno / Environment preparation
**Explicación:** Tarea de preparación. No requiere respuesta.

```text
3. No answer needed
```

### Task 4: Enumeración / Enumeration
**Explicación:** Identificación de la aplicación vulnerable. No requiere respuesta.

```text
4. No answer needed
```

### Task 5: Inyección básica de LDAP / Basic LDAP injection
**Explicación:** Se explota la inyección LDAP básica inyectando un payload en el campo de usuario/contraseña para alterar el filtro y falsear la condición de autenticación. Al loguearse con éxito en la aplicación se obtiene la flag `THM{!b451c_ld4p_inj3ct1ON!}`.

```text
5. THM{!b451c_ld4p_inj3ct1ON!}
```

### Task 6: Continuación del laboratorio / Continuing the lab
**Explicación:** Se prepara el escenario de la inyección ciega. No requiere respuesta.

```text
6. No answer needed
```

### Task 7: Inyección ciega (Blind LDAP) / Blind LDAP injection
**Explicación:** Con la inyección ciega se usa un payload del tipo `*)(|(&` para neutralizar el filtro y comprobar verdadero/falso. Mediante la respuesta observable de la aplicación o del panel se confirma la condición y se extrae la información, obteniendo la flag `THM{!!bl1nDLd4P1nj3ct10n!!}`.

```text
7. THM{!!bl1nDLd4P1nj3ct10n!!}
```

### Task 8: Conclusión / Conclusion
**Explicación:** Tarea final. No requiere respuesta.

```text
8. No answer needed
```

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Introducción a LDAP | `No answer needed` |
| 2 | Filtros LDAP | `No answer needed` |
| 3 | Preparación del entorno | `No answer needed` |
| 4 | Enumeración | `No answer needed` |
| 5 | Flag de la inyección básica | `THM{!b451c_ld4p_inj3ct1ON!}` |
| 6 | Continuación del laboratorio | `No answer needed` |
| 7 | Flag de la inyección ciega | `THM{!!bl1nDLd4P1nj3ct10n!!}` |
| 8 | Conclusión | `No answer needed` |

---

**Metodología:** Tras repasar la teoría de LDAP y los filtros, se desplegó la aplicación vulnerable y se probaron distintos payloads en los campos de autenticación. Con la inyección básica se logró falsear la consulta LDAP y entrar en el panel, capturando la primera flag. Después se explotó la inyección LDAP ciega usando condiciones que devolvían distinto resultado según el valor de la pregunta, extrajo la segunda flag mediante la comparación de respuestas verdaderas y falsas.

### Cadena de ataque / Attack Chain

```text
Teoría LDAP -> filtros LDAP -> despliegue del lab -> inyección LDAP básica (bypass de autenticación) -> flag 1 -> inyección LDAP ciega (blind) -> condición true/false -> flag 2
```

**Learning chain:** LDAP -> filtros -> SQL/LDAP injection -> bypass de login -> blind LDAP -> true/false oracle -> extracción de flags

**Lección:** *Los filtros LDAP construidos concatenando directamente la entrada del usuario son vulnerables a inyección: manipular operadores lógicos permite autenticarse sin credenciales y, con técnicas ciegas, extraer información adicional.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1059 (Command and Scripting Interpreter), T1505.003 - inyección de filtros de directorio

**Fuente:** [TryHackMe - LDAP Injection](https://tryhackme.com/room/ldapinjection)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.