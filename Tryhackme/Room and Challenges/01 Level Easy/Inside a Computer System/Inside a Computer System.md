# Inside a Computer System [EASY]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** EASY
* **Tipo / Type:** Walkthrough (Free)
* **Slug:** `insideacomputer`
* **Link:** https://tryhackme.com/room/insideacomputer
* **Sección / Section:** 01 Level Easy
* **Fuente / Source:** Redacción oficial de TryHackMe + dos ejercicios estáticos interactivos
* **Componentes:** Hardware de un ordenador (CPU, RAM, almacenamiento, GPU, placa...) · proceso de arranque (POST → BIOS/UEFI → boot loader → OS)
* **Impacto rol:** Fundamentos teóricos; conocer los componentes y el arranque de un sistema es requisito para montar entornos de análisis, entender el *bootkit* y debugging de bajo nivel.

## Solucionario de Tareas / Task Solutions

> **ES:** Un ordenador es un sistema de componentes que trabajan juntos: la **CPU** ejecuta instrucciones, la **RAM** guarda datos efímeros en uso, el **almacenamiento** (SSD/HDD) persiste los datos, la **GPU** renderiza gráficos, y la **placa base** los conecta con el resto (chipset, BIOS/UEFI, buses, fuente de alimentación). El **proceso de arranque** comienza con el **POST** (Power-On Self-Test), luego el firmware **BIOS/UEFI** carga el **boot loader** desde el disco, y este arranca el **sistema operativo**. El room usa dos simuladores estáticos: uno para identificar los componentes con sus nombres, otro para ordenar las fases del arranque.
> **EN:** A computer is a set of components working together: the **CPU** executes instructions, **RAM** holds in-use volatile data, storage (SSD/HDD) persists data, the **GPU** renders graphics, and the **motherboard** ties it all together (chipset, BIOS/UEFI, buses, PSU). The **boot process** starts with the **POST** (Power-On Self-Test), then the **BIOS/UEFI** firmware loads the **boot loader** from the disk, which starts the **operating system**. The room uses two static simulators: one to identify components by name, another to order the boot phases.

### Task 1 — Introducción / Introduction

* **Check:** `Let's get started!`
* **ES:** Parte de la ruta Pre Security; habla del hardware de un PC y de su arranque.
* **EN:** Part of the Pre Security path; covers PC hardware and booting.

### Task 2 — Dentro de un Sistema Informático / Inside a Computer System *(static-site)*

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Give in the flag you received after completing the exercise on the static site. | `THM{4llpccomp0n3nts1d3nt1f13d}` |

* **Ejercicio / Exercise:** simulador donde debes identificar cada componente de un PC (CPU, RAM, placa base, GPU, PSU, almacenamiento). Al completarlo: `THM{4llpccomp0n3nts1d3nt1f13d}` ("all pc components identified").
* **Nota / Note:** típicamente se hace por arrastrar el nombre del componente sobre su silueta en el diagrama.

### Task 3 — ¿Qué Pasa al Pulsar el Botón de Encendido? / What Happens When You Press the Start Button? *(static-site)*

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the flag that you received after completing the exercise? | `THM{pc5ucce55fully5t4rt3d}` |

* **Ejercicio / Exercise:** ordenar las fases del arranque en la secuencia correcta (POST → BIOS/UEFI → boot loader → OS). Al ordenarlo: `THM{pc5ucce55fully5t4rt3d}` ("pc successfully started").
* **Secuencia / Sequence:** **POST** (comprueba el hardware) → **BIOS/UEFI** (inicializa el firmware, localiza el disco de arranque) → **Boot Loader** (carga el kernel/OS desde el sector de arranque) → **Sistema Operativo** (toma el control y muestra la sesión).

### Task 4 — Conclusión / Conclusion

* **Check:** `I am ready to discover the different types of computer systems and their function!`
* **ES:** Enlaza con el siguiente bloque del path (tipos de sistemas: PC, servidores, móviles...).
* **EN:** Links to the next path block (system types: PCs, servers, mobile...).

## Metodología / Methodology

1. **Paso / Step:** Completar el simulador de componentes arrastrando cada nombre a su hueco → flag 1.
2. **Paso / Step:** En el simulador de arranque, ordenar: POST → firmware (BIOS/UEFI) → boot loader → OS → flag 2.
3. **Paso / Step:** Ambos flags se recolectan directamente del lab estático (sin máquina).

### Cadena de aprendizaje / Learning Chain

```
Componentes: CPU + RAM + Almacenamiento + GPU + Placa base + PSU
  -> identificarlos en el simulador  -> THM{4llpccomp0n3nts1d3nt1f13d}
Arranque: POST -> BIOS/UEFI -> Boot Loader -> OS
  -> ordenar fases                   -> THM{pc5ucce55fully5t4rt3d}
```

**Mapeo MITRE ATT&CK / relacionado:** T1542 (Pre-OS Boot: BIOS/Secure Boot) y T1542.003 (Bootkit) — entender el orden de arranque es el requisito para defender/detectar bootkits; T1497 no aplica. El room es teórico.

**Lección:** *Antes de proteger un sistema, hay que saber cómo se enciende y de qué está hecho.* POST, firmware y boot loader son el primer y último lugar donde una amenaza puede afianzarse.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.