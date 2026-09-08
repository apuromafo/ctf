# Dav

| **Dificultad** | Easy |
| **Tipo** | CTF (WebDAV) |
| **Slug** | `bsidesgtdav` |
| **Link** | [TryHackMe](https://tryhackme.com/room/bsidesgtdav) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | Nmap / feroxbuster / WebDAV / curl / cadaver / reverse shell / sudo |
| **Impacto** | Reto tipo CTF: explotar un directorio WebDAV de Apache mal protegido para subir una shell y escalar a root abusando de un sudo permitido sobre /bin/cat. |

---

**Contexto:** El escaneo inicial muestra Apache en el puerto 80 con un directorio `/webdav` protegido (401). Las credenciales por defecto se adivinan como `wampp:xampp` y una nota en el servidor confirma que está pensado para trabajar con MySQL. El directorio permite subir ficheros (método PUT), por lo que se sube una shell `.php5` con cadaver para obtener una reverse shell como www-data. Tras leer `user.txt` de merlin, la escalada es trivial: `sudo -l` muestra que www-data puede ejecutar `/bin/cat` como root.

## Solucionario

### Task 2: Flags de usuario y root

**Explicación:** Con la reverse shell como www-data se lee `/home/merlin/user.txt` (`449b40fe93f78a938523b7e4dcd66d2a`). `sudo -l` revela que www-data puede ejecutar `/bin/cat` como root, así que `sudo cat /root/root.txt` da `101101ddc16b0cdf65ba0b8a7af7afa5`.

```bash
cat /home/merlin/user.txt
sudo cat /root/root.txt
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el valor del user.txt? | `449b40fe93f78a938523b7e4dcd66d2a` |
| 2 | ¿Cuál es el valor del root.txt? | `101101ddc16b0cdf65ba0b8a7af7afa5` |

---

**Metodología:** Enumeración con nmap y feroxbuster descubre `/webdav` con código 401. Probando credenciales típicas de WAMP se entra con `wampp:xampp`; la nota `Note` y el hash `$apr1$...` confirman el usuario. Se valida que el servidor permite PUT con `curl -X PUT` y se sube la shell con cadaver (`put shell.php5`). Al visitar la shell se recibe la reverse shell como www-data; leyendo `/home/merlin/user.txt` se obtiene la primera flag y con `sudo cat /root/root.txt` la segunda, ya que el usuario puede ejecutar `/bin/cat` como root sin contraseña.

**Learning chain:** escaneo → fuzzing de directorios → autenticación por defecto → abuso de WebDAV (PUT) → reverse shell → abuso de sudo.

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1110.001 (Password Guessing), T1505.003 (Web Shell), T1059 (Command and Scripting Interpreter), T1548 (Abuse Elevation Control Mechanism)

**Fuente:** [TryHackMe - Dav](https://tryhackme.com/room/bsidesgtdav)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
