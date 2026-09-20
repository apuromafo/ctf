# VulnNet

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Medium | Reto / Challenge (Web) | vulnnet | https://tryhackme.com/room/vulnnet1 | 02 Level Medium | TryHackMe | PHP, Web exploitation, Misconfiguración | Alta - máquina de práctica realista |

> **Objeto:** Aprovechar las malas configuraciones de "VulnNet Entertainment" para comprometer la máquina y capturar ambas flags.

---

**Contexto:** "VulnNet" es un reto de dificultad media centrado en técnicas realistas sobre una única máquina. La aplicación web está escrita en PHP y exige mapear el dominio `vulnnet.thm` en `/etc/hosts` antes de comenzar. El camino combina abusos de configuración web, pivote y escalada de privilegios.

> **ES:** Reto realista basado en malas configuraciones de la aplicación web de VulnNet Entertainment.
> **EN:** Realistic challenge based on the misconfigurations made by VulnNet Entertainment.
>
> **Descripción original / Original description:** *Can you take advantage of the misconfigurations made by VulnNet Entertainment?*
> **Scenario:**
> The purpose of this challenge is to make use of more realistic techniques and include them into a single machine to practice your skills.
>
> Difficulty: Medium
> Web Language: PHP
> => You will have to add a machine IP with domain vulnnet.thm to your /etc/hosts
>
> Icon made by monkik from www.flaticon.com

## Solucionario

### Task 1: VulnNet

**Explicación:** Mapear `vulnnet.thm` en `/etc/hosts` y explotar los servicios expuestos (NFS, web, sincronización) para obtener la flag de usuario.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Cuál es la flag de usuario? / What is the user flag? | THM{907e420d979d8e2992f3d7e16bee1e8b} |

### Task 2: Escalada de privilegios / Privilege Escalation

**Explicación:** Escalar privilegios explotando la mala configuración de la máquina para lograr acceso de root y leer la última flag.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Cuál es la flag de root? / What is the root flag? | THM{220b671dd8adc301b34c2738ee8295ba} |

---

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | ¿Cuál es la flag de usuario? / What is the user flag? | `THM{907e420d979d8e2992f3d7e16bee1e8b}` |
| 1 | ¿Cuál es la flag de root? / What is the root flag? | `THM{220b671dd8adc301b34c2738ee8295ba}` |

---

**Metodología:**

1. Mapeo del dominio `vulnnet.thm` en `/etc/hosts`.
2. Enumeración de puertos y servicios expuestos.
3. Explotación de la misconfiguración de la aplicación PHP.
4. Escalada de privilegios hasta root.
5. Captura de ambas flags.

### Cadena de ataque / Attack Chain

```text
vulnnet.thm (hosts) -> Enumeración de servicios -> Explotación web -> Shell de usuario -> Privesc -> root flags
```

**Learning chain:**

- La resolución del hostname virtual es el primer requisito de la máquina.
- Las misconfiguraciones (no solo CVEs) son vectores de entrada y de escalada.
- Cada flag confirma el acceso alcanzado en la cadena.

**Lección:** *Las configuraciones erróneas en aplicaciones y servicios son tan peligrosas como las vulnerabilidades conocidas.*

**MITRE ATT&CK:**
- T1190 - Exploit Public-Facing Application
- T1082 - System Information Discovery
- T1068 - Exploitation for Privilege Escalation

**Fuente:** [TryHackMe - VulnNet](https://tryhackme.com/room/vulnnet1)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.