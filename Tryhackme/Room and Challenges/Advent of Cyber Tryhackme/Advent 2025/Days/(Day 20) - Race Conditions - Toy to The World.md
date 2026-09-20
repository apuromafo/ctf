# Race Conditions - Toy to The World

| **Dificultad** | Easy | **Tipo** | walkthrough | **Slug** | `day20raceconditionstoytotheworld` |
| **Link** | [TryHackMe](https://tryhackme.com/room/adventofcyber25) |
| **Sección** | Advent of Cyber Tryhackme |
| **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | race condition / TOCTOU / shared resource race / atomicity violation / web applications / concurrent requests |
| **Impacto** | Explotar race conditions en una tienda web para dejar el stock en negativo y obtener flags |

---

**Contexto:** Día 20 del Advent of Cyber 2025. Se estudia la vulnerabilidad de **race condition** en aplicaciones web: ocurre cuando dos o más acciones se ejecutan a la vez, el resultado depende de cuál termina primero y la aplicación carece de sincronización adecuada. Se cubren los tipos: **TOCTOU** (Time-of-Check to Time-of-Use, lo que se comprueba puede cambiar antes de usarse), **Shared Resource Race** (varios usuarios modifican los mismos datos a la vez sin control) y **Atomicity Violation** (partes de un proceso se separan y otra petición se cuela entre medias). Las race conditions explotan el timing.

## Solucionario

### Día 20: Race Conditions - Toy to The World

**Explicación:**

- Race condition vulnerability in web applications
- Race condition happens when
     1. Two or more actions run at the same time
     2. The result depends on which finishes first
     3. The application lacks proper synchronisation

- Types of race conditions
     1. TOCTOU (Time-of-Check to Time-of-Use) : a program checks something first and uses it later, but the data changes in between. This means what was true at the time of the check might no longer be true when the action happens
     2. Shared Resource Race : when multiple users or systems try to change the same data simultaneously without proper control; final result depends on which one finishes last
     3. Atomicity Violation : When parts of a process run separately, another request can sneak in between and cause inconsistent results

- Race conditions exploit timing

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag value once the stocks are negative for SleighToy Limited Edition? | `THM WINNER_OF_R@CE007}` |
| 2 | Repeat the same steps as were done for ordering the SleighToy Limited Edition. What is the flag value once the stocks are negative for Bunny Plush (Blue)? | `THM{WINNER_OF_Bunny_R@ce]` |

---

**Metodología:** Se lanzaron múltiples peticiones de compra simultáneas sobre el mismo producto (SleighToy Limited Edition y luego Bunny Plush Blue) para que el decremento de stock se procesara de forma concurrente sin sincronización. Al agotar y sobrepasar el stock (dejándolo en negativo) la aplicación reveló el flag en cada caso.
**Learning chain:** race condition -> concurrencia (dos o más acciones a la vez) -> falta de sincronización -> TOCTOU / shared resource race / atomicity violation -> explotación del timing -> stock negativo -> flags

Cadena de ataque / Attack Chain:
```
envío simultáneo de N pedidos (concurrencia) -> decremento de stock no sincronizado -> stock negativo (SleighToy) -> THM WINNER_OF_R@CE007} -> repetición con Bunny Plush (Blue) -> THM{WINNER_OF_Bunny_R@ce]
```

**Lección:** *Una race condition convierte la lógica validable ("si hay stock, déjalo comprar") en una carrera de ejecución: si el chequeo y el uso no son atómicos, N pedidos concurrentes pueden drenar el inventario; explotar el timing es la técnica y hacer las operaciones atómicas la mitigación.*

**MITRE ATT&CK:** CWE-362 - Race Condition (concurrencia en lógica de negocio; sin técnica ATT&CK Enterprise dedicada)

**Fuente:** [TryHackMe - Race Conditions - Toy to The World](https://tryhackme.com/room/adventofcyber25)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.