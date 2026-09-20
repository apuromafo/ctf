# Hack Back

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Hard | CTF | hackback | [Hack Back](https://tryhackme.com/room/hackback) | 03 Level Hard | TryHackMe | Credenciales, Flags | Alto |

---

**Contexto:**

> **ES:** Room CTF centrada en comprometer al atacante que comprometió una infraestructura: se recuperan las credenciales del atacante y dos flags que acreditan la recuperación de los fondos y el paso al entorno Web3.
> **EN:** CTF room focused on hacking back an attacker: the attacker's credentials are recovered along with two flags that certify the retrieval of the money and the move to the Web3 environment.

## Solucionario

### Task 1: Credenciales del atacante / Attacker credentials

**Explicación:**

El contenido original de la tarea es el siguiente:

1. 1. phisher@berrybears.ioc
   2. 1mTh3L33tH@x0r!

| Task | Pregunta / Question | Respuesta |
|---|---|---|
| 1 | ¿Cuál es el correo del atacante? / What is the attacker's e-mail address? | `phisher@berrybears.ioc` |
| 1 | ¿Cuál es la contraseña del atacante? / What is the attacker's password? | `1mTh3L33tH@x0r!` |

### Task 2: Recuperación de los fondos / Money recovery

**Explicación:**

El contenido original de la tarea es el siguiente:

2. THM{TIME_TO_GET_BACK_THE_MONEY}

| Task | Pregunta / Question | Respuesta |
|---|---|---|
| 2 | ¿Cuál es la flag de la recuperación? / What is the recovery flag? | `THM{TIME_TO_GET_BACK_THE_MONEY}` |

### Task 3: Entorno Web3 / Web3 environment

**Explicación:**

El contenido original de la tarea es el siguiente:

3. THM{HELLO_WEB3}

| Task | Pregunta / Question | Respuesta |
|---|---|---|
| 3 | ¿Cuál es la flag del entorno Web3? / What is the Web3 environment flag? | `THM{HELLO_WEB3}` |

---

**Metodología:**

Investigación ofensiva del atacante, recuperación de sus credenciales, acceso a su infraestructura, recuperación de los activos comprometidos y exploración del entorno Web3.

### Cadena de ataque / Attack Chain

1. Identificación del atacante y su infraestructura (phishing).
2. Recuperación de las credenciales del atacante.
3. Acceso y recuperación de los fondos comprometidos.
4. Despliegue en el entorno Web3 y captura de la flag final.

**Learning chain:**

`Hack Back` → atacante → phisher@berrybears.ioc → password → fondos → Web3 → flags.

**Lección:** *El hack-back convierte la lógica defensiva en una ofensiva controlada: conocer al atacante (sus correos, credenciales y movimientos) es la clave para recuperar lo robado sin violar los límites legales y éticos.*

**MITRE ATT&CK:** T1566 Phishing, T1078 Valid Accounts, T1530 Data from Cloud Storage Object, T1105 Ingress Tool Transfer.

**Fuente:** [TryHackMe - Hack Back](https://tryhackme.com/room/hackback)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.