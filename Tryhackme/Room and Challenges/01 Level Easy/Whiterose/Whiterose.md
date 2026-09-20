# Whiterose

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | CTF | `whiterose` | https://tryhackme.com/room/whiterose | 01 Level Easy | TryHackMe | CTF, explotación de aplicación web, flags del reto | Resolución del reto CTF Whiterose obteniendo identificador y dos flags |

---

**Contexto:** Reto CTF en el que se compromete una aplicación web para extraer la información solicitada: un identificador (`842-029-5701`) y dos flags relacionadas con la actualización de dependencias y paquetes. El resumen original conserva únicamente las respuestas posicionales, sin los enunciados de las preguntas.

> **ES:** Resuelve el reto CTF Whiterose explotando la aplicación web para obtener el identificador y las dos flags.
> **EN:** Solve the Whiterose CTF challenge by exploiting the web application to get the identifier and the two flags.

## Solucionario

### Task 1: Compromiso / Compromise

**Explicación:** Se explota la aplicación web del reto. Se obtiene el identificador `842-029-5701` y las dos flags: `THM{4lways_upd4te_uR_d3p3nd3nc!3s}` y `THM{4nd_uR_p4ck4g3s}`.

```
1. 1. 842-029-5701
   2. THM{4lways_upd4te_uR_d3p3nd3nc!3s}
   3. THM{4nd_uR_p4ck4g3s}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `842-029-5701` |
| 2 | *(Pregunta 2 no especificada en el original)* | `THM{4lways_upd4te_uR_d3p3nd3nc!3s}` |
| 3 | *(Pregunta 3 no especificada en el original)* | `THM{4nd_uR_p4ck4g3s}` |

---

**Metodología:** Reconocimiento y análisis de la aplicación web → explotación de la vulnerabilidad encontrada → extracción del identificador y de las dos flags del reto.

### Cadena de ataque / Attack Chain

```text
Acceso a la app web del reto -> análisis y explotación -> identificador 842-029-5701 -> flag de dependencias -> flag de paquetes -> reto completado
```

**Learning chain:** Reconocimiento → explotación web → extracción de identificador → flags de dependencias y paquetes

**Lección:** *Las dependencias y paquetes desactualizados de una aplicación web siguen siendo un vector Real de compromiso: el reto lo simboliza con las dos flags de actualización.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1059 (Command and Scripting Interpreter), T1078 (Valid Accounts)

**Fuente:** [TryHackMe - Whiterose](https://tryhackme.com/room/whiterose)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.