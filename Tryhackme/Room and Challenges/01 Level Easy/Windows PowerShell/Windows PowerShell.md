# Windows PowerShell

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `windowspowershell` | [TryHackMe](https://tryhackme.com/room/windowspowershell) | 01 Level Easy | TryHackMe | PowerShell / cmdlets / objetos / Get-Command / Get-Content / Get-ChildItem / Get-FileHash / Get-NetTCPConnection / Invoke-Command | Fundamentos de PowerShell: arquitectura orientada a objetos, cmdlets, pipelines, gestión del sistema, hashing y ejecución remota |

---

**Contexto:** Sala introductoria a PowerShell, el shell y lenguaje de scripting de Windows construido sobre .NET. Se cubre el enfoque orientado a objetos, los cmdlets básicos, la ayuda y ejemplos, la lectura de archivos, la enumeración de directorios y procesos, el filtrado con pipelines y Where-Object, así como el hash de archivos, el análisis de conexiones con Get-NetTCPConnection y la ejecución remota con Invoke-Command.

> **ES:** La sala explora el "poder" de PowerShell: objetos, cmdlets (Get-Command, Get-Content, Get-ChildItem), pipelines, Where-Object, Get-FileHash, Get-NetTCPConnection e Invoke-Command, terminando con la pesquisa del usuario pirata p1r4t3 y su tesoro.
> **EN:** This room explores the power of PowerShell: objects, cmdlets (Get-Command, Get-Content, Get-ChildItem), pipelines, Where-Object, Get-FileHash, Get-NetTCPConnection and Invoke-Command, ending with the hunt for the pirate user p1r4t3 and his hidden treasure.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:** Pregunta introductoria de la sala. No requiere respuesta. Contenido original de la sala (verbatim): `No answer needed`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Preparado para aprender PowerShell? | `No answer needed` |

### Task 2: Qué es PowerShell / What Is PowerShell
**Explicación:** Se presenta la arquitectura de PowerShell: un enfoque avanzado orientado a objetos (object-oriented) que combina la simplicidad del scripting con el framework .NET. Contenido original de la sala (verbatim): `object-oriented`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Cómo llamamos al enfoque avanzado usado para desarrollar PowerShell? | `object-oriented` |

### Task 3: Fundamentos de PowerShell / PowerShell Basics
**Explicación:** Se practican los cmdlets básicos: `Get-Command -Name Remove*` recupera una lista de comandos que empiezan por el verbo Remove, `Write-Output` es el cmdlet cuyo tradicional homólogo es echo, y `Get-Help New-LocalUser -examples` muestra ejemplos de uso de un cmdlet. Contenido original de la sala (verbatim): `Get-Command -Name Remove*`, `Write-Output`, `Get-Help New-LocalUser -examples`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Cómo recuperarías una lista de comandos que empiecen con el verbo Remove? [en tu respuesta evita las comillas] | `Get-Command -Name Remove*` |
| ¿Qué cmdlet tiene como alias a su tradicional contraparte echo? | `Write-Output` |
| ¿Cuál es el comando para recuperar algunos ejemplos de uso del cmdlet New-LocalUser? | `Get-Help New-LocalUser -examples` |

### Task 4: Lectura y enumeración / Get-Content y Get-ChildItem
**Explicación:** Se ven los sustitutos modernos de comandos tradicionales: `Get-Content` en lugar de `type`, `Get-ChildItem -Path C:\Users` muestra el contenido del directorio C:\Users y el comando devuelve 4 elementos. Contenido original de la sala (verbatim): `Get-Content`, `Get-ChildItem -Path C:\Users`, `4`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Qué cmdlet puedes usar en lugar del comando tradicional de Windows type? | `Get-Content` |
| ¿Qué comando de PowerShell usarías para mostrar el contenido del directorio "C:\Users"? | `Get-ChildItem -Path C:\Users` |
| ¿Cuántos elementos muestra el comando descrito en la pregunta anterior? | `4` |

### Task 5: Filtrado / Filtering
**Explicación:** Se introduce el filtrado con pipelines: `Get-ChildItem | Where-Object -Property Length -gt 100` recupera los elementos del directorio actual con un tamaño mayor que 100. Contenido original de la sala (verbatim): `Get-ChildItem | Where-Object -Property Length -gt 100`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Cómo recuperarías los elementos del directorio actual con un tamaño mayor que 100? [en tu respuesta evita las comillas] | `Get-ChildItem | Where-Object -Property Length -gt 100` |

### Task 6: Investigación del usuario pirata / The pirate user
**Explicación:** Junto al usuario actual y "Administrator" hay otro usuario habilitado llamado `p1r4t3`, cuya descripción de cuenta es "A merry life and a short one." Navegando hasta su carpeta `C:\Users\p1r4t3` se encuentra la flag `THM{p34rlInAsh3ll}`. Contenido original de la sala (verbatim): `p1r4t3`, `A merry life and a short one.`, `THM{p34rlInAsh3ll}`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| Además de tu usuario actual y de la cuenta por defecto "Administrator", ¿qué otro usuario está habilitado en la máquina objetivo? | `p1r4t3` |
| ¿Cuál es el lema que ha puesto como descripción de su cuenta? | `A merry life and a short one.` |
| ¿Puedes navegar por el sistema de archivos y encontrar el tesoro oculto en el hogar de este pirata? | `THM{p34rlInAsh3ll}` |

### Task 7: Análisis del sistema en tiempo real / Real-Time System Analysis
**Explicación:** Se calcula el hash del archivo que contiene el tesoro con `Get-FileHash` (SHA256 `71FC5EC11C2497A32F8F08E61399687D90ABE6E204D2964DF589543A613F3E08`), la propiedad por defecto de Get-NetTCPConnection que contiene el proceso es `OwningProcess` y con ella se obtiene el nombre de servicio `p1r4t3-s-compass`. Contenido original de la sala (verbatim): `71FC5EC11C2497A32F8F08E61399687D90ABE6E204D2964DF589543A613F3E08`, `OwningProcess`, `p1r4t3-s-compass`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| En la tarea anterior encontraste un maravilloso tesoro escondido en la máquina objetivo. ¿Cuál es el hash del archivo que lo contiene? | `71FC5EC11C2497A32F8F08E61399687D90ABE6E204D2964DF589543A613F3E08` |
| ¿Qué propiedad, devuelta por defecto por Get-NetTCPConnection, contiene información sobre el proceso que inició la conexión? | `OwningProcess` |
| Con esta información y tus conocimientos de PowerShell, ¿puedes encontrar el nombre del servicio? | `p1r4t3-s-compass` |

### Task 8: PowerShell remoto / Remote PowerShell
**Explicación:** Se usa la ejecución remota: `Invoke-Command -ComputerName RoyalFortune -ScriptBlock { Get-Service }` ejecuta Get-Service en una máquina remota llamada RoyalFortune. Contenido original de la sala (verbatim): `Invoke-Command -ComputerName RoyalFortune -ScriptBlock { Get-Service }`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Cuál es la sintaxis para ejecutar el comando Get-Service en una máquina remota llamada "RoyalFortune"? Asume que no necesitas credenciales. | `Invoke-Command -ComputerName RoyalFortune -ScriptBlock { Get-Service }` |

### Task 9: Conclusión / Conclusion
**Explicación:** Pregunta final de cierre de la sala. No requiere respuesta. Contenido original de la sala (verbatim): `No answer needed`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Preparado para continuar? | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Preparado para aprender PowerShell? | `No answer needed` |
| 2 | Enfoque avanzado de desarrollo de PowerShell | `object-oriented` |
| 3 | Comandos que empiecen por el verbo Remove | `Get-Command -Name Remove*` |
| 4 | Cmdlet con echo como alias | `Write-Output` |
| 5 | Ejemplos de uso de New-LocalUser | `Get-Help New-LocalUser -examples` |
| 6 | Sustituto del comando type | `Get-Content` |
| 7 | Contenido del directorio C:\Users | `Get-ChildItem -Path C:\Users` |
| 8 | Elementos mostrados por el comando anterior | `4` |
| 9 | Elementos del directorio con tamaño > 100 | `Get-ChildItem | Where-Object -Property Length -gt 100` |
| 10 | Usuario habilitado además del actual y Administrator | `p1r4t3` |
| 11 | Lema en la descripción de la cuenta | `A merry life and a short one.` |
| 12 | Tesoro oculto del pirata | `THM{p34rlInAsh3ll}` |
| 13 | Hash del archivo que contiene el tesoro | `71FC5EC11C2497A32F8F08E61399687D90ABE6E204D2964DF589543A613F3E08` |
| 14 | Propiedad de Get-NetTCPConnection con el proceso | `OwningProcess` |
| 15 | Nombre del servicio encontrado | `p1r4t3-s-compass` |
| 16 | Ejecutar Get-Service en RoyalFortune | `Invoke-Command -ComputerName RoyalFortune -ScriptBlock { Get-Service }` |
| 17 | ¿Preparado para continuar? | `No answer needed` |

---

**Metodología:** Se sigue el itinerario guiado de la sala: estudio del enfoque orientado a objetos, práctica de cmdlets básicos (Get-Command, Write-Output, Get-Help), lectura y enumeración con Get-Content y Get-ChildItem, filtrado con Where-Object, investigación del usuario p1r4t3 mediante Get-LocalUser y enumeración de archivos, hashing con Get-FileHash, análisis de conexiones con Get-NetTCPConnection (OwningProcess) y ejecución remota con Invoke-Command.

### Cadena de ataque / Attack Chain

```text
object-oriented approach -> Get-Command -Name Remove* -> echo alias (Write-Output) -> Get-Help New-LocalUser -examples -> Get-Content / Get-ChildItem -Path C:\Users (4 items) -> Where-Object Length -gt 100 -> usuario p1r4t3 -> "A merry life and a short one." -> THM{p34rlInAsh3ll} -> Get-FileHash (SHA256) -> Get-NetTCPConnection OwningProcess -> servicio p1r4t3-s-compass -> Invoke-Command remoto
```

**Learning chain:** PowerShell (object-oriented) --> cmdlets (Get-Command) --> aliases (Write-Output) --> Get-Help --> Get-Content --> Get-ChildItem --> Where-Object (Length -gt 100) --> local user p1r4t3 --> hidden treasure (THM{p34rlInAsh3ll}) --> Get-FileHash --> Get-NetTCPConnection OwningProcess --> service p1r4t3-s-compass --> Invoke-Command (remote execution)

**Lección:** *PowerShell trata todo como objetos que fluyen por pipelines: dominar Get-Command, Get-Content/Get-ChildItem, Where-Object y Get-FileHash permite enumerar sistemas Windows, localizar tesoros y analizar conexiones de red de forma rápida y scriptable.*

**MITRE ATT&CK:** T1059.001 (Command and Scripting Interpreter: PowerShell)

**Fuente:** [TryHackMe - Windows PowerShell](https://tryhackme.com/room/windowspowershell)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.