# Intermediate Nmap

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `intermediatenmap` | [TryHackMe](https://tryhackme.com/room/intermediatenmap) | 01 Level Easy | THM | Nmap, port scanning, service detection, scripts | Descubrimiento de servicios y obtención de la bandera mediante escaneo Nmap |

> **Objeto:** Aplicar técnicas intermedias de Nmap (detección de versiones, scripts, escaneos específicos) para descubrir el servicio objetivo y leer la bandera.

---

**Contexto:** Sala de TryHackMe que profundiza en el uso intermedio de Nmap para la enumeración de redes: detección de puertos abiertos, identificación de versiones de servicios y ejecución de scripts de Nmap. El objetivo final es encontrar la flag en el servicio expuesto de la máquina objetivo.

> **ES:** Una sala orientada a dominar Nmap en un nivel intermedio: descubrir el servicio correcto y recuperar la bandera con técnicas de escaneo, detección de versiones y scripts.
> **EN:** A room aimed at mastering Nmap at an intermediate level: discover the right service and recover the flag using scanning techniques, version detection, and scripts.

## Solucionario

### Task 1: Obtener la bandera / Get the Flag

**Explicación:** Se escanea la máquina objetivo con Nmap para descubrir el servicio expuesto y, accediendo a él, se localiza la bandera.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la bandera? / What is the flag? | `flag{251f309497a18888dde5222761ea88e4}` |

---

**Metodología:** Se realizó un escaneo de la máquina objetivo con Nmap, identificando el servicio expuesto mediante la detección de versiones y scripts del motor de escaneo. Al acceder al servicio se localizó y leyó la bandera `flag{251f309497a18888dde5222761ea88e4}`.

### Cadena de ataque / Attack Chain

Escaneo de puertos con Nmap → identificación del servicio → detección de versión y scripts → acceso al servicio → lectura del contenido → obtención de la bandera.

**Learning chain:** Reconocimiento Nmap → descubrimiento de puertos → detección de servicios → scripts Nmap → acceso al servicio → bandera.

**Lección:** *La enumeración con Nmap (puertos, versiones, scripts) convierte un navegador ciego en una ruta de acceso: conocer los parámetros del escaneo permite descubrir servicios expuestos y extraer información sensible como banderas o banners versionados.*

**MITRE ATT&CK:** T1046 (Network Service Scanning), T1595 (Active Scanning), T1083 (File and Directory Discovery), T1190 (Exploit Public-Facing Application).

**Fuente:** [TryHackMe - Intermediate Nmap](https://tryhackme.com/room/intermediatenmap)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.