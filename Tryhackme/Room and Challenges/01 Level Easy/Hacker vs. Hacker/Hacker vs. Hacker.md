# Hacker vs. Hacker

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `hackervshacker` | [TryHackMe](https://tryhackme.com/room/hackervshacker) | 01 Level Easy | THM | Web shell, C2, Hijacking, Flags | Tomar el control de un servidor comprometido y de su C2 |

---

**Contexto:** Reto en el que otro hacker ya ha comprometido un equipo y ha dejado su infraestructura de mando y control: hay que encontrar la web shell oculta, hacerse con el control del panel del atacante y recuperar las banderas que dejó.

> **ES:** Descubrir la web shell, interceptar el panel de control del atacante y capturar las banderas del servidor.
> **EN:** Find the web shell, hijack the attacker's control panel and capture the flags.

## Solucionario

### Task 1: El reto / The Challenge

**Explicación:** Reto de una única tarea: localizar la web shell oculta, hacerse con el control del panel de C2 del atacante y leer las credenciales y banderas que dejó.

1. `thm{af7e46b68081d4025c5ce10851430617}`
2. `thm{7b708e5224f666d3562647816ee2a1d4}`

### Tabla unificada de preguntas y respuestas

| Task | Pregunta | Respuesta |
|------|----------|-----------|
| 1.1 | Bandera del panel de administración | `thm{af7e46b68081d4025c5ce10851430617}` |
| 1.2 | Bandera de las credenciales | `thm{7b708e5224f666d3562647816ee2a1d4}` |

---

**Metodología:** Reconocimiento de la web, localización de la web shell dejada por el atacante, acceso a su panel de C2 y exfiltración de las credenciales y banderas almacenadas.

### Cadena de ataque / Attack Chain

```text
Recon -> descubrir web shell -> acceder al panel de C2 -> capturar credenciales y flags
```

**Learning chain:** Recon → Web shell discovery → C2 hijack → Credentials exfiltration → Flags

**Lección:** *Un atacante que deja su web shell y su panel de C2 accesibles se convierte a su vez en víctima: el control de la infraestructura comprometida vale más que cualquier credencial.*

**MITRE ATT&CK:** N/A (Reto de hijacking)

**Fuente:** [TryHackMe - Hacker vs. Hacker](https://tryhackme.com/room/hackervshacker)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.