# Introduction To Honeypots

| **Dificultad** | MEDIUM | **Tipo** | Free | **Slug** | `introductiontohoneypots` |
| **Link** | [TryHackMe](https://tryhackme.com/room/introductiontohoneypots) | **Sección** | 02 Level Medium | **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | Honeypots / Cowrie / T-Pot / NMAP / Fail2Ban / Hydra / Análisis de ataques / OSINT de actores | **Impacto** | Monta un honeypot real y lo expone a internet: detecta ataques (brute force con hydra, bloqueo con Fail2Ban), analiza fingerprints del host y observa campañas reales (Mikrotik, Outlaw, WordPress) |

---

**Contexto:** Sala práctica de honeypots: configurar y desplegar un honeypot (de baja interacción, tipo Cowrie sobre T-Pot) para atraer y registrar ataques reales. Incluye la conexión al laboratorio, el análisis del host (CPU reportada `Intel(R) Core(TM) i9-11900KB CPU @ 3.30GHz`), la detección de ataques (15 observados, brute force con hydra y bloqueo vía Fail2Ban), fingerprints de red con nmap (`-O`) y el registro de actividad sin historial (`unset HISTFILE`). Se observan campañas reales contra Mikrotik (credencial root), botnet Outlaw y ataques a WordPress.

## Solucionario

### Task 1: Introducción a los Honeypots

**Explicación:** Conceptos de honeypot: qué son, por qué usarlos y dónde desplegarlos. No se requiere respuesta:

1. No answer needed

### Task 2: Tipos de Honeypots y Estrategias

**Explicación:** Clasificación de los honeypots (baja/alta interacción, producción/investigación) y estrategias de despliegue. No se requiere respuesta:

2. No answer needed

### Task 3: Funcionamiento de la Decepción

**Explicación:** Primeras preguntas de control sobre el concepto. Una respuesta es directamente verificable y la otra es de confirmación (Nay = No):

3. 1. No answer needed
   2. Nay

### Task 4: Preparando el Laboratorio

**Explicación:** Pasos de despliegue del honeypot. No se requiere respuesta:

4. No answer needed

### Task 5: Detectando los Primeros Ataques

**Explicación:** Resultados de la fase de observación del honeypot en internet:

5. 1. 15
   2. hydra
   3. Fail2Ban

### Task 6: Análisis del Host y Postura Defensiva

**Explicación:** Información del host objetivo, confirmación de preguntas y técnicas de trabajo:

6. 1. Intel(R) Core(TM) i9-11900KB CPU @ 3.30GHz
   2. Nay
   3. -O
   4. unset HISTFILE

### Task 7: Actividad Maliciosa Observada

**Explicación:** Campañas y actores registrados por el honeypot:

7. 1. Mikrotik
   2. root password
   3. Outlaw

### Task 8: Ataque a WordPress

**Explicación:** Observación de ataques dirigidos a CMS WordPress y confirmación (Nay):

8. 1. WordPress
   2. Nay

### Task 9: Conclusión

**Explicación:** Cierre y reflexión final de la sala. No se requiere respuesta:

9. No answer needed

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuántos ataques detectó el honeypot en el periodo observado? | `15` |
| 2 | ¿Qué herramienta usó el atacante para el brute force de credenciales? | `hydra` |
| 3 | ¿Qué herramienta detectó/bloqueó el ataque? | `Fail2Ban` |
| 4 | ¿Qué CPU reporta el host del laboratorio? | `Intel(R) Core(TM) i9-11900KB CPU @ 3.30GHz` |
| 5 | Pregunta de confirmación (Nay = No) | `Nay` |
| 6 | ¿Qué flag de nmap genera los OS fingerprints? | `-O` |
| 7 | ¿Qué comando evita que las órdenes queden registradas en el historial? | `unset HISTFILE` |
| 8 | ¿Qué dispositivo/producto fue objetivo del atacante? | `Mikrotik` |
| 9 | ¿Qué credencial intentaba adivinar el atacante? | `root password` |
| 10 | ¿Qué botnet/campaña se observó en los honeypots? | `Outlaw` |
| 11 | ¿Qué CMS fue objetivo de los ataques? | `WordPress` |
| 12 | Pregunta de confirmación del ataque WordPress | `Nay` |

---

**Metodología:**
1. Comprender el concepto y los tipos de honeypots.
2. Desplegar el honeypot en el laboratorio (Cowrie/T-Pot).
3. Exponerlo y recopilar los ataques recibidos.
4. Analizar el host y generar fingerprints de red con `nmap -O`.
5. Asegurar la sesión de análisis con `unset HISTFILE`.
6. Correlacionar la actividad observada (Mikrotik, root password, Outlaw, WordPress).

**Learning chain:** Tipos de honeypot → despliegue → 15 ataques → hydra → Fail2Ban → CPU del host → `-O` (fingerprint) → `unset HISTFILE` → Mikrotik → root password → Outlaw → WordPress

**Lección:** *Un honeypot convierte la telemetría pasiva en inteligencia activa: expones recursos cebo, dejas que los atacantes hagan su trabajo y obtienes TTPs, credenciales objetivo y campañas reales (como Outlaw sobre Mikrotik) sin poner en riesgo infraestructura productiva.*

**MITRE ATT&CK:** T1110 - Brute Force (hydra); T1046 - Network Service Discovery (nmap -O); T1190 - Exploit Public-Facing Application (honeypot de red); T1083 - File and Directory Discovery; T1071.001 - Application Layer Protocol: Web Protocols (campañas observadas)

**Fuente:** [TryHackMe - Introduction To Honeypots](https://tryhackme.com/room/introductiontohoneypots)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.