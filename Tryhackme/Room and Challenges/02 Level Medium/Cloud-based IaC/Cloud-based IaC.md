# Cloud-based IaC

| Campo | Valor |
|---|---|
| Dificultad | Medium |
| Tipo | CTF |
| Slug | cloudbasediac |
| Link | https://tryhackme.com/room/cloudbasediac |
| Sección | 02 Level Medium |
| Fuente | TryHackMe |
| Componentes | Cloud, IaC, Terraform, CloudFormation |
| Impacto | Comprensión de infraestructura como código |

---

**Contexto:** Cloud-based IaC es una sala de TryHackMe de dificultad media que explora los conceptos de Infraestructura como Código (IaC) en entornos cloud. Cubre herramientas como Terraform y CloudFormation, incluyendo sus componentes, archivos de configuración, comandos de ciclo de vida y buenas prácticas de seguridad como revisiones de código, políticas de stack y parametrización de datos sensibles.

## Solucionario

### Task 1: Fundamentos de IaC

**Explicación:** Se identificaron los componentes fundamentales de la infraestructura como código en la nube, incluyendo el estado, los archivos de configuración Terraform y los proveedores cloud.

1. No answer needed

### Task 2: Componentes de Terraform

**Explicación:** Se reconocieron los tres componentes principales de Terraform: el estado que almacena la infraestructura real, los archivos de configuración que definen el recurso deseado y el proveedor que indica qué API cloud utilizar.

1. State
2. Terraform Config files
3. Provider

### Task 3: Estructura de archivos

**Explicación:** Se identificaron los archivos típicos de un proyecto Terraform: el proveedor, main.tf como archivo principal de configuración y variables.tf para los parámetros.

1. provider
2. main.tf
3. variables.tf

### Task 4: Comandos del ciclo de vida

**Explicación:** Se ordenaron los comandos de Terraform según su posición en el ciclo de vida: init para inicializar, plan para previsualizar y apply para aplicar cambios.

1. terraform apply
2. terraform init
3. terraform plan

### Task 5: AWS CloudFormation

**Explicación:** Se identificaron elementos clave de CloudFormation: los eventos que monitorean cambios, las referencias entre stacks para compartir datos entre plantillas.

1. events
2. yay
3. Cross-Stack References

### Task 6: Gestión de cambios en CloudFormation

**Explicación:** Se reconocieron herramientas de gestión de cambios como los change sets que permiten previsualizar y aprobar modificaciones antes de aplicarlas.

1. yay
2. change sets

### Task 7: Herramientas IaC

**Explicación:** Se compararon herramientas IaC: CloudFormation para AWS y Terraform como alternativa multi-nube.

1. nay
2. CloudFormation
3. Terraform

### Task 8: Seguridad en IaC

**Explicación:** Se identificaron las mejores prácticas de seguridad en IaC: parametrizar datos sensibles, realizar revisiones de código y usar políticas de stack para proteger recursos críticos.

1. Parameterise Sensitive Data
2. Code Reviews
3. Stack Policies

### Task 9: Flag final

**Explicación:** Se obtuvo la flag de la sala tras completar todas las tareas anteriores.

THM{c10uD-b@z3d-1@SeE}

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Fundamentos de IaC | `No answer needed` |
| 2 | Componentes de Terraform | `State`, `Terraform Config files`, `Provider` |
| 3 | Estructura de archivos | `provider`, `main.tf`, `variables.tf` |
| 4 | Comandos del ciclo de vida | `terraform apply`, `terraform init`, `terraform plan` |
| 5 | AWS CloudFormation | `events`, `Cross-Stack References` |
| 6 | Gestión de cambios | `change sets` |
| 7 | Herramientas IaC | `nay`, `CloudFormation`, `Terraform` |
| 8 | Seguridad en IaC | `Parameterise Sensitive Data`, `Code Reviews`, `Stack Policies` |
| 9 | Flag final | `THM{c10uD-b@z3d-1@SeE}` |

---

**Metodología:** Estudio teórico de conceptos IaC, identificación de componentes Terraform/CloudFormation, análisis de ciclos de vida y prácticas de seguridad.

**Learning chain:** Definición de IaC → Componentes de Terraform → Archivos de configuración → Ciclo de vida → CloudFormation vs Terraform → Seguridad en IaC → Flag.

**Lección:** *La infraestructura como código permite gestionar entornos cloud de forma reproducible, auditable y segura cuando se aplican las mejores prácticas.*

**MITRE ATT&CK:** T1552 - Unsecured Credentials (protección de datos sensibles en código IaC)

**Fuente:** [TryHackMe - Cloud-based IaC](https://tryhackme.com/room/cloudbasediac)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.