# Light

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | challenge | `light` | [TryHackMe](https://tryhackme.com/room/light) | 01 Level Easy | TryHackMe | SQLite, inyección SQL, PHP, web | Caja CTF "Light": inyección SQL en una aplicación web para volcar la base de datos y obtener el usuario `TryHackMeAdmin`, su contraseña y la flag. |

---

**Contexto:** Light es una caja CTF en la que una aplicación web (debido a su luminosidad, "Light") es vulnerable a inyección SQL sobre una base SQLite. Se realiza la extracción del esquema y de las tablas, se vuelcan los usuarios y con la técnica de inyección se obtiene el usuario administrador `TryHackMeAdmin`, su contraseña (`mamZtAuMlrsEy5bp6q17`) y la flag `THM{SQLit3_InJ3cTion_is_SimplE_nO?}`.

> **ES:** Inyección SQL en SQLite de la web: se vuelca el esquema, se extrae el usuario `TryHackMeAdmin`, la contraseña `mamZtAuMlrsEy5bp6q17` y la flag `THM{SQLit3_InJ3cTion_is_SimplE_nO?}`.
> **EN:** SQL injection into SQLite web: dump the schema, extract user `TryHackMeAdmin`, password `mamZtAuMlrsEy5bp6q17` and the flag `THM{SQLit3_InJ3cTion_is_SimplE_nO?}`.

## Solucionario

### Task 1: Flags de Light / Light flags
**Explicación:** En la tarea se debe explotar la inyección SQL del buscador de la aplicación para extraer la información de la base. Con los payloads de inyección sobre SQLite se recupera el nombre del usuario (`TryHackMeAdmin`), su contraseña (`mamZtAuMlrsEy5bp6q17`) y finalmente la flag `THM{SQLit3_InJ3cTion_is_SimplE_nO?}`.

```text
1. 1. TryHackMeAdmin
   2. mamZtAuMlrsEy5bp6q17
   3. THM{SQLit3_InJ3cTion_is_SimplE_nO?}
```

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Usuario administrador de la app | `TryHackMeAdmin` |
| 1 | Contraseña del usuario | `mamZtAuMlrsEy5bp6q17` |
| 1 | Flag final | `THM{SQLit3_InJ3cTion_is_SimplE_nO?}` |

---

**Metodología:** Se identificó que el campo de búsqueda de la aplicación es inyectable (`'`), se comprobó la base SQLite y se extrajo el esquema mediante inyección UNION. Se recorrieron las tablas de usuarios, se obtuvo el hash/la contraseña del `TryHackMeAdmin` y, con un payload de inyección sobre la cadena o el hash, se recuperó la flag.

### Cadena de ataque / Attack Chain

```text
Detección del campo inyectable -> SQLi en SQLite -> enumeración del esquema -> dump de usuarios -> TryHackMeAdmin:mamZtAuMlrsEy5bp6q17 -> flag
```

**Learning chain:** web app recon -> SQL injection test -> UNION-based SQLi -> schema dump -> credentials -> flag

**Lección:** *Un campo de búsqueda con concatenación SQL directa permite volcar entero el esquema; incluso la cadena de un hash/flag se puede extraer carácter a carácter con inyección SQL.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1505.003 - Web Server Configuration, T1003 (OS Credential Dumping)

**Fuente:** [TryHackMe - Light](https://tryhackme.com/room/light)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.