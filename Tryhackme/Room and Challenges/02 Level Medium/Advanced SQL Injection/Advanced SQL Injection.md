# Advanced SQL Injection

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Web / Explicación práctica | advancedsqlinjection | https://tryhackme.com/room/advancedsqlinjection | 02 Level Medium | TryHackMe | MySQL, MariaDB, SQLi, MSSQL | RCE / exfiltración de base de datos |

---

**Contexto:** La sala **Advanced SQL Injection** profundiza en variantes avanzadas de inyección SQL sobre **MySQL/MariaDB**: errores controlados para validar la inyección, técnicas **in-band**, exfiltración de datos por cabeceras HTTP (User-Agent), identificación de versiones y rutas, y el análisis de lo que **no** es posible en MySQL frente a **MSSQL** (por ejemplo, `xp_cmdshell`). Los retos dividen el solucionario en laboratorios donde se inyectan payloads contra una web local y se traducen los resultados en flags y datos del motor.

## Solucionario

### Task 1: Reconocimiento del puerto
**Explicación:**

Se identifica el puerto por defecto de escucha del servicio MySQL para orientar la fase de explotación.

Respuesta: `3306`

### Task 2: Tipos de inyección
**Explicación:**

Se clasifican las modalidades de ataque empleadas en la sala: la **in-band** (los datos viajan por el mismo canal de la página) y el canal HTTP utilizado para exfiltrar la información.

1. `In-band`
2. `HTTP`

### Task 3: Flags de laboratorio
**Explicación:**

Se resuelven los dos primeros laboratorios de inyección, obteniendo la flag por validación de la inyección y la flag por afectación a la tabla de la base.

1. `THM{SO_HACKED}`
2. `THM{Table_Dropped}`

### Task 4: Moldeando la inyección
**Explicación:**

Se fuerza un error deliberado para confirmar el punto ciego de la inyección: se anota el código de error devuelto por el motor y el nombre de la serie/tabla que se revela en el mensaje.

1. `1064`
2. `Animal Series`

### Task 5: Fingerprinting del motor
**Explicación:**

Se identifica el motor y la build exacta con la que está compilado el servidor de base de datos para afinar los payloads.

1. `tesla`
2. `c`

### Task 6: Versión y ruta de instalación
**Explicación:**

Se extrae la versión exacta de MariaDB y la ruta física de instalación del servicio, datos de configuración que confirman el control sobre la base.

1. `10.4.24-MariaDB`
2. `C:/xampp/mysql`

### Task 7: Exfiltración y flag
**Explicación:**

Se completa la exfiltración de datos a través de la cabecera **User-Agent**, obteniendo la flag del laboratorio.

1. `THM{HELLO}`
2. `User-Agent`

### Task 8: Limitaciones del motor
**Explicación:**

Se responde si es posible ejecutar comandos del sistema de forma nativa en esta variante de MySQL, resultado negativo (`nay`).

Respuesta: `nay`

### Task 9: Extensión de MSSQL
**Explicación:**

Se identifica la extensión del motor **MSSQL** que sí permite ejecutar comandos del sistema operativo cuando se dispone de los privilegios adecuados.

Respuesta: `xp_cmdshell`

### Task 10: Cierre
**Explicación:**

Se consolida el aprendizaje de las técnicas avanzadas de inyección vistas en la sala.

Respuesta: `No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Puerto por defecto de MySQL | `3306` |
| 2.1 | Tipo de inyección practicado | `In-band` |
| 2.2 | Canal de exfiltración | `HTTP` |
| 3.1 | Flag primer laboratorio | `THM{SO_HACKED}` |
| 3.2 | Flag segundo laboratorio | `THM{Table_Dropped}` |
| 4.1 | Código de error del motor | `1064` |
| 4.2 | Serie/tabla revelada | `Animal Series` |
| 5.1 | Build del motor | `tesla` |
| 5.2 | Compilación del motor | `c` |
| 6.1 | Versión exacta de MariaDB | `10.4.24-MariaDB` |
| 6.2 | Ruta de instalación | `C:/xampp/mysql` |
| 7.1 | Flag del laboratorio de exfiltración | `THM{HELLO}` |
| 7.2 | Cabecera usada para exfiltrar | `User-Agent` |
| 8 | ¿El motor permite RCE nativo? | `nay` |
| 9 | Extensión RCE de MSSQL | `xp_cmdshell` |
| 10 | Tarea de cierre | `No answer needed` |

---

**Metodología:** Inyección SQL activa sobre MySQL/MariaDB (in-band, error-based, blind), fingerprinting del motor, exfiltración por cabeceras HTTP y comparativa con MSSQL (xp_cmdshell); referencias OWASP WSTG (SQLi) y CWE-89.

**Learning chain:** Puerto/servicio → clasificación SQLi → inyección validada → control de tablas → fingerprint → configuración del motor → exfiltración → límites del motor → RCE en MSSQL.

**Lección:** *El motor de base de datos define el límite del ataque: dominar el fingerprint permite decidir qué es posible (y qué no) antes de disparar payloads.*

**MITRE ATT&CK:** T1190 Exploit Public-Facing Application · T1595.002 Vulnerability Scanning · T1041 Exfiltration Over C2 Channel.

**Fuente:** [TryHackMe - Advanced SQL Injection](https://tryhackme.com/room/advancedsqlinjection)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.