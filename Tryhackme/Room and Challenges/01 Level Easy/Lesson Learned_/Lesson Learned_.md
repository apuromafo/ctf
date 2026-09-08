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

**Explicación:** Room CTF creada por Tib3rius que enseña una lección crítica sobre los ataques de inyección SQL: por qué `OR 1=1` es peligroso en el pentesting del mundo real. La caja simula el comportamiento real de un sistema donde las técnicas de inyección SQL inapropiadas pueden causar daños permanentes.

**Metodología:**
1. **Reconocimiento:** escanear la máquina con `nmap` (solo puertos 80 y 22 abiertos) y probar `gobuster` para descubrir directorios ocultos.
2. **Enumeración de usuarios:** usar Hydra con wordlists para descubrir el usuario válido `martin`, observando las diferencias de respuesta de error entre usuarios inválidos y válidos con contraseña incorrecta.
3. **Bypass de autenticación:** inyectar el payload seguro `martin' AND 1=1 --` en el campo de usuario con cualquier contraseña. Evita la autenticación manteniendo la condición original del usuario, sin causar daños.
4. **Obtener la flag:** la flag se muestra al completar el bypass correctamente.
5. **La lección:** `OR 1=1` hace la WHERE siempre verdadera y afecta a todas las filas (catastrófico en aplicaciones que reutilizan la entrada en UPDATE/DELETE, borrando la flag y obligando a resetear la caja). Usar `AND 1=1` limita a los registros previstos. Payloads alternativos seguros: `martin'-- -` y `martin' union select null-- -`.

#### La lección

- **`OR 1=1` es peligroso:** hace que la cláusula WHERE sea siempre verdadera, afectando a todas las filas de la base de datos. En aplicaciones que reutilizan la entrada del usuario en operaciones UPDATE o DELETE, esto puede ser catastrófico (borrar todos los datos, incluida la flag, requiriendo reset de la caja).
- **Usar `AND 1=1` en su lugar:** requiere que la condición original también sea verdadera, limitando los resultados a los registros previstos y demostrando la vulnerabilidad sin causar daños.
- **Payloads alternativos seguros:** `martin'-- -` (comentar la comprobación de contraseña) y `martin' union select null-- -`.

**Lección:** el pentesting profesional debe demostrar la vulnerabilidad sin causar daños. Siempre considerar qué pasa cuando el payload se ejecuta en diferentes contextos (UPDATE/DELETE) y usar técnicas responsables.

**Learning chain:** Recon (nmap/gobuster) → username enumeration (Hydra → martin) → auth bypass seguro (martin' AND 1=1 --) → flag THM{aab02c6b76bb752456a54c80c2d6fb1e} → lección: OR 1=1 vs AND 1=1

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1110 (Brute Force), T1213 (Data from Information Repositories)

**Fuente:** [TryHackMe - Lesson Learned?](https://tryhackme.com/room/lessonlearned)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
