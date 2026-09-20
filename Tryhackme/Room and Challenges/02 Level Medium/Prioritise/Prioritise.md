# Prioritise

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF / Challenge | prioritise | https://tryhackme.com/room/prioritise | 02 Level Medium | TryHackMe | Enumeración, Explotación, Escalada de privilegios | Captura de la flag del sistema (compromiso total) |

---

**Contexto:** La sala **Prioritise** es un CTF de estilo boot2root en el que la resolución culmina con la captura de una flag en formato `flag{...}`. El objetivo consiste en enumerar la máquina, identificar el vector de entrada, explotarlo y priorizar las acciones hasta obtener la flag acreditativa del compromiso.

## Solucionario

### Task 1: Flags del sistema / System flags
**Explicación:**

La flag acreditativa se consigue al comprometer la máquina objetivo y acceder al contenido que resuelve la sala.

```
1. flag{65f2f8cfd53d59422f3d7cc62cc8fdcd}
```

Respuesta: `flag{65f2f8cfd53d59422f3d7cc62cc8fdcd}`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag del reto? | `flag{65f2f8cfd53d59422f3d7cc62cc8fdcd}` |

---

**Metodología:** Enumeración de la máquina objetivo, identificación de servicios y vectores de entrada, explotación de la vía crítica y captura de la flag.

### Cadena de ataque / Attack Chain

```
Reconocimiento del objetivo
        │
        ▼
Identificación del vector de entrada
        │
        ▼
Explotación → acceso inicial
        │
        ▼
Recuperación de la flag (flag{...})
```

**Learning chain:** Enumeración → focalización del vector → explotación → `flag{65f2f8cfd53d59422f3d7cc62cc8fdcd}`.

**Lección:** *En un CTF conviene priorizar los vectores de mayor impacto: la ruta más corta al compromiso suele ser la combinación de un servicio expuesto y una configuración débil.*

**MITRE ATT&CK:** T1580 Cloud Infrastructure Discovery · T1046 Network Service Discovery · T1068 Exploitation for Privilege Escalation.

**Fuente:** [TryHackMe - Prioritise](https://tryhackme.com/room/prioritise)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.