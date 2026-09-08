# K8s Best Security Practices

| **Dificultad** | Medium |
|---|---|
| **Tipo** | Walkthrough |
| **Slug** | k8sbestsecuritypractices |
| **Link** | [TryHackMe](https://tryhackme.com/room/k8sbestsecuritypractices) |
| **Sección** | 02 Level Medium |
| **Fuente** | [TryHackMe - K8s Best Security Practices](https://tryhackme.com/room/k8sbestsecuritypractices) |
| **Componentes** | Kubernetes, ServiceAccounts, RBAC (Roles/RoleBindings/ClusterRoles), API Requests (Authentication, Authorisation, Admission Controllers), Image Scanning, allowPrivilegeEscalation, cifrado de etcd, cluster upgrades, kubectl + base64 |
| **Impacto** | Aprender y aplicar las mejores prácticas de seguridad a nivel de clúster Kubernetes: control de acceso granular mediante RBAC, endurecimiento de ServiceAccounts, protección de los diferentes stages de la API y buenas prácticas de CI/CD y endurecimiento de etcd. |

---

**Contexto:**
Este room está pensado para aspirantes a DevSecOps y entusiastas de Kubernetes que ya conocen lo básico. Se centra en qué hacer DESPUÉS de crear un clúster seguro: cómo mantenerlo seguro. Se exploran los ServiceAccounts, su correcta implementación de acceso (RBAC: Roles, RoleBindings, ClusterRoles, ClusterRoleBindings), el ciclo de vida de una petición a la API de Kubernetes y varias buenas prácticas adicionales. Como prerequisitos están los rooms Intro to Containerisation, Intro to Docker y Container Hardening.

**Herramientas:** `kubectl`, YAML manifests. En el task práctico se usa `kubectl describe role <name> -n <namespace>` y la codificación del resultado con base64.

## Solucionario

### Task 1: Introduction

**Explicación:**
El room introduce los objetivos de aprendizaje: entender por qué implementar buenas prácticas de seguridad en Kubernetes, la función de los ServiceAccounts (y sus mejores prácticas), cómo definir roles y RoleBindings para implementar RBAC en el clúster, y cómo entender las peticiones a la API de Kubernetes. No hay pregunta que responder aparte de continuar.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Click to continue to the next task! | `No answer needed` |

### Task 2: ServiceAccounts

**Explicación:**
Un ServiceAccount es una identidad de Kubernetes usada por los Pods (procesos en contenedores) para autenticarse contra la API. Sus credenciales se guardan como **secrets**. Son identidades *Lightweight* (sin uso interno de tokens de corta duración), *Namespaced* (asociadas a un namespace) y **Portable** (se pueden montar y usar en distintos pods/manifests). Un pod referencia su ServiceAccount mediante `serviceAccountName` en el `spec`.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: example-pod
  namespace: example-namespace
spec:
  serviceAccountName: example-sa
  containers:
  - name: example-container
    image: nginx:latest
```

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | What are the credentials associated with a ServiceAccount stored as? | `secrets` |
| 2 | Kubernetes ServiceAccounts are Lightweight, Namespaced and which other attribute? | `Portable` |

### Task 3: RBAC

**Explicación:**
RBAC (Role-Based Access Control) prepara el clúster para el peor escenario: si un atacante obtiene acceso autenticado (pod/aplicación o usuario), solo podrá hacer lo que sus permisos le permitan. Un **Role** define permisos dentro de un namespace; para vincularlo a una identidad (usuario, grupo o ServiceAccount) se usa un **RoleBinding**. A nivel de clúster se usa **ClusterRole** (y ClusterRoleBinding). Dentro de la sección `rules`, el campo **verbs** define las acciones (get, list, watch, create, delete...) y el campo **resources** define sobre qué recursos se aplican (pods, secrets, services...).

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: example-namespace
  name: example-role
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["get", "list", "watch"]
```

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | You have defined a "Role". What should you now define to associate that role with an identity? | `RoleBinding` |
| 2 | You now want to define permissions at a cluster level; what do you define? | `ClusterRole` |
| 3 | In which field under "rules" would you define the actions that can be performed on a resource? (in the role YAML/spec) | `verbs` |
| 4 | In which field under "rules" would you define to what those actions should be applied? (in the role YAML/spec) | `resources` |

### Task 4: API Requests in Kubernetes

**Explicación:**
Para asegurar cualquier cosa es fundamental entender cómo se accede. Una petición a la API de Kubernetes pasa por varias fases:

1. **Authentication**: verificar físicamente quién es el que realiza la petición (certificados de cliente, token de ServiceAccount, etc.).
2. **Authorisation**: RBAC decide si esa identidad tiene permiso (aquí interviene RBAC).
3. **Admission Controllers**: hooks que pueden mutar o validar la petición antes de que persista (aquí aparecen las palabras "Mutating" y "Validating").

El método de acceso por **Auth Token** transmite el token de autenticación en claro, por lo que es vulnerable a un ataque **MITM** (hombres en el medio) si el tráfico no viaja cifrado. Un ServiceAccount token se usa en la fase de Authentication para verificar la identidad del ServiceAccount.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Which cluster access method would be vulnerable to a MITM attack? | `Auth Token` |
| 2 | Which API request stage would RBAC be involved in? | `Authorisation` |
| 3 | In which API request stage would we find the words "Mutating" and "Validating"? | `Admission Controllers` |
| 4 | In which API request stage would a ServiceAccount token be used to verify a ServiceAccount? | `Authentication` |

### Task 5: More Best Security Practices

**Explicación:**
Buenas prácticas adicionales a nivel de clúster:

- **Image Scanning**: introducir el escaneo de imágenes en el pipeline CI/CD para detectar vulnerabilidades en las imágenes (y en sus dependencias) antes del despliegue.
- **allowPrivilegeEscalation**: ponerlo a `false` en la configuración del securityContext del contenedor impide que un contenedor pueda escalar privilegios (no_root_squash, setuid...).
- **etcd**: además de aislarlo y protegerlo tras un firewall, debe estar **encrypted** (usar mecanismos de cifrado at rest o un encryption provider), porque contiene todos los secrets del clúster.
- **Cluster upgrades**: Kubernetes solo soporta saltos de una versión menor a la vez, por lo que ir de la 1.21 a la 1.25 requiere **4** upgrades (1.22, 1.23, 1.24, 1.25).

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Which best security practice should be introduced to the CI/CD pipeline? | `Image Scanning` |
| 2 | What should be set as "false" in configuration to ensure a container cannot have its privileges escalated? | `allowPrivilegeEscalation` |
| 3 | To ensure the security of etcd, it should be isolated, behind a firewall and? | `encrypted` |
| 4 | How many cluster upgrades would you have to do to go from version 1.21 to 1.25 | `4` |

### Task 6: Practical

**Explicación:**
Task práctico (máquina desplegable): en "Kubernetes Laboratories" hay que revisar los permisos de un rol:

1) Revisa/valida el rol `pod-checker-role`.
2) Utiliza el ServiceAccount `pod-checker` con el `pod-checker-role`.
3) Crea un RoleBinding que una `pod-checker-role` al ServiceAccount `pod-checker`.
4) Elimina el pod `pod-status-checker`.
5) Modifica `~/Documents/pod-config/pod-checker.yaml` para que el pod use el ServiceAccount `pod-checker` en vez de `pod-admin` y aplica la config.

Para completar el task, se describe el rol creado y se codifica su salida en base64:

```
thm@k8s:~ $ kubectl describe role pod-checker-role -n test-chambers
```

```base64
TmFtZTogICAgICAgICBwb2QtY2hlY2tlci1yb2xlCkxhYmVsczogICAgICAgPG5vbmU+CkFubm90YXRpb25zOiAgPG5vbmU+ClBvbGljeVJ1bGU6CiAgUmVzb3VyY2VzICBOb24tUmVzb3VyY2UgVVJMcyAgUmVzb3VyY2UgTmFtZXMgIFZlcmJzCiAgLS0tLS0tLS0tICAtLS0tLS0tLS0tLS0tLS0tLSAgLS0tLS0tLS0tLS0tLS0gIC0tLS0tCiAgcG9kcyAgICAgICBbXSAgICAgICAgICAgICAgICAgW10gICAgICAgICAgICAgIFtnZXQgbGlzdF0=
```

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | What's the encoded role? | `TmFtZTogICAgICAgICBwb2QtY2hlY2tlci1yb2xlCkxhYmVsczogICAgICAgPG5vbmU+CkFubm90YXRpb25zOiAgPG5vbmU+ClBvbGljeVJ1bGU6CiAgUmVzb3VyY2VzICBOb24tUmVzb3VyY2UgVVJMcyAgUmVzb3VyY2UgTmFtZXMgIFZlcmJzCiAgLS0tLS0tLS0tICAtLS0tLS0tLS0tLS0tLS0tLSAgLS0tLS0tLS0tLS0tLS0gIC0tLS0tCiAgcG9kcyAgICAgICBbXSAgICAgICAgICAgICAgICAgW10gICAgICAgICAgICAgIFtnZXQgbGlzdF0=` |

### Task 7: Conclusion

**Explicación:**
Resumen de las lecciones: el **Image Scanning** debe integrarse en CI/CD para evitar que imágenes vulnerables desplieguen malware en el clúster; **upgrading** mantiene el clúster con los últimos parches; para limitar la escalada de privilegios los contenedores deben correr **sin privilegios root**; y el **etcd** debe estar **aislado, tras un firewall y cifrado**. Con esto el room queda completado.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | All done! | `No answer needed` |

---

**Metodología:**
Fundamentos de seguridad de Kubernetes → ServiceAccounts → RBAC (Roles/RoleBindings/ClusterRoles) → flujo de peticiones a la API (Authentication → Authorisation → Admission Controllers) → buenas prácticas adicionales (image scanning, allowPrivilegeEscalation, cifrado de etcd, upgrades) → implementación práctica con kubectl.

**Learning chain:**
Identity (ServiceAccount + secrets) → permissions (Role/ClusterRole + verbs/resources) → binding (RoleBinding/ClusterRoleBinding) → API request stages (Auth Token/MITM → Authorisation → Admission Controllers) → CI/CD image scanning → hardening (allowPrivilegeEscalation=false, etcd encrypted, minor upgrades) → practical kubectl describe role + base64 encode.

**MITRE ATT&CK:**
T1078 (Valid Accounts), T1548 (Abuse Elevation Control Mechanism), T1552.001 (Unsecured Credentials: Files - secrets en etcd), T1204 (User Execution), T1195 (Supply Chain Compromise - imágenes), T1505 (Server Software Component), T1046 (Network Service Discovery).

**Fuente:** [TryHackMe - K8s Best Security Practices](https://tryhackme.com/room/k8sbestsecuritypractices)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
