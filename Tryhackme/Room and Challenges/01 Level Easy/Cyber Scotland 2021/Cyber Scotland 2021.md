# Cyber Scotland 2021

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|-------------|---------|
| Easy | walkthrough | `cyberscotland2021` | [TryHackMe](https://tryhackme.com/room/cyberscotland2021) | 01 Level Easy | THM | Reconocimiento, SQL Server, Microsoft SQL Bruter, OSINT | Investigación OSINT y acceso a SQL Server |

> **Objeto:** Investigar un objetivo vinculado a Cyber Scotland 2021: descubrir pistas con OSINT, obtener acceso a una base de datos SQL Server y recuperar los flags.

---

**Contexto:** Sala con formato de reto/CTF asociada a Cyber Scotland 2021. Combina reconocimiento de servicios, enumeración de SQL Server, fuerza bruta con Microsoft SQL Bruter y pistas de OSINT que conducen a la cadena de compromiso y al flag final.

> **ES:** Combina reconocimiento, SSH, SQL Server y pistas OSINT para recorrer la cadena hasta los flags.
> **EN:** Combines reconnaissance, SSH, SQL Server and OSINT clues to walk the chain of compromise up to the flags.

## Solucionario

### Task 1: Reconocimiento / Reconnaissance
**Explicación:** Tarea introductoria de reconocimiento inicial.

No answer needed

### Task 2: Exploración / Scanning
**Explicación:** Exploración de puertos y servicios del objetivo.

1. No answer needed
2. No answer needed

### Task 3: Enumeración y explotación / Enumeration and Exploitation
**Explicación:** Enumeración de servicios y uso de herramientas de fuerza bruta contra SQL Server.

1. root
2. No answer needed
3. No answer needed
4. Microsoft SQL Bruter
5. No answer needed
6. No answer needed
7. No answer needed

### Task 4: OSINT y flag final / OSINT and Final Flag
**Explicación:** Las pistas OSINT conducen a la localización y al flag final de la sala.

1. 08081 570087
2. No answer needed
3. Inverkeithing
4. No answer needed
5. SBRC{ODhiOTQ3ZTk0NzJhMWI1NTE5MGUyY2Vj}

### Tabla unificada de preguntas y respuestas

| Task | Pregunta | Respuesta |
|------|----------|-----------|
| 1 | — | `No answer needed` |
| 2.1 | — | `No answer needed` |
| 2.2 | — | `No answer needed` |
| 3.1 | Usuario de acceso | `root` |
| 3.2 | — | `No answer needed` |
| 3.3 | — | `No answer needed` |
| 3.4 | Herramienta de fuerza bruta | `Microsoft SQL Bruter` |
| 3.5 | — | `No answer needed` |
| 3.6 | — | `No answer needed` |
| 3.7 | — | `No answer needed` |
| 4.1 | Número de teléfono (OSINT) | `08081 570087` |
| 4.2 | — | `No answer needed` |
| 4.3 | Localización | `Inverkeithing` |
| 4.4 | — | `No answer needed` |
| 4.5 | Flag final | `SBRC{ODhiOTQ3ZTk0NzJhMWI1NTE5MGUyY2Vj}` |

---

**Metodología:** Reconocimiento del objetivo, escaneo de puertos, enumeración de SQL Server, fuerza bruta con Microsoft SQL Bruter, recuperación de credenciales y aplicación de pistas OSINT para localizar el remate de la sala y obtener el flag final.

### Cadena de ataque / Attack Chain

Reconocimiento → escaneo → enumeración SQL → fuerza bruta (Microsoft SQL Bruter) → acceso → OSINT → flag.

**Learning chain:** recon → nmap → SQL Server → brute force → OSINT → flag

*Lección:* Las credenciales por defecto y los servicios expuestos (SQL) combinados con OSINT comprometen el objetivo.

**MITRE ATT&CK:** TA0001 Initial Access, TA0007 Discovery, TA0009 Collection, T1078 Valid Accounts.

**Fuente:** [TryHackMe - Cyber Scotland 2021](https://tryhackme.com/room/cyberscotland2021)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.

**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.

**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).

**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.