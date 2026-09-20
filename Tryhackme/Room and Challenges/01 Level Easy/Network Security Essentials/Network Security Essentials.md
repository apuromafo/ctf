# Network Security Essentials

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `networksecurityessentials` | https://tryhackme.com/room/networksecurityessentials | 01 Level Easy | TryHackMe | Análisis de red, direcciones IP, puertos, credenciales | Formativo — identificación de direcciones y configuraciones de red (IPs, puertos y credenciales) a partir de datos de red |

---

**Contexto:** Sala de fundamentos de seguridad de redes: tras una introducción teórica, se practica la lectura de los datos de red del laboratorio (registros y configuraciones) para identificar direcciones públicas y privadas, puertos de servicio y credenciales como el usuario `svc_backup`, consolidando el análisis de tráfico básico.

> **ES:** Fundamentos de seguridad de redes con práctica de análisis de datos: identificación de IPs públicas/privadas, puertos de servicio y credenciales en el laboratorio.
> **EN:** Network security fundamentals with data analysis practice: identifying public/private IPs, service ports and credentials in the lab.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Introducción de la sala sobre los fundamentos de seguridad de redes, donde se repasan los conceptos previos al trabajo práctico. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la sala. | `No answer needed` |

### Task 2: Análisis de Red (Parte 1) / Network Analysis (Part 1)

**Explicación:** Primera tanda del análisis de datos de red: se identifican las direcciones IP del escenario (incluidos rangos documentales TEST-NET) y un puerto de servicio.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la primera dirección IP identificada en el análisis? | `203.0.113.10` |
| 2 | ¿Cuál es la segunda dirección IP identificada en el análisis? | `198.51.100.12` |
| 3 | ¿Qué puerto de servicio se observa en el análisis? | `90` |
| 4 | ¿Qué IP adicional se registra en esta parte del análisis? | `45.137.22.13` |

### Task 3: Análisis de Red (Parte 2) / Network Analysis (Part 2)

**Explicación:** Segunda tanda del análisis: direcciones IP privadas y de rangos documentales, el usuario de servicio `svc_backup` y el puerto de servicio SMB (445).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué IP se identifica en el inicio de esta parte del análisis? | `203.0.113.45` |
| 2 | ¿Qué dirección privada se registra en el análisis? | `10.0.0.20` |
| 3 | ¿Qué usuario de servicio aparece en los datos? | `svc_backup` |
| 4 | ¿Qué dirección de red virtual se observa? | `10.8.0.23` |
| 5 | ¿Qué puerto de servicio SMB se detecta? | `445` |
| 6 | ¿Qué dirección privada adicional aparece en el análisis? | `10.0.0.60` |
| 7 | ¿Qué IP de rango documental se registra? | `198.51.100.77` |
| 8 | ¿Qué última dirección privada se identifica? | `10.0.0.51` |

### Task 4: Cierre / Wrap-up

**Explicación:** Cierre de la sala con repaso de los conceptos de fundamentos de seguridad de redes. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Repasa los conceptos finales de la sala. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la sala. | `No answer needed` |
| 2 | ¿Cuál es la primera dirección IP identificada en el análisis? | `203.0.113.10` |
| 3 | ¿Cuál es la segunda dirección IP identificada en el análisis? | `198.51.100.12` |
| 4 | ¿Qué puerto de servicio se observa en el análisis? | `90` |
| 5 | ¿Qué IP adicional se registra en esta parte del análisis? | `45.137.22.13` |
| 6 | ¿Qué IP se identifica en el inicio de esta parte del análisis? | `203.0.113.45` |
| 7 | ¿Qué dirección privada se registra en el análisis? | `10.0.0.20` |
| 8 | ¿Qué usuario de servicio aparece en los datos? | `svc_backup` |
| 9 | ¿Qué dirección de red virtual se observa? | `10.8.0.23` |
| 10 | ¿Qué puerto de servicio SMB se detecta? | `445` |
| 11 | ¿Qué dirección privada adicional aparece en el análisis? | `10.0.0.60` |
| 12 | ¿Qué IP de rango documental se registra? | `198.51.100.77` |
| 13 | ¿Qué última dirección privada se identifica? | `10.0.0.51` |
| 14 | Repasa los conceptos finales de la sala. | `No answer needed` |

---

**Metodología:** Tras la parte teórica se analizan los datos de red del laboratorio: se separan las direcciones públicas, privadas y de rangos documentales (TEST-NET), se identifican los puertos de servicio y la credencial `svc_backup`, y se cierra repasando los conceptos de la sala.

### Cadena de ataque / Attack Chain

```text
Teoría de seguridad de redes -> lectura de datos de red -> IPs públicas/privadas/documentiales -> puertos de servicio -> credencial svc_backup -> cierre
```

**Learning chain:** fundamentos de red → análisis de datos → direcciones IP → puertos → credenciales → repaso.

**Lección:** *La lectura correcta de los datos de red (IPs, puertos y credenciales de servicio) es el primer paso para entender qué está expuesto en una infraestructura.*

**MITRE ATT&CK:** T1046 (Network Service Discovery), T1016 (System Network Configuration Discovery)

**Fuente:** [TryHackMe - Network Security Essentials](https://tryhackme.com/room/networksecurityessentials)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.