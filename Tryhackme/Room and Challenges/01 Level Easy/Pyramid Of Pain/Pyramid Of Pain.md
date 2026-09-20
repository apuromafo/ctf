# Pyramid Of Pain

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `pyramidofpain` | https://tryhackme.com/room/pyramidofpain | 01 Level Easy | THM | IOCs, Threat Hunting, Hash values, IPs, Domains, Host/Network artifacts, Tools, TTPs | Detección y respuesta ante indicadores de compromiso |

---

**Contexto:** Room teórico-práctico que presenta la pirámide del dolor de David Bianco: un modelo que clasifica los indicadores de compromiso (IOCs) por nivel de dificultad para el atacante (hash values, IPs, domain names, host artifacts, network artifacts, tools, TTPs) y su impacto en la caza de amenazas y respuesta a incidentes.

> **ES:** Room teórico-práctico que presenta la pirámide del dolor de David Bianco: un modelo que clasifica los indicadores de compromiso (IOCs) por nivel de dificultad para el atacante (hash values, IPs, domain names, host artifacts, network artifacts, tools, TTPs) y su impacto en la caza de amenazas y respuesta a incidentes.
> **EN:** A theoretical-practical room presenting David Bianco's pyramid of pain: a model classifying indicators of compromise (IOCs) by the difficulty they impose on the attacker (hash values, IPs, domain names, host artifacts, network artifacts, tools, TTPs) and their impact on threat hunting and incident response.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Se presenta la pirámide del dolor y el objetivo del room: entender cómo los indicadores de compromiso dificultan (o no) el trabajo del adversario.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Let's get started | `No answer needed` |

### Task 2: Valores hash (Trivial) / Hash Values (Trivial)

**Explicación:** Se explica la capa base de la pirámide: los hash únicos de archivos maliciosos. Se recupera el archivo malicioso entregado por el atacante para identificarlo por su hash hash único.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the name of the file retrieved by the attacker? | `Sales_Receipt 5606.xls` |

### Task 3: Direcciones IP (Fácil) / IP Address (Easy)

**Explicación:** Se analizan las direcciones IP de origen/C2: se identifican el endpoint malicioso y la IP asociada a la infraestructura del adversario.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the IP address of the malicious connection? | `50.87.136.52` |
| 2 | What is the domain name resolved by the malicious IP? | `craftingalegacy.com` |

### Task 4: Nombres de dominio (Simple) / Domain Names (Simple)

**Explicación:** Se estudia la capa de dominios: identificar el C2 por dominio, entender por qué el dominio es un indicador más difícil de cambiar y los ataques de Punycode que crean dominios "lookalike".

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the domain name of the identified C2 infrastructure? | `craftingalegacy.com` |
| 2 | What type of indicator is a domain name? | `Domain Name` |
| 3 | What is the attack that takes advantage of confusing look-alike domains using Punycode? | `Punycode attack` |
| 4 | Which URL points to the legitimate version of the domain? | `https://tryhackme.com/` |

### Task 5: Artefactos del host (Molesto) / Host Artifacts (Annoying)

**Explicación:** Se identifican los artefactos que el malware deja en el host (archivos, entradas de registro, tareas, procesos). Se detectan los procesos y archivos maliciosos en el endpoint afectado.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Identify the host artifacts on the endpoint | `No answer needed` |
| 2 | What is the IP address associated with the host artifacts? | `96.126.101.6` |
| 3 | What is the name of the malicious executable left on the host? | `G_jugk.exe` |
| 4 | How many steps does it take to fully block the host artifact? | `9` |

### Task 6: Artefactos de red (Molesto) / Network Artifacts (Annoying)

**Explicación:** Se analizan los artefactos de red (user-agents, servidores C2, URI patterns): se examina un pcap y se identifica desde qué navegador se originó el tráfico.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the user-agent (browser) seen in the network artifact? | `Internet Explorer` |
| 2 | How many steps does it take to block the network artifact? | `6` |

### Task 7: Herramientas (Desafiante) / Tools (Challenging)

**Explicación:** Se analiza la capa de herramientas: se usa fuzzy hashing (ssdeep) para comparar artefactos maliciosos por similitud y crear firmas que detecten variantes del mismo malware.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the name of the hashing technique that compares files by similarity? | `Fuzzy Hashing` |
| 2 | What technique is used by ssdeep to produce similarity scores based on file chunks? | `context triggered piecewise hashes` |

### Task 8: TTPs (Difícil) / TTPs (Tough)

**Explicación:** Se estudia la cima de la pirámide: las TTPs (tácticas, técnicas y procedimientos) del adversario. Es la capa más difícil de cambiar para el atacante.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | How many steps does it take to block the TTP? | `9` |
| 2 | What is the name of the C2 framework used by the adversary? | `Cobalt Strike` |

### Task 9: Práctica: La Pirámide del Dolor / Practical: The Pyramid of Pain

**Explicación:** Se completa el reto práctico interactivo que aplica todas las capas de la pirámide, revelando la flag final.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag of the practical challenge? | `THM{PYRAMIDS_COMPLETE}` |

### Task 10: Conclusión / Conclusion

**Explicación:** Se cierra el room con un resumen de cómo aplicar la pirámide en operaciones de threat hunting y detección.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Finish the room | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Let's get started | `No answer needed` |
| 2 | What is the name of the file retrieved by the attacker? | `Sales_Receipt 5606.xls` |
| 3 | What is the IP address of the malicious connection? | `50.87.136.52` |
| 4 | What is the domain name resolved by the malicious IP? | `craftingalegacy.com` |
| 5 | What is the domain name of the identified C2 infrastructure? | `craftingalegacy.com` |
| 6 | What type of indicator is a domain name? | `Domain Name` |
| 7 | What is the attack that takes advantage of confusing look-alike domains using Punycode? | `Punycode attack` |
| 8 | Which URL points to the legitimate version of the domain? | `https://tryhackme.com/` |
| 9 | Identify the host artifacts on the endpoint | `No answer needed` |
| 10 | What is the IP address associated with the host artifacts? | `96.126.101.6` |
| 11 | What is the name of the malicious executable left on the host? | `G_jugk.exe` |
| 12 | How many steps does it take to fully block the host artifact? | `9` |
| 13 | What is the user-agent (browser) seen in the network artifact? | `Internet Explorer` |
| 14 | How many steps does it take to block the network artifact? | `6` |
| 15 | What is the name of the hashing technique that compares files by similarity? | `Fuzzy Hashing` |
| 16 | What technique is used by ssdeep to produce similarity scores based on file chunks? | `context triggered piecewise hashes` |
| 17 | How many steps does it take to block the TTP? | `9` |
| 18 | What is the name of the C2 framework used by the adversary? | `Cobalt Strike` |
| 19 | What is the flag of the practical challenge? | `THM{PYRAMIDS_COMPLETE}` |
| 20 | Finish the room | `No answer needed` |

---

**Metodología:** Leer cada capa de la pirámide, identificar el IOC correspondiente (hash, IP, dominio, artefacto host/network, tool, TTP), contestar las preguntas de análisis y completar la práctica interactiva.

### Cadena de ataque / Attack Chain

```text
Identificar archivo malicioso (hash) → IP/C2 (50.87.136.52) → dominio (craftingalegacy.com) → artefactos host (G_jugk.exe) y de red (IE) → herramientas (fuzzy hashing) → TTPs (Cobalt Strike) → práctica → flag
```

**Learning chain:** Introducción → Hash values → IP Address → Domain Names → Host Artifacts → Network Artifacts → Tools → TTPs → Practical challenge → Conclusion

**Lección:** *Cuanto más arriba en la pirámide del dolor se bloquee (TTPs), mayor será el coste que impongas al atacante. Los IOCs triviales (hashes, IPs) se cambian fácilmente, por eso la detección debe centrarse en las TTPs y en postura que observe el comportamiento, no solo los valores estáticos.*

**MITRE ATT&CK:** T1059 (Command and Scripting Interpreter), T1071 (Application Layer Protocol)

**Fuente:** [TryHackMe - Pyramid Of Pain](https://tryhackme.com/room/pyramidofpain)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.