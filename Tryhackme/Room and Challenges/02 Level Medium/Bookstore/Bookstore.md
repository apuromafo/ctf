# Bookstore
| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `bookstore` |
| **Link** | [TryHackMe](https://tryhackme.com/room/bookstore) |
| **Sección** | Web Exploitation / Application Security |
| **Fuente** | Writeup de TryHackMe |
| **Componentes** | Web application analysis, hash extraction, vulnerability assessment |
| **Impacto** | Enseña a analizar aplicaciones web para extraer hashes de credenciales y identificar vulnerabilidades en el diseño de la aplicación. |
---
**Contexto:** Bookstore es una sala de TryHackMe que presenta una aplicación web de tienda de libros con vulnerabilidades. El participante debe enumerar la aplicación, extraer hashes de usuarios y identificar debilidades en la arquitectura de la web para obtener las flags.
*EN: Bookstore is a TryHackMe room presenting a vulnerable book store web application. The participant must enumerate the application, extract user hashes, and identify architectural weaknesses to obtain the flags.*
## Solucionario
### Task 1 — Web Enumeration
**Explicación:** Se explora la aplicación web de la tienda de libros para identificar información sensible expuesta. Se extraen hashes de usuarios de la base de datos expuesta o de componentes mal configurados.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the first hash? | `4ea65eb80ed441adb68246ddf7b964ab` |
| 2 | What is the second hash? | `e29b05fba5b2a7e69c24a450893158e3` |
---
**Metodología:** Enumeración de la aplicación web → inspección de endpoints y parámetros → identificación de hashes expuestos → análisis de vulnerabilidades de diseño.
**Learning chain:** aplicación web → endpoints → hashes → análisis → flags.
**Lección:** *Exponer hashes de usuarios en respuestas web o APIs sin protección es un indicador crítico de mala configuración que permite a un atacante iniciar ataques de cracking offline.*
**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1005 (Data from Local System), T1592.002 (Gather Victim Host Information: Software).
**Fuente:** [TryHackMe - Bookstore](https://tryhackme.com/room/bookstore)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
