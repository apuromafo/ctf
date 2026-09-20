# Retro

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Hard | CTF | `retro` | https://tryhackme.com/room/retro | 03 Level Hard | TryHackMe | CTF / Windows 7 / explotación / credenciales / hashes / flags | Reto CTF de nivel Hard sobre una máquina Windows 7: explotación inicial, acceso a la consola web y recuperación de credenciales/hashes. |

---

**Contexto:** Sala de reto CTF con una única tarea que engloba las tres respuestas del compromiso: la ruta de acceso a la consola (`/retro`), la credencial/hash intermedia y la flag/hash final (con su hash oculto). El contenido original recogido es únicamente ese trío de respuestas.

> **ES:** "Compromete la máquina Windows 7, accede a `/retro` y entrega las credenciales y la flag final."
> **EN:** "Compromise the Windows 7 machine, access `/retro` and submit the credentials and the final flag."

## Solucionario

### Task 1: Compromiso de la máquina / Machine compromise

**Explicación:** Las tres respuestas del compromiso: la ruta de acceso a la consola web (`/retro`), la contraseña/hash intermedio y la flag/hash final de la máquina. Contenido original de la tarea:

```text
1. 1. /retro
   2. 3b99fbdc6d430bfb51c72c651a261927
   3. 7958b569565d7bd88d10c6f22d1c4063
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Ruta de acceso a la consola web. | `/retro` |
| 2 | Credencial/hash intermedio del usuario. | `3b99fbdc6d430bfb51c72c651a261927` |
| 3 | Flag/hash final de la máquina. | `7958b569565d7bd88d10c6f22d1c4063` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Ruta de acceso a la consola web. | `/retro` |
| 2 | Credencial/hash intermedio del usuario. | `3b99fbdc6d430bfb51c72c651a261927` |
| 3 | Flag/hash final de la máquina. | `7958b569565d7bd88d10c6f22d1c4063` |

---

**Metodología:**
1. Escanear y enumerar la máquina Windows 7 (puertos y servicio web).
2. Localizar la ruta `/retro` que da acceso a la consola.
3. Obtener la credencial/hash del usuario intermedio.
4. Escalar o completar el compromiso y capturar la flag/hash final.

### Cadena de ataque / Attack Chain

```text
Recon Windows 7 -> web -> /retro -> credencial 3b99fbdc6d430bfb51c72c651a261927 -> THM/flag 7958b569565d7bd88d10c6f22d1c4063
```

**Learning chain:** `Recon -> enumeración web -> /retro -> credenciales -> flag final`

**Lección:** *En las máquinas Windows tipo CTF, cada respuesta marca un eslabón: localizar la ruta web correcta abre el acceso y las credenciales/hashes se validan de forma literal.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1595 (Active Scanning), T1078 (Valid Accounts), T1003 (OS Credential Dumping), T1210 (Exploitation of Remote Services)

**Fuente:** [TryHackMe - Retro](https://tryhackme.com/room/retro)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.