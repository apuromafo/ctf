# On-Premises IaC

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Walkthrough | onpremisesiac | https://tryhackme.com/room/onpremisesiac | 02 Level Medium | TryHackMe | Infrastructure as Code, Vagrant (Vagrantfile), Ansible (Playbook/Template/Role), pipelines de CI/CD, aprovisionamiento on-prem | Entender y poner en práctica IaC (Infrastructure as Code) con Vagrant y herramientas de configuración como Ansible, incluido el aprovisionamiento de pipelines y el análisis del escenario ofensivo "Atacando On-Prem IaC". |

---

**Contexto:** La sala **On-Premises IaC** forma parte de la temática DevSecOps y explica la **Infrastructure as Code (IaC)**: qué es, por qué versionar y automatizar el aprovisionamiento, y cómo usar herramientas reales. En las tareas prácticas se trabaja con un proyecto (`iac/`) que define máquinas con **Vagrant** y las aprovisiona con **Ansible** (roles, playbooks, templates). Incluye una tarea dedicada a atacar una infraestructura IaC on-premises (flags de `flag1-of-4.txt` a `flag4-of-4.txt`) que muestran la cara defensiva-ofensiva de estos entornos.

> **ES:** Room DevSecOps sobre Infrastructure as Code: aprovisionamiento con Vagrant y Ansible, pipelines, y una práctica de ataque a infraestructura IaC on-prem.
> **EN:** A DevSecOps room about Infrastructure as Code: provisioning with Vagrant and Ansible, pipelines, and an attacking an on-prem IaC infrastructure exercise.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:** Presentación de la sala y de los objetivos (qué es IaC, herramientas, y la parte ofensiva de la tarea 7). Se indica tener conocimientos de Linux, redes y algo de YAML.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Introduce yourself / confirm you are ready to read and continue (no answer required). | `No answer needed` |

### Task 2: Conceptos de IaC / What is IaC?
**Explicación:** Se comparan las ventajas de un pipeline **on-prem** frente a uno en la nube. Si se quiere **más control** sobre el pipeline, el on-prem es la opción (**Yea**); si se busca un despliegue **flexible y fácilmente escalable**, el on-prem no es el adecuado (**Nay**); y si la organización tiene **estrictas regulaciones de protección de datos**, el pipeline on-prem vuelve a ser la opción (**Yea**).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | If I want more control over my pipeline, should I use an on-prem IaC pipeline? (Yea/Nay) | `Yea` |
| 2 | If I want to have a flexible and easily scalable deployment, should I use an on-prem IaC pipeline? (Yea/Nay) | `Nay` |
| 3 | If I have strict data protection regulations enforced on my organisation, should I use an on-prem IaC pipeline? (Yea/Nay) | `Yea` |

### Task 3: Vagrant / Vagrant
**Explicación:** Vagrant gestiona máquinas virtuales declarativamente desde un archivo de configuración: el archivo que Vagrant usa para aprovisionar es el **Vagrantfile**; el comando que aprovisiona todos los hosts es `vagrant up`; y para aprovisionar solo el host `webserver` se usa `vagrant up webserver`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the name of the file that Vagrant uses for provisioning? / ¿Cómo se llama el archivo que Vagrant usa para aprovisionar? | `Vagrantfile` |
| 2 | What command can be used to provision all hosts with Vagrant? / ¿Qué comando aprovisiona todos los hosts con Vagrant? | `vagrant up` |
| 3 | What command can be used to provision only the webserver host with Vagrant? / ¿Qué comando aprovisiona solo el host webserver? | `vagrant up webserver` |

### Task 4: Herramientas de configuración / Configuration Tools
**Explicación:** Para aprovisionar y mantener la configuración se usa **Ansible**. El archivo que Ansible aprovisiona se denomina **Playbook**; el archivo Ansible que se actualiza inyectando variables para crear un archivo final durante el aprovisionamiento es un **Template**; y una **colección Ansible** que puede aprovisionarse con una única petición de configuración es un **Role**.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the name given to the file that Ansible will provision? / ¿Qué nombre recibe el archivo que Ansible aprovisiona? | `Playbook` |
| 2 | What is the name given to an Ansible file that will be updated, through the injection of Ansible variables, to create a final file during the provisioning process? / ¿Qué nombre tiene el archivo Ansible que se actualiza inyectando variables? | `Template` |
| 3 | What is the name given to an Ansible collection that can be provisioned with a single configuration request? / ¿Qué nombre recibe la colección Ansible que se aprovisiona con una sola petición? | `Role` |

### Task 5: Pipeline IaC / IaC Pipeline (Flag)
**Explicación:** Tras aprovisionar la infraestructura se configura el pipeline de IaC (integración y despliegue continuos). La flag aparece en la **aplicación web alojada tras el aprovisionamiento del pipeline IaC**: hay que crear un perfil y autenticarse para ver la flag `THM{IaC.Pipelines.Can.Be.Fun}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag displayed on the web application that is hosted after your IaC pipeline provisioning? You will need to create a profile and authenticate to view the flag. / ¿Cuál es la flag mostrada por la web tras el aprovisionamiento del pipeline? | `THM{IaC.Pipelines.Can.Be.Fun}` |

### Task 6: Despliegue / Deploy
**Explicación:** La tarea de despliegue lanza el aprovisionamiento completo del entorno (host + VMs guest) una vez configurados Vagrant y Ansible. No hay preguntas que responder.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Deploy the environment (no answer required). | `No answer needed` |

### Task 7: Atacando On-Prem IaC / Attacking On-Prem IaC
**Explicación:** Ejercicio ofensivo sobre la infraestructura IaC on-prem desplegada (red privada 172.20.128.2, Gitea, OliveTin en 1337 ejecutando Ansible Playbooks, panel de desarrollo `/api/testDB` con `_command`). Las cuatro flags explotan malas prácticas IaC: bypass del pipeline, claves de despliegue presentes en el repo, comparticiones de red con permisos incorrectos y provisionadores con privilegios excesivos. Se leen de los archivos `flag1-of-4.txt` a `flag4-of-4.txt`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the value stored in the flag1-of-4.txt file? / ¿Qué valor contiene flag1-of-4.txt? | `THM{Dev.Bypasses.and.Checks.can.be.Dangerous}` |
| 2 | What is the value stored in the flag2-of-4.txt file? / ¿Qué valor contiene flag2-of-4.txt? | `THM{IaC.Deployment.Keys.Must.be.Removed}` |
| 3 | What is the value stored in the flag3-of-4.txt file? / ¿Qué valor contiene flag3-of-4.txt? | `THM{IaC.Shares.Should.be.Restricted}` |
| 4 | What is the value stored in the flag4-of-4.txt file? / ¿Qué valor contiene flag4-of-4.txt? | `THM{Provisioners.Usually.Have.Privileged.Access}` |

### Task 8: Cierre / Wrap-up
**Explicación:** Conclusión: se repasa el ciclo completo de IaC (definición, versión, aprovisionamiento, pipeline) y las lecciones de seguridad de la parte ofensiva.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Summarise what you have learnt (no answer required). | `No answer needed` |

### Tabla unificada de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Task 1) Introducción a la sala. | `No answer needed` |
| 2 | (Task 2) More control over my pipeline → on-prem IaC? (Yea/Nay) | `Yea` |
| 3 | (Task 2) Flexible and easily scalable deployment → on-prem IaC? (Yea/Nay) | `Nay` |
| 4 | (Task 2) Strict data protection regulations → on-prem IaC? (Yea/Nay) | `Yea` |
| 5 | (Task 3) Name of the file that Vagrant uses for provisioning. | `Vagrantfile` |
| 6 | (Task 3) Command to provision all hosts with Vagrant. | `vagrant up` |
| 7 | (Task 3) Command to provision only the webserver host. | `vagrant up webserver` |
| 8 | (Task 4) Name given to the file that Ansible will provision. | `Playbook` |
| 9 | (Task 4) Ansible file updated through the injection of variables to create a final file. | `Template` |
| 10 | (Task 4) Ansible collection provisioned with a single configuration request. | `Role` |
| 11 | (Task 5) Flag displayed on the web app after IaC pipeline provisioning. | `THM{IaC.Pipelines.Can.Be.Fun}` |
| 12 | (Task 6) Despliegue del entorno. | `No answer needed` |
| 13 | (Task 7) Value stored in flag1-of-4.txt. | `THM{Dev.Bypasses.and.Checks.can.be.Dangerous}` |
| 14 | (Task 7) Value stored in flag2-of-4.txt. | `THM{IaC.Deployment.Keys.Must.be.Removed}` |
| 15 | (Task 7) Value stored in flag3-of-4.txt. | `THM{IaC.Shares.Should.be.Restricted}` |
| 16 | (Task 7) Value stored in flag4-of-4.txt. | `THM{Provisioners.Usually.Have.Privileged.Access}` |
| 17 | (Task 8) Cierre de la sala. | `No answer needed` |

---

**Metodología:** Definición declarativa de la infraestructura en el Vagrantfile → aprovisionamiento con Ansible (playbooks, templates, roles) → `vagrant up` del host y de las máquinas guest → configuración del pipeline de IaC → parte ofensiva: enumeración de Gitea/OliveTin, abuso del panel de desarrollo (`/api/testDB`), lectura de claves y flags en las comparticiones y con los provisionadores privilegiados.

**Learning chain:** conceptos IaC → Vagrant (Vagrantfile, vagrant up) → herramientas de configuración (Playbook/Template/Role) → pipeline CI/CD → aprovisionamiento real → ataque a entornos IaC on-prem.

**Lección:** *IaC acelera y versiona la infraestructura, pero cada automatización heredada (claves en el repo, shares abiertas, provisionadores con privilegios) es una puerta que un atacante puede aprovechar tan rápido como tú aprovisionaste.* La seguridad debe formar parte del pipeline desde el primer commit.

**MITRE ATT&CK:** T1587.003 (Develop Capabilities: Digital Certificates) · T1190 (Exploit Public-Facing Application) · T1003 (OS Credential Dumping) · T1482 (Domain Trust Discovery) · T1552.001 (Unsecured Credentials: Credentials In Files) · T1037 (Boot or Logon Initialization Scripts).

**Fuente:** [TryHackMe - On-Premises IaC](https://tryhackme.com/room/onpremisesiac)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.