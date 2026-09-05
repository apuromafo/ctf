# TryHeartMe [EASY]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** EASY
* **Tipo / Type:** CTF (Evento "Love at First Breach 2026" - Módulo LAFB CTF 2026)
* **Slug:** `lafb2026e5`
* **Link:** https://tryhackme.com/room/lafb2026e5
* **Sección / Section:** 01 Level Easy
* **Fuente / Source:** Web (API THM `api/v2/rooms/tasks?roomCode=lafb2026e5` + websearch de walkthroughs)

## Solucionario de Tareas / Task Solutions

> **ES:** Sala de evento (Love at First Breach 2026) de dificultad Fácil. El tema es la **manipulación de JWT**: el control de acceso de una tienda de perfiles depende de un token firmado con HS256 y un secreto débil (o configurable vacío/`none`). Forjando los `claims` del token (por ejemplo `role=admin` / `username=admin`) y re-firmándolo se obtiene acceso al panel de administración de la tienda y la flag.
> **EN:** Event room (Love at First Breach 2026) of Easy difficulty. The theme is **JWT tampering**: access control in a profile shop relies on a token signed with HS256 and a weak secret (or empty/`none`-accepting config). Forging the token's `claims` (e.g. `role=admin` / `username=admin`) and re-signing it grants access to the store's admin panel and the flag.

### Task 1 - Admin Shop

> **ES:** La tienda de perfiles de citas emite una cookie de sesión JWT al hacer login (`token` en cookie o header `Authorization`). Se decodifica (base64url): el header dice `{"alg":"HS256","typ":"JWT"}`. El secreto es débil y se crackea con `hashcat`/`john` sobre `jwt2john` (diccionario en segundos), o el servidor acepta `alg=none`. Se reescribe el `payload` cambiando el `role`/`username` a `admin` y se re-firma con el secreto encontrado (o con firma vacía en `alg=none`). Al enviar el token manipulado, el panel `admin`/`shop_admin` se desbloquea y muestra la flag. 1 pregunta.
> **EN:** The dating-profile shop issues a JWT session cookie on login (`token` cookie or `Authorization` header). Decode it (base64url): header says `{"alg":"HS256","typ":"JWT"}`. The secret is weak and cracked with `hashcat`/`john` over `jwt2john` (wordlist within seconds), or the server accepts `alg=none`. Rewrite the `payload` changing `role`/`username` to `admin` and re-sign with the found secret (or empty signature under `alg=none`). Sending the tampered token unlocks the `admin`/`shop_admin` panel, which shows the flag. 1 question.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the flag? | `THM{v4l3nt1n3_jwt_c00k13_t4mp3r_4dm1n_sh0p}` |

## Metodología / Methodology

1. **Paso / Step - Reconocimiento:** Web de perfiles con login. Se intercepta la sesión: la cookie es un JWT (`eyJ...`).
2. **Paso / Step - Análisis del token:** En jwt.io (o `jwt_tool`) se separan header, payload y firma. Algoritmo HS256; claims tipo `username`/`role` en el `payload`.
3. **Paso / Step - Obtener el secreto:** `jwt2john` genera el hash del token y `hashcat -m 16500` lo rompe con un diccionario; alternativamente se prueba si el servidor acepta `alg=none` (token con el header cambiado y firma vacía).
4. **Paso / Step - Forjar el token:** Se edita el `payload` (`role=admin` o `username=admin`) y se re-firma con el secreto crackeado (o se deja sin firma en `alg=none`).
5. **Paso / Step - Acceso admin:** Se sustituye la cookie/header por el token forjado; la tienda carga el panel `admin`/shop admin y muestra la flag `THM{v4l3nt1n3_jwt_c00k13_t4mp3r_4dm1n_sh0p}`.

### Cadena de ataque / Attack Chain

```
web de perfiles -> login -> cookie JWT (HS256)
  -> decodificar (jwt.io / jwt_tool) -> header alg HS256
  -> jwt2john + hashcat -> secreto débil crackeado (o alg=none)
  -> forjar payload: role=admin / username=admin
  -> re-firmar con el secreto -> cookie manipulada
  -> panel de la shop admin -> THM{v4l3nt1n3_jwt_c00k13_t4mp3r_4dm1n_sh0p}
```

**Lección:** Nunca confíes el control de acceso a gestiones de un JWT firmado con un secreto débil; usa secretos aleatorios de alta entropía y rechaza `alg=none`/algoritmos no negociados.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.