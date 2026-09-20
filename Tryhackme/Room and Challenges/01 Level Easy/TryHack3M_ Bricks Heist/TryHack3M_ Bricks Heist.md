# TryHack3M_ Bricks Heist

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | challenge | `tryhack3mbricksheist` | [TryHackMe](https://tryhackme.com/room/tryhack3mbricksheist) | 01 Level Easy | THM | WordPress, Bricks, CVE-2024-25600, PHPUnit, IRC, Bitcoin, LockBit ransomware | Explotación de WordPress vía CVE-2024-25600 y análisis del ransomware LockBit |

---

**Contexto:**

> **ES:** La sala simula un ransomware sobre una instalación de WordPress con el builder Bricks. Se explota el CVE-2024-25600 (PHPUnit) para ejecutar código, se descubre el archivo C2 de diálogo (`nm-inet-dialog`), el servicio systemd abusado (`ubuntu.service`), la configuración IRC (`inet.conf`) y la dirección Bitcoin del rescate, identificando al grupo ransomware LockBit como responsable del ataque.

> **EN:** This room simulates a ransomware attack against a WordPress installation using the Bricks builder. The CVE-2024-25600 (PHPUnit) is exploited to execute code, revealing the C2 dialog binary (`nm-inet-dialog`), the abused systemd service (`ubuntu.service`), the IRC configuration (`inet.conf`), and the Bitcoin ransom address, identifying the LockBit ransomware group as the attacker.

## Solucionario

### Task 1: Explotación y análisis del Bricks Heist / Bricks Heist Exploitation and Analysis

**Explicación:**

1. 1. THM{fl46_650c844110baced87e1606453b93f22a}
   2. nm-inet-dialog
   3. ubuntu.service
   4. inet.conf
   5. bc1qyk79fcp9hd5kreprce89tkh4wrtl8avt4l67qa
   6. LockBit

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag? | `THM{fl46_650c844110baced87e1606453b93f22a}` |
| 2 | What is the name of the C2 dialog file? | `nm-inet-dialog` |
| 3 | Which systemd service is abused for persistence? | `ubuntu.service` |
| 4 | What is the IRC configuration file? | `inet.conf` |
| 5 | What is the Bitcoin address used for the ransom? | `bc1qyk79fcp9hd5kreprce89tkh4wrtl8avt4l67qa` |
| 6 | Which ransomware group is behind the attack? | `LockBit` |

---

**Metodología:** Se identifica la instalación vulnerable de WordPress con el builder Bricks y se explota la ejecución de código remoto asociada a la cadena de explotación (CVE-2024-25600). Tras obtener ejecución, se localiza el binario C2 de diálogo (`nm-inet-dialog`), se analiza el servicio systemd que lo mantiene (`ubuntu.service`), se revisa la configuración IRC de mando y control (`inet.conf`) y se extrae la dirección Bitcoin del rescate, atribuyendo el incidente al grupo de ransomware LockBit.

### Cadena de ataque / Attack Chain

WordPress recon → CVE-2024-25600 exploitation → code execution → C2 dialog → systemd persistence → IRC configuration → ransom Bitcoin address → ransomware attribution.

**Learning chain:** WordPress recon → CVE-2024-25600 exploitation → C2 binary analysis → systemd persistence → IRC C2 → Bitcoin ransom → LockBit attribution

**Lección:** *Detrás de cada ransomware hay una cadena de infección completa: rastrear el binario C2, el servicio de persistencia y la configuración IRC es lo que permite atribuir el ataque.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1071 (Application Layer Protocol), T1486 (Data Encrypted for Impact)

**Fuente:** [TryHackMe - TryHack3M_ Bricks Heist](https://tryhackme.com/room/tryhack3mbricksheist)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.