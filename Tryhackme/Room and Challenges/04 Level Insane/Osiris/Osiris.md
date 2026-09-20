# Osiris

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|------|------|---------|--------|-------------|---------|
| Insane | CTF | `osiris` | [TryHackMe](https://tryhackme.com/room/osiris) | 04 Level Insane | TryHackMe | ctf / flags largas / resolución escalonada | Resolución del reto Osiris: tres flags obtenidas de forma escalonada, con la última de longitud considerable. |

---

**Contexto:** Sala CTF de nivel Insane con tres respuestas encadenadas. La dificultad reside en la fase final, cuya flag es notablemente más larga que las anteriores, lo que indica un proceso de recolección o reconstrucción escalonado.

> **ES:** Sala CTF de nivel Insane con tres respuestas encadenadas. La dificultad reside en la fase final, cuya flag es notablemente más larga que las anteriores, lo que indica un proceso de recolección o reconstrucción escalonado.

> **EN:** Insane-difficulty CTF room with three chained answers. The difficulty lies in the final phase, whose flag is noticeably longer than the previous ones, indicating a staged collection or reconstruction process.

## Solucionario

### Task 1: Respuestas del laboratorio / Lab answers

**Explicación:**
Lista completa de respuestas de la sala tal como se recoge en la nota original, sin modificar:

1. 1. THM{89b556686aa61301d4a72a7b12e59368a516c940}
   2. THM{d9c19f35fccde779d645f19d5bb0ac41dcd3586f}
   3. THM{a77538464954d29a64c607f2318d930ccf4da5cccb308c7334c43fef9c94984448cf732f6de227cbfae9172ee2654e56704568ada698fb241c52148d338a3245}

| # | Pregunta | Respuesta |
|---|---|-----------|
| 1 | 1.1 | `THM{89b556686aa61301d4a72a7b12e59368a516c940}` |
| 2 | 1.2 | `THM{d9c19f35fccde779d645f19d5bb0ac41dcd3586f}` |
| 3 | 1.3 | `THM{a77538464954d29a64c607f2318d930ccf4da5cccb308c7334c43fef9c94984448cf732f6de227cbfae9172ee2654e56704568ada698fb241c52148d338a3245}` |

---

**Metodología:**
1. **Resolución escalonada:** completar cada fase y recoger su flag exacta.
2. **Verificación de integridad:** comprobar la longitud de cada flag para confirmar que no falta ningún fragmento.
3. **Recolección final:** ensamblar los elementos de la última fase para obtener la flag larga completa.

### Cadena de ataque / Attack Chain

1. Fase 1 → `THM{89b556686aa61301d4a72a7b12e59368a516c940}`.
2. Fase 2 → `THM{d9c19f35fccde779d645f19d5bb0ac41dcd3586f}`.
3. Fase 3 (flag larga) → `THM{a77538464954d29a64c607f2318d930ccf4da5cccb308c7334c43fef9c94984448cf732f6de227cbfae9172ee2654e56704568ada698fb241c52148d338a3245}`.

**Learning chain:** flag 1 → flag 2 → flag larga final (fase 3).

**Lección:** *Cuando una flag crece notablemente entre fases, suele ser señal de que se construye por partes: no descartar fragmentos y validar la longitud final evita entregar una flag incompleta.*

**MITRE ATT&CK:** N/A (CTF interactivo sin infraestructura ofensiva documentada)

**Fuente:** [TryHackMe - Osiris](https://tryhackme.com/room/osiris)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.