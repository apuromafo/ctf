# Putting it all together

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `puttingitalltogether` | https://tryhackme.com/room/puttingitalltogether | 01 Level Easy | THM | Load balancers, CDN, WAF, DNS, Virtual Hosts | Integración del flujo web completo |

---

**Contexto:** Room de la ruta Pre-Security (How The Web Works) que integra los componentes vistos en módulos previos: load balancers, CDNs, WAFs, servidores web (virtual hosts, contenido estático/dinámico) y el flujo completo de una petición web desde el navegador hasta el backend.

> **ES:** Room de la ruta Pre-Security que integra los componentes del flujo web: load balancers, CDNs, WAFs, DNS y servidores web (virtual hosts, contenido estático/dinámico), cerrando con un quiz de ordenación del flujo de peticiones.
> **EN:** A Pre-Security Path room integrating the web flow components: load balancers, CDNs, WAFs, DNS and web servers (virtual hosts, static/dynamic content), closing with a quiz ordering the request flow.

## Solucionario

### Task 1: Poniendo todo junto / Putting It All Together

**Explicación:** Se introduce el módulo que une todos los componentes de la web: DNS, DNS records, caché (CDN), load balancers, WAFs y servidores web.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Let's get started on the path! | `No answer needed` |

### Task 2: Otros componentes / Other Components

**Explicación:** Se revisan los componentes adicionales que intervienen en el flujo web: la CDN para distribuir y cachear contenido, los health checks de los load balancers y el WAF que filtra el tráfico malicioso.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the name of the technology that caches and distributes website content closer to the user? | `CDN` |
| 2 | What does the load balancer use to confirm the servers are still running correctly? | `health check` |
| 3 | What filters traffic to protect the web server from attacks (e.g., SQL injection)? | `WAF` |

### Task 3: Cómo funcionan los servidores web / How Web Servers Work

**Explicación:** Se explica el funcionamiento de los servidores web: cómo los virtual hosts permiten alojar varios sitios en una misma máquina y la diferencia entre contenido estático y dinámico.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What allows multiple websites to run on a single server using the same IP? | `Virtual Hosts` |
| 2 | What type of content is generated on-the-fly (e.g., with PHP or Python)? | `Dynamic` |
| 3 | Dave only serves static content on his site. Does he need to configure virtual hosts? | `Nay` |

### Task 4: Quiz / Quiz

**Explicación:** Se completa el quiz final que ordena el flujo de una petición web (DNS → CDN → load balancer → WAF → servidor web) y entrega la flag de validación.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag at the end of the quiz? | `THM{YOU_GOT_THE_ORDER}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Let's get started on the path! | `No answer needed` |
| 2 | What is the name of the technology that caches and distributes website content closer to the user? | `CDN` |
| 3 | What does the load balancer use to confirm the servers are still running correctly? | `health check` |
| 4 | What filters traffic to protect the web server from attacks (e.g., SQL injection)? | `WAF` |
| 5 | What allows multiple websites to run on a single server using the same IP? | `Virtual Hosts` |
| 6 | What type of content is generated on-the-fly (e.g., with PHP or Python)? | `Dynamic` |
| 7 | Dave only serves static content on his site. Does he need to configure virtual hosts? | `Nay` |
| 8 | What is the flag at the end of the quiz? | `THM{YOU_GOT_THE_ORDER}` |

---

**Metodología:** Repasar los componentes del flujo web (DNS, CDN, load balancer, WAF, servidor web), diferenciar contenido estático/dinámico y virtual hosts, y resolver el quiz para demostrar el orden correcto de una petición.

### Cadena de ataque / Attack Chain

```text
Introducción a componentes → CDN/health check/WAF → virtual hosts y contenido estático/dinámico → ordenar flujo de petición → quiz → flag
```

**Learning chain:** Introducción → Otros componentes → Servidores web → Quiz

**Lección:** *Una petición web atraviesa múltiples capas (DNS, CDN, load balancer, WAF, servidor web). Comprender ese flujo completo es esencial para diagnosticar fallos, optimizar el rendimiento y ubicar dónde aplicar cada control de seguridad.*

**MITRE ATT&CK:** N/A (Room teórico de arquitectura web)

**Fuente:** [TryHackMe - Putting it all together](https://tryhackme.com/room/puttingitalltogether)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.