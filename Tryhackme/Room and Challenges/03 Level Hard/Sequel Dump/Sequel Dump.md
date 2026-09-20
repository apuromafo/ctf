# Sequel Dump

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Hard | Reto CTF | hfb1sequeldump | https://tryhackme.com/room/hfb1sequeldump | 03 Level Hard | TryHackMe | SQL, bases de datos, recuperación de dump | Alto |

---

**Contexto:**
> **ES:** Sala CTF temática de "Sequel" en la que el objetivo es recuperar el dump asociado al entorno y entregar la bandera única del reto.
> **EN:** Sequel-themed CTF room in which the goal is to retrieve the environment's dump and submit the single flag of the challenge.

## Solucionario

### Task 1: Banderas del reto / Challenge flags
**Explicación:**
Contenido original de la tarea:

```text
1. THM{r3tr13v1ng_th3_dump}
```

### Preguntas y Respuestas / Questions and Answers

| Task | Respuesta / Answer |
|---|---|
| 1.1 | `THM{r3tr13v1ng_th3_dump}` |

---

**Metodología:**
1. Exploración del entorno para localizar el almacén de datos o el punto desde el que se puede recuperar la información.
2. Extracción del dump y obtención de la bandera: `THM{r3tr13v1ng_th3_dump}`.

### Cadena de ataque / Attack Chain
```text
Exploración -> Localización del almacén de datos -> Extracción del dump -> Flag
```

**Learning chain:**
Exploración -> Dump -> Flag.

**Lección:** *Cuando el reto pide un "dump", la respuesta suele estar en los datos que no se limpiaron ni protegieron.*

**MITRE ATT&CK:**
- T1190 Exploit Public-Facing Application
- T1003 OS Credential Dumping

**Fuente:** [TryHackMe - Sequel Dump](https://tryhackme.com/room/hfb1sequeldump)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.