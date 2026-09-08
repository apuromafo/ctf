# Love Letter Locker

| **Dificultad** | Easy |
| **Tipo** | CTF |
| **Slug** | `lafb2026e2` |
| **Link** | [TryHackMe](https://tryhackme.com/room/lafb2026e2) |
| **Sección** | 01 Level Easy |
| **Fuente** | Web (API THM `api/v2/rooms/tasks?roomCode=lafb2026e2` + websearch de walkthroughs) |
| **Componentes** | curl / Burp Repeater / BOLA / IDOR / OWASP API4 |
| **Impacto** | BOLA/IDOR sobre una API de cartas de amor: leer cartas de otros usuarios sin control de autorización por objeto |

---

**Contexto:** Sala de evento (Love at First Breach 2026) de dificultad Fácil. El tema es una **casilla de cartas de amor privadas**: cada carta se referencia por un identificador secuencial en la URL sin ningún control de autorización por objeto. Enumerando ese `id` se leen cartas de otros usuarios y entre ellas aparece la flag (IDOR/BOLA).

## Solucionario

### Task 1: Private Love Letters

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag? | `THM{1_c4n_r3ad_4ll_l3tters_w1th_th1s_1d0r}` |

**Explicación:** La app lista y abre cartas mediante `GET /letter?id=<N>`. El renglón `/letter?id=1` (o similar) muestra una carta legítima del usuario actual. Probando `?id=N-1` y `?id=N+1` se obtienen cartas de otros usuarios: el servidor consulta la base de datos por `id` directamente, sin verificar a qué usuario pertenece la carta (ausencia de ACL a nivel de objeto = **BOLA/IDOR**, OWASP API4:2023). Entre las cartas ajenas se encuentra la que contiene la flag. 1 pregunta.

**Metodología:**
1. **Reconocimiento:** web de cartas de amor con el listado de los mensajes del usuario autenticado; cada carta se abre con `GET /letter?id=<N>`.
2. **Detección del patrón:** el `id` es secuencial y la respuesta incluye el contenido completo de la carta sin indicar el propietario.
3. **BOLA/IDOR:** con `curl` / Burp Repeater se pide `?id=N±1`; el servidor devuelve cartas de otros usuarios, ya que consulta por `id` directamente sin verificar a qué usuario pertenece (ausencia de ACL a nivel de objeto, OWASP API4:2023).
4. **Flag:** enumerando unos pocos ids se alcanza la carta con la flag: `THM{1_c4n_r3ad_4ll_l3tters_w1th_th1s_1d0r}`.

```
web de cartas de amor -> sesión autenticada
  -> GET /letter?id=1    -> carta propia (baseline)
  -> GET /letter?id=2..N -> sin ACL por objeto
  -> BOLA/IDOR -> carta de otro usuario leída
  -> THM{1_c4n_r3ad_4ll_l3tters_w1th_th1s_1d0r}
```

**Lección:** Un `id` enumerable sin control de autorización por objeto es BOLA/IDOR (OWASP API4): toda consulta a un recurso debe verificar la pertenencia antes de devolver datos.

**Learning chain:** web de cartas de amor → sesión autenticada → GET /letter?id=1 (baseline) → GET /letter?id=N±1 sin ACL por objeto → BOLA/IDOR → THM{1_c4n_r3ad_4ll_l3tters_w1th_th1s_1d0r}

**MITRE ATT&CK:** T1078 (Valid Accounts), T1213 (Data from Information Repositories)

**Fuente:** [TryHackMe - Love Letter Locker](https://tryhackme.com/room/lafb2026e2)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
