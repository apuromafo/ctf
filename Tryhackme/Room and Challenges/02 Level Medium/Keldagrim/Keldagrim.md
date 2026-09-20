# Keldagrim

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF / Explotación | keldagrim | https://tryhackme.com/room/keldagrim | 02 Level Medium | TryHackMe | Web, Escalada de privilegios, Linux | Compromiso del host hasta obtener las dos flags del reto |

---

**Contexto:** La sala **Keldagrim** es un CTF estilo boot2root sobre una aplicación web de temática inspirada en RuneScape. Se enumeran los servicios, se explota la aplicación web (autenticación, inyección o funcionalidad vulnerable) para obtener un primer acceso como usuario con la flag `user`, y finalmente se escala privilegios para comprometer `root` y capturar la segunda flag. La resolución combina reconocimiento, explotación web, acceso local y escalada de privilegios.

## Solucionario

### Task 1: Flag de usuario
**Explicación:**

Se enumera la máquina con `nmap` y se analiza la aplicación web. Se explota la funcionalidad vulnerable para obtener un shell / acceso como usuario, y se lee la flag del usuario en su directorio home.

```bash
nmap -sV -sC <IP>
# Tras obtener acceso como usuario:
cat /home/<user>/user.txt
```

Respuesta: `thm{d55ac4d0a728741d7b8c23b999e73cf3}`

### Task 2: Flag de root
**Explicación:**

Con acceso local se enumeran vectores de escalada de privilegios (binarios SUID, permisos de sudo, tareas programadas). Se escala a `root` y se lee la flag final del sistema.

```bash
sudo -l
find / -perm -4000 2>/dev/null
# Tras escalar a root:
cat /root/root.txt
```

Respuesta: `thm{bf2a087f833b58df233c0f24eac3aec5}`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag de usuario | `thm{d55ac4d0a728741d7b8c23b999e73cf3}` |
| 2 | Flag de root | `thm{bf2a087f833b58df233c0f24eac3aec5}` |

---

**Metodología:** Reconocimiento con nmap → análisis de la aplicación web → explotación para obtener acceso → lectura de user flag → enumeración de vectores de escalada → acceso root → captura de root flag.

**Learning chain:** Reconocimiento → aplicación web vulnerable → acceso inicial → escalada de privilegios → flags usuario/root.

**Lección:** *Un login o endpoint web aparentemente sencillo suele ser la puerta de entrada: tras el primer acceso, la escalada siempre depende de la mala configuración local.*

**MITRE ATT&CK:** T1190 Exploit Public-Facing Application · T1068 Exploitation for Privilege Escalation · T1082 System Information Discovery.

**Fuente:** [TryHackMe - Keldagrim](https://tryhackme.com/room/keldagrim)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.