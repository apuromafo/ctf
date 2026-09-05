# Shaker [HARD]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** HARD
* **Tipo / Type:** CTF (Free)
* **Slug:** `shaker`
* **Link:** https://tryhackme.com/room/shaker
* **Sección / Section:** 03 Level Hard
* **Fuente / Source:** thmrevenant (GitHub)

## Solucionario de Tareas / Task Solutions

> **ES:** Máquina Linux CTF en la que el objetivo es obtener una shell inicial y capturar la primera flag, escalar lateralmente al usuario Bob para robar su flag y, finalmente, elevar privilegios a root para completar el reto. Cada etapa requiere explotar un vector distinto (servicio expuesto, abuso de credenciales/configuración y una escalada a root).
> **EN:** Linux CTF box where the goal is to get an initial shell and capture the first flag, move laterally to the Bob user to steal his flag, and finally escalate privileges to root to complete the challenge. Each stage requires exploiting a different vector (exposed service, credential/configuration abuse, and a root escalation).

### Task 1 — Shell inicial y primera flag

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Get a shell and find the first flag! | `THM{OGZlMzhlMTQyYWMyZTExMjQyNDM2NmIyNTM4NDM3NTI=}` |

### Task 2 — Usuario Bob

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Can you find Bob's flag? | `THM{NTA2NTJiYTNmYWQ3NGViMzEyMDIyM2EwODY2MzM1YWQ=}` |

### Task 3 — Escalada a root

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Now that you're here, go on, root me :) | `THM{NzFkZGRjNmRkZWQzNWMxZTM3MjM0ZGFlMmVkZDk3MTc=}` |

## Metodología / Methodology

1. **Paso / Step:** Reconocimiento inicial de la máquina: barrido de puertos y enumeración de servicios expuestos para localizar el vector de entrada.
2. **Paso / Step:** Se identifica y explota una vulnerabilidad en un servicio o aplicación web que permite obtener una shell en la máquina víctima como un usuario de bajos privilegios.
3. **Paso / Step:** Se localiza y lee la primera flag del usuario inicial (user shell).
4. **Paso / Step:** Enumeración local (usuarios, archivos, permisos y procesos) para detectar credenciales, configuraciones o binarios que permitan el movimiento lateral hacia el usuario Bob.
5. **Paso / Step:** Acceso a la cuenta de Bob y lectura de su flag.
6. **Paso / Step:** Análisis de privilegios (sudo, SUID, capabilities, cron, etc.) para elevar a root.
7. **Paso / Step:** Se explota la escalada y se lee la última flag en la cuenta de root, completando el reto.

### Cadena de ataque / Attack Chain

```
Recon (nmap + enumeración)
  -> Explotación del servicio expuesto / app web
  -> Shell como usuario inicial
  -> User flag (THM{OGZl...})
  -> Enumeración post-explotación
  -> Movimiento lateral -> usuario Bob
  -> Bob flag (THM{NTA2...})
  -> Escalada de privilegios -> root
  -> Root flag (THM{NzFk...})
```

**Lección:** Tras comprometer la shell inicial hay que combinar enumeración post-explotación con movimiento lateral y escalada de privilegios, encadenando cada abuso hasta llegar a root.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.