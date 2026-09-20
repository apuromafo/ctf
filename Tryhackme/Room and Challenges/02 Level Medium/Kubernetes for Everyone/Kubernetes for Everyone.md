# Kubernetes for Everyone

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF / Cloud (Kubernetes) | kubernetesforeveryone | https://tryhackme.com/room/kubernetesforeveryone | 02 Level Medium | TryHackMe | Kubernetes, kubectl, Pods, Secrets | Ejecución en pods y exfiltración de secrets de un clúster Kubernetes |

---

**Contexto:** La sala **Kubernetes for Everyone** es un CTF orientado a **Kubernetes**: se despliega un clúster con pods mal configurados. El atacante accede mediante SSH/credenciales provisionadas, utiliza `kubectl` para interactuar con el clúster, ejecuta comandos dentro de los pods (`exec`) y lee los **Secrets** que contienen las flags. La resolución combina administración de clúster, enumeración de recursos y abuso de permisos excesivos en el service account.

## Solucionario

### Task 1: Credenciales de acceso
**Explicación:**

Se accede a la máquina con las credenciales provisionadas para el usuario del reto, preparando el entorno para usar `kubectl` contra el clúster.

1. `vagrant`
2. `hereiamatctf907`

Respuesta:

1. `vagrant`
2. `hereiamatctf907`

### Task 2: Primer secret
**Explicación:**

Con el acceso al clúster se enumeran namespaces, pods y secrets. La primera flag reside en un secret del clúster.

```bash
kubectl get secrets --all-namespaces
kubectl get secret <nombre> -n <namespace> -o yaml
echo <valor-base64> | base64 -d
```

Respuesta: `THM{yes_there_$s_no_$ecret}`

### Task 3: Segundo secret
**Explicación:**

Se continúa la enumeración de secrets y se accede a otro namespace o recurso con la segunda flag oculta.

Respuesta: `THM{this_joke_is_cold_joke}`

### Task 4: Flag final
**Explicación:**

Se localiza el último artefacto del reto (una palabra clave/CPE). La flag se obtiene tras completar la cadena completa de exploración del clúster.

Respuesta: `chidori`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Usuario de acceso | `vagrant` |
| 1 | Contraseña de acceso | `hereiamatctf907` |
| 2 | Primer secret | `THM{yes_there_$s_no_$ecret}` |
| 3 | Segundo secret | `THM{this_joke_is_cold_joke}` |
| 4 | Flag final | `chidori` |

---

**Metodología:** Acceso SSH al nodo → configuración de `kubectl` → enumeración de namespaces/pods/secrets → lectura de secrets en base64 → decodificación → obtención de las flags del clúster.

**Learning chain:** Credenciales → kubectl → recursos del clúster → secrets → decodificación → flags.

**Lección:** *En Kubernetes los secrets se almacenan en base64, no cifrados: un service account con permisos de lectura sobre secrets compromete todo el clúster.*

**MITRE ATT&CK:** T1552.001 Unsecured Credentials: Credentials In Files · T1087.004 Account Discovery: Cloud Account · T1555 Credentials from Password Stores.

**Fuente:** [TryHackMe - Kubernetes for Everyone](https://tryhackme.com/room/kubernetesforeveryone)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.