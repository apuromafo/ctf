# Lumberjack Turtle

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Laboratorio / CTF | lumberjackturtle | https://tryhackme.com/room/lumberjackturtle | 02 Level Medium | TryHackMe | Log4Shell (CVE-2021-44228), Log4j, JNDI, container escape, RCE | Ejecución remota de código (RCE) y escape de contenedor en un entorno Java |

---

**Contexto:** **Lumberjack Turtle** combina dos fases en un mismo escenario: explotar la vulnerabilidad Log4Shell (CVE-2021-44228) para obtener ejecución remota de código sobre una aplicación Java y, posteriormente, llevar a cabo un escape del contenedor para comprometer el host. La sala exige construir el payload JNDI/LDAP y encadenar ambas fases para capturar las flags.

## Solucionario

### Task 1: Reconocimiento / Reconnaissance
**Explicación:**

Se enumera el objetivo y se identifica la aplicación Java vulnerable a Log4Shell, preparando el marco de la explotación.

1. `No answer needed`

### Task 2: Explotación / Exploitation
**Explicación:**

Se lanza el exploit Log4Shell (payload JNDI contra Log4j) dentro del contenedor y, a continuación, se lleva a cabo el escape de contenedor para obtener acceso al host. Cada fase entrega una flag.

1. `THM{LOG4SHELL_FTW}`
2. `THM{C0NT41N3R_3SC4P3_FTW}`

### Task 3: Cierre / Conclusion
**Explicación:**

Se consolida la cadena de ataque RCE → container escape y se cierra la sala.

1. `No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Tarea de reconocimiento | `No answer needed` |
| 2.1 | Flag de la explotación Log4Shell (RCE) | `THM{LOG4SHELL_FTW}` |
| 2.2 | Flag del escape de contenedor | `THM{C0NT41N3R_3SC4P3_FTW}` |
| 3 | Tarea final de cierre | `No answer needed` |

---

**Metodología:** Reconocimiento del objetivo Java → construcción del payload JNDI/LDAP para Log4Shell (CVE-2021-44228) → RCE dentro del contenedor (captura de flag) → técnicas de escape de contenedor → acceso al host (captura de segunda flag) → cierre.

**Learning chain:** Reconocimiento → Log4Shell RCE (CVE-2021-44228) → flag del contenedor → container escape → flag del host → cierre.

**Lección:** *Log4Shell demuestra que una biblioteca de logging omnipresente puede convertirse en RCE global, y en entornos containerizados esa RCE inicial es solo el primer eslabón de una cadena que puede terminar en el host.*

**MITRE ATT&CK:** T1190 Exploit Public-Facing Application · T1059 Command and Scripting Interpreter · T1611 Escape to Host · T1505 Web Shell (post-explotación).

**Fuente:** [TryHackMe - Lumberjack Turtle](https://tryhackme.com/room/lumberjackturtle)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.