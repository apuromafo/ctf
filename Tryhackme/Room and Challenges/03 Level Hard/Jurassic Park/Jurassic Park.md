# Jurassic Park

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Hard | Boot2root | jurassicpark | https://tryhackme.com/room/jurassicpark | 03 Level Hard | TryHackMe | Enumeración, credenciales, hashes | Alto |

---

**Contexto:**
> **ES:** Reto boot-to-root de nivel Hard inspirado en la película Jurassic Park: enumeración del host, obtención de credenciales, volcado de contraseñas y explotación de la cadena de escalada hasta completar el laboratorio.
> **EN:** Hard-level boot-to-root challenge inspired by the movie Jurassic Park: host enumeration, credential harvesting, password dumps and exploitation of the privilege escalation chain to complete the lab.

## Solucionario

### Task 1: Tarea 1
**Explicación:**
1. 1. park
   2. 5
   3. Ubuntu 16.04
   4. ih8dinos
   5. b89f2d69c56b9981ac92dd267f
   6. 96ccd6b429be8c9a4b501c7a0b117b0a
   7. b4973bbc9053807856ec815db25fb3f1
   8. No answer needed
   9. 2a7074e491fcacc7eeba97808dc5e2ec

### Preguntas y Respuestas / Questions and Answers

| Task | Respuesta / Answer |
|---|---|
| 1.1 | `park` |
| 1.2 | `5` |
| 1.3 | `Ubuntu 16.04` |
| 1.4 | `ih8dinos` |
| 1.5 | `b89f2d69c56b9981ac92dd267f` |
| 1.6 | `96ccd6b429be8c9a4b501c7a0b117b0a` |
| 1.7 | `b4973bbc9053807856ec815db25fb3f1` |
| 1.8 | `No answer needed` |
| 1.9 | `2a7074e491fcacc7eeba97808dc5e2ec` |

---

**Metodología:**
1. Reconocimiento y enumeración del host objetivo.
2. Identificación del sistema operativo (`Ubuntu 16.04`), credenciales (`park`, `ih8dinos`) y otros datos del entorno.
3. Obtención y volcado de los hashes/banderas asociados a la cadena de escalada.

### Cadena de ataque / Attack Chain
1. Enumeración del host.
2. Descubrimiento de credenciales y sistema operativo.
3. Explotación de la cadena de escalada.
4. Extracción de los hashes finales.

**Learning chain:** Enumeración -> Credenciales -> Escalada -> Hashes finales.

**Lección:** *Una enumeración exhaustiva revela las credenciales y versiones que conectan toda la cadena de compromiso.*

**MITRE ATT&CK:**
- T1046 (Network Service Discovery)
- T1110 (Brute Force)
- T1068 (Exploitation for Privilege Escalation)

**Fuente:** [TryHackMe - Jurassic Park](https://tryhackme.com/room/jurassicpark)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.