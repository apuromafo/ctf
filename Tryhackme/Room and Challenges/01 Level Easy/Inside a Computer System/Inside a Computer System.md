# Inside a Computer System

| **Dificultad** | Easy |
| **Tipo** | Walkthrough |
| **Slug** | `insideacomputer` |
| **Link** | [TryHackMe](https://tryhackme.com/room/insideacomputer) |
| **Sección** | 01 Level Easy |
| **Fuente** | Redacción oficial de TryHackMe + dos ejercicios estáticos interactivos |
| **Componentes** | Hardware de un ordenador (CPU, RAM, almacenamiento, GPU, placa...) / proceso de arranque (POST → BIOS/UEFI → boot loader → OS) |
| **Impacto** | Fundamentos teóricos; conocer los componentes y el arranque de un sistema es requisito para montar entornos de análisis, entender el *bootkit* y debugging de bajo nivel. |

---

**Contexto:** Un ordenador es un sistema de componentes que trabajan juntos: la **CPU** ejecuta instrucciones, la **RAM** guarda datos efímeros en uso, el **almacenamiento** (SSD/HDD) persiste los datos, la **GPU** renderiza gráficos, y la **placa base** los conecta con el resto (chipset, BIOS/UEFI, buses, fuente de alimentación). El **proceso de arranque** comienza con el **POST** (Power-On Self-Test), luego el firmware **BIOS/UEFI** carga el **boot loader** desde el disco, y este arranca el **sistema operativo**. El room usa dos simuladores estáticos: uno para identificar los componentes con sus nombres, otro para ordenar las fases del arranque.

## Solucionario

### Task 1: Introducción

**Explicación:** Parte de la ruta Pre Security; habla del hardware de un PC y de su arranque. Sin respuesta requerida.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed - let's get started. | `No answer needed` |

### Task 2: Dentro de un Sistema Informático (Inside a Computer System)

**Explicación:** Simulador (static-site) donde debes identificar cada componente de un PC (CPU, RAM, placa base, GPU, PSU, almacenamiento), típicamente arrastrando el nombre del componente sobre su silueta en el diagrama. Al completarlo: `THM{4llpccomp0n3nts1d3nt1f13d}` ("all pc components identified").

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Give in the flag you received after completing the exercise on the static site. | `THM{4llpccomp0n3nts1d3nt1f13d}` |

### Task 3: ¿Qué Pasa al Pulsar el Botón de Encendido? (What Happens When You Press the Start Button?)

**Explicación:** Simulador (static-site) donde se ordenan las fases del arranque en la secuencia correcta: **POST** (comprueba el hardware) → **BIOS/UEFI** (inicializa el firmware, localiza el disco de arranque) → **Boot Loader** (carga el kernel/OS desde el sector de arranque) → **Sistema Operativo** (toma el control y muestra la sesión). Al ordenarlo: `THM{pc5ucce55fully5t4rt3d}` ("pc successfully started").

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag that you received after completing the exercise? | `THM{pc5ucce55fully5t4rt3d}` |

### Task 4: Conclusión

**Explicación:** Enlaza con el siguiente bloque del path (tipos de sistemas: PC, servidores, móviles...). Sin respuesta requerida.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed - ready to discover the different types of computer systems. | `No answer needed` |

---

**Metodología:**
1. Completar el simulador de componentes arrastrando cada nombre a su hueco → flag `THM{4llpccomp0n3nts1d3nt1f13d}`.
2. En el simulador de arranque, ordenar: POST → firmware (BIOS/UEFI) → boot loader → OS → flag `THM{pc5ucce55fully5t4rt3d}`.
3. Ambos flags se recolectan directamente del lab estático (sin máquina).

**Learning chain:** Componentes: CPU + RAM + Almacenamiento + GPU + Placa base + PSU → identificarlos en el simulador → THM{4llpccomp0n3nts1d3nt1f13d}. Arranque: POST → BIOS/UEFI → Boot Loader → OS → ordenar fases → THM{pc5ucce55fully5t4rt3d}.

**Lección:** *Antes de proteger un sistema, hay que saber cómo se enciende y de qué está hecho.* POST, firmware y boot loader son el primer y último lugar donde una amenaza puede afianzarse.

**MITRE ATT&CK:** T1542 (Pre-OS Boot), T1542.003 (Bootkit) — entender el orden de arranque es el requisito para defender/detectar bootkits. El room es teórico.

**Fuente:** [TryHackMe - Inside a Computer System](https://tryhackme.com/room/insideacomputer)