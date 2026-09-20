# Snyk Code

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | DevSecOps / SAST | snykcode | https://tryhackme.com/room/snykcode | 01 Level Easy | TryHackMe | Snyk Code, SAST, CWE-79 (XSS), CWE-89 (SQLi), OWASP Security Champion Playbook | Alto |

---

**Contexto:**
> **ES:** Laboratorio de escaneo estático con Snyk Code (SAST). Se analiza una aplicación para identificar vulnerabilidades clasificadas bajo CWE, y se responde sobre técnicas de mitigación y mejores prácticas defensivas.
> **EN:** A Snyk Code SAST lab. The application is scanned for vulnerabilities classified under CWE, and mitigation techniques and defensive best practices are covered.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:**
No se requiere respuesta; establece el contexto de la herramienta.

```
No answer needed
```

### Task 2: Configuración del repositorio / Repository Setup
**Explicación:**
No se requiere respuesta; preparación del entorno de escaneo.

```
No answer needed
```

### Task 3: Hallazgos del escaneo / Scan Findings
**Explicación:**
Se indica el número de vulnerabilidades identificadas por Snyk Code en el análisis.

```
3
```

### Task 4: Tipos de vulnerabilidades / Vulnerability Types
**Explicación:**
Se identifican y enumeran los tipos de vulnerabilidades halladas en el escaneo.

```
1. 4
2. 2
3. Cross-Site Request Forgery, Information Exposure
```

### Task 5: CWE detectados / Detected CWEs
**Explicación:**
Se identifican los identificadores CWE correspondientes a XSS y SQL Injection, y el parámetro vulnerable.

```
1. CWE-79
2. CWE-89
3. searchTerm
```

### Task 6: Detalles adicionales / Further Details
**Explicación:**
Se responde sobre la capacidad de control de recursos, la función vulnerable y las buenas prácticas para mitigar la inyección SQL.

```
1. Allocation of Resources Without Limits or Throttling
2. res.render
3. parameterised queries
```

### Task 7: Uso de Snyk / Snyk Usage
**Explicación:**
Respuesta afirmativa de confirmación.

```
y
```

### Task 8: Comunidad y recursos / Community & Resources
**Explicación:**
Se menciona el recurso comunitario de Snyk y no se requiere respuesta en la segunda parte.

```
1. OWASP security shampion playbook
2. No answer needed
```

### Tabla unificada de preguntas/respuestas

| # | Respuesta |
|---|---|
| 1 | `No answer needed` |
| 2 | `No answer needed` |
| 3 | `3` |
| 4.1 | `4` |
| 4.2 | `2` |
| 4.3 | `Cross-Site Request Forgery, Information Exposure` |
| 5.1 | `CWE-79` |
| 5.2 | `CWE-89` |
| 5.3 | `searchTerm` |
| 6.1 | `Allocation of Resources Without Limits or Throttling` |
| 6.2 | `res.render` |
| 6.3 | `parameterised queries` |
| 7 | `y` |
| 8.1 | `OWASP security shampion playbook` |
| 8.2 | `No answer needed` |

---

**Metodología:**
1. Preparación del repositorio y configuración de Snyk Code.
2. Ejecución del escaneo SAST sobre la aplicación.
3. Revisión de los hallazgos y su clasificación CWE.
4. Identificación del parámetro/entrada afectada (`searchTerm`).
5. Aplicación de las mitigaciones recomendadas (consultas parametrizadas).
6. Integración con la comunidad y el programa de Security Champions.

### Cadena de ataque / Attack Chain
Repositorio → Snyk Code (SAST) → Hallazgos (XSS, SQLi, CSRF, Information Exposure, DoS) → CWE-79 / CWE-89 → Mitigación (parameterised queries) → Security Champion.

**Learning chain:**
SAST → CWE → XSS/SQLi → análisis estático de flujo de datos → remediación.

**Lección:** *El escaneo estático integrado en el ciclo de desarrollo permite detectar y corregir vulnerabilidades antes de que lleguen a producción, convirtiéndose en una práctica defensiva esencial.*

**MITRE ATT&CK:**
| Técnica | ID |
|---|---|
| Exploit Public-Facing Application | T1190 |
| Command and Scripting Interpreter | T1059 |
| Input Validation / CWE-79 (XSS) | CWE-79 |
| Injection / CWE-89 (SQLi) | CWE-89 |

**Fuente:** [TryHackMe - Snyk Code](https://tryhackme.com/room/snykcode)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.