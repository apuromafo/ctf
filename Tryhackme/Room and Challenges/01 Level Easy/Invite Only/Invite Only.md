# Invite Only

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | challenge | `inviteonly` | [TryHackMe](https://tryhackme.com/room/inviteonly) | 01 Level Easy | TryHackMe | análisis de malware, AsyncRAT, phishing de Discord, ClickFix, ChromeKatz, campañas maliciosas | Analizar la cadena de infección de una campaña de malware distribuida mediante invitaciones de Discord: artefactos, familia de RAT e IOC de la campaña. |

---

**Contexto:** Sala de análisis de una campaña real de malware distribuida donde los actores de amenaza utilizan invitaciones de Discord comprometidas para llegar hasta las víctimas. Emplea técnicas de atracción como ClickFix, roba credenciales almacenadas en navegadores con ChromeKatz y despliega un troyano de acceso remoto (AsyncRAT) a través de una cadena multi-etapa con ejecutables, scripts VBS y archivos de persistencia. El resumen original conserva únicamente las respuestas posicionales del room, sin los enunciados de las preguntas.

> **ES:** Examinar los artefactos de la cadena: el ejecutable descargado, el tipo de archivo, el token de invitación, el instalador, los scripts del sistema, identificar la familia de malware, el informe de la campaña y las técnicas ClickFix y ChromeKatz asociadas a Discord.
> **EN:** Examine the chain artifacts: the downloaded executable, the file type, the invite token, the installer, the system scripts, identify the malware family, the campaign report and the ClickFix and ChromeKatz techniques tied to Discord.

## Solucionario

### Task 1: Análisis de la campaña / Campaign Analysis
**Explicación:** Se recorre de principio a fin la campaña: el primer artefacto ejecutable (syshelpers.exe), su tipo de archivo (Win32 EXE), el token de la invitación (361GJX7J), el instalador (installer.exe), el cliente implantado (Aclient.exe), los scripts y binarios del sistema (searchhost.exe, syshelpers.exe, nat.vbs, runsys.vbs), la familia de malware (AsyncRAT), el informe de inteligencia de la campaña y las técnicas ClickFix y ChromeKatz sobre el discurso de Discord.

1. syshelpers.exe
2. Win32 EXE
3. 361GJX7J,installer.exe
4. Aclient.exe
5. searchhost.exe,syshelpers.exe,nat.vbs,runsys.vbs
6. asyncrat
7. From Trust to Threat: Hijacked Discord Invites Used for Multi-Stage Malware Delivery
8. ChromeKatz
9. ClickFix
10. Discord

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Primer artefacto ejecutable / First executable artifact | `syshelpers.exe` |
| 2 | Tipo de archivo / File type | `Win32 EXE` |
| 3 | Token de invitación y archivo instalador / Invite token and installer file | `361GJX7J,installer.exe` |
| 4 | Cliente desplegado / Deployed client | `Aclient.exe` |
| 5 | Binarios y scripts del sistema / System binaries and scripts | `searchhost.exe,syshelpers.exe,nat.vbs,runsys.vbs` |
| 6 | Familia de malware / Malware family | `asyncrat` |
| 7 | Informe de inteligencia / Intelligence report | `From Trust to Threat: Hijacked Discord Invites Used for Multi-Stage Malware Delivery` |
| 8 | Técnica de robo de credenciales de navegador / Browser credential stealing technique | `ChromeKatz` |
| 9 | Técnica de atracción del usuario / User lure technique | `ClickFix` |
| 10 | Plataforma vectorial de la campaña / Campaign vector platform | `Discord` |

---

**Metodología:** Analizar los artefactos de la cadena de infección en orden cronológico, determinar el tipo de cada archivo, extraer los IOC (token, instalador, scripts), identificar la familia de malware por sus características (AsyncRAT) y contrastar el hallazgo con el informe de inteligencia de la campaña.

### Cadena de ataque / Attack Chain

```text
invitación de Discord comprometida -> ClickFix -> syshelpers.exe (Win32 EXE) -> installer.exe (token 361GJX7J) -> Aclient.exe -> scripts nat.vbs/runsys.vbs + searchhost.exe -> AsyncRAT -> ChromeKatz (robo de credenciales)
```

**Learning chain:** amenaza inicial (Discord) -> ClickFix -> descarga multi-etapa -> instalación -> persistencia (VBS) -> RAT (AsyncRAT) -> robo de credenciales (ChromeKatz) -> IOC e informes de campaña.

**Lección:** *Las campañas modernas encadenan atracción social (Discord/ClickFix), descarga multi-etapa y RAT final: identificar cada artefacto y mantenerlos correlacionados permite reconstruir la cadena completa y extraer los IOC accionables.*

**MITRE ATT&CK:** T1204 (User Execution), T1105 (Ingress Tool Transfer), T1059 (Command and Scripting Interpreter), T1555 (Credentials from Password Stores), T1102 (Web Service)

**Fuente:** [TryHackMe - Invite Only](https://tryhackme.com/room/inviteonly)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.