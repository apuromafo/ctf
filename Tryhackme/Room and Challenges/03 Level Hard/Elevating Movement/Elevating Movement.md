# Elevating Movement

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Hard | Walkthrough | `elevatingmovement` | https://tryhackme.com/room/elevatingmovement | 03 Level Hard | TryHackMe | Metasploit / Meterpreter / Procdump / LSASS / Coreinfo64 / hashes NTLM / escalada / movimiento lateral | Sala de escalada de privilegios y movimiento lateral en equipos Windows: usar el agente Meterpreter, volcar LSASS con procDump (`pcd.exe`), extraer el hash del usuario y validar el acceso elevado. |

---

**Contexto:** Sala orientada a la elevación de privilegios y el movimiento lateral. Tras una tarea de contexto sin respuesta, la investigación responde seis preguntas: la hora de inicio del proceso del atacante, la ruta de la herramienta Sysinternals (`Coreinfo64.exe`), el agente C2 usado (`Meterpreter`), el comando de volcado de LSASS (`pcd.exe /accepteula -ma lsass.exe text.txt`), la hora del mismo y el hash NTLM recuperado del volcado.

> **ES:** "Sala de elevación y movimiento lateral: con Meterpreter, descarga Coreinfo64, vuelca LSASS con procDump y recupera el hash del usuario."
> **EN:** "Elevation and lateral movement room: with Meterpreter, fetch Coreinfo64, dump LSASS with procDump and recover the user hash."

## Solucionario

### Task 1: Contexto de la sala / Room context

**Explicación:** Tarea de contexto e introducción a la escena de escalada y movimiento lateral. No requiere respuesta. Contenido original de la tarea:

```text
1. No answer needed
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Leer el contexto de la sala. | `No answer needed` |

### Task 2: Análisis del movimiento / Movement analysis

**Explicación:** Se responde la secuencia de la escalada: hora de ejecución del proceso, ruta de la herramienta descargada, agente C2 (`Meterpreter`), comando de volcado de LSASS con procDump y hash recuperado. Contenido original de la tarea:

```text
2. 1. 2025-06-30 16:33:18
   2. C:\Users\emily.ross\Documents\Coreinfo64.exe
   3. Meterpreter
   4. pcd.exe /accepteula -ma lsass.exe text.txt
   5. 2025-06-30 19:47:14
   6. eb3d2de2f21b31933fb4a4fd7a7d314d
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Hora de ejecución del proceso del atacante. | `2025-06-30 16:33:18` |
| 2 | Ruta de la herramienta Sysinternals descargada. | `C:\Users\emily.ross\Documents\Coreinfo64.exe` |
| 3 | Agente C2/implant usado. | `Meterpreter` |
| 4 | Comando de volcado de LSASS con procDump. | `pcd.exe /accepteula -ma lsass.exe text.txt` |
| 5 | Hora del volcado. | `2025-06-30 19:47:14` |
| 6 | Hash NTLM recuperado del volcado de memoria. | `eb3d2de2f21b31933fb4a4fd7a7d314d` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Leer el contexto de la sala. | `No answer needed` |
| 2 | Hora de ejecución del proceso del atacante. | `2025-06-30 16:33:18` |
| 3 | Ruta de la herramienta Sysinternals descargada. | `C:\Users\emily.ross\Documents\Coreinfo64.exe` |
| 4 | Agente C2/implant usado. | `Meterpreter` |
| 5 | Comando de volcado de LSASS con procDump. | `pcd.exe /accepteula -ma lsass.exe text.txt` |
| 6 | Hora del volcado. | `2025-06-30 19:47:14` |
| 7 | Hash NTLM recuperado del volcado de memoria. | `eb3d2de2f21b31933fb4a4fd7a7d314d` |

---

**Metodología:**
1. Obtener una sesión Meterpreter y establecer foothold en el equipo.
2. Descargar herramientas (Coreinfo64) y observar la actividad del proceso.
3. Ejecutar procDump sobre lsass para volcar la memoria del proceso (`pcd.exe /accepteula -ma lsass.exe text.txt`).
4. Extraer los hashes del volcado (e.g., con mimikatz/SecureCopy) y recuperar el hash del usuario.
5. Usar el hash/cuenta para la elevación de privilegios o el movimiento lateral.

### Cadena de ataque / Attack Chain

```text
Sesión Meterpreter -> descarga Coreinfo64.exe -> procDump de LSASS -> hash NTLM eb3d2de2f21b31933fb4a4fd7a7d314d -> elevación / movimiento lateral
```

**Learning chain:** `Meterpreter -> tooling download -> ProcDump LSASS -> hash extraction -> privesc / lateral movement`

**Lección:** *Volcar el proceso LSASS con procDump permite extraer credenciales y hashes NTLM en claro de la memoria, la base del movimiento lateral y la elevación de privilegios en entornos Windows.*

**MITRE ATT&CK:** T1003.001 (OS Credential Dumping: LSASS Memory), T1105 (Ingress Tool Transfer), T1059.003 (Windows Command Shell), T1021.002 (Remote Services: SMB/Windows Admin Shares)

**Fuente:** [TryHackMe - Elevating Movement](https://tryhackme.com/room/elevatingmovement)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.