# Lesson Learned? [EASY]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** EASY
* **Tipo / Type:** CTF (Free)
* **Slug:** `lessonlearned`
* **Link:** https://tryhackme.com/room/lessonlearned
* **Sección / Section:** Web / SQL Injection
* **Fuente / Source:** Writeup de Aardwolf Security (aardwolfsecurity.com) y Vedant Pillai (InfoSec Write-ups)

---

## Solucionario de Tareas / Task Solutions

> **ES:** Room CTF creada por Tib3rius que enseña una lección crítica sobre los ataques de inyección SQL: por qué `OR 1=1` es peligroso en el pentesting del mundo real. La caja simula el comportamiento real de un sistema donde las técnicas de inyección SQL inapropiadas pueden causar daños permanentes.
> **EN:** CTF room created by Tib3rius that teaches a critical lesson about SQL injection attacks: why `OR 1=1` is dangerous in real-world penetration testing. The box simulates actual system behavior where improper SQL injection techniques can cause permanent damage.

---

### Task 1 — The Lesson: Why OR 1=1 is Dangerous

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the flag? | `THM{aab02c6b76bb752456a54c80c2d6fb1e}` |

---

## Metodología / Methodology

1. **Reconocimiento / Recon:** escanear la máquina con `nmap` (solo puertos 80 y 22 abiertos). Probar `gobuster` para descubrir directorios ocultos.
2. **Enumeración de usuarios / Username enumeration:** usar Hydra con wordlists para descubrir el usuario válido `martin`, observando las diferentes respuestas de error entre usuarios inválidos y válidos con contraseña incorrecta.
3. **Bypass de autenticación / Authentication bypass:** inyectar el payload seguro `martin' AND 1=1 --` en el campo de usuario con cualquier contraseña. Esto evita la autenticación manteniendo la condición original del usuario, sin causar daños.
4. **Obtener la flag / Get the flag:** la flag se muestra al completar el bypass correctamente.

### La lección / The Lesson

- **`OR 1=1` es peligroso:** hace que la cláusula WHERE sea siempre verdadera, afectando a todas las filas de la base de datos. En aplicaciones que reutilizan la entrada del usuario en operaciones UPDATE o DELETE, esto puede ser catastrófico (borrar todos los datos, incluida la flag, requiriendo reset de la caja).
- **Usar `AND 1=1` en su lugar:** requiere que la condición original también sea verdadera, limitando los resultados a los registros previstos y demostrando la vulnerabilidad sin causar daños.
- **Payloads alternativos seguros:** `martin'-- -` (comentar la comprobación de contraseña) y `martin' union select null-- -`.

**Lección:** el pentesting profesional debe demostrar la vulnerabilidad sin causar daños. Siempre considerar qué pasa cuando el payload se ejecuta en diferentes contextos (UPDATE/DELETE) y usar técnicas responsables.

---

*Documentación para propósitos educativos y registro de CTF.*
