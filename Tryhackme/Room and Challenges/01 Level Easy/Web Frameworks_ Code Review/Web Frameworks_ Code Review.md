# Web Frameworks: Code Review

| **Dificultad** | Medium |
| **Tipo** | walkthrough |
| **Slug** | `webframeworkscodereview` |
| **Link** | [TryHackMe](https://tryhackme.com/r/room/webframeworkscodereview) |
| **Sección** | Secure Code Review |
| **Fuente** | THM |
| **Componentes** | Flask, source/sink, Semgrep, SSTI, pickle, IDOR |
| **Impacto** | Alto — permite ejecución remota de código, lectura arbitraria de archivos y acceso no autorizado a datos desde una aplicación Flask vulnerable |

---

**Contexto:** Este房间 nos sumerge en una auditoría de código fuente de una aplicación Flask, identificando patrones de seguridad desde las dependencias hasta la lógica de negocio. Se exploan las vulnerabilidades más comunes de web frameworks Python: SQLi por falta de parámetros, SSTI por uso inseguro de plantillas, path traversal en envío de archivos, deserialización peligrosa con pickle y IDOR en consultas ORM. El recorrido refuerza el concepto de source-sink tracking y el uso de Semgrep para detección automatizada de vulnerabilidades.

## Solucionario

### Task 1: Reconocimiento del Proyecto Flask

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which file conventionally holds the dependency manifest in a Python project? | `requirements.txt` |
| 2 | Which decorator marks a function as a route in a Flask application? | `@app.route` |
| 3 | Which file conventionally holds the debug flag and the secret key in Flask? | `config.py` |

### Task 2: Source, Sink y Trazabilidad

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Tracing backwards from cursor.execute, what do we call that entry point? | `source` |
| 2 | render_template_string and subprocess.run(…, shell=True) are both examples of which type? | `sink` |

### Task 3: SSTI y Command Injection

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | request.args.get("name") flows into render_template_string with no validation. Which vulnerability class? | `SSTI` |
| 2 | Which keyword argument hands the whole command string to the shell? (as written in code) | `shell=True` |

### Task 4: Auditoría con Semgrep

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which two-flag combination gives recursion plus line numbers for grep? | `-rn` |
| 2 | Which command-line flag selects the ruleset in Semgrep? | `--config` |

### Task 5: Deserialización Insegura y Path Traversal

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which Python function loads attacker bytes back into objects (insecure deserialization)? | `pickle.loads` |
| 2 | Which Flask function is the safe counterpart to send_file for path traversal? | `send_from_directory` |

### Task 6: Control de Acceso y Flags

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Vault.query.get(item_id) with no owner_id filter — common acronym for the access-control flaw? | `IDOR` |
| 2 | Flag SQLi | `THM{un10n_b4s3d_sql1_dump3d}` |
| 3 | Flag SSTI→RCE | `THM{j1nj4_ss71_to_rc3}` |
| 4 | Flag path traversal | `THM{send_file_tr4v3rs4l_w1n}` |

---

**Metodología:** Se siguió un enfoque de source-to-sink audit: localizar cada punto de entrada (request.args, form data) y rastrear su flujo hasta un sink peligroso (render_template_string, subprocess, send_file, pickle.loads, ORM query sin filtro). Se empleó grep con recursividad y Semgrep para detección estática. Cada vulnerabilidad se confirma teóricamente y se validan las flags en los endpoints correspondientes.
**Learning chain:** Flask project structure → source/sink identification → SSTI via Jinja2 → command injection via shell=True → grep flags for code audit → Semgrep rules → pickle deserialization → send_file path traversal → IDOR in ORM → flag extraction
**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1059.004 (Command and Scripting Interpreter: Unix Shell), T1021 (Remote Services)
**Fuente:** [TryHackMe - Web Frameworks: Code Review](https://tryhackme.com/r/room/webframeworkscodereview)
