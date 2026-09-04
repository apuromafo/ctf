 
# Cloud Security Pitfalls [EASY]
**Enlace de la sala:** [Cloud Security Pitfalls](https://tryhackme.com/room/cloudsecuritypitfalls)

Cloud Security Pitfalls
<p align="center"> <img src="https://tryhackme-images.s3.amazonaws.com/room-icons/678ecc92c80aa206339f0f23-1766592228556" alt="Cloud Security Pitfalls Logo" width="200"> </p>
Explore the risks companies face when migrating to the cloud, and learn how to address them in a SOC.
  
## Tarea 1: Introducción / Task 1: Introduction

Many companies migrate their on-premises resources to the cloud to gain benefits such as cost savings, greater stability, and improved security. This room outlines the risks and common pitfalls companies face when migrating to the cloud.

### Objetivos de Aprendizaje / Learning Objectives

* Learn the main cloud models: IaaS, PaaS, and SaaS
* Explore security risks coming from the cloud providers
* Understand the core concepts of security in the cloud
* Identify the challenges of monitoring clouds as a SOC

**Questions**

* **Continue to the next task!**
* *Answer:* No answer needed

---

## Tarea 2: Qué es la Nube / Task 2: What Is Cloud

The cloud is a paradigm in which computing resources are hosted and managed by third-party providers. There are three main models:

* **IaaS (Infrastructure as a Service):** On-demand computing infrastructure (e.g., AWS EC2, GCP).
* **PaaS (Platform as a Service):** For simple development and hosting (e.g., Vercel, Heroku).
* **SaaS (Software as a Service):** Final product used by non-technical audiences (e.g., Slack, Gmail).

**Questions**

* **Which cloud model allows you to migrate a big on-premises network to the cloud?**
* *Answer:* `IaaS`

* **Which cloud model do Elastic Cloud and CrowdStrike Falcon fit into?**
* *Answer:* `SaaS`

---

## Tarea 3: Seguridad de la Nube / Task 3: Security of the Cloud

Security **of** the cloud refers to the provider's responsibility to secure their own internal infrastructure.

### Riesgos Clave / Key Risks

* **Cloud Vulnerabilities:** Rare but high impact (supply chain risk).
* **Poor Cloud Visibility:** You cannot see the provider's internal environment or logs.
* **Shadow IT:** Departments uploading data to untrusted SaaS applications.

**Questions**

* **Is the cloud provider responsible for securing and monitoring its own infrastructure (Yea/Nay)?**
* *Answer:* `Yea`

* **But should you trust the cloud provider without watching for supply chain threats? (Yea/Nay)**
* *Answer:* `Nay`

---

## Tarea 4: Seguridad en la Nube / Task 4: Security in the Cloud

Security **in** the cloud is the customer's responsibility (Shared Responsibility Model). This includes VMs, applications, and credentials.

### Desafíos de Registro en SaaS / Logging Challenges in SaaS

* **Paid Logs:** May require premium licenses.
* **Poor Format:** Unstructured or incomplete fields.
* **Lack of Integration:** No support for SIEM.

**Questions**

* **Does moving an unpatched server to the cloud make it secure again? (Yea/Nay)**
* *Answer:* `Nay`

* **What is the first major obstacle to integrating most cloud products with a SIEM?**
* *Answer:* `Paid Logs`

---

## Tarea 5: Monitoreo de Seguridad en la Nube / Task 5: Cloud Security Monitoring

Monitoring requirements change based on the model:

* **Workloads:** VMs/Containers.
* **Cloud Services:** Databases and storage access.
* **Control Plane:** Admin console actions.

### Herramientas Especializadas / Specialized Tools

* **CASB:** Cloud Access Security Brokers.
* **CWPP:** Cloud Workload Protection Platforms.
* **CSPM:** Cloud Security Posture Management.

**Questions**

* **What term describes cloud compute resources like VMs or containers?**
* *Answer:* `Workloads`

* **Which of the mentioned cloud security tools do Falco and Tetragon fit into?**
* *Answer:* `CWPP`

---

## Tarea 6: Desafío / Task 6: Challenge

This task involves a practical exercise on cloud service models and the Shared Responsibility Model.

**Questions**

* **What is the flag you get after completing the first exercise?**
* *Answer:* `THM{flag_as_a_service!}`

* **What is the flag you get after completing the second exercise?**
* *Answer:* `THM{ready_for_cloud_migration!}`

---

## Tarea 7: Conclusión / Task 7: Conclusion

The room provided an overview of cloud service models (IaaS, PaaS, SaaS) and the security monitoring challenges inherent in cloud environments.

**Questions**

* **Complete the room!**
* *Answer:* No answer needed

---
 

### Resumen / Summary

| Task | Pregunta | Respuesta |
| --- | --- | --- |
| 2 | 1 | `IaaS` |
| 2 | 2 | `SaaS` |
| 3 | 1 | `Yea` |
| 3 | 2 | `Nay` |
| 4 | 1 | `Nay` |
| 4 | 2 | `Paid Logs` |
| 5 | 1 | `Workloads` |
| 5 | 2 | `CWPP` |
| 6 | 1 | `THM{flag_as_a_service!}` |
| 6 | 2 | `THM{ready_for_cloud_migration!}` |

---

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
