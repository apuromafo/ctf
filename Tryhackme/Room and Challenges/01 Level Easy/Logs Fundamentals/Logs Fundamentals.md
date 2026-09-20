# Logs Fundamentals

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `logsfundamentals` | [TryHackMe](https://tryhackme.com/room/logsfundamentals) | 01 Level Easy | TryHackMe | Windows logs / event viewer / network logs / security logs / log analysis | Comprensión de la estructura y contenido de logs de Windows para análisis de seguridad |

---

**Contexto:** Sala introductoria sobre los fundamentos de logs en Windows. Se cubren los tipos de logs (red, seguridad), la interpretación de eventos en el visor de sucesos y la extracción de indicadores de compromiso (IOCs) como direcciones IP, marcas de tiempo y nombres de usuario a partir de entradas de log.

## Solucionario

### Task 1

**Explicación:** Se presenta una pregunta conceptual sobre qué son los logs y su función en un sistema operativo.

1. Logs

### Task 2

**Explicación:** Se identifican los dos tipos principales de logs de Windows que se analizan en el room.

1. Network Logs
2. Security Logs

### Task 3

**Explicación:** Se extraen datos de usuario comprometido a partir de entradas de log: el usuario, su grupo, la fecha de acceso y si posee privilegios de administrador.

1. hacked
2. Administrator
3. 6/7/2024
4. Yes

### Task 4

**Explicación:** Se identifican indicadores de red en los logs: la dirección IP de origen, la marca de tiempo del evento y el endpoint accedido.

1. 10.0.0.1
2. 06/Jun/2024:13:55:44
3. /contact

### Task 5

**Explicación:** Tarea exploratoria que no requiere respuesta escrita.

No answer needed

---

| # | Task | Respuesta |
|---|------|-----------|
| 1 | Task 1 | `Logs` |
| 2.1 | Task 2 | `Network Logs` |
| 2.2 | Task 2 | `Security Logs` |
| 3.1 | Task 3 | `hacked` |
| 3.2 | Task 3 | `Administrator` |
| 3.3 | Task 3 | `6/7/2024` |
| 3.4 | Task 3 | `Yes` |
| 4.1 | Task 4 | `10.0.0.1` |
| 4.2 | Task 4 | `06/Jun/2024:13:55:44` |
| 4.3 | Task 4 | `/contact` |
| 5 | Task 5 | No answer needed |

---

**Metodología:** El room se aborda de forma secuencial: primero se comprende el concepto de logs, luego se identifican los tipos de logs de red y seguridad en Windows, y finalmente se practica la extracción de datos concretos (usuarios, IPs, timestamps, endpoints) directamente de las entradas de log.

### Cadena de ataque / Attack Chain

```text
revisión de logs -> identificar tipos de log -> extraer usuarios comprometidos -> localizar IPs y timestamps -> identificar endpoints accedidos
```

**Learning chain:** log fundamentals → network logs → security logs → IOC extraction → IP/timestamp analysis → endpoint identification

**Lección:** *Los logs de Windows son una fuente primordial de evidencia forense; aprender a leerlos permite reconstruir la línea temporal de un compromiso de seguridad.*

**MITRE ATT&CK:** T1082 (System Information Discovery), T1033 (System Owner/User Discovery)

**Fuente:** [TryHackMe - Logs Fundamentals](https://tryhackme.com/room/logsfundamentals)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
