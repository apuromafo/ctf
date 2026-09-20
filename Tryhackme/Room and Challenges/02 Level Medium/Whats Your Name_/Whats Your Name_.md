# Whats Your Name_

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF / Explotación | whatsyourname | https://tryhackme.com/room/whatsyourname | 02 Level Medium | TryHackMe | Aplicación web, autenticación, manipulación de entradas | Acceso a las cuentas moderador y administrador |

---

**Contexto:** **Whats Your Name_** es un reto web en el que la aplicación solicita un nombre como entrada y, mediante la manipulación de dicha entrada, es posible alterar el flujo de la aplicación y recuperar credenciales privilegiadas. La resolución permite obtener las credenciales de acceso de los usuarios **mod** y **admin** del sistema.

## Solucionario

### Task 1: Obtención de credenciales / Credential capture
**Explicación:**

Interactuando con la aplicación web y abusando de la entrada que pide el nombre se recuperan las credenciales de acceso de las cuentas privilegiadas del servicio.

1. `ModP@wnEd`
2. `AdM!nP@wnEd`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1.1 | Credencial de la cuenta moderador | `ModP@wnEd` |
| 1.2 | Credencial de la cuenta administrador | `AdM!nP@wnEd` |

---

**Metodología:** Análisis de la aplicación web, manipulación de la entrada ("nombre") para alterar el flujo de la aplicación y extracción de las credenciales de las cuentas privilegiadas.

**Learning chain:** Reconocimiento → análisis de la aplicación → manipulación de entrada → extracción de credenciales → acceso privilegiado.

**Lección:** *Toda entrada reflejada en una aplicación es una superficie de ataque: una validación débil del "nombre" puede exponer credenciales administrativas.*

**MITRE ATT&CK:** T1190 Exploit Public-Facing Application · T1059 Command and Scripting Interpreter · T1078 Valid Accounts.

**Fuente:** [TryHackMe - Whats Your Name_](https://tryhackme.com/room/whatsyourname)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.