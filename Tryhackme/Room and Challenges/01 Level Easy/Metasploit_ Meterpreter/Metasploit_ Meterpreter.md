# Metasploit_ Meterpreter

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|-------------|---------|
| Easy | walkthrough | `metasploitmeterpreter` | [TryHackMe](https://tryhackme.com/room/metasploitmeterpreter) | 01 Level Easy | THM | Meterpreter, Metasploit, hashdump, Windows, migración | Uso de Meterpreter para post-explotación en Windows |

> **Objeto:** Aprender a trabajar con la sesión Meterpreter de Metasploit sobre un Windows: enumerar el sistema, extraer hashes y localizar secretos y flags.

---

**Contexto:** Sala centrada en Meterpreter: se obtiene una sesión Meterpreter sobre un objetivo Windows, se identifica el equipo (ACME-TEST) y el usuario (FLASH), se vuelcan hashes y credenciales (speedster, Trustno1, KDSvbsw3849!) y se localizan los archivos de secretos del sistema para recuperar la flag final.

> **ES:** Sala de post-explotación con Meterpreter en Windows: enumeración, extracción de credenciales y recuperación de secretos y flags.
> **EN:** Meterpreter post-exploitation room on Windows: enumeration, credential dumping and secret/flag recovery.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:** Presentación de la sala y del payload/sesión Meterpreter.

No answer needed

### Task 2: Enumeración del sistema / System enumeration
**Explicación:** Compromiso del objetivo y primeras acciones de enumeración con Meterpreter.

No answer needed

### Task 3: Volcado de credenciales / Credential dumping
**Explicación:** Extracción de hashes y credenciales de la memoria del sistema.

No answer needed

### Task 4: Búsqueda de secretos / Secret hunting
**Explicación:** Localización de los archivos de secretos dentro del sistema Windows.

No answer needed

### Task 5: Preguntas finales / Final questions
**Explicación:** Se responden todas las preguntas del reto con los datos obtenidos de la sesión Meterpreter.

1. ACME-TEST
2. FLASH
3. speedster
4. 69596c7aa1e8daee17f8e78870e25a5c
5. Trustno1
6. c:\Program Files (x86)\Windows Multimedia Platform\secrets.txt
7. KDSvbsw3849!
8. c:\inetpub\wwwroot\realsecret.txt
9. The Flash is the fastest man alive

### Tabla unificada de preguntas y respuestas

| Task | Pregunta | Respuesta |
|------|----------|-----------|
| 1 | — | `No answer needed` |
| 2 | — | `No answer needed` |
| 3 | — | `No answer needed` |
| 4 | — | `No answer needed` |
| 5.1 | Nombre del equipo | `ACME-TEST` |
| 5.2 | Usuario identificado | `FLASH` |
| 5.3 | Credencial del usuario | `speedster` |
| 5.4 | Hash/NT hash obtenido | `69596c7aa1e8daee17f8e78870e25a5c` |
| 5.5 | Credencial extraída | `Trustno1` |
| 5.6 | Ruta del primer archivo de secretos | `c:\Program Files (x86)\Windows Multimedia Platform\secrets.txt` |
| 5.7 | Credencial adicional | `KDSvbsw3849!` |
| 5.8 | Ruta del segundo archivo de secretos | `c:\inetpub\wwwroot\realsecret.txt` |
| 5.9 | Contenido/mensaje del secreto | `The Flash is the fastest man alive` |

---

**Metodología:** Obtención de la sesión Meterpreter sobre el objetivo Windows, enumeración del sistema y del usuario, volcado de hashes y credenciales con Meterpreter, y búsqueda de los archivos de secretos (secrets.txt en rutas de Windows) para recuperar la flag final.

### Cadena de ataque / Attack Chain

Explotación → sesión Meterpreter → enumeración → volcado de credenciales → búsqueda de secretos → flag final.

**Learning chain:** Metasploit → Meterpreter → enumeración → credenciales → secretos → flag

*Lección:* Meterpreter centraliza la post-explotación: con unos pocos comandos permite enumerar, volcar credenciales y localizar secretos del sistema comprometido.

**MITRE ATT&CK:** T1003 - OS Credential Dumping, T1059 - Command and Scripting Interpreter.

**Fuente:** [TryHackMe - Metasploit_ Meterpreter](https://tryhackme.com/room/metasploitmeterpreter)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.

**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.

**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).

**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.