# Contrabando

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Hard | Reto CTF • Contraseñas | contrabando | https://tryhackme.com/room/contrabando | 03 Level Hard | TryHackMe | Banderas, gestor de contraseñas, artefactos del laboratorio | Alto |

---

**Contexto:**
> **ES:** Desafío tipo CTF sobre contrabando digital: recuperar las dos banderas asociadas a la actividad principal y al manejo de contraseñas del entorno.
> **EN:** CTF-style challenge about digital smuggling: recover the two flags tied to the main activity and to the environment's password handling.

## Solucionario

### Task 1: Banderas del contrabando / Smuggling flags
**Explicación:**
1. THM{Th3_BeST_SmuGGl3R_In_Da_GalaXy}
2. THM{All_AbouT_PassW0rds}

### Preguntas y Respuestas / Questions and Answers

| Task | Respuesta / Answer |
|---|---|
| 1.1 | `THM{Th3_BeST_SmuGGl3R_In_Da_GalaXy}` |
| 1.2 | `THM{All_AbouT_PassW0rds}` |

---

**Metodología:**
Localización de la bandera principal asociada a la actividad del entorno y posterior extracción de la bandera centrada en el manejo de contraseñas.

### Cadena de ataque / Attack Chain
1. Exploración del entorno y localización de la primera bandera.
2. Análisis del gestor o almacenamiento de contraseñas.
3. Obtención de la segunda bandera.

**Learning chain:**
Exploración -> Primera flag -> Análisis de contraseñas -> Segunda flag.

**Lección:** *Las contraseñas suelen ser el punto débil: donde se almacenan también se ocultan las pistas.*

**MITRE ATT&CK:**
- T1555 Credentials from Password Stores
- T1003 OS Credential Dumping

**Fuente:** [TryHackMe - Contrabando](https://tryhackme.com/room/contrabando)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.