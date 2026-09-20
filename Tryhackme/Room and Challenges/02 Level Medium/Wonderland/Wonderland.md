# Wonderland

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Walkthrough | wonderland | https://tryhackme.com/room/wonderland | 02 Level Medium | TryHackMe | Linux, CTF, Enumeration, PrivEsc | Máquina CTF Linux basada en Alicia en el País de las Maravillas: enumeración y escalada de privilegios |

---

**Contexto:** La sala **Wonderland** es una máquina CTF de nivel medio inspirada en "Alicia en el País de las Maravillas". El reto combina enumeración web y de servicios en Linux, la explotación de bins SUID y la escalada hasta el usuario root. Las respuestas del solucionario recogen las flags de usuario y de root obtenidas al completar el compromiso completo de la máquina.

## Solucionario

### Task 1: Flags de la máquina

**Explicación:**

Se completa el compromiso total de la máquina Wonderland: primero se obtiene la flag del usuario (`user.txt`) con el mensaje "Curiouser and curiouser!" y, tras la escalada de privilegios, la flag de root (`root.txt`) con la referencia al poema del Sombrerero Loco.

1. `thm{"Curiouser and curiouser!"}`
2. `thm{Twinkle, twinkle, little bat! How I wonder what you’re at!}`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1.1 | Flag de usuario | `thm{"Curiouser and curiouser!"}` |
| 1.2 | Flag de root | `thm{Twinkle, twinkle, little bat! How I wonder what you’re at!}` |

---

**Metodología:** Compromiso de máquina Linux: enumeración de servicios y contenido web, explotación inicial, búsqueda de binarios con privilegios y escalada de privilegios hasta root para extraer ambas flags.

**Learning chain:** Reconocimiento → explotación inicial → acceso como usuario → abuso de privilegios → flag de root.

**Lección:** *La metáfora del "país de las maravillas" recuerda que tras cada servicio descubierto puede esconderse un camino oculto hacia el control total del sistema.*

**MITRE ATT&CK:** T1059 Command and Scripting Interpreter · T1548 Abuse Elevation Control Mechanism · T1078 Valid Accounts.

**Fuente:** [TryHackMe - Wonderland](https://tryhackme.com/room/wonderland)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.