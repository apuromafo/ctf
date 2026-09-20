# Basic Dynamic Analysis

| Campo | Valor |
|-------|-------|
| Dificultad | Medium |
| Tipo | Room |
| Slug | basicdynamicanalysis |
| Link | https://tryhackme.com/room/basicdynamicanalysis |
| Sección | 02 Level Medium |
| Fuente | TryHackMe |
| Componentes | Dynamic Analysis, Malware Analysis, Process Monitor, RegShot |
| Impacto | Alto |

---

**Contexto:** Sala de análisis dinámico de malware que cubre las herramientas y técnicas esenciales para observar el comportamiento de software malicioso en tiempo real. Se utiliza Process Monitor, Process Hacker y RegShot para monitorear活动 del sistema, conexiones de red y cambios en el registro, permitiendo entender qué hace un malware sin necesidad de desensamblarlo.

## Solucionario

### Task 1: Introduccion al Analisis Dinamico
**Explicación:** Conceptos fundamentales de análisis dinámico y por qué es complementario al análisis estático para entender el comportamiento del malware.

1. No answer needed

### Task 2: Entorno de Laboratorio
**Explicación:** Configuración del entorno de laboratorio para análisis dinámico, incluyendo la selección del sistema operativo adecuado.

2. Linux

### Task 3: Analisis de Red
**Explicación:** Monitoreo de活动 de red del malware utilizando herramientas de captura y análisis de tráfico para identificar conexiones sospechosas y patrones de comunicación C2.

3. 1. 94-73-155-12.cizgi.net.tr:2448
   2. TCP Reconnect
   3. C:\Users\Administrator\Desktop\samples\1.exe
   4. No answer needed

### Task 4: Analisis de Procesos
**Explicación:** Monitoreo de creación y活动 de procesos del malware. Se analizan las llamadas a API, creación de archivos y comportamiento en tiempo de ejecución.

4. 1. C:\myapp.exe
   2. CreateFileA
   3. InternetConnectW
   4. Sleep
   5. No answer needed

### Task 5: Analisis de Objetos con Nombres
**Explicación:** Inspección de objetos con nombre del sistema (named objects) creados por el malware, incluyendo eventos de Windows y mutantes.

5. 1. \Sessions\X\BaseNamedObjects\SMX:XXXX:XXX:WilStaging_XX
   2. N
   3. N
   4. No answer needed

### Task 6: Analisis de Registro
**Explicación:** Análisis de cambios en el registro de Windows realizados por el malware utilizando RegShot para comparar el estado antes y después de la ejecución.

6. Software\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Compatibility Assistant\Store\C:\Users\Administrator\Desktop\samples\3.exe

### Task 7: Conclusion
**Explicación:** Revisión final de las herramientas y técnicas de análisis dinámico aprendidas.

7. No answer needed

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Task 1 | No answer needed |
| 2 | Task 2 | Linux |
| 3 | Task 3.1 | 94-73-155-12.cizgi.net.tr:2448 |
| 3 | Task 3.2 | TCP Reconnect |
| 3 | Task 3.3 | C:\Users\Administrator\Desktop\samples\1.exe |
| 3 | Task 3.4 | No answer needed |
| 4 | Task 4.1 | C:\myapp.exe |
| 4 | Task 4.2 | CreateFileA |
| 4 | Task 4.3 | InternetConnectW |
| 4 | Task 4.4 | Sleep |
| 4 | Task 4.5 | No answer needed |
| 5 | Task 5.1 | \Sessions\X\BaseNamedObjects\SMX:XXXX:XXX:WilStaging_XX |
| 5 | Task 5.2 | N |
| 5 | Task 5.3 | N |
| 5 | Task 5.4 | No answer needed |
| 6 | Task 6 | Software\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Compatibility Assistant\Store\C:\Users\Administrator\Desktop\samples\3.exe |
| 7 | Task 7 | No answer needed |

---

**Metodología:** Análisis dinámico de malware con Process Monitor, Process Hacker y RegShot. Observación de活动 en tiempo real, análisis de red, procesos y registro.

**Learning chain:** Configuración de entorno -> Monitoreo de red -> Análisis de procesos -> Named objects -> Cambios en registro -> Correlación de hallazgos

**Lección:** _El análisis dinámico complementa al estático permitiendo observar el comportamiento real del malware en un entorno controlado._

**MITRE ATT&CK:** T1059.001 (PowerShell), T1071 (Application Layer Protocol), T1105 (Ingress Tool Transfer), T1082 (System Information Discovery), T1112 (Modify Registry)

**Fuente:** [TryHackMe - Basic Dynamic Analysis](https://tryhackme.com/room/basicdynamicanalysis)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
