# Cyborg

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|-------------|---------|
| Easy | walkthrough | `cyborg` | [TryHackMe](https://tryhackme.com/room/cyborg) | 01 Level Easy | THM | BorgBackup, Esteganografía, Escaneo de puertos, SSH | Acceso inicial y extracción de backups en Linux |

> **Objeto:** Comprometer la máquina Cyborg: escanear el objetivo, detectar los servicios SSH y HTTP, recuperar una imagen cifrada de BorgBackup, descifrarla con el passphrase extraído y escalar a root.

---

**Contexto:** Sala de laboratorio sobre una máquina Linux vulnerable. El compromiso pasa por el escaneo de puertos (SSH y HTTP), el hallazgo de un archivo cifrado de backup de Borg en el servidor web, la extracción del passphrase almacenado en texto plano y la recuperación de un hash SSH que permite acceder y escalar a root.

> **ES:** Escaneo de puertos, descubrimiento de un backup Borg cifrado, extracción del passphrase y escalada final a root.
> **EN:** Port scanning, discovery of an encrypted Borg backup, passphrase extraction and final privilege escalation to root.

## Solucionario

### Task 1: Reconocimiento / Reconnaissance
**Explicación:** Reconocimiento inicial de la máquina y despliegue en laboratorio.

No answer needed

### Task 2: Explotación / Exploitation
**Explicación:** Escaneo de servicios, extracción del backup de Borg, descifrado y recuperación de credenciales hasta obtener los flags.

1. 2
2. ssh
3. http
4. flag{1_hop3_y0u_ke3p_th3_arch1v3s_saf3}
5. flag{Than5s_f0r_play1ng_H0p£_y0u_enJ053d}

### Tabla unificada de preguntas y respuestas

| Task | Pregunta | Respuesta |
|------|----------|-----------|
| 1 | — | `No answer needed` |
| 2.1 | Número de puertos abiertos | `2` |
| 2.2 | Puerto 22 | `ssh` |
| 2.3 | Puerto 80 | `http` |
| 2.4 | Flag de usuario (pista Borg) | `flag{1_hop3_y0u_ke3p_th3_arch1v3s_saf3}` |
| 2.5 | Flag de root | `flag{Than5s_f0r_play1ng_H0p£_y0u_enJ053d}` |

---

**Metodología:** Escaneo de puertos con nmap, enumeración del sitio web, localización del archivo de backup de Borg, extracción del passphrase en texto plano, descifrado y montaje del repositorio, recuperación del hash SSH, acceso a la máquina y escalada de privilegios a root.

### Cadena de ataque / Attack Chain

nmap → puertos SSH/HTTP → servidor web → archivo Borg cifrado → passphrase en texto plano → descifrado del backup → hash SSH → acceso → escalada a root.

**Learning chain:** recon → scan → web → BorgBackup → passphrase → decrypt → ssh → privesc → root

*Lección:* Los backups cifrados con passphrases débiles o almacenados en texto plano exponen las credenciales de la máquina.

**MITRE ATT&CK:** TA0001 Initial Access, TA0003 Persistence, TA0007 Discovery, T1552 Unsecured Credentials.

**Fuente:** [TryHackMe - Cyborg](https://tryhackme.com/room/cyborg)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.

**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.

**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).

**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.