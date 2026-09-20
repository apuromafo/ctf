# SQL Injection Lab

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|------------|------|------|------|---------|--------|-------------|---------|
| Easy | walkthrough | `sqlinjectionlab` | [TryHackMe](https://tryhackme.com/room/sqlinjectionlab) | 01 Level Easy | TryHackMe | SQL Injection, Web Attacks, Database Exploitation | Technical — Hands-on SQL injection exploitation |

---

**Contexto:** Este room proporciona un laboratorio práctico de inyección SQL. Se requiere explotar paso a paso diferentes puntos de inyección SQL, desde la identificación inicial hasta la extracción de información de la base de datos, recolectando un flag por cada nivel del laboratorio.

## Solucionario

### Task 1: Lab Introduction

**Explicación:** Se Introduce el laboratorio de inyección SQL sin requerir una respuesta específica.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Read the lab introduction | `No answer needed` |

### Task 2: Level 1

**Explicación:** Se Completan los niveles iniciales del laboratorio de inyección SQL, identificando los flags correspondientes a cada punto de inyección.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Level 1 flag | `THM{dccea429d73d4a6b4f117ac64724f460}` |
| 2 | Second flag | `THM{356e9de6016b9ac34e02df99a5f755ba}` |
| 3 | Third flag | `THM{645eab5d34f81981f5705de54e8a9c36}` |
| 4 | Fourth flag | `THM{727334fd0f0ea1b836a8d443f09dc8eb}` |

### Task 3: Level 2

**Explicación:** Se Explota el siguiente nivel del laboratorio de inyección SQL para obtener el flag correspondiente.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag? | `THM{b3a540515dbd9847c29cffa1bef1edfb}` |

### Task 4: Level 3

**Explicación:** Se Continúa con la explotación del laboratorio de inyección SQL en el nivel 3.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag? | `THM{f35f47dcd9d596f0d3860d14cd4c68ec}` |

### Task 5: Level 4

**Explicación:** Se Explota el nivel 4 del laboratorio de inyección SQL.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag? | `THM{fb381dfee71ef9c31b93625ad540c9fa}` |

### Task 6: Level 5

**Explicación:** Se Explota el nivel 5 del laboratorio de inyección SQL.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag? | `THM{f1f4e0757a09a0b87eeb2f33bca6a5cb}` |

### Task 7: Level 6

**Explicación:** Se Explota el nivel 6 del laboratorio de inyección SQL.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag? | `THM{4644c7e157fd5498e7e4026c89650814}` |

### Task 8: Level 7

**Explicación:** Se Explota el nivel 7 del laboratorio de inyección SQL.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag? | `THM{cd5c4f197d708fda06979f13d8081013}` |

### Task 9: Level 8

**Explicación:** Se Explota el nivel 8 del laboratorio de inyección SQL.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag? | `THM{27f8f7ce3c05ca8d6553bc5948a89210}` |

### Task 10: Level 9

**Explicación:** Se Completa la explotación del laboratorio de inyección SQL en el nivel 9.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag? | `THM{183526c1843c09809695a9979a672f09}` |

---

**Metodología:** Se Explotan progresivamente múltiples puntos de inyección SQL en un laboratorio controlado, aplicando técnicas de inyección para extraer datos y obtener los flags de cada nivel.

### Cadena de ataque / Attack Chain

**Learning chain:** SQLi Detection → Error-Based Injection → Union Injection → Blind Injection → Flag Extraction

**Lección:** *La inyección SQL requiere un enfoque metódico y progresivo: cada nivel del laboratorio presenta variaciones que exigen adaptar las técnicas de explotación para extraer los datos objetivo.*

**MITRE ATT&CK:** T1190 — Exploit Public-Facing Application; T1505.003 — Web Shell: SQL Injection

**Fuente:** [TryHackMe - SQL Injection Lab](https://tryhackme.com/room/sqlinjectionlab)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.