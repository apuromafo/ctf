# K8s Runtime Security

| **Dificultad** | MEDIUM | **Tipo** | Walkthrough (Containers/K8s Security) | **Slug** | `k8sruntimesecurity` |
| **Link** | [TryHackMe](https://tryhackme.com/room/k8sruntimesecurity) | **Sección** | 02 Level Medium | **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | Kubernetes / Falco / eBPF / Syscalls / Seccomp / Runtime Security / Falcosidekick | **Impacto** | Evalúa la detección de amenazas en runtime de contenedores con Falco y la cadena de alertas |

---

**Contexto:** Sala de seguridad en runtime para Kubernetes centrada en Falco: cómo detectar actividad maliciosa dentro de los contenedores mediante system calls y eBPF. Cubre los componentes de Falco (event sources: syscall/plugin), las bases de reglas (rules, fields, macros, lists, condition/output/priority), la arquitectura de detección (Event Stream, Kernel Module/eBPF probe, gVisor) y la cadena de alertas (Grafana, Prometheus, Falcosidekick). Incluye un reto final de crear una regla personalizada para detectar `curl` y obtener la flag.

## Solucionario

### Task 1: Introducción

**Explicación:** Tarea de puesta en marcha de la sala; no requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Pregunta introductoria | `No answer needed` |

### Task 2: Fundamentos de Falco

**Explicación:** Falco observa eventos de distintos tipos. Preguntas sobre las fases de la arquitectura de Falco: eventos, filtros, rules y uso de metadata para enriquecer el contexto de las alertas.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Fase 1 de la arquitectura Falco | `ResponseStarted` |
| 2 | Fase 2 de la arquitectura Falco | `RequestResponse` |
| 3 | Fase 3 de la arquitectura Falco | `rule` |
| 4 | Fase 4 de la arquitectura Falco | `Metadata` |

### Task 3: El stack de detección

**Explicación:** Falco como runtime security (70 librerías), el origen de los eventos (system calls) y la tecnología de captura a nivel kernel (eBPF/seccomp).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Número de librerías de Falco | `70` |
| 2 | Fuente primaria de eventos en Falco | `System Calls` |
| 3 | Mecanismo de filtrado a nivel kernel | `Seccomp` |

### Task 4: Reglas de Falco

**Explicación:** Las reglas definen la detección: fuentes de logs (Audit Logs), motor de captura (eBPF) y las condiciones que activan las alertas (rules).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Fuente de logs usada por Falco en Kubernetes | `Audit Logs` |
| 2 | Tecnología de captura | `eBPF` |
| 3 | Elemento de Falco que define la condición de detección | `rules` |

### Task 5: Sintaxis de reglas

**Explicación:** Las reglas se escriben con una condición (por ejemplo `proc.name = bash`), y reutilizan estructuras como lists y macros para agrupar valores y condiciones.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Ejemplo de condición: `proc.name = bash` | `proc.name = bash` |
| 2 | Listas de valores agrupados en Falco | `Lists` |
| 3 | Reutilización de condiciones en Falco | `Macros` |

### Task 6: Configuración de salida y alertas

**Explicación:** Falco puede emitir alertas a distintos canales de observabilidad: Grafana (visualización/dashboards), Prometheus (métricas) y Falcosidekick (integración/forwarding de alertas).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Herramienta de dashboards/visualización | `Grafana` |
| 2 | Sistema de métricas | `Prometheus` |
| 3 | Conector/forwarder de alertas de Falco | `Falcosidekick` |

### Task 7: Reto — regla personalizada

**Explicación:** Reto integrador: crear una regla personalizada de Falco que detecte el uso del comando `curl` dentro de un contenedor, y responder con la regla codificada en base64 y la flag del challenge.

Regla en claro (base64 decodificada):
```yaml
- rule: Detect Usage of Curl
  desc: Detects when the curl command is used inside a container.
  condition: >
    container.id != host and
    proc.name = curl and
    evt.type = execve
  output: >
    Curl command used in container (user=%user.name container=%container.name
    shell=%proc.name parent=%proc.pname cmdline=%proc.cmdline)
  priority: WARNING
  tags: [network, command, security]
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Regla Falco personalizada en base64 | `ICAGIC0gcnVsZTogRGV0ZWN0IFVzYWdlIG9mIEN1cmwKICAgICAgZGVzYzogRGV0ZWN0cyB3aGVuIHRoZSBjdXJsIGNvbW1hbmQgaXMgdXNlZCBpbnNpZGUgYSBjb250YWluZXIuCiAgICAgIGNvbmRpdGlvbjogPgogICAgICAgIGNvbnRhaW5lci5pZCAhPSBob3N0IGFuZAogICAgICAgIHByb2MubmFtZSA9IGN1cmwgYW5kCiAgICAgICAgZXZ0LnR5cGUgPSBleGVjdmUKICAgICAgb3V0cHV0OiA+CiAgICAgICAgQ3VybCBjb21tYW5kIHVzZWQgaW4gY29udGFpbmVyICh1c2VyPSV1c2VyLm5hbWUgY29udGFpbmVyPSVjb250YWluZXIubmFtZQogICAgICAgIHNoZWxsPSVwcm9jLm5hbWUgcGFyZW50PSVwcm9jLnBuYW1lIGNtZGxpbmU9JXByb2MuY21kbGluZSkKICAgICAgcHJpb3JpdHk6IFdBUk5JTkcKICAgICAgdGFnczogW25ldHdvcmssIGNvbW1hbmQsIHNlY3VyaXR5XSAgCg==` |
| 2 | Flag del reto | `THM{th3_c4k3_1s_a_l13}` |

### Task 8: Conclusión

**Explicación:** Cierre de la sala; no requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Pregunta de cierre | `No answer needed` |

---

**Metodología:**
1. Comprender la arquitectura de Falco: event sources (syscall/plugin), fases del pipeline y metadata de enriquecimiento.
2. Revisar el stack de detección: paquetes del sistema, system calls, eBPF y seccomp.
3. Aprender el modelo de reglas de Falco: condition/output/priority, lists, macros y campos.
4. Configurar la cadena de alertas con Grafana, Prometheus y Falcosidekick.
5. Escribir una regla personalizada de detección de `curl` en contenedor y validar la flag.

**Learning chain:** Arquitectura Falco (event sources/metadata) → Stack detección (70 libs / syscalls / eBPF / seccomp) → Reglas (rules, lists, macros) → Configuración de salida (Grafana/Prometheus/Falcosidekick) → Reto: regla personalizada curl → flag THM{th3_c4k3_1s_a_l13}

**Lección:** *Falco convierte los system calls del kernel en una visibilidad continua del runtime de Kubernetes: escribir buenas reglas (con lists, macros y fields) permite detectar herramientas como `curl` abusadas en contenedores antes de que el atacante exfiltre datos.*

**MITRE ATT&CK:** T1059 - Command and Scripting Interpreter; T1105 - Ingress Tool Transfer; T1204 - User Execution; T1046 - Network Service Discovery

**Fuente:** [TryHackMe - K8s Runtime Security](https://tryhackme.com/room/k8sruntimesecurity)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
