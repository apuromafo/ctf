# En-pass

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF / Explotación Web | enpass | https://tryhackme.com/room/enpass | 02 Level Medium | TryHackMe | Gobuster, RSA privada cifrada, SSH, cronjob | Compromiso total de la máquina (user + root) |

---

**Contexto:** **En-pass** es un CTF Linux de nivel medio ("think out of the box") que expone un servidor web en el puerto **8001**. Mediante fuerza bruta de directorios con `gobuster` se descubre una ruta oculta que alberga una clave RSA privada cifrada (`/web/resources/infoseek/configure/key`). La frase de paso se obtiene analizando el código de `reg.php` y usando `ssh2john` + `john`, lo que permite acceder por SSH. Una vez dentro, se explota un cronjob mal configurado para obtener un shell como **root** y capturar las dos flags que acreditan el compromiso.

## Solucionario

### Task 1: Flag submission (path, flag de usuario y flag de root)
**Explicación:**

El laboratorio pide localizar el recurso que contiene la clave RSA cifrada, conectarse a la máquina tras romper su frase de paso y escalar privilegios hasta root. La **path** corresponde al fichero descubierto con `gobuster` sobre el servidor web (puerto 8001), y ambas flags son las cadenas hash (MD5) entregadas por la máquina al leer `user.txt` y `root.txt`.

Respuestas del lab (contenido original):

```
1. /web/resources/infoseek/configure/key
2. 1c5ccb6ce6f3561e302e0e516c633da9
3. 5d45f08ee939521d59247233d3f8faf
```

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Name the path (ruta donde se guarda la clave RSA cifrada) | `/web/resources/infoseek/configure/key` |
| 2 | ¿Cuál es la flag de usuario? | `1c5ccb6ce6f3561e302e0e516c633da9` |
| 3 | ¿Cuál es la flag de root? | `5d45f08ee939521d59247233d3f8faf` |

---

**Metodología:** Escaneo de puertos y descubrimiento del servicio web en 8001, fuerza bruta de directorios con gobuster, localización de una clave RSA privada cifrada, obtención de la passphrase analizando el código fuente de `reg.php`, crackeo de la clave con `ssh2john` + `john`, acceso SSH, explotación de un cronjob y escalada a root.

**Learning chain:** Reconocimiento → enumeración de directorios → hallazgo de clave privada cifrada → crackeo de passphrase → SSH → escalada de privilegios vía cron → flags.

**Lección:** *Un servidor web expuesto sin restricciones de directorios puede filtrar material sensible como claves privadas; además, los cronjobs con privilegios elevados son un vector clásico de escalada.*

**MITRE ATT&CK:** T1190 Exploit Public-Facing Application · T1003.001 OS Credential Dumping: LSASS Memory · T1552.004 Unsecured Credentials: Private Keys · T1053.005 Scheduled Task/Job: Cron.

**Fuente:** [TryHackMe - En-pass](https://tryhackme.com/room/enpass)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.