# Shock and Silence

| **Dificultad** | Hard |
| **Tipo** | CTF |
| **Slug** | `shockandsilence` |
| **Link** | [TryHackMe](https://tryhackme.com/room/shockandsilence) |
| **Sección** | 03 Level Hard |
| **Fuente** | vishak-soc.github.io + Crofter-dev/ctf_writeups |
| **Componentes** | MFT / MFTECmd / Ransomware Analysis / Forensics / BlackLock |
| **Impacto** | Análisis forense completo del despliegue de ransomware BlackLock reconstruyendo la cadena de ataque a partir de artefactos de la Master File Table. |

---

**Contexto:** Sala parte de la cadena "Honeynet Collapse" (DeceptiTech). Se analiza la Master File Table (MFT) y artefactos del sistema de archivos para reconstruir el despliegue del ransomware BlackLock sobre la imagen de disco parcial del DC-01, usando MFTECmd sobre el `$MFT`.

## Solucionario

### Task 1: Delivery & Download

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the full URL from which the ransomware was downloaded to the system? | `https://store5.gofile.io/download/web/e23cb33f-0e4d-4a5f-8c55-ea2d78057d40/HiddenFile.zip` |

### Task 2: Payload Identification

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What was the original file name of the ransomware executable downloaded to the host? | `pb.exe` |

### Task 3: Execution & Encryption

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which executable file initiated the encryption process on the system? | `HpAgent.exe` |

### Task 4: Impact Analysis

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What file extension was appended to the encrypted files? | `EeUfy` |

### Task 5: Attribution

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Go beyond the obvious - which ransomware group targeted the organisation? | `BlackLock` |

---

**Metodología:**

1. Se exporta el `$MFT` de la imagen de disco parcial del DC-01 y se procesa con MFTECmd para reconstruir la línea temporal del despliegue del ransomware.
2. Se localiza la URL completa de descarga del ransomware: `https://store5.gofile.io/download/web/e23cb33f-0e4d-4a5f-8c55-ea2d78057d40/HiddenFile.zip`.
3. Se identifica el nombre de archivo original del ejecutable descargado en el host: `pb.exe`.
4. Se determina qué ejecutable inició el proceso de cifrado en el sistema: `HpAgent.exe`.
5. Se analiza el impacto del cifrado identificando la extensión añadida a los archivos cifrados: `EeUfy`.
6. Se atribuye el ataque al grupo de ransomware BlackLock.

```
Extracción del $MFT del DC-01 (imagen de disco parcial)
  -> MFTECmd para reconstruir línea temporal
  -> URL de descarga: store5.gofile.io (HiddenFile.zip)
  -> Nombre original: pb.exe
  -> Ejecutable de cifrado: HpAgent.exe
  -> Extensión cifrada: EeUfy
  -> Atribución: BlackLock
```

**Learning chain:** Extracción del $MFT → MFTECmd → URL de descarga → Identificación del payload → Cadena de ejecución → Análisis de impacto → Atribución del grupo ransomware

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1059 (Command and Scripting Interpreter), T1486 (Data Encrypted for Impact), T1489 (Service Stop), T1027 (Obfuscated Files or Information)

**Fuente:** [TryHackMe - Shock and Silence](https://tryhackme.com/room/shockandsilence)
