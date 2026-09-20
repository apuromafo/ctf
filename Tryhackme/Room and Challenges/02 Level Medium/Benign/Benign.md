# Benign

| Campo | Valor |
|-------|-------|
| Dificultad | Medium |
| Tipo | Room |
| Slug | benign |
| Link | https://tryhackme.com/room/benign |
| Sección | 02 Level Medium |
| Fuente | TryHackMe |
| Componentes | Forense Digital, Malware Analysis, C2 Analysis |
| Impacto | Alto |

---

**Contexto:** Sala de análisis forense y reverse engineering de un binario malicioso denominado benign.exe. Se investiga un archivo sospechoso examinando sus conexiones de red, usuarios involucrados, herramientas utilizadas por el adversario, y se extraen credenciales y artefactos de C2 para reconstruir la activity del ataque.

## Solucionario

### Task 1: Introduccion
**Explicación:** Presentación del escenario de análisis y contexto del binario benign.exe que será investigado.

1. No answer needed

### Task 2: Analisis Completo
**Explicación:** Análisis forense completo del binario benign.exe. Se examinan conexiones de red, usuarios del sistema, herramientas utilizadas por el malware, fechas de compilación, dominios de C2, y se extraen credenciales y URLs de control remoto.

2. 1. 13959
   2. Amel1a
   3. Chris.fort
   4. haroon
   5. certutil.exe
   6. 2022-03-04
   7. controlc.com
   8. benign.exe
   9. THM{KJ&*H^B0}
   10. https://controlc.com/e4d11035

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Task 1 | No answer needed |
| 2 | Task 2.1 | 13959 |
| 2 | Task 2.2 | Amel1a |
| 2 | Task 2.3 | Chris.fort |
| 2 | Task 2.4 | haroon |
| 2 | Task 2.5 | certutil.exe |
| 2 | Task 2.6 | 2022-03-04 |
| 2 | Task 2.7 | controlc.com |
| 2 | Task 2.8 | enign.exe |
| 2 | Task 2.9 | THM{KJ&*H^B0} |
| 2 | Task 2.10 | https://controlc.com/e4d11035 |

---

**Metodología:** Análisis forense y reverse engineering de malware. Examen de conexiones de red, usuarios, herramientas del adversario y extracción de artefactos C2.

**Learning chain:** Análisis estático -> Identificación de conexiones -> Extracción de usuarios -> Análisis de herramientas -> Credenciales y C2 -> Reconstrucción del ataque

**Lección:** _El análisis forense de malware requiere examinar múltiples capas del binario para reconstruir la narrativa completa del ataque._

**MITRE ATT&CK:** T1059.001 (PowerShell), T1105 (Ingress Tool Transfer), T1071.001 (Web Protocols), T1078 (Valid Accounts), T1104 (Multi-Stage Channels)

**Fuente:** [TryHackMe - Benign](https://tryhackme.com/room/benign)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
