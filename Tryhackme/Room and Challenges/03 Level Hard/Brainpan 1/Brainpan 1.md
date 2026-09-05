# Brainpan 1 [HARD]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** HARD
* **Tipo / Type:** Walkthrough (Free)
* **Slug:** `brainpan`
* **Link:** https://tryhackme.com/room/brainpan
* **Sección / Section:** 03 Level Hard
* **Fuente / Source:** thmrevenant (GitHub)

## Solucionario de Tareas / Task Solutions

> **ES:** Brainpan 1 es una sala clásica de buffer overflow (basada en la máquina Brainpan del VulnHub). No se capturan flags: el objetivo se mide por niveles de acceso. Un fuzzer encuentra el offset de EIP, el programa `brainpan.exe` revela a la máquina Windows de desarrollo, y una shellcode explota el servicio `abyss` en el puerto 9999 para obtener acceso al sistema Linux y escalar a root.
> **EN:** Brainpan 1 is a classic buffer overflow room (based on the VulnHub Brainpan box). No flags are captured: the goal is measured by access level. A fuzzer finds the EIP offset, the `brainpan.exe` program reveals the Windows dev machine, and shellcode exploits the `abyss` service on port 9999 to get access to the Linux system and escalate to root.

### Task 1 — No se requiere respuesta / No answer needed

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| No answer needed | `No answer needed` |

## Metodología / Methodology

1. **Paso / Step:** Escaneo de puertos: `9999` (`abyss`/Brainpan, pide contraseña) y `10000` (SimpleHTTPServer Python 2.7.3).
2. **Paso / Step:** Enumeración web en el puerto 10000 → directorio `/bin` → se descarga `brainpan.exe`.
3. **Paso / Step:** Fuzzing del servicio `9999`: el programa crashea a ~600 bytes; el desbordamiento ocurre entre 500 y 600 bytes.
4. **Paso / Step:** Con un patrón cíclico se calcula el offset de EIP = `524` bytes.
5. **Paso / Step:** Con `mona`/`!mona jmp esp` se obtiene la dirección `0x311712f3` (brainpan.exe) para el control de flujo.
6. **Paso / Step:** Se identifica `msfvenom` para generar shellcode de reverse shell (sin badcharacter `\x00`) y se añade un NOP-sled.
7. **Paso / Step:** Se envía el exploit envíando la shellcode `windows/meterpreter/reverse_tcp` → conexión como usuario `puck`.
8. **Paso / Step:** Escalada de privilegios: `/etc/passwd` es escritible → se añade un usuario root con hash conocido → `su` → acceso root.

### Cadena de ataque / Attack Chain

```
espacio nmap -> puerto 9999 (abyss) y 10000 (SimpleHTTPServer) -> /bin -> brainpan.exe -> fuzzer (crash a 600 bytes) -> offset de EIP (524) -> JMP ESP (0x311712f3) -> shellcode -> reverse shell como puck -> /etc/passwd escritible -> root
```

**Lección:** El desbordamiento clásico se resuelve con fuzzing determinista, patrón de crash, control de EIP y escalada local; la flag se sustituye por la escalada de privilegios hasta `root`.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.