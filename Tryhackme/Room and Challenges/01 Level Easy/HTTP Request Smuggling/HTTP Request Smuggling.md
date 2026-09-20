# HTTP Request Smuggling

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `httprequestsmuggling` | https://tryhackme.com/room/httprequestsmuggling | 01 Level Easy | TryHackMe | HTTP desync / Reverse Proxy / Content-Length / Transfer-Encoding / CL.TE / TE.CL / TE.TE | Contrabando de peticiones HTTP para envenenar la comunicación proxy-servidor y saltarse controles. |

---

**Contexto:** Sala avanzada de seguridad web sobre HTTP Request Smuggling: cuando el front-end (un reverse proxy) y el back-end interpretan de forma distinta las cabeceras Content-Length y Transfer-Encoding, se produce una desincronización que permite colar peticiones adicionales en la misma conexión. Se practican las variantes CL.TE, TE.CL y TE.TE y se obtiene una flag final.

> **ES:** Comprende cómo el desajuste entre Content-Length y Transfer-Encoding permite el contrabando de peticiones y practica las variantes CL.TE, TE.CL y TE.TE.
> **EN:** Understand how mismatches between Content-Length and Transfer-Encoding enable request smuggling and practise the CL.TE, TE.CL and TE.TE variants.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Presentación del concepto de HTTP Request Smuggling; tarea introductoria de despliegue y lectura sin respuesta.

1. 1. No answer needed

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Despliega la sala y lee la introducción. | `No answer needed` |

### Task 2: Proxies y desincronización / Proxies and Desynchronization

**Explicación:** El componente situado entre el cliente y el servidor que reenvía las peticiones es un reverse proxy; su interpretación de las cabeceras puede diferir de la del back-end.

1. 1. Reverse Proxy

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué componente se sitúa entre el cliente y el servidor para reenviar las peticiones? / What component sits between the client and the server forwarding requests? | `Reverse Proxy` |

### Task 3: CL.TE

**Explicación:** En la variante CL.TE el front-end utiliza la cabecera Content-Length para delimitar la petición, mientras que el back-end usa Transfer-Encoding.

1. 1. Content-Length
   2. Content-Length/Transfer-Encoding

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué cabecera usa el front-end en CL.TE? / What header does the front-end use in CL.TE? | `Content-Length` |
| 2 | ¿Qué combinación de cabeceras define el ataque CL.TE? / What header combination defines the CL.TE attack? | `Content-Length/Transfer-Encoding` |

### Task 4: TE.CL

**Explicación:** En la variante TE.CL el front-end confía en Transfer-Encoding y el back-end en Content-Length, invirtiendo la discrepancia.

1. 1. Transfer-Encoding/Content-Length

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué combinación de cabeceras define el ataque TE.CL? / What header combination defines the TE.CL attack? | `Transfer-Encoding/Content-Length` |

### Task 5: TE.TE

**Explicación:** En TE.TE ambas cabeceras intentan usar Transfer-Encoding, pero cada componente procesa la codificación de forma distinta, permitiendo también el contrabando.

1. 1. Transfer-Encoding/Transfer-Encoding

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué combinación de cabeceras define el ataque TE.TE? / What header combination defines the TE.TE attack? | `Transfer-Encoding/Transfer-Encoding` |

### Task 6: Práctica / Practice

**Explicación:** En la parte práctica se explota la desincronización contra el laboratorio para conseguir la flag del reto.

1. 1. THM{1c4N_$mU66l3!!}

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag? / What is the flag? | `THM{1c4N_$mU66l3!!}` |

### Task 7: Cierre / Wrap-up

**Explicación:** Resumen final de la sala; no requiere respuesta.

1. 1. No answer needed

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Revisa el resumen final. | `No answer needed` |

---

| Task | # | Pregunta | Respuesta |
|------|---|----------|-----------|
| 1 | 1 | Despliega la sala y lee la introducción. | `No answer needed` |
| 2 | 1 | ¿Qué componente se sitúa entre el cliente y el servidor para reenviar las peticiones? / What component sits between the client and the server forwarding requests? | `Reverse Proxy` |
| 3 | 1 | ¿Qué cabecera usa el front-end en CL.TE? / What header does the front-end use in CL.TE? | `Content-Length` |
| 3 | 2 | ¿Qué combinación de cabeceras define el ataque CL.TE? / What header combination defines the CL.TE attack? | `Content-Length/Transfer-Encoding` |
| 4 | 1 | ¿Qué combinación de cabeceras define el ataque TE.CL? / What header combination defines the TE.CL attack? | `Transfer-Encoding/Content-Length` |
| 5 | 1 | ¿Qué combinación de cabeceras define el ataque TE.TE? / What header combination defines the TE.TE attack? | `Transfer-Encoding/Transfer-Encoding` |
| 6 | 1 | ¿Cuál es la flag? / What is the flag? | `THM{1c4N_$mU66l3!!}` |
| 7 | 1 | Revisa el resumen final. | `No answer needed` |

---

**Metodología:** Identificar la presencia de un reverse proxy, analizar la forma en que front-end y back-end interpretan las cabeceras Content-Length y Transfer-Encoding, construir la petición desincronizada según la variante (CL.TE, TE.CL, TE.TE) y explotarla contra el laboratorio para obtener la flag.

### Cadena de ataque / Attack Chain

```text
identificar reverse proxy -> CL.TE -> TE.CL -> TE.TE -> desincronización HTTP -> inyectar petición -> flag
```

**Learning chain:** HTTP Desync -> request smuggling -> CL.TE -> TE.CL -> TE.TE -> explotación.

**Lección:** *Cuando front-end y back-end interpretan las cabeceras HTTP de forma distinta, un atacante puede colar peticiones extra y envenenar la conexión entre el proxy y el servidor, saltándose los controles de la capa intermedia.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application)

**Fuente:** [TryHackMe - HTTP Request Smuggling](https://tryhackme.com/room/httprequestsmuggling)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
