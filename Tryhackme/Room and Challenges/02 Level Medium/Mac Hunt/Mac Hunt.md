# Mac Hunt

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Forensics | machunt | https://tryhackme.com/room/machunt | 02 Level Medium | TryHackMe | macOS forensics, pkg, Safari, iPhone backup, LaunchAgents, Full Disk Access, exfiltration | Investigación forense de un compromiso en macOS |

---

**Contexto:** **Mac Hunt** es un ejercicio de forense sobre un sistema macOS comprometido. Se reconstruye la intrusión a partir de artefactos locales: descargas (`.pkg`), historial de Safari, un backup de iPhone asociado al usuario Jake M., conexiones de red (192.168.64.2), permisos de Full Disk Access, el agente de arranque (LaunchAgents) y la URL de exfiltración usada por el malware.

## Solucionario

### Task 1: Investigación forense / Forensic Investigation
**Explicación:**

Se analizan los artefactos del Mac: la carpeta con la descarga inicial, la red social desde la que se obtuvo el instalador, la URL del archivo `.pkg` malicioso, el dispositivo de backup vinculado al usuario (Jake M. iPhone), la IP de la conexión sospechosa, la fecha/hora del evento, el permiso concedido, el mecanismo de persistencia y la URL de exfiltración.

1. `Downloads`
2. `Linkedin`
3. `http://files.techthm.careers.thm:8080/MeetMeLiveInstaller.pkg`
4. `Jake M. iPhone`
5. `192.168.64.2`
6. `2025-04-30 08:54:20`
7. `Full Disk Access`
8. `LaunchAgents`
9. `http://techthm.thm/exfil`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1.1 | Carpeta donde se localiza la descarga inicial | `Downloads` |
| 1.2 | Red social origen del instalador malicioso | `Linkedin` |
| 1.3 | URL del archivo `.pkg` descargado | `http://files.techthm.careers.thm:8080/MeetMeLiveInstaller.pkg` |
| 1.4 | Dispositivo de backup asociado al usuario | `Jake M. iPhone` |
| 1.5 | IP de la conexión sospechosa | `192.168.64.2` |
| 1.6 | Fecha y hora del evento | `2025-04-30 08:54:20` |
| 1.7 | Permiso concedido al proceso malicioso | `Full Disk Access` |
| 1.8 | Mecanismo de persistencia utilizado | `LaunchAgents` |
| 1.9 | URL de exfiltración del malware | `http://techthm.thm/exfil` |

---

**Metodología:** Análisis forense de un host macOS: localización del archivo inicial en `Downloads`, correlación con el historial de Safari (Linkedin) y el backup de iPhone (`Jake M. iPhone`), revisión de conexiones de red (192.168.64.2), permisos de TCC (Full Disk Access), mecanismo de persistencia (LaunchAgents) y detección de la URL de exfiltración (`http://techthm.thm/exfil`).

**Learning chain:** Artefacto inicial (pkg en Downloads) → vector social (Linkedin) → análisis del instalador → evidencias de red y backup → timestamp → permisos (Full Disk Access) → persistencia (LaunchAgents) → exfiltración.

**Lección:** *Una intrusión en macOS deja artefactos muy determinados: la cadena start de una descarga, un permiso de TCC abusado y un agente de arranque bastan para reconstruir compromiso y exfiltración.*

**MITRE ATT&CK:** T1204.001 User Execution: Malicious Link · T1543.001 Create or Modify System Process: Launch Agent · T1567 Exfiltration Over Web Service · T1059 Command and Scripting Interpreter.

**Fuente:** [TryHackMe - Mac Hunt](https://tryhackme.com/room/machunt)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.