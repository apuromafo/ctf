# Weaponization

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Medium | Defensa / Red Team (Weaponization) | weaponization | https://tryhackme.com/room/weaponization | 02 Level Medium | TryHackMe | MSFvenom, Windows payloads, Veil, Container Discovery | Media - fase de armado de malware |

> **Objeto:** Completar el módulo de weaponization: generar un ejecutable malicioso, evitar detección y determinar el método de despliegue en medios removibles.

---

**Contexto:** Habitación de introducción a la fase de weaponization del kill chain. Se aprende a generar payloads para Windows con MSFvenom, a compilar binarios con mingw-w64 y a evadir AV con Veil, además de identificar métodos de propagación como USB Delivery.

> **ES:** Laboratorio de armado de malware y evasión de antivirus.
> **EN:** Malware weaponization and antivirus evasion lab.

## Solucionario

### Task 1: Configuración / Setup

**Explicación:** Preparar la infraestructura necesaria (máquinas Kali/Windows, directorios de trabajo) para el laboratorio.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Interactuar con el laboratorio? / Do we need to interact? | No answer needed |

### Task 2: Descargar el binario / Download the binary

**Explicación:** Obtener el binario de entrega inicial que se analizará en las siguientes tareas.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Interactuar con el laboratorio? / Do we need to interact? | No answer needed |

### Task 3: Analizar el binario / Analyze the binary

**Explicación:** Examinar el ejecutable con herramientas de análisis estático/dinámico para entender su comportamiento.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Interactuar con el laboratorio? / Do we need to interact? | No answer needed |

### Task 4: Evasión con Veil / Veil evasion

**Explicación:** Generar un payload evasivo con Veil-Evasion para saltarse la detección del antivirus.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Interactuar con el laboratorio? / Do we need to interact? | No answer needed |

### Task 5: MSFvenom Windows / MSFvenom Windows payload

**Explicación:** Crear un ejecutable para Windows con `msfvenom -p windows/meterpreter/reverse_tcp`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Interactuar con el laboratorio? / Do we need to interact? | No answer needed |

### Task 6: Compilar con mingw / mingw compilation

**Explicación:** Compilar el payload en Windows mediante cross-compilation con `mingw-w64`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Interactuar con el laboratorio? / Do we need to interact? | No answer needed |

### Task 7: Clasificación del antivirus / Antivirus classification

**Explicación:** Comprobar la clasificación del binario por el antivirus y anotar el resultado del laboratorio.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Interactuar con el laboratorio? / Do we need to interact? | No answer needed |

### Task 8: Método de despliegue / Deployment method

**Explicación:** Determinar qué técnica de distribución de malware usa la inserción en dispositivos de almacenamiento extraíbles.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Qué método de despliegue usa medios removibles? / Which deployment method uses removable media? | USB Delivery |

### Task 9: Flag final / Final flag

**Explicación:** Localizar el contenedor/instancia comprometida y leer la flag final del laboratorio.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Cuál es la flag final? / What is the final flag? | THM{b4dbc2f16afdfe9579030a929b799719} |

---

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | ¿Interactuar con el laboratorio? / Do we need to interact? | `No answer needed` |
| 2 | ¿Interactuar con el laboratorio? / Do we need to interact? | `No answer needed` |
| 3 | ¿Interactuar con el laboratorio? / Do we need to interact? | `No answer needed` |
| 4 | ¿Interactuar con el laboratorio? / Do we need to interact? | `No answer needed` |
| 5 | ¿Interactuar con el laboratorio? / Do we need to interact? | `No answer needed` |
| 6 | ¿Interactuar con el laboratorio? / Do we need to interact? | `No answer needed` |
| 7 | ¿Interactuar con el laboratorio? / Do we need to interact? | `No answer needed` |
| 8 | ¿Qué método de despliegue usa medios removibles? / Which deployment method uses removable media? | `USB Delivery` |
| 9 | ¿Cuál es la flag final? / What is the final flag? | `THM{b4dbc2f16afdfe9579030a929b799719}` |

---

**Metodología:**

1. Preparación del entorno de laboratorio.
2. Descarga y análisis del binario de entrega.
3. Evasión de antivirus con Veil-Evasion.
4. Generación de payloads con MSFvenom para Windows.
5. Compilación con mingw-w64 y clasificación AV.
6. Identificación del método de despliegue (USB Delivery) y captura de la flag.

### Cadena de ataque / Attack Chain

```text
Weaponization -> MSFvenom payload -> Veil/Mingw -> Evasión AV -> USB Delivery -> Ejecución en Windows -> Flag
```

**Learning chain:**

- La fase de weaponization convierte un exploit en un arma operativa.
- Evadir AV requiere modificar firmas (Veil) o recompilar (mingw).
- El método de despliegue determina la superficie de infección (USB Delivery).

**Lección:** *La ofuscación y el reempaquetado son la clave para superar el antivirus en la fase de armado.*

**MITRE ATT&CK:**
- T1204.002 - User Execution: Malicious File
- T1192 - Supply Chain Compromise / Distribution
- T1059 - Command and Scripting Interpreter

**Fuente:** [TryHackMe - Weaponization](https://tryhackme.com/room/weaponization)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.