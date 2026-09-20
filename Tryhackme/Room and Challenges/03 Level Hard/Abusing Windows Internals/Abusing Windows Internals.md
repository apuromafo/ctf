# Abusing Windows Internals

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Hard | Reto • Abuso de internals de Windows | abusingwindowsinternals | https://tryhackme.com/room/abusingwindowsinternals | 03 Level Hard | TryHackMe | Windows API, DLL Injection, APC, RtlCreateUserThread, Hooking | Alto |

---

**Contexto:**
> **ES:** Laboratorio orientado al abuso de las internals de Windows: inyección de DLL en procesos legítimos, inyección APC, creación de hilos remotos con RtlCreateUserThread y mecanismos de hooking para evadir controles.
> **EN:** Lab focused on abusing Windows internals: DLL injection into legitimate processes, APC injection, remote thread creation with RtlCreateUserThread and hooking mechanisms to evade controls.

## Solucionario

### Task 1: Activación del laboratorio / Lab activation
**Explicación:**
1. No answer needed

### Task 2: Inyección de procesos / Process injection
**Explicación:**
1. No answer needed
2. THM{1nj3c710n_15_fun!}

### Task 3: Offuscación / Offuscation
**Explicación:**
1. No answer needed
2. THM{7h3r35_n07h1n6_h3r3}

### Task 4: Arma de defensa / Weaponization
**Explicación:**
1. No answer needed
2. THM{w34p0n1z3d_53w1n6}

### Task 5: DLL maliciosa / Malicious DLL
**Explicación:**
1. No answer needed
2. THM{n07_4_m4l1c10u5_dll}

### Task 6: APC - Llamada a procedimiento asíncrono / APC - Asynchronous Procedure Call
**Explicación:**
1. Asynchronous Procedure Call
2. QueueUserAPC
3. n

### Task 7: RtlCreateUserThread y hooks / RtlCreateUserThread and hooks
**Explicación:**
1. RtlCreateUserThread
2. y
3. write_hook_iter

### Task 8: Cierre / Wrap-up
**Explicación:**
1. No answer needed

### Preguntas y Respuestas / Questions and Answers

| Task | Respuesta / Answer |
|---|---|
| 1 | `No answer needed` |
| 2.1 | `No answer needed` |
| 2.2 | `THM{1nj3c710n_15_fun!}` |
| 3.1 | `No answer needed` |
| 3.2 | `THM{7h3r35_n07h1n6_h3r3}` |
| 4.1 | `No answer needed` |
| 4.2 | `THM{w34p0n1z3d_53w1n6}` |
| 5.1 | `No answer needed` |
| 5.2 | `THM{n07_4_m4l1c10u5_dll}` |
| 6.1 | `Asynchronous Procedure Call` |
| 6.2 | `QueueUserAPC` |
| 6.3 | `n` |
| 7.1 | `RtlCreateUserThread` |
| 7.2 | `y` |
| 7.3 | `write_hook_iter` |
| 8 | `No answer needed` |

---

**Metodología:**
Abuso de mecanismos internos de Windows: observación de procesos, inyección de DLL, cola de APC, hilos remotos y parches de hooking. Cada respuesta se obtiene analizando el comportamiento del payload sobre el proceso objetivo.

### Cadena de ataque / Attack Chain
1. Elección del proceso víctima y estudio de sus módulos cargados.
2. Inyección de una DLL maliciosa en el espacio de direcciones del proceso.
3. Cola de APC sobre un hilo existente para ejecutar el payload.
4. Creación de hilo remoto con RtlCreateUserThread para técnicas alternativas.
5. Aplicación de hooks (write_hook_iter) para redirigir funciones clave.

**Learning chain:**
Observación de procesos -> Identificación de técnicas de inyección -> Explotación de APIs legítimas de Windows -> Comprensión de patterns de EDR bypass.

**Lección:** *La confianza en las APIs legítimas de Windows también es un vector; un EDR solo detecta aquello que sabe observar.*

**MITRE ATT&CK:**
- T1055 Process Injection
- T1055.001 DLL Injection
- T1055.004 APC Injection
- T1106 Native API
- T1059.003 Command and Scripting Interpreter

**Fuente:** [TryHackMe - Abusing Windows Internals](https://tryhackme.com/room/abusingwindowsinternals)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.