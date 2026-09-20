# Tech_Supp0rt_ 1

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|------------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `techsupp0rt1` | [TryHackMe](https://tryhackme.com/room/techsupp0rt1) | 01 Level Easy | THM | WordPress, reverse shell, escalada de privilegios | Compromiso total del servidor |

---

**Contexto:**

> **ES:** Sala de nivel fácil centrada en comprometer un servicio de soporte técnico basado en WordPress: enumeración web, obtención de una reverse shell y escalada de privilegios para leer la flag del usuario.
> **EN:** Easy-level room focused on compromising a WordPress-based tech support service: web enumeration, gaining a reverse shell and privilege escalation to read the user flag.

## Solucionario

### Task 1: Obtención de la flag / Obtaining the flag

**Explicación:**

La lista de respuestas del room original contiene un único valor que corresponde a la bandera buscada durante la resolución del laboratorio. Se conserva de forma literal:

1. 851b8233a8c09400ec30651bd1529bf1ed02790b

### Tabla Unificada de Preguntas y Respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el valor de la flag del usuario (user.txt)? | `851b8233a8c09400ec30651bd1529bf1ed02790b` |

---

**Metodología:** Enumeración del sitio WordPress → identificación de plugins vulnerables → explotación para obtener una reverse shell → escalada de privilegios → extracción de la flag.

### Cadena de ataque / Attack Chain

- Enumeración web (WordPress y plugins)
- Explotación de una vulnerabilidad de la aplicación pública
- Reverse shell como usuario de bajos privilegios
- Escalada de privilegios hasta root
- Lectura de la flag

**Learning chain:** Reconocimiento → Explotación web → Shell inversa → Escalada de privilegios → Captura de flag

**Lección:** *La enumeración exhaustiva de plugins y versiones de un CMS suele ser la puerta de entrada para comprometer un servidor; una shell inicial casi nunca es el destino final.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1059 (Command and Scripting Interpreter), T1068 (Exploitation for Privilege Escalation)

**Fuente:** [TryHackMe - Tech_Supp0rt_ 1](https://tryhackme.com/room/techsupp0rt1)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.