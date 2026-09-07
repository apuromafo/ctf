# Beach Bar

| **Dificultad** | Easy |
| **Tipo** | challenge |
| **Slug** | `hh-beachbar-d849f7f7` |
| **Link** | [TryHackMe](https://tryhackme.com/r/room/hh-beachbar-d849f7f7) |
| **Sección** | Hunt & Hack House |
| **Fuente** | THM |
| **Componentes** | nmap/enumeration/credential reuse/yml playlist |
| **Impacto** | Captura de credenciales reutilizadas y escalada a root mediante un playlist YAML expuesto |

---

**Contexto:** Una playa tropical esconde más que arena y sol: el servidor del Beach Bar aloja archivos de configuración en formato YAML que contienen credenciales reutilizadas. La enumeración inicial revela servicios ocultos y un playlist que sirve como vector de acceso inicial al sistema.

## Solucionario

### Task 1: User Flag

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the user flag? | `THM{y4ml_pl4yl1st_pwns_th3_b34ch}` |

### Task 2: Root Flag

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the root flag? | `THM{cr3d3nt14l_r3us3_4t_th3_b34ch_b4r}` |

---

**Metodología:** Se inicia con un escaneo nmap completo de la máquina target para identificar servicios abiertos. Posteriormente se procede a la enumeración exhaustiva de directorios y archivos, localizando un archivo YAML con credenciales reutilizadas. Con las credenciales obtenidas se establece conexión SSH como usuario regular y se completa la captura del user flag. La escalada de privilegios se logra explotando credenciales reutilizadas que otorgan acceso root al sistema, permitiendo capturar el root flag.

**Learning chain:** nmap scanning → port enumeration → directory discovery → YAML playlist analysis → credential extraction → SSH access → user flag capture → credential reuse escalation → root access → root flag capture

**MITRE ATT&CK:** T1078 (Valid Accounts), T1110 (Brute Force), T1021 (Remote Services), T1552 (Credentials In Files)

**Fuente:** [TryHackMe - Beach Bar](https://tryhackme.com/r/room/hh-beachbar-d849f7f7)
