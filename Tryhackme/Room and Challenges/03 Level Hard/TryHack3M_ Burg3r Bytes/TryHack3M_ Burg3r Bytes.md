# TryHack3M_ Burg3r Bytes

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Hard | Reto CTF | burg3rbytes | https://tryhackme.com/room/burg3rbytes | 03 Level Hard | TryHackMe | Aplicación, TFTP, banderas | Alto |

---

**Contexto:**
> **ES:** Sala CTF de la serie TryHack3M_ centrada en una aplicación web y en el servicio TFTP: dos banderas que abarcan el hackeo de la aplicación y la diversión con el protocolo TFTP.
> **EN:** TryHack3M_ series CTF room focused on a web application and the TFTP service: two flags covering the app hack and the TFTP fun.

## Solucionario

### Task 1: Banderas del reto / Challenge flags
**Explicación:**
Contenido original de la tarea:

```text
1. 1. THM{TryH4ck3M-APP-H4CK}
   2. THM{Try4ck3M-TFTP-FUN}
```

### Preguntas y Respuestas / Questions and Answers

| Task | Respuesta / Answer |
|---|---|
| 1.1 | `THM{TryH4ck3M-APP-H4CK}` |
| 1.2 | `THM{Try4ck3M-TFTP-FUN}` |

---

**Metodología:**
1. Análisis de la aplicación web del entorno para obtener la primera flag: `THM{TryH4ck3M-APP-H4CK}`.
2. Interacción con el servicio TFTP para obtener la segunda flag: `THM{Try4ck3M-TFTP-FUN}`.

### Cadena de ataque / Attack Chain
```text
Aplicación web -> Flag 1 (APP H4CK) -> TFTP -> Flag 2 (TFTP FUN)
```

**Learning chain:**
Aplicación -> Flag 1 -> TFTP -> Flag 2.

**Lección:** *Los servicios "olvidados" como TFTP suelen quedar sin autenticación: probar cada puerto expuesto puede entregar la flag que la web no da.*

**MITRE ATT&CK:**
- T1190 Exploit Public-Facing Application
- T1071 Application Layer Protocol

**Fuente:** [TryHackMe - TryHack3M_ Burg3r Bytes](https://tryhackme.com/room/burg3rbytes)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.