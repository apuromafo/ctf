# Custom Tooling Using Python

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | Offensive Security / Scripting & Red Teaming | `customtoolingusingpython` | https://tryhackme.com/room/customtoolingusingpython | 01 Level Easy | TryHackMe | Python / requests / zfill / brute force / threading / scripting / portería de exploits / automatización | Crear herramientas propias en Python para automatizar ataques (brute force de login, exploits básicos) y adaptar el tooling a las necesidades del pentesting/red teaming. |

---

**Contexto:** Sala ofensiva que explica por qué un red teamer debe crear su propio tooling (los tools comerciales no siempre se ajustan, y el código propio suele evadir mejor la detección). Se elige el lenguaje (Python, Go, JavaScript con distintos propósitos) y se practica escribiendo scripts reales: un brute force de autenticación con la librería `requests`, un script con hilos (`Threading`) para acelerar el ataque y un pequeño exploit de ejemplo, capturando banderas en cada fase.

> **ES:** "Crea tus propias herramientas con Python: automatiza un ataque de fuerza bruta a un login, usa threading y escribe un exploit básico. El tooling propio es clave en red teaming."
> **EN:** "Create your own tooling with Python: automate a brute-force login attack, use threading and write a basic exploit. Custom tooling is key in red teaming."

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Se introducen los motivos por los que el tooling personalizado es importante en red teaming: adaptarse a necesidades concretas, modificar exploits, automatizar tareas repetitivas y, a menudo, evadir mejor la detección. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | He leído la introducción. / I've read the introduction. | `No answer needed` |

---

### Task 2: Usando un lenguaje de programación / Using a Coding Language for Custom Tooling

**Explicación:** A la hora de elegir lenguaje hay que decidir entre scripting o compilado. Se analizan opciones: Python es muy popular para scripting, Go es ideal para tareas de bajo nivel y procesos, y JavaScript destaca por su ejecución en el navegador. Aunque este reto usa Python, las lecciones aplican también a Bash, Go, Rust o JavaScript.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Según el contenido, ¿es Python el lenguaje más popular para crear tooling? (Yea/Nay) / Based on the content, is Python the most popular language for custom tooling? (Yea/Nay) | `Nay` |
| 2 | ¿Qué lenguaje se destaca para tareas de bajo nivel y gestión de procesos? / Which language stands out for low-level tasks and process management? | `Go` |
| 3 | ¿Qué lenguaje se ejecuta principalmente en el navegador? / Which language runs primarily in the browser? | `JavaScript` |

---

### Task 3: Scripting con Python (Brute Force) / Custom Scripting with Python

**Explicación:** Se crea un script de Python que automatiza un ataque de fuerza bruta contra un formulario de login. La librería `requests` envía peticiones HTTP POST probando combinaciones usuario/contraseña, y se usa manipulación de strings (`zfill()`) para generar candidatos. Al encontrar las credenciales válidas, el servidor responde con las banderas de éxito correspondientes a cada wordlist.

```python
import requests

for num in range(10000):
    pw = str(num).zfill(4)
    r = requests.post(url, data={"username": user, "password": pw})
    if "Success" in r.text:
        print(pw, r.text)   # bandera de éxito
        break
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué librería se usa para enviar las peticiones HTTP? / Which library is used to send HTTP requests? | `requests` |
| 2 | ¿Cuál es la bandera de éxito al usar la primera wordlist (mark001)? / What is the success flag when using the first wordlist (mark001)? | `THM{Brute_Force_Success007}` |
| 3 | ¿Cuál es la bandera de éxito al usar la segunda wordlist (mark002)? / What is the success flag when using the second wordlist (mark002)? | `THM{Brute_Force_Success_Mark001}` |

---

### Task 4: Más scripting / More scripting (Threading)

**Explicación:** Se mejora el script aplicando concurrencia: se configuran varios parámetros del ataque y se lanzan peticiones en paralelo con `Threading` para acelerar el brute force. Los valores requeridos del ejercicio (parámetro de salida, número de hilos y la opción correcta) se completan tal como indica el reto.

```python
import threading
# número de hilos (threads) y parámetros de salida configurados según el reto.
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué valor se asigna al parámetro de salida indicado en el ejercicio? / What value is assigned to the output parameter in the exercise? | `0` |
| 2 | ¿Cuántos hilos (threads) se configuran en el script? / How many threads are configured in the script? | `2` |
| 3 | ¿Cuál es la opción correcta (letra) del ejercicio? / Which is the correct option (letter) in the exercise? | `b` |
| 4 | ¿Qué librería/módulo de Python se usa para gestionar la concurrencia? / Which Python module is used for concurrency? | `Threading` |

---

### Task 5: Explotación con Python / Basic exploit using Python

**Explicación:** Se escribe un exploit básico en Python contra el servicio vulnerable del lab: tras la ejecución correcta se obtiene la bandera de éxito del exploit.

```python
import socket
# exploit básico contra el servicio del lab.
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la bandera del exploit básico? / What is the flag of the basic exploit? | `THM{basic_exploit_using_python}` |

---

### Task 6: Reto final / Final challenge

**Explicación:** Se completa el reto final combinando el tooling creado (fuerza bruta + exploit) para comprometer el objetivo y capturar la bandera final.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la bandera final del reto? / What is the final flag of the challenge? | `THM{6470e394cbf6dab6a91682cc8585059b}` |

---

### Task 7: Conclusión / Conclusion

**Explicación:** Resumen de la sala: dominar la creación de tooling propio amplía la caja de herramientas del red teamer y permite personalizar cada ataque. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | He completado la sala. / I've completed the room. | `No answer needed` |

---

| # | Task | Pregunta | Respuesta |
|---|------|----------|-----------|
| 1 | Task 1 | Introducción. / Introduction. | `No answer needed` |
| 2 | Task 2 | ¿Es Python el más popular? / Is Python the most popular? | `Nay` |
| 3 | Task 2 | ¿Qué lenguaje para bajo nivel? / Which language for low-level? | `Go` |
| 4 | Task 2 | ¿Qué lenguaje usa el navegador? / Which language runs in the browser? | `JavaScript` |
| 5 | Task 3 | ¿Qué librería se usa para HTTP? / Which library is used for HTTP? | `requests` |
| 6 | Task 3 | Bandera mark001. / mark001 flag. | `THM{Brute_Force_Success007}` |
| 7 | Task 3 | Bandera mark002. / mark002 flag. | `THM{Brute_Force_Success_Mark001}` |
| 8 | Task 4 | Parámetro de salida. / Output parameter. | `0` |
| 9 | Task 4 | Número de hilos. / Number of threads. | `2` |
| 10 | Task 4 | Opción correcta. / Correct option. | `b` |
| 11 | Task 4 | Módulo de concurrencia. / Concurrency module. | `Threading` |
| 12 | Task 5 | Bandera del exploit básico. / Basic exploit flag. | `THM{basic_exploit_using_python}` |
| 13 | Task 6 | Bandera final. / Final flag. | `THM{6470e394cbf6dab6a91682cc8585059b}` |
| 14 | Task 7 | Conclusión. / Conclusion. | `No answer needed` |

---

**Metodología:** Elegir el lenguaje según el objetivo (scripting vs compilado) -> escribir un script de brute force con `requests` y `zfill()` -> capturar las banderas de éxito -> optimizar con hilos (`Threading`) -> desarrollar un exploit básico contra el servicio del lab -> encadenar las herramientas para resolver el reto final.

### Cadena de ataque / Attack Chain

```text
Python + requests -> brute force login (zfill) -> bandera mark001/mark002 -> Threading (2 hilos) -> exploit básico -> THM{basic_exploit_using_python} -> reto final -> flag
```

**Learning chain:** custom tooling -> Python -> requests -> zfill -> brute force -> threading -> exploit scripting -> flag.

**Lección:** *El tooling propio puede ser tan simple como un bucle con `requests`; automatizar la fuerza bruta y paralelizarla con hilos convierte horas de trabajo manual en segundos de script.*

**MITRE ATT&CK:** T1110 (Brute Force), T1059.007 (Command and Scripting Interpreter: JavaScript/Python), T1106 (Native API)

**Fuente:** [TryHackMe - Custom Tooling Using Python](https://tryhackme.com/room/customtoolingusingpython)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.