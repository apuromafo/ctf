# Lesson Learned?

| **Dificultad** | Easy |
| **Tipo** | CTF |
| **Slug** | `lessonlearned` |
| **Link** | [TryHackMe](https://tryhackme.com/room/lessonlearned) |
| **Sección** | 01 Level Easy |
| **Fuente** | Writeup de Aardwolf Security (aardwolfsecurity.com) y Vedant Pillai (InfoSec Write-ups) |
| **Componentes** | nmap / gobuster / Hydra / SQL Injection (OR 1=1 vs AND 1=1) / UNION |
| **Impacto** | Lección práctica sobre por qué `OR 1=1` es peligroso en el pentesting real y cómo demostrar SQLi sin dañar datos |

---

**Contexto:** Room CTF creada por Tib3rius que enseña una lección crítica sobre los ataques de inyección SQL: por qué `OR 1=1` es peligroso en el pentesting del mundo real. La caja simula el comportamiento real de un sistema donde las técnicas de inyección SQL inapropiadas pueden causar daños permanentes.

## Solucionario

### Task 1: The Lesson: Why OR 1=1 is Dangerous

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag? | `THM{aab02c6b76bb752456a54c80c2d6fb1e}` |

---

**Metodología:**
1. **Reconocimiento:** escanear la máquina con `nmap` (solo puertos 80 y 22 abiertos) y probar `gobuster` para descubrir directorios ocultos.
2. **Enumeración de usuarios:** usar Hydra con wordlists para descubrir el usuario válido `martin`, observando las diferencias de respuesta de error entre usuarios inválidos y válidos con contraseña incorrecta.
3. **Bypass de autenticación:** inyectar el payload seguro `martin' AND 1=1 --` en el campo de usuario con cualquier contraseña. Evita la autenticación manteniendo la condición original del usuario, sin causar daños.
4. **Obtener la flag:** la flag se muestra al completar el bypass correctamente.
5. **La lección:** `OR 1=1` hace la WHERE siempre verdadera y afecta a todas las filas (catastrófico en aplicaciones que reutilizan la entrada en UPDATE/DELETE, borrando la flag y obligando a resetear la caja). Usar `AND 1=1` limita a los registros previstos. Payloads alternativos seguros: `martin'-- -` y `martin' union select null-- -`.

**Learning chain:** Recon (nmap/gobuster) → username enumeration (Hydra → martin) → auth bypass seguro (martin' AND 1=1 --) → flag THM{aab02c6b76bb752456a54c80c2d6fb1e} → lección: OR 1=1 vs AND 1=1

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1110 (Brute Force), T1213 (Data from Information Repositories)

**Fuente:** [TryHackMe - Lesson Learned?](https://tryhackme.com/room/lessonlearned)