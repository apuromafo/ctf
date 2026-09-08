# Cloud Security Pitfalls

| **Dificultad** | Easy |
| **Tipo** | Walkthrough |
| **Slug** | `cloudsecuritypitfalls` |
| **Link** | [TryHackMe](https://tryhackme.com/room/cloudsecuritypitfalls) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | IaaS / PaaS / SaaS / CASB / CWPP / CSPM / SIEM |
| **Impacto** | Entender los riesgos de migrar a la nube (modelos IaaS/PaaS/SaaS, visibilidad, responsabilidad compartida) y cómo monitorizarlos en un SOC. |

---

**Contexto:** Salas teóricas sobre los errores y riesgos habituales al migrar a la nube. Explica los tres modelos principales (IaaS, PaaS, SaaS), la distinción entre seguridad "de" la nube (responsable del proveedor) y seguridad "en" la nube (responsabilidad compartida del cliente), los retos de logging en SaaS, y las herramientas especializadas de monitoreo (CASB, CWPP, CSPM) para supervisar workloads, servicios y plano de control. Termina con un desafiío práctico sobre modelos de servicio y responsabilidad compartida.

## Solucionario

### Task 1: Introducción

**Explicación:** Presentación de la sala: riesgos y errores típicos al adoptar la nube y cómo esos problemas llegan al SOC. Solo lectura.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Continúa con la siguiente tarea. | `No answer needed` |

### Task 2: Qué es la nube

**Explicación:** Modelos de servicio cloud: `IaaS` (Infraestructura como Servicio: VMs, redes; permite migrar infraestructura on-premises "as is"), `PaaS` (plataformas de desarrollo) y `SaaS` (software gestionado por el proveedor). Elastic Cloud y CrowdStrike Falcon son ejemplos de `SaaS`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué modelo de nube permite migrar una gran red on-premises a la nube? | `IaaS` |
| 2 | ¿En qué modelo encajan Elastic Cloud y CrowdStrike Falcon? | `SaaS` |

### Task 3: Seguridad de la nube

**Explicación:** "Seguridad de la nube" = la del proveedor: sí (`Yea`) es responsable de asegurar/monitorizar su propia infraestructura. Pero NO (`Nay`) se debe confiar ciegamente: también hay que vigilar las amenazas de la cadena de suministro.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿El proveedor de nube es responsable de asegurar y monitorizar su propia infraestructura? (Yea/Nay) | `Yea` |
| 2 | ¿Debes confiar ciegamente en el proveedor sin vigilar las amenazas de la cadena de suministro? (Yea/Nay) | `Nay` |

### Task 4: Seguridad en la nube

**Explicación:** "Seguridad en la nube" = responsabilidad compartida del cliente: migrar un servidor sin parchear NO (`Nay`) lo vuelve seguro. El primer obstáculo real al integrar productos cloud en un SIEM son los `Paid Logs` (logs de pago).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Mover un servidor sin parchear a la nube lo hace seguro de nuevo? (Yea/Nay) | `Nay` |
| 2 | ¿Cuál es el primer gran obstáculo para integrar la mayoría de productos cloud con un SIEM? | `Paid Logs` |

### Task 5: Monitoreo de seguridad en la nube

**Explicación:** Los recursos de cómputo cloud (VMs, contenedores) se llaman `Workloads`. Herramientas especializadas: `CWPP` (protección de workloads, p. ej. Falco y Tetragon), `CSPM` (visor del plano de control/stack de seguridad) y `CASB` (control de acceso a SaaS).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué término describe los recursos de cómputo cloud como VMs o contenedores? | `Workloads` |
| 2 | ¿En cuál de las herramientas cloud mencionadas encajan Falco y Tetragon? | `CWPP` |

### Task 6: Desafío

**Explicación:** Ejercicio práctico de clasificación: identificando el modelo de servicio correcto y quién es responsable en cada escenario se obtienen las dos flags de validación.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag que obtienes al completar el primer ejercicio? | `THM{flag_as_a_service!}` |
| 2 | ¿Cuál es la flag que obtienes al completar el segundo ejercicio? | `THM{ready_for_cloud_migration!}` |

### Task 7: Conclusión

**Explicación:** Repaso de los conceptos clave de la sala y cierre.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Completa la sala. | `No answer needed` |

---

**Metodología:** La sala es de lectura y pequeños ejercicios mentales. Tras asimilar los modelos de nube (IaaS/PaaS/SaaS) y el modelo de responsabilidad compartida, se aplican los conceptos a casos prácticos: elegir el modelo correcto según el recurso, decidir sobre la confianza en el proveedor, identificar el problema de logs de pago y clasificar herramientas de monitoreo (CASB/CWPP/CSPM). El desafío final valida la comprensión con dos flags.

**Learning chain:** modelos cloud → seguridad del proveedor vs del cliente → obstáculos de SIEM → monitoreo de workloads → ejercicios de responsabilidad compartida.

**MITRE ATT&CK:** T1552 (Unsecured Credentials), T1190 (Exploit Public-Facing Application)

**Fuente:** [TryHackMe - Cloud Security Pitfalls](https://tryhackme.com/room/cloudsecuritypitfalls)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
