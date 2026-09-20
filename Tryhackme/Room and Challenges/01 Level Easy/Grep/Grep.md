# Grep

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `grep` | [TryHackMe](https://tryhackme.com/room/grep) | 01 Level Easy | THM | Grep, Fuzzing, Password Spray, Enumeración | Resolución de un reto web usando grep y enumeración |

---

**Contexto:** Reto que aterriza el uso de la herramienta `grep` en un caso práctico híbrido: se fuzza la web para descubrir usuarios y subdominios, se aplica password spraying y se usa grep para filtrar la información relevante (credenciales, correos y banderas) del análisis.

> **ES:** Usar grep de forma práctica para localizar credenciales, usuarios y datos sensibles en un servidor comprometido.
> **EN:** Use grep hands-on to locate credentials, users and sensitive data on a compromised server.

## Solucionario

### Task 1: El reto / The Challenge

**Explicación:** Reto de una única tarea que combina la enumeración de usuarios y subdominios con la herramienta `grep`. Se obtienen los hashes y banderas filtrando los resultados del análisis.

1. `ffe60ecaa8bba2f12b43d1a4b15b8f39`
2. `THM{4ec9806d7e1350270dc402ba870ccebb}`
3. `admin@searchme2023cms.grep.thm`
4. `leakchecker.grep.thm`
5. `admin_tryhackme!`

### Tabla unificada de preguntas y respuestas

| Task | Pregunta | Respuesta |
|------|----------|-----------|
| 1.1 | Valor del hash | `ffe60ecaa8bba2f12b43d1a4b15b8f39` |
| 1.2 | Bandera del reto | `THM{4ec9806d7e1350270dc402ba870ccebb}` |
| 1.3 | Correo administrador | `admin@searchme2023cms.grep.thm` |
| 1.4 | Subdominio de leak checker | `leakchecker.grep.thm` |
| 1.5 | Usuario descubierto | `admin_tryhackme!` |

---

**Metodología:** Enumerar usuarios y subdominios de la aplicación, filtrar con grep las respuestas relevantes, descubrir credenciales y hashes, y aplicar password spraying hasta capturar la bandera.

### Cadena de ataque / Attack Chain

```text
Enumeración -> grep sobre respuestas -> descubrir hash/credenciales -> subdominio leak checker -> usuario admin -> bandera
```

**Learning chain:** Enumeration → Grep filtering → Credentials discovery → Subdomain discovery → Flag

**Lección:** *grep convierte un maremágnum de respuestas en datos accionables: filtrar por patrones es lo que permite encontrar el detalle sensible dentro del ruido.*

**MITRE ATT&CK:** N/A (Reto de análisis/enumeración)

**Fuente:** [TryHackMe - Grep](https://tryhackme.com/room/grep)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.