# TryPwnMe Two

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Hard | Reto • Pwn | trypwnmetwo | https://tryhackme.com/room/trypwnmetwo | 03 Level Hard | TryHackMe | Pwn, Reversing, Format String, Heap, ROP, Servidor web | Alto |

---

**Contexto:**
> **ES:** Reto de explotación de binarios (pwn) que ejercita el reversing de ejecutables sin llamadas al sistema, vulnerabilidades de format string, entornos del heap y cadenas ROP en torno a un servidor web mal configurado.
> **EN:** Binary exploitation (pwn) challenge covering the reversing of executables with no syscalls, format string vulnerabilities, heap environments and ROP chains around a badly configured web server.

## Solucionario

### Task 1: Visión general / Overview
**Explicación:**
1. No answer needed

### Task 2: Preparación / Setup
**Explicación:**
1. No answer needed

### Task 3: Reversing sin syscalls / Reversing with no syscalls
**Explicación:**
1. THM{TryExecMe-reveng3-with-no-s1sc4lls-nic3}

### Task 4: Format String
**Explicación:**
1. THM{f0rm4t-str1ng-n0t-sp3cified-ag4in}

### Task 5: Heap internals / Heap internals
**Explicación:**
1. THM{l3arning-h3ap-1nt3rn4ls-with-the-b3ar}

### Task 6: ROP
**Explicación:**
1. THM{ab4d-w3b-s3rv3r-g00d-rop-my-fr1end}

### Task 7: Conclusión / Conclusion
**Explicación:**
1. No answer needed

### Preguntas y Respuestas / Questions and Answers

| Task | Respuesta / Answer |
|---|---|
| 1 | `No answer needed` |
| 2 | `No answer needed` |
| 3 | `THM{TryExecMe-reveng3-with-no-s1sc4lls-nic3}` |
| 4 | `THM{f0rm4t-str1ng-n0t-sp3cified-ag4in}` |
| 5 | `THM{l3arning-h3ap-1nt3rn4ls-with-the-b3ar}` |
| 6 | `THM{ab4d-w3b-s3rv3r-g00d-rop-my-fr1end}` |
| 7 | `No answer needed` |

---

**Metodología:**
Explotación progresiva de binarios: análisis estático y dinámico de binarios sin syscalls, abuso de especificadores de formato no controlados, estudio de las estructuras internas del heap y encadenado de gadgets ROP.

### Cadena de ataque / Attack Chain
1. Reversing del binario inicial y bypass de las restricciones de syscalls.
2. Detección y explotación de una vulnerabilidad de format string.
3. Análisis de los internals del heap.
4. Construcción de una cadena ROP contra un servidor web vulnerable.
5. Obtención de cada flag de fase desde el servidor.

**Learning chain:**
Reversing sin syscalls → Format String → Heap → ROP → Flags.

**Lección:** *La explotación de binarios es gradual: cada técnica (reversing, format string, heap, ROP) desbloquea la siguiente bandera.*

**MITRE ATT&CK:**
- T1210 (Exploitation of Remote Services), T1059 (Command and Scripting Interpreter).

**Fuente:** [TryHackMe - TryPwnMe Two](https://tryhackme.com/room/trypwnmetwo)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.