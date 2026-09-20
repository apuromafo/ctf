# Evil-GPT

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | ctf | `evilgpt` | [TryHackMe - Evil-GPT](https://tryhackme.com/room/evilgpt) | `01 Level Easy` | THM | LLM, prompt injection, nc, AI shell, AI security | Exploitation — abuso de un asistente IA conectado a ejecución de comandos |

> **Objeto:** Practicar habilidades de hacking de LLMs explotando un asistente de IA que traduce peticiones en comandos Linux y ejecutarlos para leer la flag, demostrando el riesgo de la prompt injection.

---

**Contexto:** Evil-GPT simula un asistente IA comprometido que ejecuta comandos del sistema a partir de peticiones en lenguaje natural. Al conectar con `nc` al puerto indicado, el usuario pide al modelo que genere comandos Linux; el modelo los genera como root y, aceptando su ejecución, permite enumerar y leer el contenido de `/root/flag.txt`. Es una introducción básica al abuso de modelos de lenguaje con capacidades de ejecución.

> **ES:** Sala de IA ofensiva: un asistente LLM genera comandos Linux y los ejecuta como root; mediante peticiones en lenguaje natural se lee la flag de `/root/flag.txt`.
>
> **EN:** Offensive AI room: an LLM assistant generates Linux commands and executes them as root; using natural language the flag in `/root/flag.txt` is read.

## Solucionario

### Task 1: Inyección de prompts en el AI shell / Prompt Injection in the AI Shell

**Explicación:** Se conecta al AI shell con `nc` y se instruye al modelo en lenguaje natural para que genere los comandos que permiten confirmar privilegios (root), listar `/root` y leer el archivo `flag.txt`. Al confirmar la ejecución de los comandos propuestos por el modelo, se obtiene la bandera.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag de la sala | `THM{AI_HACK_THE_FUTURE}` |

---

**Metodología:** Se conecta al servicio con `nc <IP> 1337`. Mediante peticiones en lenguaje natural se induce al modelo a generar comandos: primero `sudo whoami` para confirmar que ejecuta como root, luego un listado de `/root` para localizar `flag.txt` y finalmente `cat /root/flag.txt` para leer el contenido. Cada comando generado se confirma y se captura la flag.

### Cadena de ataque / Attack Chain

Conexión al AI shell → Petición de verificación de privilegios (root) → Enumeración de `/root` → Lectura de `/root/flag.txt` → Flag obtenida.

**Learning chain:** LLM security → Prompt injection → AI-to-shell bridge → Command execution → Data exfiltration

**Lección:** *Un asistente de IA con capacidad de ejecución de comandos y sin validación de entrada es un vector crítico: la prompt injection convierte lenguaje natural en ejecución de código (root), por lo que estos agentes deben desplegarse en sandbox, sin privilegios y con control estricto de las acciones que ejecutan.*

**MITRE ATT&CK:** T1059.006 - Command and Scripting Interpreter: Python (contexto IA), T1204 - User Execution, T1005 - Data from Local System; LLM01:2025 - Prompt Injection (OWASP Top 10 for LLM Applications)

**Fuente:** [TryHackMe - Evil-GPT](https://tryhackme.com/room/evilgpt)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.