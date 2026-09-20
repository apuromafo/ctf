# Library

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | challenge | `bsidesgtlibrary` | [TryHackMe](https://tryhackme.com/room/bsidesgtlibrary) | 01 Level Easy | TryHackMe | Boot2root, C#/Mono, escalada de privilegios, web, sudo | Máquina "boot2root" creada para el CTF de FIT y bsides Guatemala: compromiso de la web y escalada para leer `user.txt` y `root.txt`. |

---

**Contexto:** Library es una máquina boot2root creada para el CTF de FIT y bsides Guatemala. Hay que comprometer el servicio web que expone la caja, realizar la escalada de privilegios y leer los archivos `user.txt` y `root.txt`, cuyas flags son `6d488cbb3f111d135722c33cb635f4ec` (user) y `e8c8c6c256c35515d1d344ee0488c617` (root).

> **ES:** Caja "boot2root" del FIT y bsides Guatemala CTF: la aplicación web de la biblioteca es la puerta de entrada; se lee `user.txt` (`6d488cbb3f111d135722c33cb635f4ec`) y tras escalar `root.txt` (`e8c8c6c256c35515d1d344ee0488c617`).
> **EN:** FIT and bsides Guatemala CTF "boot2root" box: the library web application is the entry point; read `user.txt` (`6d488cbb3f111d135722c33cb635f4ec`) and after privilege escalation `root.txt` (`e8c8c6c256c35515d1d344ee0488c617`).

## Solucionario

### Task 1: Library / Library
**Explicación:** Frente a la caja se debe leer `user.txt` y `root.txt`. Tras comprometer la aplicación web de la biblioteca y escalar privilegios, se capturan el `user.txt` con `6d488cbb3f111d135722c33cb635f4ec` y el `root.txt` con `e8c8c6c256c35515d1d344ee0488c617`.

https://tryhackme.com/room/bsidesgtlibrary
Library
boot2root machine for FIT and bsides guatemala CTF

 #Task 1 : Library

Read user.txt and root.txt

Answer the questions below
user.txt
`6d488cbb3f111d135722c33cb635f4ec`

root.txt

`e8c8c6c256c35515d1d344ee0488c617`

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | user.txt | `6d488cbb3f111d135722c33cb635f4ec` |
| 1 | root.txt | `e8c8c6c256c35515d1d344ee0488c617` |

---

**Metodología:** La caja se abordó con escaneo y enumeración del servicio web de la biblioteca. Se encontró una vulnerabilidad de ejecución (el servicio web montaba una aplicación en C#/Mono) que permitió obtener una shell de bajo privilegio, leer el `user.txt` y, mediante el abuso de algún binario o su configuración sudo, elevar a root para leer el `root.txt`.

### Cadena de ataque / Attack Chain

```text
Enumeración web -> identificación de la aplicación de la biblioteca -> explotación -> shell de bajo privilegio -> user.txt -> escalada a root -> root.txt
```

**Learning chain:** web recon -> library app -> exploit -> low-priv shell -> user.txt -> privesc (sudo/capability) -> root.txt

**Lección:** *Las aplicaciones web custom (como la de la biblioteca) suelen esconder rutas de lectura de archivos o superficies de ejecución; tras la shell de bajo privilegio la escalada suele estar a un sudo mal configurado o a un binario abusable.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1505.001 - web app RCE, T1068 (Exploitation for Privilege Escalation), T1083 (File and Directory Discovery)

**Fuente:** [TryHackMe - Library](https://tryhackme.com/room/bsidesgtlibrary)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.