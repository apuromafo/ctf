# When Hearts Collide [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM
* **Tipo / Type:** CTF (Evento "Love at First Breach 2026" - Módulo LAFB CTF 2026)
* **Slug:** `lafb2026e1`
* **Link:** https://tryhackme.com/room/lafb2026e1
* **Sección / Section:** 02 Level Medium
* **Fuente / Source:** Web (API THM `api/v2/rooms/tasks?roomCode=lafb2026e1` + websearch de walkthroughs)

## Solucionario de Tareas / Task Solutions

> **ES:** Sala de evento (Love at First Breach 2026) de dificultad Media. El tema es una **app de citas para perros**: la web calcula el hash MD5 de la fotografía que subes y lo compara contra los hashes de los candidatos ("one true dog"). Como MD5 sufre colisiones prácticas, se puede subir una foto inocente cuyo hash coincida con el del perro objetivo y obtener el *love match* y la flag.
> **EN:** Event room (Love at First Breach 2026) of Medium difficulty. The theme is a **dog dating app**: the web computes the MD5 hash of the photo you upload and compares it against the hashes of the candidates ("one true dog"). Because MD5 suffers practical collisions, you can upload a benign photo whose hash matches the target dog's and get the *love match* and the flag.

### Task 1 - The One True Dog

> **ES:** `nmap` revela `22/tcp` (SSH) y `80/tcp` (web). La aplicación implementa un *matchmaker* de perros: `POST` tu foto, calcula su MD5 `md5(foto)` y lo compara con una tabla de hashes de candidatos calculada con el mismo algoritmo. Se busca la foto del "one true dog" cuyo hash está en la tabla. El ataque es una **colisión MD5**: se genera (con herramientas de fastcollación/fastcoll) una foto alternativa que produzca exactamente el mismo digest que la fotografía objetivo; al coincidir el hash, el sistema da el *love match* y devuelve la flag. 1 pregunta.
> **EN:** `nmap` reveals `22/tcp` (SSH) and `80/tcp` (web). The app implements a dog *matchmaker*: you `POST` your photo, it computes `md5(photo)` and compares it against a table of candidate hashes computed with the same algorithm. You need the photo of the "one true dog" whose hash is in the table. The attack is an **MD5 collision**: generate (with fastcoll-style tooling) an alternate photo that yields exactly the same digest as the target photograph; once the hash matches, the system gives the *love match* and returns the flag. 1 question.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the flag obtained by finding your one true dog? | `THM{hash_puppies_4_all}` |

## Metodología / Methodology

1. **Paso / Step - Reconocimiento:** `nmap -sV -sC <target>` → `22/tcp` OpenSSH y `80/tcp` servidor web con la app de citas canina.
2. **Paso / Step - Análisis de la app:** La web de *matching* pide subir una foto. Interceptando la petición (Burp) se ve que el servidor responde con el par `md5(foto)` y su veredicto sobre cada candidato.
3. **Paso / Step - Comprender la validación:** El servidor compara `md5(foto_subida)` contra una lista de hashes de candidatos; el "one true dog" es el perfil cuya foto corresponde a uno de esos digests.
4. **Paso / Step - Colisión MD5:** Con `fastcoll` (o equivalentes) se genera una foto con el mismo MD5 que la fotografía del perro objetivo pero contenido diferente. Se sube esta foto.
5. **Paso / Step - Love match:** El servidor ve que `md5` coincide con el hash del "one true dog" → *love match* → se devuelve la flag `THM{hash_puppies_4_all}`.

### Cadena de ataque / Attack Chain

```
nmap -> 22/tcp SSH + 80/tcp web (app love/dog matching)
  -> POST foto -> servidor calcula md5(foto)
  -> tabla de candidatos con md5("one true dog")
  -> fastcoll -> colisión MD5 (mismo digest, contenido distinto)
  -> hash coincide -> love match
  -> THM{hash_puppies_4_all}
```

**Lección:** MD5 no es apto para autenticar o validar fotos; cualquier verificación de integridad o identidad debe usar funciones criptográficas resistentes a colisiones (SHA-256/SHA-3).

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.