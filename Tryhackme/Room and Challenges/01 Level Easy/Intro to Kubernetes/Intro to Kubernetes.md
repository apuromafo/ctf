# Intro to Kubernetes

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `introtokubernetes` | [TryHackMe](https://tryhackme.com/room/introtokubernetes) | 01 Level Easy | TryHackMe | Kubernetes, Pods, etcd, kube-proxy, Services, ReplicaSet, Deployments, kubectl, RBAC, YAML, Secrets | Fundamentos de orquestación de contenedores con Kubernetes: arquitectura, objetos, configuración YAML, kubectl, seguridad y explotación |

> **Objeto:** Aprender los fundamentos de Kubernetes: qué es la orquestación de contenedores, la arquitectura del clúster, los objetos principales, los ficheros de configuración YAML, los comandos kubectl, las prácticas de seguridad (RBAC, Pod Security) y una tarea final de explotación práctica.

---

**Contexto:** Sala del path DevSecOps que recorre los conceptos básicos de Kubernetes ("K8s"): orquestación de contenedores, arquitectura (pod, etcd, kube-proxy), el landscape de objetos (service, ReplicaSet, deployment), la configuración declarativa en YAML (spec, kind), los comandos kubectl, la seguridad en clústeres (RBAC, Pod Security Standards, Pod Security Admission, Secrets) y una tarea práctica final de explotación sobre un clúster real para recuperar una flag.

> **ES:** Sala introductoria a Kubernetes: orquestación de contenedores, arquitectura, objetos, YAML, kubectl, seguridad con RBAC/Pod Security y explotación final.
> **EN:** Introductory room to Kubernetes: container orchestration, architecture, objects, YAML, kubectl, RBAC/Pod Security and a final exploitation task.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:** Presentación de la sala: se explica por qué Kubernetes es clave en el espacio DevSecOps y qué se va a aprender (fundamentos, prácticas seguras y experiencia hands-on).

No answer needed

### Task 2: Kubernetes 101 / Kubernetes 101
**Explicación:** Se introduce la orquestación de contenedores: las aplicaciones contenedorizadas son altamente portables y Kubernetes gestiona la orquestación de contenedores entre diferentes entornos.

1. highly portable
2. container orchestration

### Task 3: Arquitectura de Kubernetes / Kubernetes Architecture
**Explicación:** Se describen los componentes que forman un clúster de Kubernetes: el pod como unidad mínima de computación, etcd como almacén clave-valor de estado y kube-proxy como componente de red del nodo worker.

1. pod
2. etcd
3. kube-proxy

### Task 4: Landscape de Kubernetes / Kubernetes Landscape
**Explicación:** Se recorren los objetos que se pueden desplegar en un clúster: service para exponer los pods, replicaset para mantener el número de réplicas y deployments para gestionar los despliegues.

1. service
2. replicaset
3. deployments

### Task 5: Configuración de Kubernetes / Kubernetes Configuration
**Explicación:** Se aprende a definir recursos de forma declarativa en YAML: el campo spec define el estado deseado, kind define el tipo de objeto y se indica el puerto del servicio (80).

1. spec
2. kind
3. 80

### Task 6: Kubectl / Kubectl
**Explicación:** Se practican los comandos principales de kubectl para interactuar con el clúster: describe, exec, get y apply.

1. describe
2. exec
3. get
4. apply

### Task 7: Kubernetes y DevSecOps / Kubernetes & DevSecOps
**Explicación:** Se revisan las prácticas de seguridad para Kubernetes: RBAC para regular el acceso al clúster, Pod Security Standards para definir políticas de seguridad en tres niveles, Pod Security Admission como enforcer de esas políticas y el objeto Secret para almacenar información sensible de forma segura.

1. RBAC
2. Pod Security Standards
3. Pod Security Admission
4. Secret

### Task 8: Hands-on con Kubernetes / Hands-on with Kubernetes
**Explicación:** Tarea práctica final: se investiga el clúster (por ejemplo, los ConfigMaps del despliegue con kubectl get configmap) para recuperar la flag, y se identifica la apiVersion usada por el RoleBinding.

1. THM{k8s_k3nno1ssarus}
2. rbac.authorization.k8s.io/v1

### Tabla unificada de preguntas y respuestas

| Task | Pregunta | Respuesta |
|------|----------|-----------|
| 1 | Introducción a la sala | `No answer needed` |
| 2.1 | ¿Cómo se describen las aplicaciones de un clúster (alta disponibilidad, altamente portables, etc.)? | `highly portable` |
| 2.2 | ¿Qué término describe la gestión de contenedores entre múltiples entornos? | `container orchestration` |
| 3.1 | ¿Cuál es la unidad más pequeña de computación en Kubernetes? | `pod` |
| 3.2 | ¿Qué componente del control plane es un almacén clave-valor con el estado del clúster? | `etcd` |
| 3.3 | ¿Qué componente del nodo worker gestiona la comunicación de red del clúster? | `kube-proxy` |
| 4.1 | ¿Qué objeto permite exponer y comunicar los pods? | `service` |
| 4.2 | ¿Qué objeto mantiene el número deseado de réplicas? | `replicaset` |
| 4.3 | ¿Qué objeto gestiona los despliegues y las actualizaciones de los pods? | `deployments` |
| 5.1 | ¿Qué campo YAML define el estado deseado del recurso? | `spec` |
| 5.2 | ¿Qué campo YAML define el tipo de objeto? | `kind` |
| 5.3 | ¿Qué puerto escucha el servicio definido? | `80` |
| 6.1 | ¿Qué comando kubectl muestra información detallada de un recurso? | `describe` |
| 6.2 | ¿Qué comando kubectl ejecuta un proceso dentro de un contenedor en ejecución? | `exec` |
| 6.3 | ¿Qué comando kubectl lista los recursos del clúster? | `get` |
| 6.4 | ¿Qué comando kubectl aplica una configuración declarativa? | `apply` |
| 7.1 | ¿Qué práctica de seguridad regula el acceso al clúster y a sus recursos? | `RBAC` |
| 7.2 | ¿Qué se usa para definir políticas de seguridad de pods en tres niveles? | `Pod Security Standards` |
| 7.3 | ¿Qué hace cumplir esas políticas? | `Pod Security Admission` |
| 7.4 | ¿Qué objeto almacena información sensible de forma segura? | `Secret` |
| 8.1 | Flag recuperada en la parte práctica | `THM{k8s_k3nno1ssarus}` |
| 8.2 | apiVersion usada por el RoleBinding | `rbac.authorization.k8s.io/v1` |

---

**Metodología:** Estudio conceptual de la orquestación de contenedores, reconocimiento de la arquitectura del clúster (pod, etcd, kube-proxy), revisión de los objetos del landscape (service, replicaset, deployments), lectura de manifiestos YAML (spec, kind), práctica de comandos kubectl, aplicación de medidas de seguridad (RBAC, Pod Security Standards/Admission, Secrets) y explotación final del clúster para extraer la flag.

### Cadena de ataque / Attack Chain

Orquestación de contenedores -> arquitectura (pod/etcd/kube-proxy) -> objetos (service/replicaset/deployments) -> YAML (spec/kind) -> kubectl -> RBAC/Pod Security/Secrets -> explotación del clúster -> flag

**Learning chain:** Kubernetes -> container orchestration -> architecture -> objects -> YAML config -> kubectl -> security (RBAC, Pod Security) -> exploitation

**Lección:** *Kubernetes permite desplegar aplicaciones de forma escalable y portable, pero amplía la superficie de ataque; dominar sus objetos y sus controles de acceso es imprescindible para asegurarlo.*

**MITRE ATT&CK:** T1078 (Valid Accounts).

**Fuente:** [TryHackMe - Intro to Kubernetes](https://tryhackme.com/room/introtokubernetes)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.