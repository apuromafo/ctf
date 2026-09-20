# You Got Mail

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Walkthrough | yougotmail | https://tryhackme.com/room/yougotmail | 02 Level Medium | TryHackMe | Phishing, Email Analysis, CTF | Análisis de un correo de phishing, sus adjuntos maliciosos y la flag oculta |

---

**Contexto:** La sala **You Got Mail** desarrolla un escenario de phishing realista: el alumno recibe un correo sospechoso y debe analizarlo, identificando el adjunto malicioso, su comportamiento y las contraseñas o pistas encubiertas. El solucionario recoge la flag obtenida al inspeccionar el contenido del correo, junto con el archivo adjunto y la contraseña utilizados en el ejercicio.

## Solucionario

### Task 1: Introducción

**Explicación:**

La sala presenta el escenario de phishing y el análisis que se realizará sobre el correo recibido.

Respuesta: `No answer needed`

### Task 2: Análisis del correo y adjuntos

**Explicación:**

Se analiza el correo malicioso: se obtiene la flag de la sala al inspeccionar el contenido, se identifica el adjunto que acompaña al correo (`superstar`) y la contraseña que protege o describe el artefacto (`password`).

1. `THM{l1v1n_7h3_br1ck_l1f3}`
2. `superstar`
3. `password`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lectura de la introducción | `No answer needed` |
| 2.1 | Flag de la sala | `THM{l1v1n_7h3_br1ck_l1f3}` |
| 2.2 | Adjunto del correo | `superstar` |
| 2.3 | Contraseña del artefacto | `password` |

---

**Metodología:** Análisis de un correo de phishing: inspección de los campos del mensaje, extracción del adjunto y de las credenciales o pistas embebidas, y resolución de la flag oculta en el escenario.

**Learning chain:** Correo recibido → análisis del mensaje → adjunto → contraseña → flag.

**Lección:** *Los correos de phishing esconden el artefacto malicioso en los adjuntos; analizar el mensaje completo, incluidas las credenciales embebidas, revela el objetivo real del atacante.*

**MITRE ATT&CK:** T1566 Phishing · T1204 User Execution · T1059 Command and Scripting Interpreter.

**Fuente:** [TryHackMe - You Got Mail](https://tryhackme.com/room/yougotmail)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.