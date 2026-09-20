# Secure GitOps

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `securegitops` | [TryHackMe](https://tryhackme.com/room/securegitops) | `01 Level Easy` | THM | GitOps, Argo CD, Kubernetes, seccomp, security context | Resolución completa del reto Secure GitOps |

---

**Contexto:** Room sobre GitOps aplicado a Kubernetes y su endurecimiento: se repasa Argo CD como herramienta declarativa de sincronización, el role de Kubernetes en el despliegue y mecanismos de seguridad como el security context, runAsNonRoot y los perfiles seccomp.

> **ES:** Repaso de GitOps en Kubernetes: Argo CD (sincronización declarativa), seguridad de los contenedores con security context, runAsNonRoot y perfiles seccomp, hasta recuperar los valores de la room.
> **EN:** Review of GitOps on Kubernetes: Argo CD (declarative synchronisation), container security with security context, runAsNonRoot and seccomp profiles, ending with the room values.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Tarea inicial de despliegue: no requiere respuesta técnica más allá de comenzar la room.

1. No answer needed

### Task 2: Herramienta de GitOps / GitOps tool

**Explicación:** Se identifica Argo CD como la herramienta de despliegue continuo y se destaca el modelo declarativo que usa Git como fuente de verdad.

1. Argo CD
2. declarative

### Task 3: Plataforma y sincronización / Platform and synchronization

**Explicación:** Se reconoce Kubernetes como la plataforma sobre la que se despliega y la sincronización automatizada como el mecanismo que mantiene el estado real igual al deseado.

1. Kubernetes
2. automated synchronisation

### Task 4: Seguridad de la configuración / Configuration security

**Explicación:** Se responde el concepto de seguridad que define los permisos del pod en el manifiesto.

4. security context

### Task 5: Estado y perfiles de seguridad / State and security profiles

**Explicación:** Se completan los valores observados en el despliegue: el estado sincronizado, runAsNonRoot, el perfil seccomp y la versión del kernel y el hash del sistema afectado.

1. synced
2. runAsNonRoot
3. seccompProfile
4. 5.15.0-1066-aws
5. a22f5a6

### Tabla unificada de preguntas y respuestas

| Task | Pregunta | Respuesta |
|---|---|---|
| 1.1 | Despliegue y arranque de la room | `No answer needed` |
| 2.1 | Herramienta de GitOps usada | `Argo CD` |
| 2.2 | Modelo de configuración de la herramienta | `declarative` |
| 3.1 | Plataforma de despliegue | `Kubernetes` |
| 3.2 | Mecanismo de puesta al día del estado | `automated synchronisation` |
| 4.1 | Definición de seguridad del manifiesto | `security context` |
| 5.1 | Estado del despliegue | `synced` |
| 5.2 | Opción de no ejecutar como root | `runAsNonRoot` |
| 5.3 | Perfil de seguridad del sistema | `seccompProfile` |
| 5.4 | Versión del kernel | `5.15.0-1066-aws` |
| 5.5 | Hash del sistema | `a22f5a6` |

---

**Metodología:** 1) Desplegar la room. 2) Identificar la herramienta de GitOps (Argo CD) y su modelo declarativo. 3) Reconocer Kubernetes y la sincronización automatizada. 4) Revisar la configuración de seguridad del pod (security context). 5) Leer el estado del despliegue y los perfiles de seguridad para completar los valores.

### Cadena de ataque / Attack Chain

```text
Room desplegada -> Argo CD (declarativo) -> Kubernetes + sincronización automatizada -> security context -> estado synced -> runAsNonRoot + seccompProfile -> 5.15.0-1066-aws / a22f5a6
```

**Learning chain:** GitOps fundamentals -> Argo CD declarativo -> Kubernetes y sincronización -> security context (runAsNonRoot, seccomp) -> lectura del estado del despliegue

**Lección:** *En GitOps la infraestructura se trata como código: herramientas declarativas como Argo CD junto a controles de seguridad por manifiesto (security context, runAsNonRoot, seccomp) permiten auditar y endurecer los despliegues de Kubernetes.*

**MITRE ATT&CK:** T1204 (User Execution), T1083 (File and Directory Discovery), T1068 (Exploitation for Privilege Escalation)

**Fuente:** [TryHackMe - Secure GitOps](https://tryhackme.com/room/securegitops)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.