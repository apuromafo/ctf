# Ledger

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Hard | CTF | ledger | https://tryhackme.com/room/ledger | 03 Level Hard | TryHackMe | Web, enumeración, bypass de autenticación | Alto |

---

**Contexto:**
> **ES:** Reto web de nivel Hard centrado en una aplicación "Ledger". La clave está en la enumeración exhaustiva y en un bypass de autenticación/certificación para obtener las dos banderas del entorno.
> **EN:** Hard-level web challenge focused on a "Ledger" application. The key lies in exhaustive enumeration and an authentication/certification bypass to obtain the two environment flags.

## Solucionario

### Task 1: Tarea 1
**Explicación:**
1. 1. THM{ENUMERATION_IS_THE_KEY}
   2. THM{THE_BYPASS_IS_CERTIFIED!}

### Preguntas y Respuestas / Questions and Answers

| Task | Respuesta / Answer |
|---|---|
| 1.1 | `THM{ENUMERATION_IS_THE_KEY}` |
| 1.2 | `THM{THE_BYPASS_IS_CERTIFIED!}` |

---

**Metodología:**
1. Enumeración exhaustiva de la aplicación web para descubrir rutas, parámetros y mecanismos de autenticación.
2. Identificación del bypass aplicable al flujo de autenticación.
3. Obtención de las banderas.

### Cadena de ataque / Attack Chain
1. Enumeración de la aplicación.
2. Bypass de autenticación.
3. Extracción de las banderas.

**Learning chain:** Enumeración -> Bypass de autenticación -> Banderas.

**Lección:** *La enumeración es la clave: muchas protecciones caen cuando se conoce el mecanismo exacto que las sostiene.*

**MITRE ATT&CK:**
- T1046 (Network Service Discovery)
- T1190 (Exploit Public-Facing Application)
- T1550 (Use Alternate Authentication Material)

**Fuente:** [TryHackMe - Ledger](https://tryhackme.com/room/ledger)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.