# h4cked

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `h4cked` | [TryHackMe](https://tryhackme.com/room/h4cked) | 01 Level Easy | THM | FTP, Hydra, Reverse Shell, Privilege Escalation, Rootkit | Análisis ofensivo y defensivo de una intrusión |

---

**Contexto:** Sala en dos partes: la primera reconstruye paso a paso una intrusión real (fuerza bruta al FTP con Hydra, subida de una reverse shell PHP, acceso al sistema, escalada de privilegios a root y detección del kernel module Reptile, un rootkit); la segunda hace lo mismo desde el lado defensivo, preparando la respuesta al incidente y recuperando la bandera final.

> **ES:** Reconstruir paso a paso una intrusión (FTP, shells, escalada) y analizarla después desde el lado azul.
> **EN:** Walk through a real intrusion step by step (FTP, shells, privesc) and then analyse it from the blue side.

## Solucionario

### Task 1: Análisis de la intrusión / The Attack

**Explicación:** Se reproduce el ataque que comprometió el servidor: crackeo del FTP con Hydra, credenciales de la cuenta Jenny, subida de una reverse shell PHP a `/var/www/html`, uso de la shell de pentestmonkey, identificación como `wir3` con `whoami`, mejora de la shell con Python PTY, `sudo su` para escalar a root y descubrimiento del módulo Reptile (un rootkit).

1. `No answer needed`
2. `FTP`
3. `Hydra`
4. `Jenny`
5. `password123`
6. `/var/www/html`
7. `shell.php`
8. `http://pentestmonkey.net/tools/php-reverse-shell`
9. `whoami`
10. `wir3`
11. `python3 -c 'import pty; pty.spawn("/bin/bash")'`
12. `sudo su`
13. `Reptile`
14. `Rootkit`

### Task 2: Respuesta al incidente / The Response

**Explicación:** Desde la perspectiva defensiva se preparan las herramientas de detección y respuesta, se documenta el incidente y, al completar el flujo, se recupera la bandera final.

1. `No answer needed`
2. `No answer needed`
3. `No answer needed`
4. `No answer needed`
5. `No answer needed`
6. `ebcefd66ca4b559d17b440b6e67fd0fd`

### Tabla unificada de preguntas y respuestas

| Task | Pregunta | Respuesta |
|------|----------|-----------|
| 1.1 | — | `No answer needed` |
| 1.2 | Servicio comprometido | `FTP` |
| 1.3 | Herramienta de fuerza bruta | `Hydra` |
| 1.4 | Usuario con credenciales débiles | `Jenny` |
| 1.5 | Contraseña del usuario | `password123` |
| 1.6 | Ruta del sitio web | `/var/www/html` |
| 1.7 | Archivo de shell subido | `shell.php` |
| 1.8 | Fuente de la reverse shell | `http://pentestmonkey.net/tools/php-reverse-shell` |
| 1.9 | Comando de identificación | `whoami` |
| 1.10 | Usuario con la shell | `wir3` |
| 1.11 | Comando para mejorar la shell | `python3 -c 'import pty; pty.spawn("/bin/bash")'` |
| 1.12 | Comando de escalada a root | `sudo su` |
| 1.13 | Kernel module descubierto | `Reptile` |
| 1.14 | Tipo de malware | `Rootkit` |
| 2.1 | — | `No answer needed` |
| 2.2 | — | `No answer needed` |
| 2.3 | — | `No answer needed` |
| 2.4 | — | `No answer needed` |
| 2.5 | — | `No answer needed` |
| 2.6 | Bandera final | `ebcefd66ca4b559d17b440b6e67fd0fd` |

---

**Metodología:** Reproducir el ataque en orden cronológico: fuerza bruta FTP (Hydra), subida de reverse shell PHP, ejecución y mejora de la shell, escalada con `sudo su` y detección del rootkit Reptile; después cambiar a la óptica defensiva para responder al incidente y recuperar la bandera.

### Cadena de ataque / Attack Chain

```text
Hydra + FTP -> Jenny:password123 -> subir shell.php a /var/www/html -> pentestmonkey reverse shell -> whoami/wir3 -> PTY upgrade -> sudo su (root) -> Reptile/rootkit -> IR (blueteam) -> flag
```

**Learning chain:** FTP brute-force → Reverse shell → Shell upgrade → Privilege escalation → Rootkit discovery → Incident response

**Lección:** *Un solo par de credenciales débiles en FTP es suficiente para comprometer todo el servidor, y un rootkit como Reptile puede esconder la persistencia del atacante en el kernel.*

**MITRE ATT&CK:** N/A (Room de intrusión/IR)

**Fuente:** [TryHackMe - h4cked](https://tryhackme.com/room/h4cked)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.