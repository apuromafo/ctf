# Shock and Silence [HARD]

### Información de la Sala / Room Information

* **Dificultad:** HARD.
* **Tipo:** Premium (requiere suscripción).
* **Slug:** `shockandsilence`
* **Link:** https://tryhackme.com/room/shockandsilence
* **Objeto:** Análisis forense de ransomware (BlackLock) sobre la imagen de disco parcial del DC-01 (`.ad1`), usando MFTECmd sobre el `$MFT` para reconstruir la descarga, ejecución y cifrado del ransomware.

---

## Solucionario de Tareas / Task Solutions

> La sala es parte de la cadena "Honeynet Collapse" (DeceptiTech). Se analiza la Master File Table (MFT) y artefactos del sistema de archivos para reconstruir el despliegue del ransomware.
> This room is part of the "Honeynet Collapse" (DeceptiTech) chain. The Master File Table (MFT) and file-system artifacts are analyzed to reconstruct the ransomware deployment.

### Tarea / Task — Delivery & Download

**¿Cuál es la URL completa desde la que se descargó el ransomware al sistema? / What is the full URL from which the ransomware was downloaded to the system?**
`https://store5.gofile.io/download/web/e23cb33f-0e4d-4a5f-8c55-ea2d78057d40/HiddenFile.zip`

Fuente / Source: vishak-soc.github.io/security-writeups/tryhackme/honeynet-collapse/task-5-file-system/ · github.com/Crofter-dev/ctf_writeups/blob/main/Shock-and-Silence-Writeup.md

### Tarea / Task — Payload Identification

**¿Cuál era el nombre de archivo original del ejecutable del ransomware descargado en el host? / What was the original file name of the ransomware executable downloaded to the host?**
`pb.exe`

Fuente / Source: vishak-soc.github.io/security-writeups/tryhackme/honeynet-collapse/task-5-file-system/ · github.com/Crofter-dev/ctf_writeups

### Tarea / Task — Execution & Encryption

**¿Qué ejecutable inició el proceso de cifrado en el sistema? / Which executable file initiated the encryption process on the system?**
`HpAgent.exe`

Fuente / Source: vishak-soc.github.io/security-writeups/tryhackme/honeynet-collapse/task-5-file-system/ · github.com/Crofter-dev/ctf_writeups

### Tarea / Task — Impact Analysis

**¿Qué extensión de archivo se añadió a los archivos cifrados? / What file extension was appended to the encrypted files?**
`EeUfy`

Fuente / Source: vishak-soc.github.io/security-writeups/tryhackme/honeynet-collapse/task-5-file-system/ · github.com/Crofter-dev/ctf_writeups

### Tarea / Task — Attribution

**Más allá de lo obvio: ¿qué grupo de ransomware atacó a la organización? / Go beyond the obvious - which ransomware group targeted the organisation?**
`BlackLock`

Fuente / Source: vishak-soc.github.io/security-writeups/tryhackme/honeynet-collapse/task-5-file-system/ · github.com/Crofter-dev/ctf_writeups

---

*Documentación para propósitos educativos y registro de CTF.*
*Fuente de respuestas / Answer source: https://vishak-soc.github.io/security-writeups/tryhackme/honeynet-collapse/task-5-file-system/ · https://github.com/Crofter-dev/ctf_writeups/blob/main/Shock-and-Silence-Writeup.md*
