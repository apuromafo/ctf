# Intro to IaC

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `introtoiac` | https://tryhackme.com/room/introtoiac | 01 Level Easy | TryHackMe | IaC / características (Repeatable, Versionable, Scalable) / declarativo vs imperativo / CloudFormation-Ansible-Terraform / CI/CD / virtualización (contenedores, hipervisores) / on-prem vs cloud | Comprender la Infraestructura como Código: características, tipos de herramientas, integración con CI/CD, virtualización y diferencias on-prem vs cloud, con dos laboratorios de flags. |

---

**Contexto:** La room introduce la Infraestructura como Código (IaC). Cubre las características clave (**Repeatable, Versionable, Scalable**), la diferencia entre herramientas declarativas e imperativas, el enfoque en caso práctico de CyberMyne (fases de guía del desarrollo de infraestructura y buenas prácticas: **Repeatable** y **Continual**, con **Rollback** como resultado de Monitoring/Maintenance), la relación con la virtualización (**Containerisation, Hypervisor, Resource Isolation, Kubernetes**), el debate on-prem vs cloud (**cloud service provider**, **scalability**) y dos laboratorios: recuperar las coordenadas (`thm{l4b_C0mpl3x_co0rds}`) y la flag final (`thm{1Nfr4StrUctUr3_Pr0}`).

> **ES:** Infraestructura como Codigo: caracteristicas IaC, herramientas declarativas/imperativas, CI/CD, virtualizacion y comparativa on-prem vs cloud, con dos labs de flags.
> **EN:** Infrastructure as Code: IaC characteristics, declarative vs imperative tools, CI/CD, virtualisation and on-prem vs cloud comparison, with two flag labs.

## Solucionario

### Task 1: Introduction / Introducción

**Explicación:** Presentación de la room: qué es IaC, por qué importa (automatización, consistencia, versionado) y el entorno de práctica de CyberMyne. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | I am ready to learn about IaC! / Estoy listo para aprender sobre IaC. | `No answer needed` |

### Task 2: IaC - The Concept / IaC - El concepto

**Explicación:** Las tres características esenciales de la IaC que agilizan el aprovisionamiento de infraestructura: **Repeatable** (se repite el mismo proceso de aprovisionamiento de forma fiable y sin pasos manuales propensos a error), **Versionable** (permite volver a la última versión funcional conocida de una configuración, como se haría con código) y **Scalable** (permite aumentar los recursos ante el crecimiento de la demanda).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which IaC characteristic will streamline the provisioning of infrastructure deployed at enterprise scale by removing error-prone manual steps? / ¿Qué característica de IaC agiliza el aprovisionamiento de infraestructura a escala empresarial eliminando pasos manuales propensos a error? | `Repeatable` |
| 2 | Which IaC characteristic allows us to go back to the last known working version of our configuration? / ¿Qué característica de IaC permite volver a la última versión funcional conocida de la configuración? | `Versionable` |
| 3 | Which IaC characteristic enables us to increase the resources when the traffic demand grows? / ¿Qué característica de IaC permite aumentar los recursos cuando crece la demanda de tráfico? | `Scalable` |

### Task 3: IaC - The Tools Part 1 / IaC - Las herramientas, parte 1

**Explicación:** Presentación de las categorías de herramientas. En el escenario dado (una ruta con coordenadas hasta un punto objetivo X), **Declarative** es el tipo de herramienta que considera dónde estás en el mapa y da instrucciones para llegar al punto X deseado, definiendo el estado final en lugar del procedimiento para alcanzarlo.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | In the scenario given, which type of IaC tool considers where you are on the map and gives instructions to reach the desired X point? / En el escenario dado, ¿qué tipo de herramienta IaC considera dónde estás en el mapa y da instrucciones para llegar al punto X deseado? | `Declarative` |

### Task 4: IaC - The Tools Part 2 / IaC - Las herramientas, parte 2

**Explicación:** Repaso de herramientas concretas (Terraform, Ansible, CloudFormation...) y un mini-laboratorio: navegando por el entorno se deben recuperar las coordenadas (ubicación) para obtener la flag.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Can you retrieve the location and retrieve the flag? / ¿Puedes recuperar la ubicación y obtener la flag? | `thm{l4b_C0mpl3x_co0rds}` |

### Task 5: IaC & Continuous Integration / IaC & Continuous Integration (CI/CD)

**Explicación:** Papel de la IaC en el ciclo CI/CD en el caso de CyberMyne. Las fases que proporcionan guía durante el desarrollo o la configuración de la infraestructura son de tipo **Repeatable**; las que aseguran buenas prácticas a lo largo del desarrollo y la gestión son de tipo **Continual**. La fase continual de Monitoring/Maintenance puede disparar la fase continual de **Rollback** (volver a un estado funcional previo si el resultado no es el esperado).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | A DevSecOps Engineer at CyberMyne is looking for guidance on developing their next infrastructure. What type of phases provide guidance during the development or configuration of an infrastructure? / Un DevSecOps de CyberMyne busca guía para desarrollar su próxima infraestructura. ¿Qué tipo de fases proporcionan guía durante el desarrollo o la configuración? | `Repeatable` |
| 2 | What type of phases ensure best practices throughout infrastructure development and management? / ¿Qué tipo de fases aseguran las buenas prácticas a lo largo del desarrollo y la gestión de la infraestructura? | `Continual` |
| 3 | The 'Monitoring/Maintenance' continual phase can trigger which other continual phase? / La fase continual de 'Monitoring/Maintenance' puede disparar ¿qué otra fase continual? | `Rollback` |

### Task 6: Virtualisation & IaC / Virtualización e IaC

**Explicación:** Relación entre virtualización e IaC según los distintos niveles de abstracción: a nivel de aplicación se usa **Containerisation**; cuando la infraestructura necesita una capa completa del sistema se emplea un **Hypervisor**; la **Resource Isolation** se usa para que el consumo de recursos de un componente no afecte al rendimiento del resto; y para automatizar el orquestado de contenedores a escala se utiliza **Kubernetes**.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | At the application level, what level of virtualisation would be needed to package and run the application? / A nivel de aplicación, ¿qué nivel de virtualización se necesita para empaquetar y ejecutar la aplicación? | `Containerisation` |
| 2 | When the operating system and the entire machine need to be virtualised, which level of virtualisation would be needed? / Cuando hay que virtualizar el sistema operativo y la máquina completa, ¿qué nivel de virtualización se necesita? | `Hypervisor` |
| 3 | Which 'Use of IaC' will ensure that this resource consumption won't affect the performance of the machine's other components? / ¿Qué uso de IaC garantiza que el consumo de recursos no afecte al rendimiento de los demás componentes de la máquina? | `Resource Isolation` |
| 4 | Which container orchestration software can be used to automate this process? / ¿Qué software de orquestación de contenedores puede usarse para automatizar este proceso? | `Kubernetes` |

### Task 7: On-Prem IaC vs. Cloud-Based IaC / IaC on-prem vs. basada en la nube

**Explicación:** Comparativa de responsabilidad y límites. En los entornos cloud los recursos se aprovisionan en la infraestructura del proveedor: la infraestructura subyacente la gestiona el **cloud service provider** (proveedor del servicio en la nube). La infraestructura on-prem, limitada por el hardware físico, sufre especialmente en la categoría de **scalability** (escalabilidad) cuando crece el tráfico.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Cloud-based resources are provisioned / configured in a cloud environment. Who handles the underlying infrastructure? / Los recursos cloud se aprovisionan en el entorno de la nube. ¿Quién gestiona la infraestructura subyacente? | `cloud service provider` |
| 2 | What category does on-prem infrastructure struggle with due to hardware limitations when facing increased traffic? / ¿En qué categoría sufre la infraestructura on-prem por las limitaciones de hardware al aumentar el tráfico? | `scalability` |

### Task 8: Practical / Práctica (Final Lab)

**Explicación:** Laboratorio final donde se ponen en práctica las habilidades de Infraestructura como Código en el entorno desplegado: explorar, aprovisionar y resolver el ejercicio para obtener la flag.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Can you get the flag using your infrastructure as code skills? / ¿Puedes obtener la flag usando tus habilidades de infraestructura como código? | `thm{1Nfr4StrUctUr3_Pr0}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which IaC characteristic will streamline the provisioning of infrastructure deployed at enterprise scale by removing error-prone manual steps? | `Repeatable` |
| 2 | Which IaC characteristic allows us to go back to the last known working version of our configuration? | `Versionable` |
| 3 | Which IaC characteristic enables us to increase the resources when the traffic demand grows? | `Scalable` |
| 4 | In the scenario given, which type of IaC tool considers where you are on the map and gives instructions to reach the desired X point? | `Declarative` |
| 5 | Can you retrieve the location and retrieve the flag? | `thm{l4b_C0mpl3x_co0rds}` |
| 6 | A DevSecOps Engineer at CyberMyne is looking for guidance on developing their next infrastructure. What type of phases provide guidance during the development or configuration of an infrastructure? | `Repeatable` |
| 7 | What type of phases ensure best practices throughout infrastructure development and management? | `Continual` |
| 8 | The 'Monitoring/Maintenance' continual phase can trigger which other continual phase? | `Rollback` |
| 9 | At the application level, what level of virtualisation would be needed to package and run the application? | `Containerisation` |
| 10 | When the operating system and the entire machine need to be virtualised, which level of virtualisation would be needed? | `Hypervisor` |
| 11 | Which 'Use of IaC' will ensure that this resource consumption won't affect the performance of the machine's other components? | `Resource Isolation` |
| 12 | Which container orchestration software can be used to automate this process? | `Kubernetes` |
| 13 | Cloud-based resources are provisioned/configured in a cloud environment. Who handles the underlying infrastructure? | `cloud service provider` |
| 14 | What category does on-prem infrastructure struggle with due to hardware limitations when facing increased traffic? | `scalability` |
| 15 | Can you get the flag using your infrastructure as code skills? | `thm{1Nfr4StrUctUr3_Pr0}` |

---

**Metodología:** Del concepto a la practica: (1) identificar las caracteristicas de IaC (Repeatable, Versionable, Scalable); (2) clasificar herramientas declarativas vs imperativas; (3) explorar el ciclo CI/CD (fases Repeatable/Continual, con Rollback como consecuencia de Monitoring/Maintenance); (4) integrar la virtualizacion por niveles (contenedores, hipervisores, aislamiento de recursos, Kubernetes); (5) contrastar responsabilidad y limites on-prem vs cloud; (6) resolver los dos laboratorios de flags.

### Cadena de ataque / Attack Chain

```text
IaC (Repeatable/Versionable/Scalable) -> tools declarativas -> CI/CD (Continual/Rollback) -> virtualizacion (Containerisation/Hypervisor/Resource Isolation/Kubernetes) -> on-prem vs cloud (CSP, scalability) -> labs (coordenadas + flag)
```

**Learning chain:** Que es IaC -> caracteristicas -> herramientas -> CI/CD -> virtualizacion -> on-prem vs cloud -> laboratorios.

**Lección:** *La infraestructura como codigo convierte el datacenter en un repositorio versionado: lo que antes era documentacion muerta ahora es codigo repetible, auditable y reversible, y las decisiones de virtualizacion y de proveedor se vuelven decisiones de configuracion.*

**MITRE ATT&CK:** T1530 (Data from Cloud Storage Object), T1048 (Exfiltration Over Alternative Protocol), T1078 (Valid Accounts)

**Fuente:** [TryHackMe - Intro to IaC](https://tryhackme.com/room/introtoiac)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.