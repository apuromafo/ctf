# Accessing a Compromised Network

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Medium | walkthrough | `accessingacompromisednetwork` | [TryHackMe](https://tryhackme.com/room/accessingacompromisednetwork) | 02 Level Medium | TryHackMe | VPN, WinRM, WMI, RDP, RustDesk, KAPE, DFIR, Active Directory | Acceso seguro y a escala a una red comprometida para la recolección forense |

---

**Contexto:** Tras el análisis preliminar de la brecha en OpenDoor LTD (fase DFIR), el equipo de respuesta debe acceder a la red Active Directory comprometida para recolectar evidencia. La pregunta central es cómo hacerlo de forma segura y a escala: por VPN, escritorio remoto o desplazamiento on-site. Se exploran las credenciales de Active Directory/Domain Admin entregadas por el personal y se comparan los protocolos de acceso (RDP, WinRM, WMI) con sus pitfalls de OPSEC y de contaminación de evidencia.

## Solucionario

### Task 1: Introduction / Introducción

**Explicación:** Presenta la sala dentro del escenario DFIR de OpenDoor LTD y el objetivo: acceder a una red Active Directory comprometida para recolectar evidencia sin alterarla. Es una tarea informativa que enmarca el flujo de trabajo: elección de la vía de acceso, solicitud de credenciales y uso de protocolos remotos.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Let's begin! | `No answer needed` |

### Task 2: Network Access Options / Opciones de Acceso a la Red

**Explicación:** Te comunicas con Jesse Moore (Network Engineer), quien coordina tu acceso por VPN como actor externo. El portal VPN de OpenDoor es `vpn.opendoor.thm:10443` (puerto propio de FortiClient). Se configura el perfil VPN y se entrega una contraseña temporal para conectarte.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Who is responding to you? (Full name, role) | `Jesse Moore, Network Engineer` |
| 2 | What is the address of OpenDoor's VPN portal? | `vpn.opendoor.thm:10443` |
| 3 | What password was 'created' for your VPN profile? | `kyWy213z` |

### Task 3: Remote Desktop Scenario / Escenario de Escritorio Remoto

**Explicación:** Se recibe acceso por escritorio remoto vía RustDesk (herramienta RMM) con un código de acceso y la contraseña del usuario Administrador. Con RDP entras a la máquina y, al revisar el directorio raíz de IIS (`C:\inetpub`), descubres que `contacts.php` fue backdoorizado con un web shell: evidencia temprana de la brecha.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the RustDesk access code you received? | `448 236 499` |
| 2 | What is the provided Administrator's password? | `Secure!` |
| 3 | What PHP file was backdoored with a web shell? | `contacts.php` |

### Task 4: Access With EDR & RMM / Acceso con EDR y RMM

**Explicación:** Tarea informativa que explica el uso de soluciones de EDR y RMM (como RustDesk) en escenarios de acceso remoto legítimo durante una investigación, así como el abuso que el adversario puede hacer de ellas. Sin preguntas con respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Tarea informativa | `No answer needed` |

### Task 5: Requesting AD Credentials / Solicitud de Credenciales AD

**Explicación:** Evalúas si el perfil VPN ya otorga acceso al dominio Active Directory; la respuesta es negativa (Nay). Jesse te facilita entonces credenciales de nivel Domain Admin: el usuario `da.ext-incident`, pensado específicamente para la investigación de incidentes.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Does the VPN profile already grant you AD access? (Yea/Nay) | `Nay` |
| 2 | What DA username have you received from Jesse? | `da.ext-incident` |

### Task 6: WinRM and WMI Access / Acceso por WinRM y WMI

**Explicación:** Con las credenciales del laboratorio (`ServiceUser:DcG3w4b8`) entras vía WinRM/WMI, protocolos que no crean una sesión interactiva. Al conectarte por RDP como Administrator, `quser` muestra tu sesión `rdp-tcp#1`; en cambio, una sesión WinRM como ServiceUser no aparece en la lista (Nay). En `Documents` de ServiceUser está `flag.txt` y, durante la recolección, se detecta un comando malicioso persistente en `Win32_StartupCommand`: `c:\Users\Public\Pictures\shell.exe`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What session name does the quser command show? | `rdp-tcp#1` |
| 2 | Does quser show your session in the list? (Yea/Nay) | `Nay` |
| 3 | What is the flag's value? | `THM{similar_to_ssh_right?}` |
| 4 | What is the full malicious command persisting in startup? | `c:\Users\Public\Pictures\shell.exe` |

### Task 7: Conclusion / Conclusión

**Explicación:** Cierre de la sala: se resume el flujo de acceso a la red comprometida y se refuerzan las buenas prácticas de recolección forense, priorizando técnicas que minimicen la alteración de la evidencia.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Tarea informativa | `No answer needed` |

---

**Metodología:** La sala sigue el flujo real de acceso de un investigador externo: (1) coordinar por chat la vía de entrada (VPN) y obtener credenciales temporales, (2) validar el entorno con un escritorio remoto (RustDesk + RDP) e identificar evidencia temprana (web shell en IIS), (3) solicitar credenciales de AD/Domain Admin al personal, y (4) operar con WinRM/WMI para recolectar indicadores sin crear sesiones interactivas que contaminen la evidencia ni llamen la atención del adversario.

### Cadena de ataque / Attack Chain

```text
DFIR - Brecha en OpenDoor LTD (Active Directory comprometido)
  │
  ├─ 1. Acceso por VPN
  │      Chat con Jesse Moore (Network Engineer)
  │      Portal VPN: vpn.opendoor.thm:10443
  │      Perfil VPN + contraseña temporal (kyWy213z)
  │      → NO otorga acceso al dominio (Nay)
  │
  ├─ 2. Escritorio remoto
  │      RustDesk (RMM): access code 448 236 499
  │      RDP como Administrator (Secure!)
  │      Evidencia temprana: web shell en contacts.php (IIS root C:\inetpub)
  │
  ├─ 3. Credenciales AD
  │      Solicitud a Jesse → usuario DA: da.ext-incident
  │
  └─ 4. Recolección con WinRM/WMI (ServiceUser:DcG3w4b8)
         WinRM/WMI no crean sesión interactiva (quser = Nay)
         Flag: THM{similar_to_ssh_right?}
         Win32_StartupCommand → c:\Users\Public\Pictures\shell.exe
         Recolección forense a escala (KAPE/DFIR)
```

**Learning chain:** Elección de la vía de acceso remoto (VPN) → escritorio remoto con RMM (RustDesk) y RDP → identificación de evidencia (web shell en IIS) → solicitud de credenciales Domain Admin → acceso no interactivo con WinRM/WMI → detección de persistencia (startup) → recolección forense.

**Lección:** *El protocolo de acceso forma parte de la metodología DFIR: WinRM/WMI permiten operar sin sesiones interactivas, reduciendo la contaminación de evidencia y el ruido OPSEC frente al adversario.*

**MITRE ATT&CK:** T1021.001 (Remote Services: RDP), T1078 (Valid Accounts), T1119 (Automated Collection), T1059.001 (PowerShell).

**Fuente:** [TryHackMe - Accessing a Compromised Network](https://tryhackme.com/room/accessingacompromisednetwork)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.