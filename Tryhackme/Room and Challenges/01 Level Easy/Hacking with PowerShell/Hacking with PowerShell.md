# Hacking with PowerShell

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `hackingwithpowershell` | [TryHackMe](https://tryhackme.com/room/hackingwithpowershell) | 01 Level Easy | THM | PowerShell, Enumeración, Scripting, Windows | Fundamentos de PowerShell para tareas ofensivas |

---

**Contexto:** Sala del principiante que enseña PowerShell desde el lado ofensivo y defensivo: conceptos básicos del intérprete, comandos esenciales (Get-Location, Invoke-WebRequest, Get-Process), enumeración del sistema y scripting básico e intermedio para extraer información y banderas.

> **ES:** Aprender PowerShell: comandos básicos, enumeración de un sistema Windows y scripting para automatizar tareas.
> **EN:** Learn PowerShell: basic commands, Windows system enumeration and scripting to automate tasks.

## Solucionario

### Task 1: Objetivos / Objectives

**Explicación:** Presentación de la sala y de los objetivos formativos.

No answer needed

### Task 2: ¿Qué es PowerShell? / What is Powershell?

**Explicación:** Se introduce el intérprete de PowerShell y el comando para obtener nuevos cmdlets.

- `Get-New`

### Task 3: Comandos básicos de PowerShell / Basic Powershell Commands

**Explicación:** Práctica con comandos esenciales: rutas de instalación, contenido de archivos, procesos, hashes de servicios, ubicación actual con `Get-Location`, opciones de booleano y peticiones web con `Invoke-WebRequest`, hasta llegar a la bandera del apartado.

1. `C:\Program Files`
2. `notsointerestingcontent`
3. `6638`
4. `49A586A2A9456226F8A1B4CEC6FAB329`
5. `Get-Location`
6. `N`
7. `Invoke-WebRequest`
8. `ihopeyoudidthisonwindows`

### Task 4: Enumeración / Enumeration

**Explicación:** Enumeración completa del sistema Windows: número de módulos, cuentas como `Guest`, direcciones IP con `Get-NetIPAddress`, protocolos, fechas de último inicio de sesión, banderas en registros, comandos de procesos con `Get-Process`, particiones y cuentas de servicio como `NT SERVICE\TrustedInstaller`.

1. `5`
2. `Guest`
3. `4`
4. `24`
5. `Get-NetIPAddress`
6. `20`
7. `::`
8. `20`
9. `6/15/2017 12:00:00 AM`
10. `backpassflag`
11. `fakekey123`
12. `Get-Process`
13. `/`
14. `NT SERVICE\TrustedInstaller`

### Task 5: Reto de scripting básico / Basic Scripting Challenge

**Explicación:** Se combinan los conocimientos en un script que automatiza el descubrimiento de credenciales y usuarios.

1. `Doc3M`
2. `johnisalegend99`
3. `Doc2Mary`

### Task 6: Scripting intermedio / Intermediate Scripting

**Explicación:** Script más complejo que resume el trabajo de enumeración y scripting previo.

- `11`

### Tabla unificada de preguntas y respuestas

| Task | Pregunta | Respuesta |
|------|----------|-----------|
| 1 | — | `No answer needed` |
| 2 | ¿Qué comando obtiene nuevos cmdlets? | `Get-New` |
| 3.1 | Ruta de instalación | `C:\Program Files` |
| 3.2 | Contenido de archivo | `notsointerestingcontent` |
| 3.3 | PID encontrado | `6638` |
| 3.4 | Hash de servicio | `49A586A2A9456226F8A1B4CEC6FAB329` |
| 3.5 | Cmdlet de ubicación actual | `Get-Location` |
| 3.6 | Opción booleana | `N` |
| 3.7 | Cmdlet de petición web | `Invoke-WebRequest` |
| 3.8 | Bandera del apartado | `ihopeyoudidthisonwindows` |
| 4.1 | Número de módulos | `5` |
| 4.2 | Cuenta encontrada | `Guest` |
| 4.3 | Valor de enumeración | `4` |
| 4.4 | Valor de enumeración | `24` |
| 4.5 | Cmdlet de IP | `Get-NetIPAddress` |
| 4.6 | Valor de enumeración | `20` |
| 4.7 | Dirección IPv6 | `::` |
| 4.8 | Valor de enumeración | `20` |
| 4.9 | Último inicio de sesión | `6/15/2017 12:00:00 AM` |
| 4.10 | Bandera de proceso | `backpassflag` |
| 4.11 | Credencial encontrada | `fakekey123` |
| 4.12 | Cmdlet de procesos | `Get-Process` |
| 4.13 | Partición/raíz | `/` |
| 4.14 | Cuenta de servicio | `NT SERVICE\TrustedInstaller` |
| 5.1 | Usuario 1 | `Doc3M` |
| 5.2 | Contraseña | `johnisalegend99` |
| 5.3 | Usuario 2 | `Doc2Mary` |
| 6 | Resultado del reto | `11` |

---

**Metodología:** Familiarizarse con el intérprete de PowerShell, practicar los comandos esenciales del sistema, enumerar el host Windows (usuarios, red, procesos, servicios, fechas), y automatizar el descubrimiento de credenciales y banderas mediante scripting básico e intermedio.

### Cadena de ataque / Attack Chain

```text
Objetivos -> cmdlets básicos -> enumeración del sistema -> scripting básico (credenciales) -> scripting intermedio -> resultado
```

**Learning chain:** PowerShell basics → Essential commands → Enumeration → Basic scripting → Intermediate scripting

**Lección:** *PowerShell no es solo una shell: es un entorno completo de enumeración y automatización; dominar sus cmdlets permite recoger en minutos lo que requeriría horas a mano.*

**MITRE ATT&CK:** N/A (Room de PowerShell/Windows)

**Fuente:** [TryHackMe - Hacking with PowerShell](https://tryhackme.com/room/hackingwithpowershell)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.