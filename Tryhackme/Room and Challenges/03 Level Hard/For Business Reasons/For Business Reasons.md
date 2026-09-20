# For Business Reasons

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Hard | CTF | forbusinessreasons | [For Business Reasons](https://tryhackme.com/room/forbusinessreasons) | 03 Level Hard | TryHackMe | Contraseñas | Alto |

---

**Contexto:**

> **ES:** Room CTF cuyo reto conduce a la recuperación de varias contraseñas durante el recorrido por el entorno comprometido. Las respuestas son cadenas de credenciales obtenidas en distintas fases del reto.
> **EN:** CTF room whose challenge leads to the recovery of several passwords while moving through the compromised environment. The answers are credential strings obtained during different phases of the challenge.

## Solucionario

### Task 1: Recuperación de contraseñas / Password recovery

**Explicación:**

El contenido original de la tarea es el siguiente:

1. 1. ya7ooShiivagaipi
   2. osh4loNi
   3. Kainiy1Onoonoh3j

| Task | Pregunta / Question | Respuesta |
|---|---|---|
| 1 | ¿Cuál es la primera contraseña recuperada? / What is the first recovered password? | `ya7ooShiivagaipi` |
| 1 | ¿Cuál es la segunda contraseña recuperada? / What is the second recovered password? | `osh4loNi` |
| 1 | ¿Cuál es la tercera contraseña recuperada? / What is the third recovered password? | `Kainiy1Onoonoh3j` |

---

**Metodología:**

Enumeración del entorno, acceso a servicios expuestos, obtención y cracking de credenciales almacenadas, y validación de cada contraseña recuperada en las distintas fases del reto.

### Cadena de ataque / Attack Chain

1. Enumeración inicial de servicios y accesos del entorno.
2. Explotación o configuración insegura para obtener el primer material.
3. Extracción de las contraseñas almacenadas en cada fase.
4. Validación de las credenciales recuperadas.

**Learning chain:**

`For Business Reasons` → enumeración → acceso inicial → credenciales → passwords → validación.

**Lección:** *Las contraseñas débilmente guardadas o reutilizadas son el hilo dorado que conecta fases aparentemente independientes de un compromiso: una sola cadena comprometida abre el acceso al resto.*

**MITRE ATT&CK:** T1078 Valid Accounts, T1110 Brute Force, T1003 OS Credential Dumping.

**Fuente:** [TryHackMe - For Business Reasons](https://tryhackme.com/room/forbusinessreasons)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.