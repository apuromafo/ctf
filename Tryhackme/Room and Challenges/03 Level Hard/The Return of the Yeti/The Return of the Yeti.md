# The Return of the Yeti

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Hard | Reto CTF | surfingyetiiscomingtotown | https://tryhackme.com/room/surfingyetiiscomingtotown | 03 Level Hard | TryHackMe | WiFi, credenciales, mimikatz | Alto |

---

**Contexto:**
> **ES:** Sala CTF heredera de las sagas "Surfer" y "Yeti": el reto entrega cinco respuestas que van de nombres de red, contraseñas y herramientas (mimikatz) hasta puertos y hashes exactos que completan el desafío.
> **EN:** CTF room in the line of the "Surfer" and "Yeti" sagas: the challenge provides five answers going from network names, passwords and tools (mimikatz) to exact ports and hashes that complete it.

## Solucionario

### Task 1: Banderas del reto / Challenge flags
**Explicación:**
Contenido original de la tarea:

```text
1. 1. FreeWifiBFC
   2. Christmas
   3. mimikatz
   4. 31337-0
   5. 1-1f9548f131522e85ea30e801dfd9b1a4e526003f9e83301faad85e6154ef2834
```

### Preguntas y Respuestas / Questions and Answers

| Task | Respuesta / Answer |
|---|---|
| 1.1 | `FreeWifiBFC` |
| 1.2 | `Christmas` |
| 1.3 | `mimikatz` |
| 1.4 | `31337-0` |
| 1.5 | `1-1f9548f131522e85ea30e801dfd9b1a4e526003f9e83301faad85e6154ef2834` |

---

**Metodología:**
1. Recorrido del laboratorio siguiendo las pistas de la temática Yeti/Surfer.
2. Obtención de la SSID o nombre de red: `FreeWifiBFC`.
3. Obtención de la contraseña de la red: `Christmas`.
4. Identificación de la herramienta de volcado de credenciales involucrada: `mimikatz`.
5. Obtención del puerto: `31337-0`.
6. Obtención del hash final que cierra el reto: `1-1f9548f131522e85ea30e801dfd9b1a4e526003f9e83301faad85e6154ef2834`.

### Cadena de ataque / Attack Chain
```text
Temática Yeti -> Red WiFi -> SSID -> Contraseña -> mimikatz -> Puerto -> Hash final
```

**Learning chain:**
SSID -> Contraseña -> Herramienta (mimikatz) -> Puerto -> Hash.

**Lección:** *Los retos temáticos esconden las respuestas en el propio relato: la herramienta, el puerto y el hash aparecen cuando se sigue el hilo de la historia.*

**MITRE ATT&CK:**
- T1555 Credentials from Password Stores
- T1003 OS Credential Dumping

**Fuente:** [TryHackMe - The Return of the Yeti](https://tryhackme.com/room/surfingyetiiscomingtotown)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.