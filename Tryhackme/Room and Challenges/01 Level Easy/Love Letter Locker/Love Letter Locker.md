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

---

**Metodología:**
1. **Reconocimiento:** web de cartas de amor con el listado de los mensajes del usuario autenticado; cada carta se abre con `GET /letter?id=<N>`.
2. **Detección del patrón:** el `id` es secuencial y la respuesta incluye el contenido completo de la carta sin indicar el propietario.
3. **BOLA/IDOR:** con `curl` / Burp Repeater se pide `?id=N±1`; el servidor devuelve cartas de otros usuarios, ya que consulta por `id` directamente sin verificar a qué usuario pertenece (ausencia de ACL a nivel de objeto, OWASP API4:2023).
4. **Flag:** enumerando unos pocos ids se alcanza la carta con la flag: `THM{1_c4n_r3ad_4ll_l3tters_w1th_th1s_1d0r}`.

**Learning chain:** web de cartas de amor → sesión autenticada → GET /letter?id=1 (baseline) → GET /letter?id=N±1 sin ACL por objeto → BOLA/IDOR → THM{1_c4n_r3ad_4ll_l3tters_w1th_th1s_1d0r}

**MITRE ATT&CK:** T1078 (Valid Accounts), T1213 (Data from Information Repositories)

**Fuente:** [TryHackMe - Love Letter Locker](https://tryhackme.com/room/lafb2026e2)