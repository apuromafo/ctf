# Welcome

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `welcome` | https://tryhackme.com/room/welcome | 01 Level Easy | TryHackMe | Sala de bienvenida, verificación de conexión a la red de TryHackMe | Confirmación de acceso al entorno y verificación de la conexión a la red de TryHackMe |

---

**Contexto:** Sala de bienvenida de TryHackMe: comprueba que el usuario puede conectarse al entorno (VPN o AttackBox) y verifica la conexión a la red de la plataforma mediante una flag. El resumen original conserva únicamente las respuestas posicionales, sin los enunciados de las preguntas.

> **ES:** Sala de bienvenida: conecta al entorno de TryHackMe y verifica la conexión a la red para obtener la flag de bienvenida.
> **EN:** Welcome room: connect to the TryHackMe environment and verify the network connection to get the welcome flag.

## Solucionario

### Task 1: Conexión inicial / Initial Connection

**Explicación:** Primera tarea de la sala: confirmar la conexión al entorno de TryHackMe. No requiere respuesta.

```
1. No answer needed
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `No answer needed` |

### Task 2: Verificación de la conexión / Connection Verification

**Explicación:** Se lanza la máquina y se contesta correctamente a la prueba de conexión, obteniendo la flag `flag{connection_verified}`.

```
2. flag{connection_verified}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `flag{connection_verified}` |

### Task 3: Cierre / Wrap-up

**Explicación:** Tarea de cierre de la sala de bienvenida. No requiere respuesta.

```
3. No answer needed
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `No answer needed` |

---

**Metodología:** Conexión al entorno (VPN/AttackBox) → lanzamiento de la máquina → verificación de la conexión a la red → obtención de la flag de bienvenida.

### Cadena de ataque / Attack Chain

```text
Conectarse a la red de TryHackMe -> desplegar la máquina -> verificar la conexión -> flag{connection_verified} -> completar la sala
```

**Learning chain:** Conexión → despliegue → verificación de red → flag de bienvenida

**Lección:** *Tener la conexión con el entorno de lab verificada es el requisito previo de cualquier reto práctico en TryHackMe.*

**MITRE ATT&CK:** T1078 (Valid Accounts)

**Fuente:** [TryHackMe - Welcome](https://tryhackme.com/room/welcome)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.