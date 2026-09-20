# AI in Security - old sAInt nick

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | challenge | `AIforcyber-aoc2025-y9wWQ1zRgB` | https://tryhackme.com/room/AIforcyber-aoc2025-y9wWQ1zRgB | Advent of Cyber 2025 | THM | AI security, LLM agents, SQLi exploit | Todas las preguntas resueltas, Writeup completo |

---

**Contexto:** Durante el Advent of Cyber 2025 (Día 4), Santa despliega un "AI Showcase" donde un agente de IA de red team automatiza el análisis de aplicaciones web vulnerables. El reto combina una demo interactiva del agente con un exploit real de SQL injection entregado por el propio agente. El objetivo es completar la showcase para obtener la bandera de validación y posteriormente ejecutar el payload proporcionado para demostrar el impacto real en el host `MACHINE_IP:5000`.

> **ES:** Un agente IA de red team automatiza el recon y la explotación: primero se completa la demo (flag de showcasing) y luego se ejecuta el payload SQLi que el propio agente generó.
> **EN:** A red team AI agent automates recon and exploitation: first complete the showcase (validation flag) and then run the SQLi payload that the agent itself generated.

## Solucionario

### Task 1: Escaparate de IA / AI Showcase

**Explicación:** Se interactúa con la demo del agente de IA (red team): hay que avanzar por todos los stages del showcase hasta que el agente identifica la aplicación vulnerable y entrega el payload de SQL injection. Completar todos los pasos de la demo presenta la flag de validación.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Complete the AI showcase by progressing through all of the stages. What is the flag presented to you? | `THM{AI_MANIA}` |

### Task 2: Explotar la aplicación vulnerable / Exploiting the Vulnerable Application

**Explicación:** Se toma el exploit generado por el agente de IA contra la aplicación web vulnerable alojada en `MACHINE_IP:5000`. Al ejecutar el script, su salida revela la flag, demostrando que el agente fue capaz de identificar y explotar la inyección SQL de forma autónoma.

```bash
# payload de SQLi proporcionado por el agente de IA
python3 <exploit_generado> --host http://MACHINE_IP:5000
# la salida del script incluye la flag de explotación
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Execute the exploit provided by the red team agent against the vulnerable web application hosted at MACHINE_IP:5000. What flag is provided in the script's output after it? | `THM{SQLI_EXPLOIT}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Complete the AI showcase by progressing through all of the stages. What is the flag presented to you? | `THM{AI_MANIA}` |
| 2 | Execute the exploit provided by the red team agent against the vulnerable web application hosted at MACHINE_IP:5000. What flag is provided in the script's output after it? | `THM{SQLI_EXPLOIT}` |

---

**Metodología:** El flujo empieza en la demo del agente de IA (red team), donde avanzamos por los distintos stages del showcase hasta que el agente entrega el payload de SQLi. Completar todos los pasos de la showcase otorga la primera bandera. Luego tomamos el script de exploit generado por el agente y lo ejecutamos contra la app vulnerable en el puerto 5000; la salida del script revela la segunda bandera, demostrando que la IA fue capaz de identificar y explotar una inyección SQL de forma autónoma.

### Cadena de ataque / Attack Chain

```text
AI Showcase (stages) -> el agente IA hace recon y detecta la app vulnerable -> entrega payload SQLi -> flag de showcase (THM{AI_MANIA}) -> ejecutar exploit contra MACHINE_IP:5000 -> flag de explotación (THM{SQLI_EXPLOIT})
```

**Learning chain:** AI agents de red team → automatización de recon → generación de exploits → SQL injection → validación del compromiso en producción.

**Lección:** *Un agente IA puede automatizar el ciclo completo de ataque (descubrir, explotar y validar); saber revisar y ejecutar sus entregables con cuidado es la nueva habilidad del pentester.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1059 (Command and Scripting Interpreter), T1189 (Drive-by Compromise), T1112 (hunting via agentic IA).

**Fuente:** [TryHackMe - AI in Security - old sAInt nick](https://tryhackme.com/room/AIforcyber-aoc2025-y9wWQ1zRgB)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.