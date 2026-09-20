# Cyber Kill Chain

| Campo | Valor |
|-------|-------|
| **Dificultad** | Medium |
| **Tipo** | CTF / Theory |
| **Slug** | cyberkillchain |
| **Link** | https://tryhackme.com/room/cyberkillchain |
| **Sección** | 02 Level Medium |
| **Fuente** | TryHackMe |
| **Componentes** | Cyber Kill Chain, Reconnaissance, Weaponization, Exploitation, Post-Exploitation |
| **Impacto** | Medio — Comprensión del marco de ataque completo para defensa y detección |

---

**Contexto:** Esta sala enseña la Cyber Kill Chain de Lockheed Martin, un modelo de 7 fases que describe el progreso de un ciberataque: Reconnaissance, Weaponization, Delivery, Exploitation, Installation, Command & Control y Actions on Objectives. Cada fase se explora con técnicas, herramientas y contra-medidas.

## Solucionario

### Task 1: ¿Cuántas fases tiene la Cyber Kill Chain?

**Explicación:** La Cyber Kill Chain consta de 7 fases.

1. 7

### Task 2: Reconnaissance

**Explicación:** Técnicas de reconocimiento pasivo y activo para recopilar información del objetivo.

2. 1. Google Dorking
   2. passive reconnaissance

### Task 3: Weaponization

**Explicación:** Preparación de los artefactos de ataque, incluyendo payloads ofuscados y macros maliciosas.

3. 1. Obfuscation
   2. Macro

### Task 4: Delivery

**Explicación:** Vectores de entrega del payload al objetivo, incluyendo publicidad maliciosa y SMS phishing.

4. 1. Malvertising
   2. Smishing

### Task 5: Exploitation

**Explicación:** Explotación de vulnerabilidades, incluyendo exploits de día cero y bypass de autenticación multifactor.

5. 1. Zero-day exploit
   2. MFA

### Task 6: Installation

**Explicación:** Instalación persistente del malware, usando web shells y técnicas de allowlisting.

6. 1. web shell
   2. allowlisting

### Task 7: Command & Control

**Explicación:** Establecimiento de canales de comunicación ocultos para control del sistema comprometido.

7. 1. DNS tunnelling
   2. HTTPS

### Task 8: Actions on Objectives

**Explicación:** Acciones finales del atacante: exfiltración de datos, movilidad lateral y ransomware.

8. 1. Data Exfiltration
   2. principle of least privilege
   3. Ransomware

### Task 9: Cierre

**Explicación:** Preguntas finales de verificación de conocimientos.

9. 1. THM{CKC_NJHERDX327}
   2. No answer needed

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Fases de la Kill Chain | `7` |
| 2.1 | Técnica de reconocimiento | `Google Dorking` |
| 2.2 | Tipo de reconocimiento | `passive reconnaissance` |
| 3.1 | Técnica de evasión | `Obfuscation` |
| 3.2 | Tipo de payload | `Macro` |
| 4.1 | Vector de entrega | `Malvertising` |
| 4.2 | Vector de entrega | `Smishing` |
| 5.1 | Tipo de exploit | `Zero-day exploit` |
| 5.2 | Mecanismo de autenticación | `MFA` |
| 6.1 | Tipo de persistencia | `web shell` |
| 6.2 | Técnica de evasión | `allowlisting` |
| 7.1 | Canal C2 | `DNS tunnelling` |
| 7.2 | Protocolo C2 | `HTTPS` |
| 8.1 | Acción final | `Data Exfiltration` |
| 8.2 | Principio de defensa | `principle of least privilege` |
| 8.3 | Tipo de ataque | `Ransomware` |
| 9.1 | Flag | `THM{CKC_NJHERDX327}` |
| 9.2 | Cierre | `No answer needed` |

---

**Metodología:** Identificación de fase → Técnicas asociadas → Herramientas utilizables → Contra-medidas defensivas → Validación de conocimiento.

**Learning chain:** Kill Chain overview → Phase-by-phase analysis → Attack techniques → Defense strategies → Practical quiz

**Lección:** *Cada fase de la Kill Chain ofrece oportunidades de detección; defender en múltiples fases maximiza la resiliencia.*

**MITRE ATT&CK:**
- T1595 — Active Scanning
- T1566 — Phishing
- T1203 — Exploitation for Client Execution

**Fuente:** [TryHackMe - Cyber Kill Chain](https://tryhackme.com/room/cyberkillchain)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.