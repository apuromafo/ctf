# Surfer

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | CTF / Web challenge | `surfer` | https://tryhackme.com/room/surfer | 01 Level Easy | TryHackMe | SSRF / Burp Suite / Export to PDF / /robots.txt / /backup/chat.txt / /internal/admin.php / admin:admin | Lectura de una página interna restringida a localhost mediante SSRF en la funcionalidad de exportar a PDF y captura de la flag. |

---

**Contexto:** Reto web de nivel fácil centrado en SSRF (Server-Side Request Forgery). La aplicación 24X7 System+ expone un login y un botón "Export to PDF" que hace que el servidor genere un PDF a partir de una URL. Tras enumerar `/robots.txt` se descubre `/backup/chat.txt`, donde Kate deja la pista de que el usuario y la contraseña son iguales; se accede con `admin:admin`. En el panel aparece la página interna `/internal/admin.php`, restringida a localhost. Interceptando con Burp Suite la petición del exportador y cambiando el parámetro `url` a `http://127.0.0.1/internal/admin.php`, el servidor solicita esa página interna y revela la flag.

> **ES:** Reto de SSRF: tras loguear en la app con `admin:admin` (pista en `/backup/chat.txt`), se abusa de "Export to PDF" modificando el parámetro `url` hacia `http://127.0.0.1/internal/admin.php` para que el servidor lea la página interna y muestre la flag.
> **EN:** SSRF challenge: after logging in to the app with `admin:admin` (hint in `/backup/chat.txt`), abuse the "Export to PDF" feature by changing the `url` parameter to `http://127.0.0.1/internal/admin.php` so the server fetches the internal page and reveals the flag.

## Solucionario

### Task 1: Obtén la bandera / Get the flag

**Explicación:** El objetivo es leer el contenido de `/internal/admin.php`, que solo es accesible desde localhost. Usando Burp Suite se intercepta la petición que dispara "Export to PDF" y se modifica el valor del campo `url` para que apunte a `http://127.0.0.1/internal/admin.php`; el servidor ejecuta esa petición internamente y devuelve la página con la flag.

```text
1. flag{6255c55660e292cf0116c053c9937810}
```

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | ¿Cuál es la flag? / What is the flag? | `flag{6255c55660e292cf0116c053c9937810}` |

---

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | ¿Cuál es la flag? / What is the flag? | `flag{6255c55660e292cf0116c053c9937810}` |

---

**Metodología:** Enumeración web (robots.txt -> /backup/chat.txt) -> login admin:admin -> descubrir /internal/admin.php (solo localhost) -> interceptar "Export to PDF" con Burp Suite -> modificar el parámetro `url` a http://127.0.0.1/internal/admin.php -> leer la página interna -> flag.

### Cadena de ataque / Attack Chain

```text
Nmap -> puertos 22/80 -> robots.txt -> /backup/chat.txt -> pista de credenciales -> login admin:admin -> /internal/admin.php (restringido) -> Burp Suite -> export2pdf con url=http://127.0.0.1/internal/admin.php -> SSRF -> flag
```

**Learning chain:** Enumeración web -> obtención de credenciales -> identificación de recurso interno restringido -> interceptación con proxy -> manipulación de la URL -> SSRF -> exfiltración de la flag.

**Lección:** *Un endpoint que renderiza una URL controlable a petición del usuario es un SSRF: si una página interna solo se sirve a localhost, basta con apuntar la URL del exportador a 127.0.0.1 para leerla.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1005 (Data from Local System).

**Fuente:** [TryHackMe - Surfer](https://tryhackme.com/room/surfer)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.

**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.

**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).

**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.