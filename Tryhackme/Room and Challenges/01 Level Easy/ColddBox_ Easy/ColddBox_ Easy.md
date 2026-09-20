# ColddBox_ Easy

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | boot2root (máquina CTF) | `colddboxeasy` | https://tryhackme.com/room/colddboxeasy | 01 Level Easy | TryHackMe | WordPress / wpscan / fuerza bruta / escalada de privilegios (sudo) / flags en base64 | Obtener acceso a la máquina ColddBox: Easy y capturar ambas flags (usuario y root) tras escalar privilegios. |

---

**Contexto:** Máquina Linux de nivel Easy del catálogo TryHackMe, creada por Hixec, con múltiples vías para escalar privilegios. El flujo clásico pasa por enumerar la máquina y el sitio WordPress, obtener credenciales válidas, conseguir una shell inicial y escalar privilegios (por ejemplo abusando de permisos de `sudo` sobre binarios como `chmod`) para leer ambas flags. Las respuestas del lab se presentan ofuscadas en base64.

> **ES:** "ColddBox: Easy": una máquina de nivel fácil con múltiples vías para escalar privilegios. ¿Puedes conseguir acceso y obtener ambas flags?
> **EN:** "ColddBox: Easy": an easy level machine with multiple ways to escalate privileges. Can you get access and get both flags?

## Solucionario

### Task 1: boot2Root / Acceso y doble flag (boot2Root)

**Explicación:** La máquina se resuelve con un flujo clásico de boot2root: escaneo de puertos, enumeración del servicio web y de WordPress (versión, plugins y usuarios con `wpscan`), fuerza bruta de credenciales para acceder al panel de WordPress, abuso del panel para ejecutar comandos y conseguir una shell, y escalada de privilegios abusando de un binario ejecutable con `sudo` (p. ej. `chmod`) para alcanzar root y leer las dos flags. El lab pide "conseguir acceso y obtener ambas flags"; las dos respuestas se entregan codificadas en base64.

> **Texto original del lab / Original lab text:** Start Machine. Can you get access and get both flags? Good Luck!. By Marti from Hixec. Doubts and / or help in Hixec Community. Thumbnail box image credits, designed by Freepik from www.flaticon.es

```text
nmap <IP>
wpscan --url http://<IP> --enumerate u
<fuerza bruta del usuario de WordPress>
<acceso al panel -> shell>
sudo -l                       # binario con permisos sudo (ej.: chmod)
<escalada a root y lectura de flags>
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Primera flag del lab (flag de usuario) en base64. / First lab flag (user flag), base64. | `RmVsaWNpZGFkZXMsIHByaW1lciBuaXZlbCBjb25zZWd1aWRvIQ==` |
| 2 | Segunda flag del lab (flag de root) en base64. / Second lab flag (root flag), base64. | `wqFGZWxpY2lkYWRlcywgbcOhcXVpbmEgY29tcGxldGFkYSE=` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Primera flag del lab (flag de usuario) en base64. / First lab flag (user flag), base64. | `RmVsaWNpZGFkZXMsIHByaW1lciBuaXZlbCBjb25zZWd1aWRvIQ==` |
| 2 | Segunda flag del lab (flag de root) en base64. / Second lab flag (root flag), base64. | `wqFGZWxpY2lkYWRlcywgbcOhcXVpbmEgY29tcGxldGFkYSE=` |

---

**Metodología:** Se comienza con un escaneo de puertos y la enumeración del sitio (WordPress). Se emplea `wpscan` para enumerar usuarios y versiones y se realiza fuerza bruta de la contraseña del usuario de WordPress. Se logra ejecutar código en el host (shell) y se escala privilegios explotando un binario ejecutable con `sudo` (como `chmod`) hasta llegar a root y leer las dos flags, que el lab devuelve codificadas en base64.

### Cadena de ataque / Attack Chain

```text
nmap -> enumeración web/WordPress -> wpscan (usuarios y plugins) -> fuerza bruta -> shell inicial -> escalada de privilegios (sudo/chmod) -> lectura de flags (user y root)
```

**Learning chain:** Enumeración -> WordPress/wpscan -> fuerza bruta -> acceso inicial -> escalada de privilegios -> flags en base64.

**Lección:** *En las máquinas "fáciles" casi siempre queda abierta una vía clásica (WordPress + fuerza bruta + sudo); enumerar primero y revisar `sudo -l` es la forma más rápida de resolverlas.*

**MITRE ATT&CK:** T1078 - Valid Accounts; T1548 - Abuse Elevation Control Mechanism

**Fuente:** [TryHackMe - ColddBox_ Easy](https://tryhackme.com/room/colddboxeasy)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.