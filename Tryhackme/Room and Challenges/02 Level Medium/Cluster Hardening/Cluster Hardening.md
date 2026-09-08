# Cluster Hardening
| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `clusterhardening` |
| **Link** | [TryHackMe](https://tryhackme.com/room/clusterhardening) |
| **Sección** | 02 Level Medium |
| **Fuente** | TryHackMe |
| **Componentes** | Kubernetes, CIS Kubernetes Benchmarks, Kube-bench, Kubelet, Kube-apiserver, Admission Controllers (Mutating/Validating, EventRateLimit, Webhooks), NetworkPolicy, kubectl, base64 |
| **Impacto** | Implementa hardening de clústeres Kubernetes: benchmarks CIS, endurecimiento de Kubelet/API server, admission controllers y NetworkPolicies para restringir pod-to-pod, cerrando con un laboratorio práctico de una NetworkPolicy codificada en base64. |
---
**Contexto:** Sala de hardening de clústeres Kubernetes (DevSecOps). "Kubernetes Laboratories" necesita asegurar su clúster. Se repasan los componentes y mindset (security-first), los **security benchmarks** CIS (y Kube-bench para auditar el clúster), cómo asegurar **Kubelet** y el **kube-apiserver**, el uso de **admission controllers** y la restricción del tráfico **pod-to-pod** con **NetworkPolicy**. La práctica final pide crear una NetworkPolicy y entregar la parte `spec:` codificada en base64.
## Solucionario
### Task 1: Introduction
**Explicación:** Reto para DevSecOps: construir un clúster con prácticas de hardening siguiendo benchmarks CIS.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Familiarízate con el entorno de la sala. | `No answer needed` |
### Task 2: Kubernetes Cluster Hardening
**Explicación:** La arquitectura de Kubernetes está formada por el control plane y el plano de datos; al nivel más alto vive el **Kubernetes cluster** (que comprende todos los componentes de niveles inferiores). En el mundo del cyber, la mentalidad **Security-first** siempre es beneficiosa.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué vive el nivel más alto de la arquitectura Kubernetes y está compuesto por todos los componentes de nivel inferior? | `Kubernetes cluster` |
| 2 | ¿Qué mentalidad es siempre beneficiosa en el mundo de la ciberseguridad? | `Security-first` |
### Task 3: Security Benchmarks
**Explicación:** Para comprobar el nivel de seguridad de un clúster se usan **security benchmarks** (estándares). El benchmark CIS que asegura que el tráfico anónimo no está permitido es **4.2.1**. La herramienta open-source que automatiza la valoración de seguridad de un clúster es **Kube-bench**.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué estándares se usan para comprobar el nivel de seguridad de un clúster? | `security benchmarks` |
| 2 | ¿Qué benchmark de seguridad CIS asegura que el tráfico anónimo está deshabilitado? | `4.2.1` |
| 3 | ¿Qué herramienta open-source puede realizar valoraciones de seguridad automatizadas sobre un clúster de Kubernetes? | `Kube-bench` |
### Task 4: Kubelet Hardening
**Explicación:** Kubelet, el agente que corre en cada nodo, sirve la kubelet-api en el puerto **10250**, que permite acceso total si no se asegura. Para bloquear el tráfico no autorizado, el valor `authentication:anonymous:enabled` debe estar en `false`. Además de la "X509 Client Certificate Authentication", Kubelet acepta **API Bearer Token** como método de autenticación.
```yaml
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
authentication:
  anonymous:
    enabled: false
```
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿En qué puerto sirve Kubelet la kubelet-api y permite acceso total? | `10250` |
| 2 | ¿Qué valor debe ponerse en "false" para asegurar que el tráfico no autorizado queda bloqueado? | `authentication:anonymous:enabled` |
| 3 | Un método de autenticación de peticiones a Kubelet es la "X509 Client Certificate Authentication", ¿cuál es el otro? | `API Bearer Token` |
### Task 5: API Server Hardening
**Explicación:** El **Kube-apiserver** actúa tanto como "Server" como "Client" (es el frontend del control plane y el único componente que se comunica con etcd). Implementar TLS en las comunicaciones cubre los benchmarks CIS **1.2.24 - 27**.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué componente actúa a la vez como 'Server' y como 'Client'? | `Kube-apiserver` |
| 2 | ¿Qué benchmarks de seguridad CIS cubriría la implementación de TLS? | `1.2.24 - 27` |
### Task 6: Admission Controllers
**Explicación:** Los **Admission Controllers** interceptan las peticiones autenticadas antes de que se persistan los objetos. Un controller **Mutating** puede modificar el objeto de la petición que admite. **EventRateLimit** evita que la API se inunde con peticiones para almacenar nuevos eventos. Para estándares de seguridad personalizados o checks específicos de despliegue de pods, se usan **Admission Controller Webhooks**. Las dos built-ins que llaman a un webhook definido son **ValidatingAdmissionWebhook** y **MutatingAdmissionWebhook**.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué tipo de admission controller puede modificar el objeto relacionado con la petición que admite? | `Mutating` |
| 2 | ¿Qué admission controller built-in ayuda a evitar el problema de que la API de Kubernetes se inunde con peticiones para almacenar nuevos eventos? | `EventRateLimit` |
| 3 | ¿Qué se puede usar si tu organización quiere imponer estándares de seguridad personalizados o comprobaciones de despliegue de pods específicas de la organización? | `Admission Controller Webhooks` |
| 4 | ¿Cuáles son los nombres de los dos admission controllers built-in que llaman a un admission controller webhook definido? (Formato: Respuesta1, Respuesta2) | `ValidatingAdmissionWebhook, MutatingAdmissionWebhook` |
### Task 7: Network Policies
**Explicación:** El recurso de Kubernetes usado para restringir la comunicación pod-a-pod es la **NetworkPolicy**. Se aplica a nivel de namespace y filtra según las etiquetas del `podSelector`. Para restringir el tráfico hacia una app etiquetada como "database", la etiqueta se coloca en el campo `spec:PodSelector:matchLabels:app`. Definir NetworkPolicies en todos los namespaces cumple el benchmark CIS 5.3.2.
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: db-ingress-policy
spec:
  podSelector:
    matchLabels:
      app: database
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app: api
    ports:
    - protocol: TCP
      port: 8080
```
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué recurso de Kubernetes se usa para restringir la comunicación pod-a-pod? | `NetworkPolicy` |
| 2 | Si tenemos una app corriendo con la etiqueta "database", ¿en qué campo pondríamos esa etiqueta si quisiéramos restringir el tráfico hacia esa app? | `spec:PodSelector:matchLabels:app` |
### Task 8: Scenario: Network Policy (encoded policy)
**Explicación:** Ticket del escenario: solo `backend-service1` puede comunicarse con `backend-service2` (puerto 8888/TCP); todo el resto del tráfico ingress se rechaza. Se crea `network-policy.yaml`, se aplica y se comprueba con `kubectl describe networkpolicy allow-backend-service1-ingress`. Desde la línea `Spec:` hacia abajo (sin whitespace extra ni líneas al final) se codifica en base64. Respuesta (decodificada): perfil básico `Spec: PodSelector: app=backend-service2, Allow ingress traffic: To Port 8888/TCP From PodSelector app=backend-service1, Not affecting egress traffic, Policy Types: Ingress`.
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-backend-service1-ingress
spec:
  podSelector:
    matchLabels:
      app: backend-service2
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app: backend-service1
    ports:
    - protocol: TCP
      port: 8888
```
```bash
kubectl apply -f network-policy.yaml
kubectl describe networkpolicy allow-backend-service1-ingress
```
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la Policy codificada? | `U3BlYzoKICBQb2RTZWxlY3RvcjogICAgIGFwcD1iYWNrZW5kLXNlcnZpY2UyCiAgQWxsb3dpbmcgaW5ncmVzcyB0cmFmZmljOgogICAgVG8gUG9ydDogODg4OC9UQ1AKICAgIEZyb206CiAgICAgIFBvZFNlbGVjdG9yOiBhcHA9YmFja2VuZC1zZXJ2aWNlMQogIE5vdCBhZmZlY3RpbmcgZWdyZXNzIHRyYWZmaWMKICBQb2xpY3kgVHlwZXM6IEluZ3Jlc3M=` |
---
**Metodología:** Hardening de infraestructura cloud-native: revisión de config (Kubelet/apiserver), benchmarks CIS con Kube-bench, controles de admisión y NetworkPolicies, validando en un lab con kubectl.
**Learning chain:** Arquitectura Kubernetes → benchmarks CIS → hardening de Kubelet y API server → admission controllers → NetworkPolicy → aplicación práctica (lab) con verificación de tráfico pod-a-pod.
**MITRE ATT&CK:** T1204.003 (contexto), T1543 (Create or Modify System Process - servicios del plano de control), T1046 (Network Service Scanning - puertos kubelet), policy de red como mitigación (M1035 Limit Access to Resource Over Network).
**Fuente:** [TryHackMe - Cluster Hardening](https://tryhackme.com/room/clusterhardening)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
