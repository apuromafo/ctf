# Fusion Corp

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Hard | CTF | fusioncorp | [Fusion Corp](https://tryhackme.com/room/fusioncorp) | 03 Level Hard | TryHackMe | Flags | Alto |

---

**Contexto:**

> **ES:** Room CTF en la que el recorrido por una infraestructura corporativa comprometida concluye con la obtención de tres flags que acreditan cada fase del reto.
> **EN:** CTF room where the traversal of a compromised corporate infrastructure ends with the recovery of three flags that certify each phase of the challenge.

## Solucionario

### Task 1: Obtención de las flags / Flag recovery

**Explicación:**

El contenido original de la tarea es el siguiente:

1. 1. THM{c105b6fb249741b89432fada8218f4ef}
   2. THM{b4aee2db2901514e28db4242e047612e}
   3. THM{f72988e57bfc1deeebf2115e10464d15}

| Task | Pregunta / Question | Respuesta |
|---|---|---|
| 1 | ¿Cuál es la primera flag? / What is the first flag? | `THM{c105b6fb249741b89432fada8218f4ef}` |
| 1 | ¿Cuál es la segunda flag? / What is the second flag? | `THM{b4aee2db2901514e28db4242e047612e}` |
| 1 | ¿Cuál es la tercera flag? / What is the third flag? | `THM{f72988e57bfc1deeebf2115e10464d15}` |

---

**Metodología:**

Reconocimiento de la infraestructura, explotación de servicios expuestos, movimientos laterales y recolección de cada flag conforme se completa cada fase del reto.

### Cadena de ataque / Attack Chain

1. Enumeración de los servicios de la infraestructura corporativa.
2. Explotación del vector de acceso inicial.
3. Movimiento lateral y captura de las flags intermedias.
4. Compromiso final y obtención de la última flag.

**Learning chain:**

`Fusion Corp` → infraestructura → acceso → movimiento lateral → flags → compromiso final.

**Lección:** *Cada flag de un reto corporativo representa un salto de confianza: conocer los límites entre cuentas, servicios y segmentos determina cuántas compañías (y cuánto daño) un atacante puede recorrer.*

**MITRE ATT&CK:** T1078 Valid Accounts, T1190 Exploit Public-Facing Application, T1021 Remote Services, T1046 Network Service Discovery.

**Fuente:** [TryHackMe - Fusion Corp](https://tryhackme.com/room/fusioncorp)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.