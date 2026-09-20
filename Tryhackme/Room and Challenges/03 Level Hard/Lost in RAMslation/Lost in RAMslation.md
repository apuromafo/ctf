# Lost in RAMslation

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Hard | Forense | lostinramslation | https://tryhackme.com/room/lostinramslation | 03 Level Hard | TryHackMe | Memory forensics, Volatility, análisis de malware, rundll32 | Alto |

---

**Contexto:**
> **ES:** Ejercicio de memoria forense (RAM): análisis de un volcado de memoria para identificar el malware persistente (`C:\Windows\Tasks\MicrosoftUpdate.dll` lanzado con `rundll32.exe`), su PID, los procesos implicados (incluido `notepad.exe`), el hash del artefacto y la IP de comunicaciones con el atacante.
> **EN:** Memory forensics (RAM) exercise: analysis of a memory dump to identify the persistent malware (`C:\Windows\Tasks\MicrosoftUpdate.dll` launched with `rundll32.exe`), its PID, the involved processes (including `notepad.exe`), the artefact hash and the attacker's communication IP.

## Solucionario

### Task 1: Tarea 1
**Explicación:**
1. No answer needed

### Task 2: Tarea 2
**Explicación:**
2. 1. C:\Windows\Tasks\MicrosoftUpdate.dll
   2. 2928
   3. rundll32.exe C:\windows\tasks\MicrosoftUpdate.dll, RunMe
   4. notepad.exe
   5. fc4889ce48
   6. 172.16.2.9

### Preguntas y Respuestas / Questions and Answers

| Task | Respuesta / Answer |
|---|---|
| 1.1 | `No answer needed` |
| 2.1 | `C:\Windows\Tasks\MicrosoftUpdate.dll` |
| 2.2 | `2928` |
| 2.3 | `rundll32.exe C:\windows\tasks\MicrosoftUpdate.dll, RunMe` |
| 2.4 | `notepad.exe` |
| 2.5 | `fc4889ce48` |
| 2.6 | `172.16.2.9` |

---

**Metodología:**
1. Cargar el volcado de memoria y enumerar procesos con herramientas de memoria forense (Volatility).
2. Localizar el artefacto malicioso (`C:\Windows\Tasks\MicrosoftUpdate.dll`) y el PID del proceso (`2928`).
3. Reconstruir la línea de comandos de ejecución (`rundll32.exe ... , RunMe`) e identificar procesos comprometidos (`notepad.exe`).
4. Extraer el hash del archivo (`fc4889ce48`) y la IP de comunicaciones (`172.16.2.9`).

### Cadena de ataque / Attack Chain
1. Análisis de procesos en el volcado de memoria.
2. Identificación del artefacto malicioso y su PID.
3. Reconstrucción de la línea de comandos y de los procesos implicados.
4. Extracción del hash y de la IP de C2.

**Learning chain:** Volcado de memoria -> Procesos -> Artefacto malicioso -> PID -> Línea de comandos -> Hash -> IP C2.

**Lección:** *Los volcados de memoria conservan toda la cadena de ejecución del malware: procesos, argumentos y rutas deben examinarse con detalle.*

**MITRE ATT&CK:**
- T1059.003 (Command and Scripting Interpreter: Windows Command Shell)
- T1218.011 (System Binary Proxy Execution: Rundll32)
- T1569.002 (System Services: Service Execution)
- T1064 (Scripting)

**Fuente:** [TryHackMe - Lost in RAMslation](https://tryhackme.com/room/lostinramslation)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.