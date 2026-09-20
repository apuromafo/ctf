# SQHell
| **Dificultad** | Medium |
| **Tipo** | Challenge / CTF |
| **Slug** | `sqhell` |
| **Link** | [TryHackMe](https://tryhackme.com/room/sqhell) |
| **Sección** | Web Application Security / SQL Injection |
| **Fuente** | TryHackMe |
| **Componentes** | SQL Injection, UNION-based, error-based, blind SQLi, inyección en cookies/headers, MySQL |
| **Impacto** | Reto CTF que encadena cinco vulnerabilidades de inyección SQL en distintos puntos de la aplicación (parámetros, cookies, headers, etc.) para obtener cinco flags. |
---
**Contexto:** SQHell es un reto de inyección SQL que obliga a encontrar cinco flags a través de diferentes vectores de la misma aplicación web. Cada flag requiere localizar el punto de inyección (parámetro GET/POST, cookie, cabecera HTTP), determinar el tipo de SQLi (UNION-based, error-based, blind/time-based) y extraer la información de la base de datos MySQL. El reto refuerza la enumeración manual y el uso de herramientas como `sqlmap` o peticiones `curl` personalizadas.
## Solucionario
### Task 1: Flag 1 / Flag 1
**Explicación:** Primera inyección SQL de la aplicación, normalmente en un parámetro de la URL. Se determina el número de columnas, se usa la técnica UNION/error-based para volcar datos y se obtiene la flag 1.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. What is Flag 1? | `THM{FLAG1:E786483E5A53075750F1FA792E823BD2}` |
### Task 2: Flag 2 / Flag 2
**Explicación:** Segundo punto de inyección, típicamente en una cookie o en un parámetro POST. Se adapta el payload al nuevo contexto y se extrae la flag 2.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. What is Flag 2? | `THM{FLAG2:C678ABFE1C01FCA19E03901CEDAB1D15}` |
### Task 3: Flag 3 / Flag 3
**Explicación:** Tercer vector de inyección SQL (cabecera HTTP o endpoint adicional). Se reutiliza la lógica de extracción adaptada a la consulta vulnerable para obtener la flag 3.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. What is Flag 3? | `THM{FLAG3:97AEB3B28A4864416718F3A5FAF8F308}` |
### Task 4: Flag 4 / Flag 4
**Explicación:** Cuarto punto de inyección, a menudo con filtrado/WAF parcial que obliga a usar técnicas de evasión o inyección blind. Se obtiene la flag 4.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. What is Flag 4? | `THM{FLAG4:BDF317B14EEF80A3F90729BF2B426BEF}` |
### Task 5: Flag 5 / Flag 5
**Explicación:** Quinta y última inyección, la de mayor dificultad. Se combinan las técnicas aprendidas (blind/time-based o subconsultas anidadas) para extraer la flag 5.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. What is Flag 5? | `THM{FLAG5:B9C690D3B914F7038BA1FC65B3FDF3C8}` |
---
**Metodología:** Enumerar la aplicación y sus parámetros → identificar cada punto de inyección → determinar tipo de SQLi (UNION, error-based, blind/time-based) → adaptar payloads al contexto (GET/POST/cookie/header) → extraer datos de la base MySQL y capturar cada flag.
### Cadena de ataque / Attack Chain
```
Reconocimiento web -> identificación de parámetros -> prueba de inyección -> determinación de columnas/DB -> explotación UNION/blind -> extracción de flags 1-5
```
**Learning chain:** enumeración → detección de SQLi → explotación manual → técnicas avanzadas (blind/evasión) → captura de flags.
**Lección:** *La inyección SQL no siempre está en el parámetro evidente: cookies, cabeceras y endpoints secundarios también son vectores, y cada contexto exige adaptar el payload.*
**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1565.001 (Stored Data Manipulation), T1078 (Valid Accounts).
**Fuente:** [TryHackMe - SQHell](https://tryhackme.com/room/sqhell)
---
## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
