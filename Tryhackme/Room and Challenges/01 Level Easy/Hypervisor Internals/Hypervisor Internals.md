# Hypervisor Internals

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `hypervisorinternals` | https://tryhackme.com/room/hypervisorinternals | 01 Level Easy | TryHackMe | Virtualización / hypervisores tipo 1 y 2 / Hyper-V / VirtualBox / vCPU / vNIC / nested virtualisation / CVEs | Comprender el funcionamiento interno de los hypervisores y su superficie de ataque. |

---

**Contexto:** Sala sobre el funcionamiento interno de los hypervisores: tipos de hypervisores (bare-metal tipo 1 y hospedados tipo 2), ejemplos como Hyper-V y VirtualBox, superficie de ataque (ransomware, costes asociados), componentes virtualizados (vCPU, vNIC, virtualización anidada) y CVEs conocidos, terminando con una flag.

> **ES:** Estudia los tipos de hypervisores, sus componentes virtuales y sus CVEs, y resuelve la práctica final para obtener la flag.
> **EN:** Study hypervisor types, their virtual components and CVEs, and solve the final challenge to get the flag.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Presentación del concepto de hypervisor y de la virtualización; tarea de lectura sin respuesta.

1. 1. No answer needed

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción a los hypervisores. | `No answer needed` |

### Task 2: Tipos de hypervisores / Types of Hypervisors

**Explicación:** Existen dos tipos de hypervisores: el tipo 1 (bare-metal, se ejecuta directamente sobre el hardware) y el tipo 2 (hospedado, se ejecuta sobre un sistema operativo).

1. 1. type 1
   2. type 2

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cómo se llama el hypervisor que se ejecuta directamente sobre el hardware? / What is the hypervisor that runs directly on the hardware called? | `type 1` |
| 2 | ¿Cómo se llama el hypervisor hospedado que se ejecuta sobre un sistema operativo? / What is the hosted hypervisor that runs on top of an OS called? | `type 2` |

### Task 3: Ejemplos / Examples

**Explicación:** Se identifican ejemplos reales: Hyper-V es el hypervisor de Microsoft y VirtualBox es el hypervisor hospedado de uso común en seguridad.

1. 1. Hyper-V
   2. VirtualBox

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el hypervisor de Microsoft? / What is Microsoft's hypervisor? | `Hyper-V` |
| 2 | ¿Qué hypervisor hospedado se usa habitualmente? / What hosted hypervisor is commonly used? | `VirtualBox` |

### Task 4: Superficie de ataque / Attack Surface

**Explicación:** Se analiza el valor económico de los objetivos virtualizados, el uso de la virtualización en investigación y la presencia de grupos de ransomware que se dirigen a entornos virtualizados.

1. 1. $250,000
   2. Research
   3. ALPHAV

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la cifra de coste o recompensa mencionada? / What is the cost or reward amount mentioned? | `$250,000` |
| 2 | ¿Para qué uso se menciona la virtualización? / What use of virtualization is mentioned? | `Research` |
| 3 | ¿Qué grupo de ransomware se cita? / What ransomware group is mentioned? | `ALPHAV` |

### Task 5: Componentes de la máquina virtual / VM Components

**Explicación:** Dentro de la VM se encuentran componentes virtualizados como la vCPU (procesador virtual), la vNIC (interfaz de red virtual) y la virtualización anidada (nested virtualisation).

1. 1. vCPU
   2. vNIC
   3. Nested virtualisation

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cómo se llama el procesador virtual de la VM? / What is the virtual CPU of the VM called? | `vCPU` |
| 2 | ¿Cómo se llama la interfaz de red virtual? / What is the virtual network interface called? | `vNIC` |
| 3 | ¿Cómo se llama la capacidad de ejecutar una VM dentro de otra? / What is the ability to run a VM inside another VM called? | `Nested virtualisation` |

### Task 6: CVEs y servicios / CVEs and Services

**Explicación:** Se estudian vulnerabilidades conocidas sobre hypervisores y los servicios responsables, como el fallo en VirtualBox y el servicio de VMware Tools.

1. 1. CVE-2018-2693
   2. VMware Tools Core Service

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué CVE de VirtualBox se menciona? / What VirtualBox CVE is mentioned? | `CVE-2018-2693` |
| 2 | ¿Qué servicio de VMware permite ejecución o escalada? / What VMware service allows execution or escalation? | `VMware Tools Core Service` |

### Task 7: Práctica / Practice

**Explicación:** Se resuelve la parte práctica de la sala, donde se obtiene la flag final.

1. 1. THM{LAYERS_UPON_LAYERS}

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag? / What is the flag? | `THM{LAYERS_UPON_LAYERS}` |

---

| Task | # | Pregunta | Respuesta |
|------|---|----------|-----------|
| 1 | 1 | Lee la introducción a los hypervisores. | `No answer needed` |
| 2 | 1 | ¿Cómo se llama el hypervisor que se ejecuta directamente sobre el hardware? / What is the hypervisor that runs directly on the hardware called? | `type 1` |
| 2 | 2 | ¿Cómo se llama el hypervisor hospedado que se ejecuta sobre un sistema operativo? / What is the hosted hypervisor that runs on top of an OS called? | `type 2` |
| 3 | 1 | ¿Cuál es el hypervisor de Microsoft? / What is Microsoft's hypervisor? | `Hyper-V` |
| 3 | 2 | ¿Qué hypervisor hospedado se usa habitualmente? / What hosted hypervisor is commonly used? | `VirtualBox` |
| 4 | 1 | ¿Cuál es la cifra de coste o recompensa mencionada? / What is the cost or reward amount mentioned? | `$250,000` |
| 4 | 2 | ¿Para qué uso se menciona la virtualización? / What use of virtualization is mentioned? | `Research` |
| 4 | 3 | ¿Qué grupo de ransomware se cita? / What ransomware group is mentioned? | `ALPHAV` |
| 5 | 1 | ¿Cómo se llama el procesador virtual de la VM? / What is the virtual CPU of the VM called? | `vCPU` |
| 5 | 2 | ¿Cómo se llama la interfaz de red virtual? / What is the virtual network interface called? | `vNIC` |
| 5 | 3 | ¿Cómo se llama la capacidad de ejecutar una VM dentro de otra? / What is the ability to run a VM inside another VM called? | `Nested virtualisation` |
| 6 | 1 | ¿Qué CVE de VirtualBox se menciona? / What VirtualBox CVE is mentioned? | `CVE-2018-2693` |
| 6 | 2 | ¿Qué servicio de VMware permite ejecución o escalada? / What VMware service allows execution or escalation? | `VMware Tools Core Service` |
| 7 | 1 | ¿Cuál es la flag? / What is the flag? | `THM{LAYERS_UPON_LAYERS}` |

---

**Metodología:** Estudio del material sobre virtualización, identificación de los tipos de hypervisores y sus componentes (vCPU, vNIC, nested), análisis de la superficie de ataque (costes, ransomware, investigación) y de los CVEs conocidos, y resolución de la práctica para obtener la flag.

### Cadena de ataque / Attack Chain

```text
tipos de hypervisor -> Hyper-V/VirtualBox -> componentes virtuales -> superficie de ataque -> CVE-2018-2693 -> VMware Tools -> flag
```

**Learning chain:** Virtualización -> hypervisores tipo 1/2 -> componentes virtuales -> CVEs -> flag.

**Lección:** *Comprender cómo se construyen las capas de virtualización (vCPU, vNIC, nested virtualisation) y conocer los CVEs de los hypervisores permite valorar correctamente el riesgo de cada entorno virtualizado.*

**MITRE ATT&CK:** T1068 (Exploitation for Privilege Escalation), T1005 (Data from Local System)

**Fuente:** [TryHackMe - Hypervisor Internals](https://tryhackme.com/room/hypervisorinternals)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
