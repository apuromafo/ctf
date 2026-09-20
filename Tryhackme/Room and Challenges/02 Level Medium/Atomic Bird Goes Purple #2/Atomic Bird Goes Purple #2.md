# Atomic Bird Goes Purple #2

| Campo | Valor |
|-------|-------|
| Dificultad | Medium |
| Tipo | Room |
| Slug | atomicbirdgoespurple2 |
| Link | https://tryhackme.com/room/atomicbirdgoespurple2 |
| Sección | 02 Level Medium |
| Fuente | TryHackMe |
| Componentes | Atomic Red Team, MITRE ATT&CK, Emulation, YARA |
| Impacto | Alto |

---

**Contexto:** Segunda parte de la serie Atomic Bird Goes Purple. Continúa la emulación ofensiva con Atomic Red Team, enfocándose en técnicas avanzadas de persistencia, lateral movement y exfiltración de datos. Se trabaja con reglas YARA, análisis de servicios maliciosos y conexión reversa.

## Solucionario

### Task 1: Introduccion
**Explicación:** Presentación de la continuación de la emulación ofensiva. Se revisan conceptos previos y se prepara el entorno para las nuevas técnicas.

1. No answer needed

### Task 2: Analisis de Artefactos
**Explicación:** Análisis de artefactos encontrados durante la emulación, incluyendo archivos de configuración YARA y patrones de indicadores de compromiso.

2. 1. YamlDotNet.xml
   2. ,*.bak
   3. L1LAFLHQ5peGsjh7Pee8wHFY1SBQHe85A1HZhVrK47Yf6cqmH3n8
   4. Adminstrator

### Task 3: Persistencia y Lateral Movement
**Explicación:** Emulación de técnicas de persistencia a través de servicios maliciosos y movimiento lateral dentro de la red. Se identifica el servicio registrado malicioso y se establece conexión reversa.

3. 1. thm-registered-service
   2. C:\Windows\system32\services.exe
   3. THM{THM_Offline_Index_Emulation}
   4. .thm-jhn
   5. nc 10.10.thm.jhn 4499 -e powershell

### Task 4: Limpieza
**Explicación:** Limpieza del entorno y eliminación de artefactos creados durante la emulación.

4. No answer needed

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Task 1 | No answer needed |
| 2 | Task 2.1 | YamlDotNet.xml |
| 2 | Task 2.2 | ,*.bak |
| 2 | Task 2.3 | L1LAFLHQ5peGsjh7Pee8wHFY1SBQHe85A1HZhVrK47Yf6cqmH3n8 |
| 2 | Task 2.4 | Adminstrator |
| 3 | Task 3.1 | 	hm-registered-service |
| 3 | Task 3.2 | C:\Windows\system32\services.exe |
| 3 | Task 3.3 | THM{THM_Offline_Index_Emulation} |
| 3 | Task 3.4 | .thm-jhn |
| 3 | Task 3.5 | 
c 10.10.thm.jhn 4499 -e powershell |
| 4 | Task 4 | No answer needed |

---

**Metodología:** Atomic Red Team / Emulación de adversarios con persistencia, lateral movement y exfiltración.

**Learning chain:** Artefactos YARA -> Análisis de indicadores -> Persistencia via servicios -> Conexión reversa -> Limpieza

**Lección:** _La emulación avanzada permite detectar persistencia y movimiento lateral en entornos controlados._

**MITRE ATT&CK:** TA0003 (Persistence), T1543.003 (Windows Service), TA0008 (Lateral Movement), T1572 (Protocol Tunneling), TA0010 (Exfiltration)

**Fuente:** [TryHackMe - Atomic Bird Goes Purple #2](https://tryhackme.com/room/atomicbirdgoespurple2)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
