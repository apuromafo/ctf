# Billing

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | challenge | `billing` | [TryHackMe](https://tryhackme.com/room/billing) | 01 Level Easy | TryHackMe | node.js / web exploitation / command injection | Compromiso de una aplicación web vulnerable que permite la ejecución de comandos y la captura de las flags de usuario y de root |

---

**Contexto:** Billing es una sala tipo challenge centrada en una aplicación web vulnerable. El objetivo es explotar una vulnerabilidad en la aplicación para obtener una shell y, a partir de ahí, escalar privilegios y capturar tanto el user flag como el root flag dentro del sistema.

> **ES:** La sala plantea una aplicación web de facturación (Billing) vulnerable. Mediante la explotación de una vulnerabilidad se obtiene ejecución de comandos, acceso al sistema y ambas flags.
> **EN:** This challenge targets a vulnerable billing web application. Exploiting a vulnerability leads to command execution, system access and both flags.

## Solucionario

### Task 1: User Flag
**Explicación:** Tras explotar la vulnerabilidad de la aplicación web, se obtiene acceso al sistema y se localiza el archivo que contiene el user flag.

| Pregunta / Question | Respuesta / Answer |
|--------------------|--------------------|
| ¿Cuál es el user flag? | `THM{4a6831d5f124b25eefb1e92e0f0da4ca}` |

### Task 2: Root Flag
**Explicación:** Se escala privilegios dentro del sistema comprometido y se captura el root flag.

| Pregunta / Question | Respuesta / Answer |
|--------------------|--------------------|
| ¿Cuál es el root flag? | `THM{33ad5b530e71a172648f424ec23fae60}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | User flag | `THM{4a6831d5f124b25eefb1e92e0f0da4ca}` |
| 2 | Root flag | `THM{33ad5b530e71a172648f424ec23fae60}` |

---

**Metodología:** Se identifica la aplicación web vulnerable del challenge y se estudia su comportamiento. Mediante la explotación de una vulnerabilidad en la propia aplicación se consigue ejecución de comandos, lo que permite obtener una shell en el sistema. Con esa shell se ubica el user flag y, tras escalar privilegios en la máquina, se accede al root flag.

### Cadena de ataque / Attack Chain

```text
recon web -> identificación de la app Billing -> explotación (ejecución de comandos) -> shell -> user flag -> escalada de privilegios -> root flag
```

**Learning chain:** web recon --> vulnerable node.js app --> command execution --> shell --> user flag --> privilege escalation --> root flag

**Lección:** *Las aplicaciones web vulnerables a la ejecución de comandos son una puerta de entrada rápida al sistema; tras la explotación inicial siempre conviene buscar la escalada de privilegios.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1059 (Command and Scripting Interpreter), T1068 (Exploitation for Privilege Escalation), T1005 (Data from Local System)

**Fuente:** [TryHackMe - Billing](https://tryhackme.com/room/billing)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.