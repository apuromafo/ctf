# envizon

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Hard | CTF | envizon | [envizon](https://tryhackme.com/room/envizon) | 03 Level Hard | TryHackMe | Contraseña, Hashes | Alto |

---

**Contexto:**

> **ES:** Room del catálogo TryHackMe sobre la herramienta de descubrimiento y análisis de redes Envizon. El reto entrega credenciales de acceso a la interfaz y hashes MD5 obtenidos durante el análisis de la red.
> **EN:** TryHackMe catalog room about the Envizon network discovery / analysis tool. The challenge yields interface access credentials and MD5 hashes obtained during network analysis.

## Solucionario

### Task 1: Acceso a Envizon / Envizon access

**Explicación:**

El contenido original de la tarea es el siguiente:

1. 1. rE8Z*qyM!DTKNP8fGu4T3CtW*aurBQwLF
   2. 7953ba7f83b3fd00279627de052bc078
   3. 40963d170c949f8325783c552e150236

| Task | Pregunta / Question | Respuesta |
|---|---|---|
| 1 | ¿Cuál es la contraseña de acceso a Envizon? / What is the Envizon access password? | `rE8Z*qyM!DTKNP8fGu4T3CtW*aurBQwLF` |
| 1 | ¿Cuál es el primer hash MD5? / What is the first MD5 hash? | `7953ba7f83b3fd00279627de052bc078` |
| 1 | ¿Cuál es el segundo hash MD5? / What is the second MD5 hash? | `40963d170c949f8325783c552e150236` |

---

**Metodología:**

Técnicas de descubrimiento y enumeración de servicios, recopilación de credenciales y extracción de hashes mediante el uso de Envizon como herramienta de análisis de red.

### Cadena de ataque / Attack Chain

1. Despliegue y configuración de Envizon en el entorno objetivo.
2. Enumeración de hosts, servicios y recursos de red.
3. Obtención de las credenciales de acceso a la interfaz.
4. Extracción y validación de los hashes MD5 resultantes del análisis.

**Learning chain:**

`envizon` → descubrimiento de activos → enumeración → credenciales → hashes → validación de resultados.

**Lección:** *La información que una herramienta de descubrimiento expone solo es tan segura como el control de acceso que la protege: las credenciales débiles o por defecto convierten la visibilidad en un vector de compromiso.*

**MITRE ATT&CK:** T1595 Active Scanning, T1592 Gather Victim Host Information, T1078 Valid Accounts.

**Fuente:** [TryHackMe - envizon](https://tryhackme.com/room/envizon)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.