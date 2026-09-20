# Intro to Containerisation

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `introtocontainerisation` | https://tryhackme.com/room/introtocontainerisation | 01 Level Easy | TryHackMe | namespaces / Docker / imágenes / YAML / Docker Engine / contexto histórico (2013, PyCon, UNIX V7) / ps aux | Entender qué es la containerización, cómo los namespaces aíslan procesos y cómo Docker empaqueta, publica y despliega aplicaciones en contenedores. |

---

**Contexto:** La room introduce la containerización como primer capítulo de una serie. Explica por qué los contenedores son más ligeros que las máquinas virtuales (no llevan un SO completo), cómo el kernel aísla procesos con **namespaces**, qué es Docker (plataforma open source que permite empaquetar aplicaciones en **imágenes** y desplegarlas), el lenguaje **YAML** con el que se define la construcción y una breve historia: Docker se creó en **2013**, se presentó en **PyCon** y sus conceptos provienen de UNIX **V7**. Cierra con dos prácticas: ejecutar y containerizar la aplicación de un sitio estático.

> **ES:** Qué es la containerización y Docker: aislamiento con namespaces, imágenes y sintaxis YAML, historia (2013 / PyCon / UNIX V7), ejecución de procesos y prácticas de empaquetado con flags.
> **EN:** What containerisation and Docker are: isolation via namespaces, images and YAML syntax, history (2013 / PyCon / UNIX V7), running processes and practical packaging with flags.

## Solucionario

### Task 1: Introduction / Introducción

**Explicación:** Se presenta el concepto de contenedor y los objetivos de la serie de rooms sobre containerización. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Deploy the machine and read the introduction. / Despliega la máquina y lee la introducción. | `No answer needed` |

### Task 2: What is Containerisation? / ¿Qué es la containerización?

**Explicación:** La containerización se apoya en los **namespaces** del kernel: una feature que permite a los procesos usar los recursos del sistema operativo sin interactuar con otros procesos. En una configuración normal, los contenedores **no** pueden interactuar entre sí (**nay**), porque cada uno tiene su propio espacio aislado de procesos, red, sistema de archivos, etc. Además, los contenedores no ejecutan un SO completo por cada instancia, a diferencia de las máquinas virtuales.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the name of the kernel feature that allows for processes to use resources of the Operating System without being able to interact with other processes? / ¿Cómo se llama la feature del kernel que permite a los procesos usar recursos del SO sin poder interactuar con otros procesos? | `namespace` |
| 2 | In a normal configuration, can other containers interact with each other? (yay/nay) / En una configuración normal, ¿pueden los contenedores interactuar entre sí? (yay/nay) | `nay` |

### Task 3: Introducing Docker / Presentando Docker

**Explicación:** Docker es el motor de containerización open source más utilizado: unifica el empaquetado y despliegue de aplicaciones. Cuando una aplicación se publica con Docker pasada a ser **An Image** (una imagen: paquete con la aplicación, sus dependencias y la configuración de ejecución). Docker usa la abreviatura de sintaxis de programación **YAML** (YAML Ain't a Markup Language) para definir cómo se construye el contenedor y qué se ejecuta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What does an application become when it is published using Docker? (Format: An xxxxx) / ¿En qué se convierte una aplicación al publicarla con Docker? (Formato: An xxxxx) | `An Image` |
| 2 | What is the abbreviation of the programming syntax language that Docker uses? / ¿Cuál es la abreviatura del lenguaje de sintaxis de programación que usa Docker? | `YAML` |

### Task 4: The History of Docker / La historia de Docker

**Explicación:** Historia de la containerización: Docker fue creado originalmente en el año **2013** y se presentó por primera vez en **PyCon** (la conferencia de Python). Los conceptos de containerización más antiguos vienen de la versión **V7** de UNIX (años 70), donde ya se planteaba el aislamiento de procesos y del sistema de archivos.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | In what year was Docker originally created? / ¿En qué año se creó Docker originalmente? | `2013` |
| 2 | Where was Docker first showcased? / ¿Dónde se presentó Docker por primera vez? | `PyCon` |
| 3 | What version of Unix had the first concepts of containerisation? / ¿Qué versión de Unix tuvo los primeros conceptos de containerización? | `V7` |

### Task 5: How does Containerisation Work? / ¿Cómo funciona la containerización?

**Explicación:** Se explica internamente el aislamiento: a través de los namespaces del kernel, cada contenedor percibe un sistema operativo propio, y el Docker Engine interactúa directamente con el host. Se comparan los contenedores con alternativas como las máquinas virtuales para entender su ligereza. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Read the explanation of how containerisation works. / Lee la explicación de cómo funciona la containerización. | `No answer needed` |

### Task 6: Practical: Running the application / Práctica: ejecutar la aplicación

**Explicación:** En el laboratorio se despliega un entorno para visualizar la carga del sistema. Para demostrar carga de CPU y memoria se lanza un proceso y se inspecciona con **ps aux**, que lista todos los procesos en ejecución con su consumos.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | In our simple example to demonstrate CPU and Memory load, what command do we use to view the running processes? / En el ejemplo para demostrar la carga de CPU y memoria, ¿qué comando usamos para ver los procesos en ejecución? | `ps aux` |

### Task 7: Practical: Containerising the application / Práctica: containerizar la aplicación

**Explicación:** Se containeriza la aplicación del sitio estático desplegado: se prepara la imagen, se ejecuta el contenedor y se verifica que el servicio responde para obtener la flag.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Containerise the applications in the static site. What is the flag? / Containeriza las aplicaciones del sitio estático. ¿Cuál es la flag? | `THM{APPLICATION_SHIPPED}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the name of the kernel feature that allows for processes to use resources of the Operating System without being able to interact with other processes? | `namespace` |
| 2 | In a normal configuration, can other containers interact with each other? (yay/nay) | `nay` |
| 3 | What does an application become when it is published using Docker? (Format: An xxxxx) | `An Image` |
| 4 | What is the abbreviation of the programming syntax language that Docker uses? | `YAML` |
| 5 | In what year was Docker originally created? | `2013` |
| 6 | Where was Docker first showcased? | `PyCon` |
| 7 | What version of Unix had the first concepts of containerisation? | `V7` |
| 8 | In our simple example to demonstrate CPU and Memory load, what command do we use to view the running processes? | `ps aux` |
| 9 | Containerise the applications in the static site. What is the flag? | `THM{APPLICATION_SHIPPED}` |

---

**Metodología:** Concepto -> historia -> práctica: (1) entender el aislamiento por namespaces; (2) conocer la plataforma Docker, sus imágenes y sintaxis YAML; (3) situar el contexto histórico (2013, PyCon, UNIX V7); (4) ejecutar la aplicación y medir carga con `ps aux`; (5) containerizar el sitio estático y validar que sirve la flag.

### Cadena de ataque / Attack Chain

```text
namespaces (aislamiento de procesos) -> Docker Engine -> imagenes + YAML -> despliegue -> ps aux (verificación de carga) -> actualizacion del sitio estatico -> flag
```

**Learning chain:** Containers vs VMs -> namespaces -> Docker/images/YAML -> historia -> ps aux -> empaquetado -> flag.

**Lección:** *Un contenedor no es una mini-VM: comparte el kernel del host y su aislamiento depende de los namespaces; por eso es ligero, reproducible y seguro siempre que el último recurso, el kernel, esté sano.*

**MITRE ATT&CK:** T1610 (Deploy Container), T1525 (Implant Container Image), T1609 (Container Administration Command)

**Fuente:** [TryHackMe - Intro to Containerisation](https://tryhackme.com/room/introtocontainerisation)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.