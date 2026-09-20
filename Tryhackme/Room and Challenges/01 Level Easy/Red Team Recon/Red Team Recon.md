# Red Team Recon

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `redteamrecon` | https://tryhackme.com/room/redteamrecon | 01 Level Easy | TryHackMe | Red Team / recon / Google dorking / Shodan / recon-ng / Censys / NIST NVD / MISP | Reconocimiento ofensivo de un Red Team contra un dominio de prueba: búsquedas, Shodan, recon-ng y fuentes de inteligencia basadas en objetivos. |

---

**Contexto:** Sala práctica de reconocimiento (recon) en el contexto de un Red Team. Se hace footprinting de un dominio objetivo (clinic.thmredteam.com) con búsquedas avanzadas de Google (dorking), consultas de Shodan para la IP pública, la herramienta recon-ng con workspaces y módulos (migrate_hosts, Censys) y fuentes de inteligencia de amenazas y vulnerabilidades (NIST NVD, MISP). Todo orientado a recopilar información del objetivo antes del ataque.

> **ES:** "Red Team Recon" — reconocimiento ofensivo: dorking de Google, Shodan, recon-ng y fuentes de inteligencia contra un dominio objetivo.
> **EN:** "Red Team Recon" — offensive reconnaissance: Google dorking, Shodan, recon-ng and intelligence sources against a target domain.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Presentación de la sala: el reconocimiento como primera fase de cualquier operación de Red Team y de qué herramientas se van a utilizar. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la sala. / Read the room introduction. | `No answer needed` |

### Task 2: Configuración del entorno / Environment Setup

**Explicación:** Preparación del entorno de trabajo del laboratorio (acceso VPN, hosts y herramientas). No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Configura el entorno del laboratorio. / Set up the lab environment. | `No answer needed` |

### Task 3: Huella del objetivo / Footprinting

**Explicación:** Se hace footprinting del dominio objetivo. La fecha registrada en la búsqueda inicial es `2021-09-24`, y la búsqueda devuelve `2` resultados relevantes que, tras filtrar subdominios, se reducen a `2` hosts de interés.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué fecha aparece registrada en la búsqueda inicial? / What date appears in the initial search? | `2021-09-24` |
| 2 | ¿Cuántos resultados devuelve la búsqueda inicial? / How many results does the initial search return? | `2` |
| 3 | ¿Cuántos subdominios o resultados relevantes aparecen? / How many relevant subdomains or results appear? | `2` |

### Task 4: Búsquedas de Google / Google Dorking

**Explicación:** Mediante Google dorking se acota la búsqueda al dominio clinic.thmredteam.com: la consulta `filetype:xls site:clinic.thmredteam.com` busca archivos Excel publicados, y la consulta `passwords site:clinic.thmredteam.com` busca referencias a contraseñas en el dominio.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué búsqueda de Google localiza archivos Excel en el dominio objetivo? / What Google search finds Excel files on the target domain? | `filetype:xls site:clinic.thmredteam.com` |
| 2 | ¿Qué búsqueda de Google localiza referencias a contraseñas en el dominio objetivo? / What Google search finds password references on the target domain? | `passwords site:clinic.thmredteam.com` |

### Task 5: Shodan

**Explicación:** Se usa Shodan para identificar la dirección IP pública propia desde la que se opera: el comando es `shodan myip`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué comando de Shodan muestra la IP pública del propio equipo? / What Shodan command shows the user's own public IP? | `shodan myip` |

### Task 6: Recon-ng

**Explicación:** La herramienta recon-ng se usa con un workspace propio del objetivo. Se crea el workspace con `recon-ng -w clinicredteam`, se cargan `2` módulos, se usa `migrate_hosts` para importar los hosts descubiertos y el host encontrado se atribuye a la organización `Censys Inc`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué comando crea el workspace de recon-ng para la clínica? / What command creates the recon-ng workspace for the clinic? | `recon-ng -w clinicredteam` |
| 2 | ¿Cuántos módulos se cargan en el workspace? / How many modules are loaded in the workspace? | `2` |
| 3 | ¿Qué módulo se usa para migrar los hosts descubiertos? / What module is used to migrate the discovered hosts? | `migrate_hosts` |
| 4 | ¿Qué organización aparece como fuente del host encontrado? / What organization appears as the source for the found host? | `Censys Inc` |

### Task 7: Fuentes de inteligencia / Intelligence Sources

**Explicación:** Para completar la inteligencia del objetivo se consultan fuentes externas: `NIST NVD` para vulnerabilidades publicadas por el NIST y `MISP Project` como plataforma de inteligencia de amenazas.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué fuente se consulta para las vulnerabilidades del NIST? / What source is consulted for NIST vulnerabilities? | `NIST NVD` |
| 2 | ¿Qué proyecto se usa como plataforma de inteligencia de amenazas? / What project is used as a threat intelligence platform? | `MISP Project` |

### Task 8: Conclusión / Conclusion

**Explicación:** Cierre de la sala con el resumen del proceso de reconocimiento. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la conclusión de la sala. / Read the room conclusion. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la sala. / Read the room introduction. | `No answer needed` |
| 2 | Configura el entorno del laboratorio. / Set up the lab environment. | `No answer needed` |
| 3 | ¿Qué fecha aparece registrada en la búsqueda inicial? / What date appears in the initial search? | `2021-09-24` |
| 4 | ¿Cuántos resultados devuelve la búsqueda inicial? / How many results does the initial search return? | `2` |
| 5 | ¿Cuántos subdominios o resultados relevantes aparecen? / How many relevant subdomains or results appear? | `2` |
| 6 | ¿Qué búsqueda de Google localiza archivos Excel en el dominio objetivo? / What Google search finds Excel files on the target domain? | `filetype:xls site:clinic.thmredteam.com` |
| 7 | ¿Qué búsqueda de Google localiza referencias a contraseñas en el dominio objetivo? / What Google search finds password references on the target domain? | `passwords site:clinic.thmredteam.com` |
| 8 | ¿Qué comando de Shodan muestra la IP pública del propio equipo? / What Shodan command shows the user's own public IP? | `shodan myip` |
| 9 | ¿Qué comando crea el workspace de recon-ng para la clínica? / What command creates the recon-ng workspace for the clinic? | `recon-ng -w clinicredteam` |
| 10 | ¿Cuántos módulos se cargan en el workspace? / How many modules are loaded in the workspace? | `2` |
| 11 | ¿Qué módulo se usa para migrar los hosts descubiertos? / What module is used to migrate the discovered hosts? | `migrate_hosts` |
| 12 | ¿Qué organización aparece como fuente del host encontrado? / What organization appears as the source for the found host? | `Censys Inc` |
| 13 | ¿Qué fuente se consulta para las vulnerabilidades del NIST? / What source is consulted for NIST vulnerabilities? | `NIST NVD` |
| 14 | ¿Qué proyecto se usa como plataforma de inteligencia de amenazas? / What project is used as a threat intelligence platform? | `MISP Project` |
| 15 | Lee la conclusión de la sala. / Read the room conclusion. | `No answer needed` |

---

**Metodología:** Se empieza con el footprinting del dominio objetivo registrando fechas y resultados, se refina con Google dorking (filetype, site) contra clinic.thmredteam.com, se identifica la IP propia con Shodan, se estructura la recolección con recon-ng (workspace clinicredteam, migrate_hosts, fuente Censys Inc) y se complementa con inteligencia externa (NIST NVD y MISP).

### Cadena de ataque / Attack Chain

```text
Footprinting (2021-09-24) -> Google dorking (filetype:xls / passwords site:clinic.thmredteam.com) -> Shodan (shodan myip) -> recon-ng (workspace clinicredteam -> migrate_hosts -> Censys Inc) -> Inteligencia externa (NIST NVD / MISP)
```

**Learning chain:** Footprinting -> Google dorking -> Shodan -> recon-ng -> fuentes de inteligencia (NIST NVD / MISP).

**Lección:** *El reconocimiento es una disciplina ordenada: una búsqueda de Google bien construida o un host atribuido por Censys pueden valer más que un escáner, si se registran y centralizan (recon-ng) de forma estructurada.*

**MITRE ATT&CK:** T1595 (Active Scanning), T1596 (Search Open Technical Databases), T1598 (Phishing for Information)

**Fuente:** [TryHackMe - Red Team Recon](https://tryhackme.com/room/redteamrecon)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.