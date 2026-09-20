# Cold VVars

| Campo | Valor |
|---|---|
| Dificultad | Medium |
| Tipo | CTF |
| Slug | coldvvars |
| Link | https://tryhackme.com/room/coldvvars |
| Sección | 02 Level Medium |
| Fuente | TryHackMe |
| Componentes | Variables de entorno, enumeración |
| Impacto | Obtención de credenciales y flags ocultas |

---

**Contexto:** Cold VVars es una sala de TryHackMe de dificultad media que se centra en la explotación de variables de entorno mal configuradas. El participante debe enumerar el sistema, identificar variables de entorno sensibles expuestas y utilizarlas para obtener las flags de la sala.

## Solucionario

### Task 1: Resolución del desafío

**Explicación:** Se resolvieron las 2 preguntas/flags de la sala mediante enumeración de variables de entorno y extracción de datos sensibles.

1. ae39f419ce0a3a26f15db5aaa7e446ff
2. 42f191b937ea71cd2052a06a7a08585a

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag 1 | `ae39f419ce0a3a26f15db5aaa7e446ff` |
| 2 | Flag 2 | `42f191b937ea71cd2052a06a7a08585a` |

---

**Metodología:** Enumeración de variables de entorno, identificación de valores sensibles, extracción de credenciales y obtención de flags.

**Learning chain:** Enumeración del sistema → inspección de variables de entorno → detección de valores sensibles → uso de credenciales → obtención de flags.

**Lección:** *Las variables de entorno mal configuradas exponen credenciales y datos sensibles que comprometen toda la seguridad del sistema.*

**MITRE ATT&CK:** T1552 - Unsecured Credentials, T1082 - System Information Discovery

**Fuente:** [TryHackMe - Cold VVars](https://tryhackme.com/room/coldvvars)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.