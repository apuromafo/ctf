# File and Hash Threat Intel
This room seeks to teach on enriching file and hash artefacts using threat intelligence.
**Room Link:**  https://tryhackme.com/room/fileandhashthreatintel

 <img src="https://tryhackme-images.s3.amazonaws.com/room-icons/5fc2847e1bbebc03aa89fbf2-1754051466692" width="250" alt="File and Hash Threat Intel">



## 🛡️ Resumen de Investigación de Amenazas (Lab THM)

### **1. Heurística y Nombres de Archivo**

En esta fase identificaste técnicas comunes de evasión:

* **Archivo detectado:** `payroll.pdf`
* **Indicador:** **Double extensions** (Extensiones dobles). Probablemente el nombre real era `payroll.pdf.exe`, aprovechando que Windows oculta las extensiones por defecto.

### **2. Análisis del Malware "bl0gger"**

Utilizando herramientas de inteligencia de hashes (VirusTotal/Hybrid Analysis):

* **SHA256:** `2672b6688d7b32a90f9153d2ff607d6801e6cbde61f509ed36d0450745998d58`
* **Etiqueta de amenaza (VT):** `trojan.graftor/blackmoon`
* **Comportamiento en Sandbox:** * Ejecutó un comando sigiloso: `regsvr32 %WINDIR%\Media\ActiveX.ocx /s`
* Procesos secundarios: `werfault.exe`
* Tags en Hybrid Analysis: `BlackMoon`, `Discovery`, `windows-server-utility`.



### **3. Análisis del Malware "Morse-Code-Analyzer"**

* **Falso Positivo:** El vendor **CyberFortress** lo clasificó como no malicioso.
* **Técnica MITRE ATT&CK:** Se identificó **DLL Side-Loading** para persistencia y escalada de privilegios.
* **Infraestructura C2:** URL asociada `hxxp://121.182.174.27:3000/server.exe`.

### **4. Ransomware Akira (Task 5)**

Análisis de una muestra de ransomware moderna:

* **SHA256:** `43b0ac119ff957bb209d86ec206ea1ec3c51dd87bebf7b4a649c7e6c7f3756e7`
* **Familia:** `akira`, `filecryptor`
* **Nota de rescate:** `akira_readme.txt`
* **Técnica de Inhibición de Recuperación:** * Comando: `Get-WmiObject Win32_Shadowcopy | Remove-WmiObject` (Borrado de copias de seguridad).
* ID de MITRE: **T1490** (Inhibit System Recovery).



---

### **Puntos clave que este lab refuerza:**

1. **Enriquecimiento:** Un hash por sí solo no dice mucho, pero al cruzarlo con sandboxes obtenemos TTPs (Tácticas, Técnicas y Procedimientos).
2. **Mascarada:** El uso de nombres como `svchost.exe` o archivos `.pdf` falsos para engañar al usuario y al analista.
3. **Análisis Dinámico:** El sandbox reveló conexiones de red y strings extraídas (454 en total) que no son visibles a simple vista.
 
 
 Solo respuestas:
1. 1. `No answer needed`
2. 1. `payroll.pdf, Double extensions`
3. 1. `2672b6688d7b32a90f9153d2ff607d6801e6cbde61f509ed36d0450745998d58`
   2. `trojan.graftor/blackmoon`
   3. `2025-05-15 12:03:49`
   4. `CyberFortress`
   5. `DLL Side-Loading`
4. 1. `BlackMoon, Discovery, windows-server-utility`
   2. `regsvr32 %WINDIR%\Media\ActiveX.ocx /s`
   3. `werfault.exe`
   4. `svchost.exe`
   5. `hxxp://121.182.174.27:3000/server.exe`
   6. `454
5. 1. `43b0ac119ff957bb209d86ec206ea1ec3c51dd87bebf7b4a649c7e6c7f3756e7`
   2. `akira, filecryptor`
   3. `2024-10-30 17:17:24 UTC`
   4. `akira_readme.txt`
   5. `Get-WmiObject Win32_Shadowcopy | Remove-WmiObject`
   6. `T1490`
6. 1. `No answer needed`


Fecha: 29.12.2025

