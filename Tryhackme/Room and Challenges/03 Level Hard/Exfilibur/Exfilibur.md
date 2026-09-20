# Exfilibur

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Hard | CTF | exfilibur | [Exfilibur](https://tryhackme.com/room/exfilibur) | 03 Level Hard | TryHackMe | Flags | Alto |

---

**Contexto:**

> **ES:** Room CTF sobre exfiltración de datos a través de consultas DNS analizadas con Burp Suite. El reto culmina con la recuperación de dos flags que evidencian el abuso de privilegios.
> **EN:** CTF room about data exfiltration through DNS queries analysed with Burp Suite. The challenge ends with the recovery of two flags that evidence privilege abuse.

## Solucionario

### Task 1: Exfiltración por DNS / DNS exfiltration

**Explicación:**

El contenido original de la tarea es el siguiente:

1. 1. THM{HACKERS_EXFILTRATE_DATA_NOT_DRAGONS}
   2. THM{STOP_ABUSING_PRIVILEGES_IN_CAMELOT}

| Task | Pregunta / Question | Respuesta |
|---|---|---|
| 1 | ¿Cuál es la primera flag? / What is the first flag? | `THM{HACKERS_EXFILTRATE_DATA_NOT_DRAGONS}` |
| 1 | ¿Cuál es la segunda flag? / What is the second flag? | `THM{STOP_ABUSING_PRIVILEGES_IN_CAMELOT}` |

---

**Metodología:**

Intercepción y análisis de tráfico DNS con Burp Suite, identificación de subdominios que transportan datos, reconstrucción de la información exfiltrada y detección del abuso de privilegios.

### Cadena de ataque / Attack Chain

1. Intercepción del tráfico DNS con la herramienta de análisis.
2. Identificación de las consultas que transportan datos exfiltrados.
3. Reconstrucción y decodificación de los datos.
4. Obtención de las flags que evidencian la exfiltración.

**Learning chain:**

`Exfilibur` → intercepción DNS → consultas maliciosas → reconstrucción → flags de exfiltración.

**Lección:** *El DNS es un canal silencioso y frecuentemente ignorado para exfiltrar datos: cualquier política que confíe ciegamente en este protocolo convierte la red interna en un conducto de fuga.*

**MITRE ATT&CK:** T1048 Exfiltration Over Alternative Protocol, T1041 Exfiltration Over C2 Channel, T1071 Application Layer Protocol.

**Fuente:** [TryHackMe - Exfilibur](https://tryhackme.com/room/exfilibur)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.