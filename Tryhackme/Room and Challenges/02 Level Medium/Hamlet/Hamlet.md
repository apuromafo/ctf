# Hamlet

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF | hamlet | https://tryhackme.com/room/hamlet | 02 Level Medium | TryHackMe | FTP, HTTP/lighttpd, WebAnno (8080), Nagios NSCA (501), Apache (8000), webshell PHP, Docker escape | Recuperación de 6 flags y acceso root |

---

**Contexto:** **Hamlet** es un CTF Medium centrado en Shakespeare. Tras enumerar puertos se encuentran varios servicios: FTP, un servidor HTTP con `robots.txt`, el puerto 501 (acertijo de los sepultureros) y WebAnno en 8080. Se fuerza la contraseña del usuario `ghost` (Michael Canterbury) con un diccionario custom generado de `hamlet.txt` respetando la política de contraseñas: el password resulta ser `vnsanctified`. Subiendo una webshell PHP dentro de WebAnno se obtiene una shell en un contenedor Docker y, tras el breakout (`release_agent`), root en el host para las 6 flags.

## Solucionario

### Task 1

**Explicación:** Enumeration inicial: puertos FTP (21), HTTP 80 (lighttpd) con `robots.txt` (flag 1), puerto 501 (Nagios NSCA / "Gravediggers" que entrega el flag 2), WebAnno en 8080 y Apache en 8000. La password de Michael se fuerza con un diccionario limitado construido a partir de `hamlet.txt` (password policy del FTP) contra el login de WebAnno con el usuario `ghost`; el password encontrado es `vnsanctified`. El resto de flags: `/home/ophelia/flag` (3), `/stage/flag` en el contenedor (4), `/root/.flag` en el contenedor (5) y `/root/flag` en el host tras el Docker escape (6).

```bash
nmap -sV -sC <IP>
# Wordlist custom desde hamlet.txt + política de contraseñas
# Login WebAnno: ghost / vnsanctified (fuerza bruta con Burp/Hydra)
# Webshell PHP subida en WebAnno (Documents -> archivos -> shell.php en $WEBANNO/repository/project/0/document/.../source/)
find / -type f -iname "*flag*" 2>/dev/null
```

Respuestas de la tarea:

1. `vnsanctified`
2. `THM{1_most_mechanical_and_dirty_hand}`
3. `THM{2_ophelia_s_grave}`
4. `THM{3_i_was_the_more_deceived}`
5. `THM{4_the_murder_of_gonzago}`
6. `THM{5_murder_most_foul}`
7. `THM{6_though_this_be_madness_yet_there_is_method_in_t}`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1.1 | What is Michael's password? | `vnsanctified` |
| 1.2 | Flag 1 | `THM{1_most_mechanical_and_dirty_hand}` |
| 1.3 | Flag 2 | `THM{2_ophelia_s_grave}` |
| 1.4 | Flag 3 | `THM{3_i_was_the_more_deceived}` |
| 1.5 | Flag 4 | `THM{4_the_murder_of_gonzago}` |
| 1.6 | Flag 5 | `THM{5_murder_most_foul}` |
| 1.7 | Flag 6 | `THM{6_though_this_be_madness_yet_there_is_method_in_t}` |

---

**Metodología:** Enumeración multi-puerto, OSINT del sitio (vocabulario Shakepeare, usuario ghost), generación de diccionario custom con la password policy, fuerza bruta de login WebAnno, subida de webshell PHP, movimiento de contenedor a host vía Docker escape (`release_agent` / hueco de controladores cgroup v1) (PTES/OWASP: enumeration, credential attacks, RCE, container breakout).

**Learning chain:** nmap multi-puerto → lighttpd robots.txt (flag1) → puerto 501 acertijo sepultureros (flag2) → WebAnno 8080 → diccionario de hamlet.txt → ghost:vnsanctified → webshell PHP → user web → /home/ophelia/flag (flag3) → /stage/flag (flag4) → escape contenedor (release_agent) → /root/.flag (flag5) → host root → /root/flag (flag6).

**Lección:** *El password de un usuario obsesionado con Shakespeare se puede derivar de su propio texto favorito: los diccionarios dirigidos por el contexto del target vencen a rockyou.*

**MITRE ATT&CK:** T1593 Search Open Websites/Domains (OSINT del sitio) · T1110.001 Password Guessing (fuerza bruta login) · T1505.003 Web Shell · T1068 Exploitation for Privilege Escalation · T1610 Deploy Container / T1611 Escape to Host (Docker release_agent).

**Fuente:** [TryHackMe - Hamlet](https://tryhackme.com/room/hamlet)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.