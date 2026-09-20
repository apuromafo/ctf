# Dead End_

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Hard | Forense | deadend | https://tryhackme.com/room/deadend | 03 Level Hard | TryHackMe | DFIR, Persistencia, BAM Registry, Autoconnector, Svchost | Medio |

---

**Contexto:**
> **ES:** Laboratorio forense en Windows: tras un incidente se localiza un proceso sospechoso (C:\Tools\svchost.exe) y artefactos (tmp\part2.txt). El análisis revela un binario Autoconnector.exe y una persistencia basada en el registro BAM de Windows (UserSettings), cuyo payload codificado en Base64 permite reconstruir la flag.
> **EN:** Windows forensics lab: after an incident a suspicious process (C:\Tools\svchost.exe) and artefacts (tmp\part2.txt) are located. Analysis reveals an Autoconnector.exe binary and persistence based on the Windows BAM registry (UserSettings), whose Base64-encoded payload enables rebuilding the flag.

## Solucionario

### Task 1: Descubrimiento inicial / Initial discovery
**Explicación:**
1. C:\Tools\svchost.exe
2. C:\Users\Bobby\Documents\tmp\part2.txt

### Task 2: Persistencia BAM / BAM persistence
**Explicación:**
1. C:\Tools\windows-networking-tools-master\windows-networking-tools-master\LatestBuilds\x64\Autoconnector.exe
2. HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\bam\State\UserSettings\S-1-5-21-1966530601-3185510712-10604624-1008
3. faDB3XzJfcDF2T1R9
4. THM{6l4D_y0u_kNOw_h0w_2_p1vOT}

### Preguntas y Respuestas / Questions and Answers

| Task | Respuesta / Answer |
|---|---|
| 1.1 | `C:\Tools\svchost.exe` |
| 1.2 | `C:\Users\Bobby\Documents\tmp\part2.txt` |
| 2.1 | `C:\Tools\windows-networking-tools-master\windows-networking-tools-master\LatestBuilds\x64\Autoconnector.exe` |
| 2.2 | `HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\bam\State\UserSettings\S-1-5-21-1966530601-3185510712-10604624-1008` |
| 2.3 | `faDB3XzJfcDF2T1R9` |
| 2.4 | `THM{6l4D_y0u_kNOw_h0w_2_p1vOT}` |

---

**Metodología:**
Investigación del proceso y del disco para hallar evidencias, correlación con el binario Autoconnector.exe, inspección de la clave de registro BAM (UserSettings del SID del usuario) y decodificación del payload para componer la flag.

### Cadena de ataque / Attack Chain
1. Identificación del proceso sospechoso y sus rutas.
2. Localización de artefactos relacionados en el sistema.
3. Correlación con el binario Autoconnector.exe.
4. Análisis de la persistencia en HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\bam\State\UserSettings.
5. Decodificación del payload y obtención de la flag.

**Learning chain:**
Proceso anómalo → Artefacto tmp → Binario (BAM) → Payload Base64 → Flag.

**Lección:** *El registro BAM (Background Activity Moderator) de Windows puede revelar las aplicaciones ejecutadas más recientemente, convirtiéndose en una fuente forense y también en un mecanismo de persistencia.*

**MITRE ATT&CK:**
- T1547 (Boot or Logon Autostart Execution), T1005 (Data from Local System), T1012 (Query Registry).

**Fuente:** [TryHackMe - Dead End_](https://tryhackme.com/room/deadend)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.