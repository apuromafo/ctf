# Windows Fundamentals 3

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Info | walkthrough | `windowsfundamentals3xzx` | [TryHackMe](https://tryhackme.com/room/windowsfundamentals3xzx) | 00 Level Info | THM | Windows Updates, Windows Security, Virus & threat protection, Firewall & network protection, Device security, BitLocker, VSS | Comprensión de las herramientas de seguridad integradas de Windows |

---

**Contexto:**
> **ES:** Tercera parte del módulo Windows Fundamentals: actualizaciones de Windows, Windows Security (protección contra virus y amenazas, firewall y red), seguridad del dispositivo (TPM), cifrado BitLocker y Volume Shadow Copy Service.
> **EN:** Third part of the Windows Fundamentals module: Windows Updates, Windows Security (virus & threat protection, firewall & network), device security (TPM), BitLocker encryption and the Volume Shadow Copy Service.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:**
1. No answer needed

### Task 2: Actualizaciones de Windows / Windows Updates
**Explicación:**
2. 5/3/2021

### Task 3: Seguridad de Windows / Windows Security
**Explicación:**
3. Virus & threat protection

### Task 4: Protección contra Virus y Amenazas / Virus & threat protection
**Explicación:**
4. Real-time protection

### Task 5: Firewall y Protección de Red / Firewall & network protection
**Explicación:**
5. Public network

### Task 6: Control de Aplicaciones y Navegador / App & browser control
**Explicación:**
6. No answer needed

### Task 7: Seguridad del Dispositivo / Device security
**Explicación:**
7. Trusted Platform Module

### Task 8: BitLocker / BitLocker
**Explicación:**
8. startup key

### Task 9: Servicio de Copias de Sombra de Volumen / Volume Shadow Copy Service
**Explicación:**
9. Volume Shadow Copy Service

### Task 10: Conclusión / Conclusion
**Explicación:**
10. No answer needed

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Read the above and start the virtual machine. | `No answer needed` |
| 2 | There were two definition updates installed in the attached VM. On what date were these updates installed? | `5/3/2021` |
| 3 | In the above image, which area needs immediate attention? | `Virus & threat protection` |
| 4 | Specifically, what is turned off that Windows is notifying you to turn on? | `Real-time protection` |
| 5 | If you were connected to airport Wi-Fi, what most likely will be the active firewall profile? | `Public network` |
| 6 | Read the above. | `No answer needed` |
| 7 | What is the TPM? | `Trusted Platform Module` |
| 8 | What must a user insert on computers that DO NOT have a TPM version 1.2 or later? | `startup key` |
| 9 | What is VSS? | `Volume Shadow Copy Service` |
| 10 | Read the above. | `No answer needed` |

---

**Metodología:**
Revisión de las funciones de seguridad integradas de Windows: historial de actualizaciones y definition updates, panel de Windows Security, configuración de protección en tiempo real, perfiles de firewall según la red, seguridad del dispositivo con TPM, requisitos de BitLocker sin TPM y el servicio VSS de copias de sombra.

### Cadena de ataque / Attack Chain
1. Comprobación de las actualizaciones instaladas y de los definition updates.
2. Revisión del panel de Windows Security y de las alertas pendientes.
3. Inspección de la protección contra virus y amenazas (protección en tiempo real).
4. Análisis de los perfiles de firewall según el tipo de red.
5. Revisión de la seguridad del dispositivo (TPM), BitLocker y VSS.

**Learning chain:**
Windows Updates -> Windows Security -> Virus & threat protection -> Firewall & network protection -> Device security (TPM) -> BitLocker -> VSS

**Lección:** *Windows reúne su seguridad en herramientas integradas (Windows Security, BitLocker, TPM, VSS) que deben auditarse y mantenerse actualizadas para proteger tanto consumidores como empresas.*

**MITRE ATT&CK:**
- N/A (Room de aprendizaje / walkthrough — herramientas de seguridad de Windows)

**Fuente:** [TryHackMe - Windows Fundamentals 3](https://tryhackme.com/room/windowsfundamentals3xzx)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.