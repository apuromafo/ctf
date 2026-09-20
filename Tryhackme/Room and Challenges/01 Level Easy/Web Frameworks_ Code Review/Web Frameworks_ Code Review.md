# Web Frameworks: Code Review

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Medium | walkthrough | `webframeworkscodereview` | https://tryhackme.com/room/webframeworkscodereview | Secure Code Review | TryHackMe | Flask, source/sink, Semgrep, SSTI, pickle, IDOR | Alto — permite ejecución remota de código, lectura arbitraria de archivos y acceso no autorizado a datos desde una aplicación Flask vulnerable |

---

**Contexto:** Este房间 nos sumerge en una auditoría de código fuente de una aplicación Flask, identificando patrones de seguridad desde las dependencias hasta la lógica de negocio. Se exploan las vulnerabilidades más comunes de web frameworks Python: SQLi por falta de parámetros, SSTI por uso inseguro de plantillas, path traversal en envío de archivos, deserialización peligrosa con pickle y IDOR en consultas ORM. El recorrido refuerza el concepto de source-sink tracking y el uso de Semgrep para detección automatizada de vulnerabilidades.

> **ES:** Auditoría de código de una aplicación Flask: trazado source→sink, SSTI, command injection, Semgrep, deserialización insegura con pickle e IDOR en ORM.
> **EN:** Code audit of a Flask application: source→sink tracking, SSTI, command injection, Semgrep, insecure pickle deserialization and IDOR in ORM queries.

## Solucionario

### Task 1: Reconocimiento del Proyecto Flask / Flask Project Reconnaissance

**Explicación:** Se identifica la estructura del proyecto Flask: el manifest de dependencias (`requirements.txt`), el decorador que convierte una función en ruta (`@app.route`) y el archivo que por convención contiene el debug flag y la secret key (`config.py`).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which file conventionally holds the dependency manifest in a Python project? | `requirements.txt` |
| 2 | Which decorator marks a function as a route in a Flask application? | `@app.route` |
| 3 | Which file conventionally holds the debug flag and the secret key in Flask? | `config.py` |

### Task 2: Source, Sink y Trazabilidad / Source, Sink and Taint Tracking

**Explicación:** Se traza el flujo de datos en la aplicación: el punto de entrada que alimenta `cursor.execute` se denomina `source`, mientras que `render_template_string` y `subprocess.run(…, shell=True)` son ejemplos de `sink`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Tracing backwards from cursor.execute, what do we call that entry point? | `source` |
| 2 | render_template_string and subprocess.run(…, shell=True) are both examples of which type? | `sink` |

### Task 3: SSTI y Command Injection / SSTI and Command Injection

**Explicación:** `request.args.get("name")` fluye directamente a `render_template_string` sin validación, lo que permite `SSTI`; y el argumento `shell=True` entrega la cadena de comando completa al shell, habilitando command injection.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | request.args.get("name") flows into render_template_string with no validation. Which vulnerability class? | `SSTI` |
| 2 | Which keyword argument hands the whole command string to the shell? (as written in code) | `shell=True` |

### Task 4: Auditoría con Semgrep / Auditing with Semgrep

**Explicación:** Para la auditoría estática se combina grep con recursividad y números de línea (`-rn`) y se selecciona el ruleset de Semgrep con el flag `--config`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which two-flag combination gives recursion plus line numbers for grep? | `-rn` |
| 2 | Which command-line flag selects the ruleset in Semgrep? | `--config` |

### Task 5: Deserialización Insegura y Path Traversal / Insecure Deserialization and Path Traversal

**Explicación:** `pickle.loads` vuelve a cargar bytes no fiables como objetos (deserialización insegura), y `send_from_directory` es la contrapartida segura de `send_file` frente a path traversal.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which Python function loads attacker bytes back into objects (insecure deserialization)? | `pickle.loads` |
| 2 | Which Flask function is the safe counterpart to send_file for path traversal? | `send_from_directory` |

### Task 6: Control de Acceso y Flags / Access Control and Flags

**Explicación:** `Vault.query.get(item_id)` sin filtro de `owner_id` provoca un `IDOR`. Con las vulnerabilidades confirmadas se recuperan las tres flags: SQLi (`THM{un10n_b4s3d_sql1_dump3d}`), SSTI→RCE (`THM{j1nj4_ss71_to_rc3}`) y path traversal (`THM{send_file_tr4v3rs4l_w1n}`).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Vault.query.get(item_id) with no owner_id filter — common acronym for the access-control flaw? | `IDOR` |
| 2 | Flag SQLi | `THM{un10n_b4s3d_sql1_dump3d}` |
| 3 | Flag SSTI→RCE | `THM{j1nj4_ss71_to_rc3}` |
| 4 | Flag path traversal | `THM{send_file_tr4v3rs4l_w1n}` |

---

**Metodología:** Se siguió un enfoque de source-to-sink audit: localizar cada punto de entrada (request.args, form data) y rastrear su flujo hasta un sink peligroso (render_template_string, subprocess, send_file, pickle.loads, ORM query sin filtro). Se empleó grep con recursividad y Semgrep para detección estática. Cada vulnerabilidad se confirma teóricamente y se validan las flags en los endpoints correspondientes.

### Cadena de ataque / Attack Chain

```text
Análisis de dependencias y estructura Flask -> rastreo source→sink -> SSTI vía render_template_string -> command injection vía shell=True -> auditoría con grep -rn y Semgrep --config -> pickle.loads (deserialización insegura) -> send_file path traversal -> IDOR en ORM -> flags
```

**Learning chain:** Flask project structure → source/sink identification → SSTI via Jinja2 → command injection via shell=True → grep flags for code audit → Semgrep rules → pickle deserialization → send_file path traversal → IDOR in ORM → flag extraction

**Lección:** *Una auditoría source-to-sink sobre una aplicación Flask permite localizar de forma sistemática SSTI, command injection, path traversal, deserialización insegura e IDOR, y herramientas como Semgrep aceleran su detección estática.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1059.004 (Command and Scripting Interpreter: Unix Shell), T1021 (Remote Services)

**Fuente:** [TryHackMe - Web Frameworks: Code Review](https://tryhackme.com/room/webframeworkscodereview)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.