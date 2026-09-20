# Intro to GraphQL Hacking

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `introtographqlhacking` | https://tryhackme.com/room/introtographqlhacking | 01 Level Easy | TryHackMe | GraphQL / queries & mutations / endpoints (/graphql) / introspection / schema / SQL injection | Entender GraphQL, localizar sus endpoints, enumerar el esquema mediante introspección y explotar una inyección SQL a través de una query. |

---

**Contexto:** La room introduce GraphQL y su hacking desde cero: qué es GraphQL (un lenguaje de consulta para APIs), la búsqueda de endpoints GraphQL (típicamente `/graphql`), las vulnerabilidades más comunes, la **introspección** (que permite enumerar el esquema completo en producción), y la explotación de una **inyección SQL** mediante queries. Incluye una máquina de práctica: al inspeccionar el esquema se descubren los tipos **Query, User y Post**, se abusan los nombres de columnas para obtener el email del usuario **bob** y se inyecta SQL para leer la flag.

> **ES:** Hacking de APIs GraphQL: qué es GraphQL, descubrir endpoints, enumerar el esquema con introspection, y explotar SQL injection via queries, con la maquina de practica y sus flags.
> **EN:** GraphQL API hacking: what GraphQL is, discovering endpoints, enumerating the schema via introspection, and exploiting SQL injection through queries, with the practice machine and its flags.

## Solucionario

### Task 1: Introduction / Introducción

**Explicación:** Presentación de la room y despliegue de la máquina de práctica. Se motivan los riesgos de exponer APIs GraphQL sin proteger. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Deploy the machine and read the introduction. / Despliega la máquina y lee la introducción. | `No answer needed` |

### Task 2: Understanding GraphQL / Entendiendo GraphQL

**Explicación:** Conceptos de GraphQL: un lenguaje de consulta y un runtime para APIs que permite pedir exactamente los datos que se necesitan con una única petición a `/graphql`. Todo el esquema gira en torno a **queries** (lectura), **mutations** (escritura) y los tipos que las componen. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Read and understand the GraphQL basics. / Lee y comprende los conceptos básicos de GraphQL. | `No answer needed` |

### Task 3: Searching for GraphQL Endpoints / Buscando endpoints GraphQL

**Explicación:** Metodología para descubrir endpoints GraphQL: fuzzing de rutas comunes (`/graphql`, `/graphiql`, `/api`), análisis de la respuesta y uso de herramientas de descubrimiento. Como GraphQL usa un único endpoint, encontrarlo da acceso a prompt de introspección. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Practice discovering GraphQL endpoints. / Practica el descubrimiento de endpoints GraphQL. | `No answer needed` |

### Task 4: Common GraphQL Vulnerabilities / Vulnerabilidades comunes de GraphQL

**Explicación:** Lista de vulnerabilidades típicas de GraphQL: introspección habilitada en producción, queries costosas que permiten DoS, autorización insuficiente por objeto/campo y combinación con inyecciones clásicas (SQL, NoSQL). No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Review the common GraphQL vulnerabilities. / Revisa las vulnerabilidades comunes de GraphQL. | `No answer needed` |

### Task 5: Understanding Introspection / Entendiendo la introspección

**Explicación:** La introspección GraphQL permite consultar el propio esquema. En la práctica, tras una query de introspección aparecen dos objetos de consulta: **User** y falta **Post** (junto con la query base Query). Como la introspección no oculta los nombres de las columnas, se construye una query que las lista y revela el email del usuario **bob**: **bob@graphql.thm**.

```graphql
query {
  __schema {
    types { name fields { name } }
  }
}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | There are two queries after the introspection, namely User, and XXXX. What is the missing query? / Tras la introspección hay dos queries: User y XXXX. ¿Cuál es la query que falta? | `Post` |
| 2 | Challenge! Since you're able to disclose the column names, what is the email of the user named bob? / Reto: ya que puedes ver los nombres de las columnas, ¿cuál es el email del usuario llamado bob? | `bob@graphql.thm` |

### Task 6: GraphQL SQL Injection / Inyección SQL en GraphQL

**Explicación:** Las queries GraphQL pueden fragmentarse o manipularse para inyectar SQL en el backend si no hay consultas parametrizadas. Inyectando en el campo correspondiente se logra hacer que la base de datos devuelva la flag.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag? / ¿Cuál es la flag? | `GRAPHQL{sQl_1Nj3cti0n}` |

### Task 7: Securing GraphQL / Asegurando GraphQL

**Explicación:** Medidas para proteger GraphQL: deshabilitar la introspección en producción, limitar la profundidad y complejidad de las queries, autorización por campo y uso de consultas parametrizadas/preparadas contra inyecciones. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Review the securing best practices. / Revisa las buenas prácticas de seguridad. | `No answer needed` |

### Task 8: Conclusion / Conclusión

**Explicación:** Recapitulación de la room: descubrimiento de endpoints, introspección, enumeración y explotación, junto a referencias para profundizar. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Read the conclusion. / Lee la conclusión. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | There are two queries after the introspection, namely User, and XXXX. What is the missing query? | `Post` |
| 2 | Challenge! Since you're able to disclose the column names, what is the email of the user named bob? | `bob@graphql.thm` |
| 3 | What is the flag? | `GRAPHQL{sQl_1Nj3cti0n}` |

---

**Metodología:** Enumeración y explotación de una API GraphQL: (1) entender como funciona el lenguaje de consulta y su schema; (2) descubrir el endpoint GraphQL en la máquina de práctica; (3) identificar vulnerabilidades comunes; (4) abusar de la introspección para enumerar el esquema y los nombres de columnas (tipos Query/User/Post) y extraer datos (email de bob); (5) explotar la inyección SQL a traves de la query para obtener la flag; (6) repasar las medidas de endurecimiento.

### Cadena de ataque / Attack Chain

```text
Descubrir /graphql -> introspection del schema -> enumerar tipos (User, Post) y columnas -> abusar de columnas -> email bob@graphql.thm -> SQL injection en query -> GRAPHQL flag
```

**Learning chain:** GraphQL -> endpoints -> vulnerabilidades -> introspection -> enumeracion de columnas -> SQLi -> flag.

**Lección:** *Una API GraphQL con introspección activa en producción convierte el endpoint en un mapa sin censura del modelo de datos: si además hay SQLi, enumerar el esquema es el primer paso de la exfiltración.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1059 (Command and Scripting Interpreter), T1005 (Data from Local System)

**Fuente:** [TryHackMe - Intro to GraphQL Hacking](https://tryhackme.com/room/introtographqlhacking)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.