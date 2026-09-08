# When Hearts Collide

| **Dificultad** | Medium |
| **Tipo** | CTF |
| **Slug** | `lafb2026e1` |
| **Link** | [TryHackMe](https://tryhackme.com/room/lafb2026e1) |
| **Sección** | 02 Level Medium |
| **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | MD5 / hash collision / fastcoll / web app / crypto |
| **Impacto** | Explotar una colisión MD5 en una app de citas para perros para "encontrar" el one true dog y obtener la flag |

---

**Contexto:** Sala de evento (Love at First Breach 2026) de dificultad Media. El tema es una **app de citas para perros**: la web calcula el hash MD5 de la fotografía que subes y lo compara contra los hashes de los candidatos ("one true dog"). Como MD5 sufre colisiones prácticas, se puede subir una foto inocente cuyo hash coincida con el del perro objetivo y obtener el *love match* y la flag.

## Solucionario

### Task 1: The One True Dog

**Explicación:**

`nmap` revela `22/tcp` (SSH) y `80/tcp` (web). La aplicación implementa un *matchmaker* de perros: `POST` tu foto, calcula su MD5 `md5(foto)` y lo compara con una tabla de hashes de candidatos calculada con el mismo algoritmo. Se busca la foto del "one true dog" cuyo hash está en la tabla. El ataque es una **colisión MD5**: se genera (con herramientas de fastcoll/fastcollación) una foto alternativa que produzca exactamente el mismo digest que la fotografía objetivo; al coincidir el hash, el sistema da el *love match* y devuelve la flag: `THM{hash_puppies_4_all}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag obtained by finding your one true dog? | `THM{hash_puppies_4_all}` |

---

**Metodología:**

1. **Reconocimiento:** `nmap -sV -sC <target>` → `22/tcp` OpenSSH y `80/tcp` servidor web con la app de citas canina.
2. **Análisis de la app:** La web de *matching* pide subir una foto. Interceptando la petición (Burp) se ve que el servidor responde con el par `md5(foto)` y su veredicto sobre cada candidato.
3. **Comprender la validación:** El servidor compara `md5(foto_subida)` contra una lista de hashes de candidatos; el "one true dog" es el perfil cuya foto corresponde a uno de esos digests.
4. **Colisión MD5:** Con `fastcoll` (o equivalentes) se genera una foto con el mismo MD5 que la fotografía del perro objetivo pero contenido diferente. Se sube esta foto.
5. **Love match:** El servidor ve que `md5` coincide con el hash del "one true dog" → *love match* → se devuelve la flag `THM{hash_puppies_4_all}`.

**Learning chain:** nmap -> 22/tcp SSH + 80/tcp web -> POST foto -> md5(foto) -> tabla de candidatos -> fastcoll colisión MD5 -> hash coincide -> love match -> flag

**Lección:** *MD5 no es apto para autenticar o validar fotos; cualquier verificación de integridad o identidad debe usar funciones criptográficas resistentes a colisiones (SHA-256/SHA-3).*

**MITRE ATT&CK:** T1600 (Weaken Encryption) · T1203 (Exploitation for Client Execution) · CWE-327 (Broken or Risky Crypto Algorithm)

**Fuente:** [TryHackMe - When Hearts Collide](https://tryhackme.com/room/lafb2026e1)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
