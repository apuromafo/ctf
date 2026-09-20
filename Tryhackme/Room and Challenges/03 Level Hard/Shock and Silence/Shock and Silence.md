# Shock and Silence

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Hard | CTF | shockandsilence | https://tryhackme.com/room/shockandsilence | 03 Level Hard | vishak-soc.github.io + Crofter-dev/ctf_writeups | MFT / MFTECmd / Ransomware Analysis / Forensics / BlackLock | Análisis forense completo del despliegue de ransomware BlackLock reconstruyendo la cadena de ataque a partir de artefactos de la Master File Table. |

---

**Contexto:** Sala parte de la cadena "Honeynet Collapse" (DeceptiTech). Se analiza la Master File Table (MFT) y artefactos del sistema de archivos para reconstruir el despliegue del ransomware BlackLock sobre la imagen de disco parcial del DC-01, usando MFTECmd sobre el `$MFT`.

> **ES:** Sala forense: reconstruir el despliegue del ransomware BlackLock a partir del $MFT del DC-01 con MFTECmd.
> **EN:** Forensics room: rebuild the BlackLock ransomware deployment from the DC-01 $MFT using MFTECmd.

## Solucionario

### Task 1: Delivery & Download / Entrega y descarga
**Explicación:**
Contenido original de la tarea:

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the full URL from which the ransomware was downloaded to the system? | `https://store5.gofile.io/download/web/e23cb33f-0e4d-4a5f-8c55-ea2d78057d40/HiddenFile.zip` |

### Task 2: Payload Identification / Identificación del payload
**Explicación:**
Contenido original de la tarea:

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What was the original file name of the ransomware executable downloaded to the host? | `pb.exe` |

### Task 3: Execution & Encryption / Ejecución y cifrado
**Explicación:**
Contenido original de la tarea:

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which executable file initiated the encryption process on the system? | `HpAgent.exe` |

### Task 4: Impact Analysis / Análisis de impacto
**Explicación:**
Contenido original de la tarea:

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What file extension was appended to the encrypted files? | `EeUfy` |

### Task 5: Attribution / Atribución
**Explicación:**
Contenido original de la tarea:

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Go beyond the obvious - which ransomware group targeted the organisation? | `BlackLock` |

### Preguntas y Respuestas / Questions and Answers

| # | Task | Pregunta | Respuesta |
|---|---|---|---|
| 1 | Task 1 | What is the full URL from which the ransomware was downloaded to the system? | `https://store5.gofile.io/download/web/e23cb33f-0e4d-4a5f-8c55-ea2d78057d40/HiddenFile.zip` |
| 2 | Task 2 | What was the original file name of the ransomware executable downloaded to the host? | `pb.exe` |
| 3 | Task 3 | Which executable file initiated the encryption process on the system? | `HpAgent.exe` |
| 4 | Task 4 | What file extension was appended to the encrypted files? | `EeUfy` |
| 5 | Task 5 | Go beyond the obvious - which ransomware group targeted the organisation? | `BlackLock` |

---

**Metodología:**

1. Se exporta el `$MFT` de la imagen de disco parcial del DC-01 y se procesa con MFTECmd para reconstruir la línea temporal del despliegue del ransomware.
2. Se localiza la URL completa de descarga del ransomware: `https://store5.gofile.io/download/web/e23cb33f-0e4d-4a5f-8c55-ea2d78057d40/HiddenFile.zip`.
3. Se identifica el nombre de archivo original del ejecutable descargado en el host: `pb.exe`.
4. Se determina qué ejecutable inició el proceso de cifrado en el sistema: `HpAgent.exe`.
5. Se analiza el impacto del cifrado identificando la extensión añadida a los archivos cifrados: `EeUfy`.
6. Se atribuye el ataque al grupo de ransomware BlackLock.

### Cadena de ataque / Attack Chain

```text
Extracción del $MFT del DC-01 (imagen de disco parcial)
  -> MFTECmd para reconstruir línea temporal
  -> URL de descarga: store5.gofile.io (HiddenFile.zip)
  -> Nombre original: pb.exe
  -> Ejecutable de cifrado: HpAgent.exe
  -> Extensión cifrada: EeUfy
  -> Atribución: BlackLock
```

**Learning chain:**
Extracción del $MFT → MFTECmd → URL de descarga → Identificación del payload → Cadena de ejecución → Análisis de impacto → Atribución del grupo ransomware

**Lección:** *La MFT guarda la huella completa del incidente: nombres originales, ejecutables de cifrado y extensiones permiten atribuir el ransomware sin depender de la memoria del sistema.*

**MITRE ATT&CK:**
T1190 (Exploit Public-Facing Application), T1059 (Command and Scripting Interpreter), T1486 (Data Encrypted for Impact), T1489 (Service Stop), T1027 (Obfuscated Files or Information)

**Fuente:** [TryHackMe - Shock and Silence](https://tryhackme.com/room/shockandsilence)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.