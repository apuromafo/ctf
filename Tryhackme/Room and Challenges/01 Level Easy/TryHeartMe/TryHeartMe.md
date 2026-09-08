# TryHeartMe

| **Dificultad** | Easy |
| **Tipo** | CTF |
| **Slug** | `lafb2026e5` |
| **Link** | [TryHackMe](https://tryhackme.com/room/lafb2026e5) |
| **Sección** | 01 Level Easy |
| **Fuente** | Web (API THM `api/v2/rooms/tasks?roomCode=lafb2026e5` + websearch de walkthroughs) |
| **Componentes** | JWT / HS256 / jwt.io / jwt_tool / jwt2john / hashcat / alg=none / cookie tampering |
| **Impacto** | Manipulación de JWT para escalar privilegios: forjar el rol del token y acceder al panel admin de una tienda |

---

**Contexto:** Sala de evento (Love at First Breach 2026) de dificultad Fácil. El tema es la **manipulación de JWT**: el control de acceso de una tienda de perfiles depende de un token firmado con HS256 y un secreto débil (o configurable vacío/`none`). Forjando los `claims` del token (por ejemplo `role=admin` / `username=admin`) y re-firmándolo se obtiene acceso al panel de administración de la tienda y la flag.

## Solucionario

### Task 1: Admin Shop

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag? | `THM{v4l3nt1n3_jwt_c00k13_t4mp3r_4dm1n_sh0p}` |

**Explicación:** La tienda de perfiles de citas emite una cookie de sesión JWT al hacer login (`token` en cookie o header `Authorization`). Se decodifica (base64url): el header dice `{"alg":"HS256","typ":"JWT"}`. El secreto es débil y se crackea con `hashcat`/`john` sobre `jwt2john` (diccionario en segundos), o el servidor acepta `alg=none`. Se reescribe el `payload` cambiando el `role`/`username` a `admin` y se re-firma con el secreto encontrado (o con firma vacía en `alg=none`). Al enviar el token manipulado, el panel `admin`/`shop_admin` se desbloquea y muestra la flag `THM{v4l3nt1n3_jwt_c00k13_t4mp3r_4dm1n_sh0p}`.

---

**Metodología:**
1. **Reconocimiento:** web de perfiles con login. Se intercepta la sesión: la cookie es un JWT (`eyJ...`).
2. **Análisis del token:** en jwt.io (o `jwt_tool`) se separan header, payload y firma. El header dice `{"alg":"HS256","typ":"JWT"}`; hay claims tipo `username`/`role` en el `payload`.
3. **Obtener el secreto:** `jwt2john` genera el hash del token y `hashcat -m 16500` lo rompe con un diccionario (segundos); alternativamente se prueba si el servidor acepta `alg=none` (token con el header cambiado y firma vacía).
4. **Forjar el token:** se edita el `payload` (`role=admin` o `username=admin`) y se re-firma con el secreto crackeado (o se deja sin firma en `alg=none`).
5. **Acceso admin:** se sustituye la cookie/header por el token forjado; la tienda carga el panel `admin`/shop admin y muestra la flag `THM{v4l3nt1n3_jwt_c00k13_t4mp3r_4dm1n_sh0p}`.

**Learning chain:** web de perfiles → login → cookie JWT (HS256) → decodificar (jwt.io / jwt_tool) → header alg HS256 → jwt2john + hashcat → secreto débil crackeado (o alg=none) → forjar payload: role=admin / username=admin → re-firmar con el secreto → cookie manipulada → panel de la shop admin → THM{v4l3nt1n3_jwt_c00k13_t4mp3r_4dm1n_sh0p}

**MITRE ATT&CK:** T1550.001 (Use Alternate Authentication Material: Application Access Token), T1190 (Exploit Public-Facing Application), T1110 (Brute Force)

**Fuente:** [TryHackMe - TryHeartMe](https://tryhackme.com/room/lafb2026e5)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
