# Epoch

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | ctf | `epoch` | [TryHackMe - Epoch](https://tryhackme.com/room/epoch) | `01 Level Easy` | THM | Linux, epoch, timestamps, date, flags | Exploitation — manipulación de timestamps |

> **Objeto:** Resolver el desafío de la sala donde el tiempo es falso y los timestamps mienten, demostrando dominio de la línea de comandos UNIX y capturar la bandera final.

---

**Contexto:** La sala Epoch es un desafío CTF de nivel inicial centrado en la manipulación de la hora y los timestamps de Unix. El objetivo es demostrar que "el tiempo es falso y los timestamps mienten" manipulando el reloj del sistema para cumplir las condiciones del entorno y obtener la bandera.

> **ES:** Sala CTF sobre el epoch de Unix y la manipulación de la fecha/hora del sistema. Se resuelve ajustando el reloj del equipo y obteniendo la bandera final de la sala.
>
> **EN:** CTF room about the Unix epoch and system time/date manipulation. It is solved by adjusting the machine clock and capturing the final flag.

## Solucionario

### Task 1: Manipular el tiempo / Manipulate the time

**Explicación:** La sala plantea la resolución del desafío ajustando el reloj del sistema para engañar al entorno de validación. La bandera final se entrega como resultado de completar la manipulación de timestamps.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Bandera final de la sala / Final flag | `flag{7da6c7debd40bd611560c13d8149b647}` |

---

**Metodología:** Se inicia la máquina objetivo y se manipula la fecha y hora del sistema (epoch) mediante la línea de comandos hasta satisfacer la condición del desafío. Una vez validada la hora correcta, el entorno entrega la bandera, que se registra literalmente para completar la tarea.

### Cadena de ataque / Attack Chain

Arranque del laboratorio → manipulación del reloj/timestamps → validación del tiempo → obtención de la bandera.

**Learning chain:** Linux CLI → date/epoch timestamps → clock manipulation → CTF flags

**Lección:** *Los timestamps del sistema no son una fuente de confianza por sí mismos: cualquier servicio que valide tiempo debe contrastarse con una fuente externa fiable.*

**MITRE ATT&CK:** T1070.006 - Indicator Removal on Host: Timestomp; N/A (CTF / entorno de práctica)

**Fuente:** [TryHackMe - Epoch](https://tryhackme.com/room/epoch)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.