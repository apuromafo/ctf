# Intro to Threat Emulation

| **Dificultad** | MEDIUM | **Tipo** | Free | **Slug** | `introtothreatemulation` |
| **Link** | [TryHackMe](https://tryhackme.com/room/introtothreatemulation) | **Sección** | 02 Level Medium | **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | Threat Emulation / Threat Simulation / MITRE CALDERA / Atomic Red Team / Adversary Emulation / Blue Team | **Impacto** | Ejercita el ciclo completo de emulación de amenazas: del marco conceptual (emulación vs simulación) a operaciones reales con CALDERA contra objetivos Linux y Windows, resolviendo flags THM |

---

**Contexto:** Sala que introduce la emulación de amenazas como disciplina de seguridad: recrear los pasos (TTPs) de adversarios reales con herramientas como MITRE CALDERA y Atomic Red Team, en lugar de solo "simular" el comportamiento esperado de un atacante genérico. Recorre el ciclo de emulación (Preparation → ejecución), analiza la complejidad de TTPs del adversario (AdFind, Cobalt Strike, Mimikatz), define el Scope y termina lanzando operaciones CALDERA contra objetivos Linux y Windows, donde se capturan flags `THM{...}`.

## Solucionario

### Task 1: Introducción a la Emulación de Amenazas

**Explicación:** Primera toma de contacto con el concepto de emulación de amenazas y con la plataforma MITRE CALDERA (#1 en emulación). No se requiere respuesta en esta tarea:

1. No answer needed

### Task 2: Emulación vs Simulación

**Explicación:** Diferencia conceptual clave entre ambas disciplinas:

2. 1. Threat Emulation
   2. Threat simulation

### Task 3: El Ciclo de Emulación

**Explicación:** Fases del proceso de emulación y sus motores/paquetes:

3. 1. Preparation
   2. Atomic Red Team

### Task 4: Complejidad de TTPs del Adversario

**Explicación:** Las herramientas del adversario emulado y el concepto que mide la dificultad de reproducir sus TTPs:

4. 1. AdFind, Cobalt Strike, Mimikatz
   2. TTP Complexity

### Task 5: Operación contra el Objetivo Linux (CALDERA)

**Explicación:** Usando los agentes de CALDERA se configura el Scope y se ejecuta la operación sobre la víctima Linux, obteniendo dos flags:

5. 1. Scope
   2. THM{C4RB0N_$P1D3R_1$_F1N7}
   3. THM{3$P1ON4G3_F0R_R34P3R}

### Task 6: Operación contra el Objetivo Windows (CALDERA)

**Explicación:** Nueva operación emulada contra la víctima Windows (defensa y refuerzo del objetivo), con sus respectivos flags:

6. 1. THM{D3F3NC3_1N_3MUL4T10N}
   2. THM{S3CUR3_4LL_W3B_4553T5}

### Task 7: Conclusión

**Explicación:** Cierre y repaso de la sala. No se requiere respuesta:

7. No answer needed

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cómo se llama el proceso de reproducir el comportamiento de un adversario? | `Threat Emulation` |
| 2 | ¿Cómo se llama el proceso que modela el comportamiento esperado de un adversario? | `Threat simulation` |
| 3 | ¿Cuál es la primera fase del ciclo de emulación? | `Preparation` |
| 4 | ¿Qué motor/kit de pruebas se usa dentro del ciclo? | `Atomic Red Team` |
| 5 | ¿Qué conjunto de herramientas usa el adversario emulado? | `AdFind, Cobalt Strike, Mimikatz` |
| 6 | ¿Qué concepto indica la dificultad de reproducir un TTP? | `TTP Complexity` |
| 7 | ¿Cuál es el Scope de la operación LAB-VM? | `Scope` |
| 8 | Flag de la operación Linux 1 | `THM{C4RB0N_$P1D3R_1$_F1N7}` |
| 9 | Flag de la operación Linux 2 | `THM{3$P1ON4G3_F0R_R34P3R}` |
| 10 | Flag de la operación Windows 1 | `THM{D3F3NC3_1N_3MUL4T10N}` |
| 11 | Flag de la operación Windows 2 | `THM{S3CUR3_4LL_W3B_4553T5}` |

---

**Metodología:**
1. Entender la diferencia entre emulación y simulación de amenazas.
2. Recorrer el ciclo de emulación empezando por la fase de Preparation.
3. Mapear las herramientas del adversario (AdFind, Cobalt Strike, Mimikatz) y su TTP Complexity.
4. Definir el Scope de la operación CALDERA.
5. Ejecutar la operación de emulación sobre el target Linux y capturar los flags.
6. Ejecutar la operación sobre el target Windows y capturar los flags.

**Learning chain:** Emulación vs simulación → Preparation → Atomic Red Team → AdFind/Cobalt Strike/Mimikatz → TTP Complexity → Scope → operación CALDERA sobre Linux → flags → operación CALDERA sobre Windows → flags

**Lección:** *Emular amenazas es reconstruir el camino concreto de un adversario real, no un ataque genérico: con la preparación adecuada, un Scope claro y herramientas como CALDERA, el equipo proactivo puede validar sus defensas midiendo la complejidad de cada TTP antes de que el atacante real llegue.*

**MITRE ATT&CK:** T1087.002 - Account Discovery: Domain Account (AdFind); T1219 - Remote Access Software (Cobalt Strike); T1003.001 - OS Credential Dumping: LSASS Memory (Mimikatz); T1204.002 - User Execution: Malicious File; T1059 - Command and Scripting Interpreter

**Fuente:** [TryHackMe - Intro to Threat Emulation](https://tryhackme.com/room/introtothreatemulation)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.