# Intro to Cloud Security

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `introtocloudsecurity` | https://tryhackme.com/room/introtocloudsecurity | 01 Level Easy | TryHackMe | IaaS/PaaS/SaaS / modelos de despliegue / ciclo de vida del dato / biometría / políticas IAM / security groups / cifrado (at rest/in transit) / Disaster Recovery | Comprender los conceptos fundamentales de seguridad en la nube: arquitectura, modelos de despliegue, ciclo de vida de los datos, gestión de accesos, políticas, red y almacenamiento. |

---

**Contexto:** La room presenta los cimientos de la seguridad en la nube. Explica qué despliega el proveedor según el modelo de servicio (en IaaS: Hardware), los modelos de despliegue (nube pública, privada, comunitaria e híbrida) y conceptos de seguridad con mini-ejercicios: ciclo de vida del dato (fase Create), factores de autenticación, políticas IAM con ventanas temporales, security groups basados en "deny all unless allowed explicitly", cifrado de datos en reposo/tránsito y buenas prácticas de Disaster Recovery.

> **ES:** Nube y seguridad: modelos de servicio y despliegue, ciclo de vida del dato, gestión de accesos y políticas, grupos de seguridad de red, cifrado del almacenamiento y respaldo/recuperación (DR), con breves ejercicios prácticos.
> **EN:** Cloud and security: service and deployment models, data lifecycle, access management and policies, network security groups, storage encryption and backup/DR, with short hands-on exercises.

## Solucionario

### Task 1: Introduction / Introducción

**Explicación:** Introducción a la room y a los conceptos que se van a cubrir (nube, modelos de servicio, riesgos de seguridad). No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | I am ready to get started. / Estoy listo para empezar. | `No answer needed` |

### Task 2: Architectural Concepts of Cloud / Conceptos arquitectónicos de la nube

**Explicación:** Se presentan los tres modelos de servicio: IaaS (Infrastructure as a Service), PaaS (Platform as a Service) y SaaS (Software as a Service). En IaaS el proveedor despliega la capa de **Hardware** (servidores, almacenamiento, red), mientras que el cliente gestiona el resto. Se distingue también la nube dedicada a un único cliente: la nube **Private** (privada), frente a la pública, comunitaria o híbrida.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | In Infrastructure as a Service, what will be deployed by the vendor (Hardware or Software)? / En Infrastructure as a Service, ¿qué despliega el proveedor (Hardware o Software)? | `Hardware` |
| 2 | What is the type of cloud dedicated to a single customer called? / ¿Cómo se denomina el tipo de nube dedicada a un único cliente? | `Private` |

### Task 3: Cloud Security Concepts / Conceptos de seguridad en la nube

**Explicación:** Se introducen los conceptos de seguridad del dato en la nube: el ciclo de vida del dato comienza con la fase **Create** (creación), seguido de almacenamiento, uso, compartición, archivado y destrucción, cada una con sus requisitos (confidencialidad, integridad y disponibilidad). En el ejercicio interactivo (botón View Site) se repasan estos conceptos y se obtiene la flag.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the first phase in the cloud data lifecycle? / ¿Cuál es la primera fase del ciclo de vida del dato en la nube? | `Create` |
| 2 | Click the View Site button located at the end of the task and complete the exercise. What is the flag? / Haz clic en el botón View Site y completa el ejercicio. ¿Cuál es la flag? | `THM{CLOUD_11101}` |

### Task 4: Cloud Security Risks Concerning Deployment Models / Riesgos de seguridad en la nube según los modelos de despliegue

**Explicación:** Se analizan los riesgos de cada modelo de despliegue. En la nube **Public** el cliente puede quedar secuestrado por el proveedor (vendor lock-in) y depender de sus decisiones y precios; en la nube comunitaria, al compartir infraestructura entre varias organizaciones, es **difícil (yea)** imponer decisiones y procedimientos de negocio específicos.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | In which cloud model does the customer become the hostage of cloud providers (vendor locked in)? / ¿En qué modelo de nube el cliente queda a merced del proveedor (vendor lock-in)? | `Public` |
| 2 | Is it challenging to enforce specific business decisions and procedures in the community cloud (yea/nay)? / ¿Es difícil imponer decisiones y procedimientos de negocio concretos en la nube comunitaria (yea/nay)? | `yea` |

### Task 5: Security Through Access Management / Seguridad a través de la gestión de accesos

**Explicación:** La gestión de accesos se apoya en los factores de autenticación: algo que sabes (contraseña), algo que tienes (token) y algo que eres (biometría). El reconocimiento facial (FaceID) y los sistemas biométricos son **factores de autenticación (yea)**, ya que verifican "algo que eres". El ejercicio práctico complementa la teoría con interacción en el sitio.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Are FaceID and biometric types of Authentication factors (yea/nay)? / ¿Son FaceID y la biometría factores de autenticación (yea/nay)? | `yea` |
| 2 | I have completed the practical exercise. / He completado el ejercicio práctico. | `No answer needed` |

### Task 6: Security Through Policies / Seguridad a través de políticas

**Explicación:** Las políticas en la nube permiten un control fino y dinámico: sí es posible crear una política que habilite el acceso de un usuario a la base de datos solo en un momento concreto del día (**yea**). Es la base de los entornos basados en políticas JSON de los proveedores cloud.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | In a cloud environment, can we create a policy to enable Database access for a user at a specific time of the day (yea/nay)? / En un entorno cloud, ¿podemos crear una política que habilite el acceso a la base de datos en un momento específico del día (yea/nay)? | `yea` |
| 2 | I have completed the practical exercise. / He completado el ejercicio práctico. | `No answer needed` |

### Task 7: Security Through Network Management / Seguridad a través de la gestión de redes

**Explicación:** La seguridad de red en la nube se materializa con security groups y reglas de firewall. Operar los grupos de seguridad bajo el principio "deny all unless allowed explicitly" (denegar todo salvo lo permitido explícitamente) es una **buena práctica (yea)**; de hecho, los security groups de los proveedores bloquean por defecto y solo se abren los puertos necesarios.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Is it a good practice to operate security groups on the principle of "deny all unless allowed explicitly" (yea/nay)? / ¿Es buena práctica operar los grupos de seguridad con el principio "deny all unless allowed explicitly" (yea/nay)? | `yea` |
| 2 | I have completed the practical exercise. / He completado el ejercicio práctico. | `No answer needed` |

### Task 8: Security Through Storage Management / Seguridad a través de la gestión de almacenamiento

**Explicación:** El almacenamiento debe protegerse en los dos estados: en tránsito (mientras viaja por la red) y en reposo (en disco). El cifrado de datos **en reposo es necesario incluso si ciframos en tránsito** (`nay`): ambos deben aplicarse, no son excluyentes.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Encryption of data at rest is unnecessary if we carry out encryption at transit (yea/nay)? / ¿El cifrado de datos en reposo es innecesario si ciframos en tránsito (yea/nay)? | `nay` |
| 2 | I have completed the practical exercise. / He completado el ejercicio práctico. | `No answer needed` |

### Task 9: Cloud Security - Some Additional Concepts / Seguridad en la nube - Conceptos adicionales

**Explicación:** Conceptos adicionales como el Disaster Recovery (DR): guardar las copias de respaldo del servidor en la misma zona o datacenter es una **mala práctica** (`nay`), porque ante un desastre local (incendio, apagón, fallo regional) se perderían tanto el servidor como sus copias. Las copias DR deben ubicarse en regiones geográficamente separadas.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Is it a good practice to keep Disaster Recovery Backups of a server in the same vicinity or data centre (yea/nay)? / ¿Es buena práctica guardar las copias de Disaster Recovery de un servidor en la misma zona o datacenter (yea/nay)? | `nay` |
| 2 | I have completed the practical exercise. / He completado el ejercicio práctico. | `No answer needed` |

### Task 10: Conclusion / Conclusión

**Explicación:** Recapitulación de la room: modelos de servicio y despliegue, ciclo de vida del dato, gestión de accesos, políticas, red, almacenamiento y recursos adicionales para seguir aprendiendo. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | I have completed the room. / He completado la room. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | In Infrastructure as a Service, what will be deployed by the vendor (Hardware or Software)? | `Hardware` |
| 2 | What is the type of cloud dedicated to a single customer called? | `Private` |
| 3 | What is the first phase in the cloud data lifecycle? | `Create` |
| 4 | Click the View Site button located at the end of the task and complete the exercise. What is the flag? | `THM{CLOUD_11101}` |
| 5 | In which cloud model does the customer become the hostage of cloud providers (vendor locked in)? | `Public` |
| 6 | Is it challenging to enforce specific business decisions and procedures in the community cloud (yea/nay)? | `yea` |
| 7 | Are FaceID and biometric types of Authentication factors (yea/nay)? | `yea` |
| 8 | In a cloud environment, can we create a policy to enable Database access for a user at a specific time of the day (yea/nay)? | `yea` |
| 9 | Is it a good practice to operate security groups on the principle of "deny all unless allowed explicitly" (yea/nay)? | `yea` |
| 10 | Encryption of data at rest is unnecessary if we carry out encryption at transit (yea/nay)? | `nay` |
| 11 | Is it a good practice to keep Disaster Recovery Backups of a server in the same vicinity or data centre (yea/nay)? | `nay` |

---

**Metodología:** Revisión conceptual progresiva por capas de la nube: (1) arquitectura y modelos de servicio (IaaS/PaaS/SaaS) y despliegue (pública/privada/comunitaria/híbrida); (2) ciclo de vida del dato; (3) riesgos de cada modelo; (4) gestión de accesos (factores de autenticación); (5) políticas IAM; (6) seguridad de red con security groups; (7) almacenamiento (cifrado en reposo y en tránsito); (8) Disaster Recovery. Cada concepto se cierra con un mini-ejercicio en el sitio (View Site).

### Cadena de ataque / Attack Chain

```text
Modelos de servicio (IaaS=Hardware) -> modelos de despliegue (pública/privada/comunitaria) -> ciclo de vida del dato (Create) -> riesgos (vendor lock-in) -> accesos (factores) -> políticas (ventanas temporales) -> red (security groups) -> almacenamiento (cifrado) -> DR (zonas separadas)
```

**Learning chain:** Conceptos cloud -> servicios/despliegue -> datos -> accesos -> políticas -> red -> almacenamiento -> DR.

**Lección:** *La seguridad en la nube no es un único control: se construye por capas (identidad, política, red, almacenamiento y continuidad), y cada decisión —de modelo, de cifrado o de ubicación de copias— cambia la superficie de riesgo.*

**MITRE ATT&CK:** T1530 (Data from Cloud Storage Object), T1078 (Valid Accounts), T1048 (Exfiltration Over Alternative Protocol)

**Fuente:** [TryHackMe - Intro to Cloud Security](https://tryhackme.com/room/introtocloudsecurity)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.