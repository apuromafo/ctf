# Mobile Acquisition

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough (forense móvil) | `mobileacquisition` | https://tryhackme.com/room/mobileacquisition | 01 Level Easy | TryHackMe | Forense móvil / métodos de adquisición (física, lógica) / Android & iOS / ADB / idevicebackup2 / jailbreak | Introducción a la adquisición forense de dispositivos móviles: métodos de volcado, entornos de ejecución y herramientas clásicas. |

---

**Contexto:** Sala de forense digital centrada en la adquisición de dispositivos móviles (Android/iOS). Se explican los conceptos de punto de entrada (*Entrypoint*), el proceso de arranque seguro (*Secure Boot*), el papel del hardware, la diferencia entre tiendas de aplicaciones (Google Play) y malware (Pegasus), y los métodos de adquisición: física, lógica, `idevicebackup2` (iOS) y ADB (Android). También se cubren los procedimientos de *Custom Boot Loading* y *Jailbreaking* para acceder al dispositivo. Cierra con una flag temática.

> **ES:** Métodos de adquisición forense móvil: física vs. lógica, Android (ADB) e iOS (idevicebackup2), arranque seguro, jailbreak/root.
> **EN:** Mobile forensic acquisition methods: physical vs. logical, Android (ADB) and iOS (idevicebackup2), secure boot, jailbreak/rooting.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Presentación de la sala: por qué es importante la adquisición forense de dispositivos móviles. Tarea de lectura sin respuesta.

Contenido original de la tarea / Original task content:

```text
1. No answer needed
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee el contenido de la tarea. / Read the task content. | `No answer needed` |

### Task 2: Punto de partida / Entry point

**Explicación:** Se identifica dónde se realiza el análisis y cuál es el punto de entrada del caso forense. Las respuestas son la ubicación del volcado/dónde empieza la investigación (`South Africa`) y el término que designa el punto de entrada en el flujo de adquisición (`Entrypoint`).

Contenido original de la tarea / Original task content:

```text
2. 1. South Africa
   2. Entrypoint
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Ubicación del caso / Location of the case | `South Africa` |
| 2 | Punto de entrada del flujo / Entry point of the flow | `Entrypoint` |

### Task 3: Arranque seguro y hardware / Secure boot & hardware

**Explicación:** Se repasa la cadena de confianza del dispositivo móvil: el mecanismo que valida el sistema en cada arranque es el proceso de arranque seguro (*Secure boot process*), y el componente del dispositivo donde se ancla dicha verificación es el *hardware*.

Contenido original de la tarea / Original task content:

```text
3. 1. Secure boot process
   2. hardware
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Mecanismo de validación en el arranque / Boot validation mechanism | `Secure boot process` |
| 2 | Componente donde se ancla la verificación / Component where verification is anchored | `hardware` |

### Task 4: Apps y amenazas / Apps & threats

**Explicación:** Se comparan las fuentes legítimas de software y las amenazas móviles: la tienda oficial de Android es `Google Play`, y el spyware de referencia citado en la sala es `Pegasus`.

Contenido original de la tarea / Original task content:

```text
4. 1. Google Play
   2. Pegasus
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Tienda oficial de Android / Official Android store | `Google Play` |
| 2 | Spyware de referencia / Reference spyware | `Pegasus` |

### Task 5: Métodos de adquisición / Acquisition methods

**Explicación:** Se presentan las técnicas de obtención de evidencia: adquisición `Physical` (volcado bit a bit) y `Logical Acquisition` (solo archivos accesibles por el SO), junto con las herramientas según plataforma: `idevicebackup2` para iOS y `ADB` para Android.

Contenido original de la tarea / Original task content:

```text
5. 1. Physical
   2. Logical Acquisition
   3. idevicebackup2
   4. ADB
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Método de adquisición física / Physical acquisition method | `Physical` |
| 2 | Método de adquisición lógica / Logical acquisition method | `Logical Acquisition` |
| 3 | Herramienta de adquisición iOS / iOS acquisition tool | `idevicebackup2` |
| 4 | Herramienta de adquisición Android / Android acquisition tool | `ADB` |

### Task 6: Acceso avanzado al dispositivo / Custom boot & jailbreak

**Explicación:** Para desbloquear capacidades de adquisición avanzadas se utilizan cargas de arranque personalizadas (`Custom Boot Loading`) y el proceso de eliminación de restricciones de iOS: el `Jailbreaking`.

Contenido original de la tarea / Original task content:

```text
6. 1. Custom Boot Loading
   2. Jailbreaking
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Carga de arranque personalizada / Custom boot loading | `Custom Boot Loading` |
| 2 | Eliminación de restricciones en iOS / iOS restriction removal | `Jailbreaking` |

### Task 7: Flag de la sala / Room flag

**Explicación:** Al completar las tareas de la sala se entrega la flag temática de adquisición móvil.

Contenido original de la tarea / Original task content:

```text
7. THM{MOBILE_ACQUISITION}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag de la sala / Room flag | `THM{MOBILE_ACQUISITION}` |

### Task 8: Conclusión / Conclusion

**Explicación:** Cierre de la sala recapitulando los métodos de adquisición forense móvil. Tarea de lectura sin respuesta.

Contenido original de la tarea / Original task content:

```text
8. No answer needed
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee el contenido de la tarea. / Read the task content. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Ubicación del caso / Location of the case | `South Africa` |
| 2 | Punto de entrada del flujo / Entry point of the flow | `Entrypoint` |
| 3 | Mecanismo de validación en el arranque / Boot validation mechanism | `Secure boot process` |
| 4 | Componente donde se ancla la verificación / Component where verification is anchored | `hardware` |
| 5 | Tienda oficial de Android / Official Android store | `Google Play` |
| 6 | Spyware de referencia / Reference spyware | `Pegasus` |
| 7 | Método de adquisición física / Physical acquisition method | `Physical` |
| 8 | Método de adquisición lógica / Logical acquisition method | `Logical Acquisition` |
| 9 | Herramienta de adquisición iOS / iOS acquisition tool | `idevicebackup2` |
| 10 | Herramienta de adquisición Android / Android acquisition tool | `ADB` |
| 11 | Carga de arranque personalizada / Custom boot loading | `Custom Boot Loading` |
| 12 | Eliminación de restricciones en iOS / iOS restriction removal | `Jailbreaking` |
| 13 | Flag de la sala / Room flag | `THM{MOBILE_ACQUISITION}` |

---

**Metodología:** Seguir el flujo de la adquisición forense: determinar el punto de entrada del caso, comprender la cadena de arranque seguro anclada en hardware, distinguir fuentes legítimas (Google Play) de amenazas (Pegasus), elegir entre adquisición física y lógica con las herramientas adecuadas (ADB en Android, idevicebackup2 en iOS) y habilitar accesos avanzados mediante Custom Boot Loading y Jailbreaking.

### Cadena de ataque / Attack Chain

```text
Entrypoint del caso -> Secure boot process (hardware) -> fuentes de apps (Google Play vs Pegasus) -> Physical vs Logical Acquisition -> ADB / idevicebackup2 -> Custom Boot Loading / Jailbreaking -> flag
```

**Learning chain:** Forense móvil -> entrada del caso -> arranque seguro/hardware -> amenazas (Pegasus) -> adquisición física/lógica -> ADB e idevicebackup2 -> jailbreak/root.

**Lección:** *Cada método de adquisición móvil (física, lógica, backup) tiene un alcance distinto sobre la evidencia; elegirlo bien depende del estado del dispositivo y de las herramientas disponibles.* 

**MITRE ATT&CK:** T1560 (Archive Collected Data), T1074 (Data Staged)

**Fuente:** [TryHackMe - Mobile Acquisition](https://tryhackme.com/room/mobileacquisition)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.