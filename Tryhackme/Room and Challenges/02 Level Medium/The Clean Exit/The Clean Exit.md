# The Clean Exit

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Medium | challenge | `thecleanexit` | [TryHackMe](https://tryhackme.com/room/thecleanexit) | 02 Level Medium | TryHackMe | KAPE, Windows Forensics (USB/WMI, Prefetch, Amcache, MFT, USN), Windows Search, BITS, RDP, SMB | Reconstrucción forense de una exfiltración de datos por insider: identificar el dispositivo USB, el binario exfiltrador, la transferencia interna (SMB) y el borrado de logs |

---

**Contexto:** THM Security Services (TSS) contrata al jugador como analista forense para un caso de fuga de datos: un empleado llamado Turner exfiltró información confidencial de la empresa y borró sus rastros del sistema. Como escenario DFIR, la sala entrega una workstation forense (usuario `DFIRUser`, contraseña `TryH@cKMe1!433`, acceso por RDP a `MACHINE_IP`) con las herramientas en `C:\Users\DFIRUser\DFIR Tools` y los artefactos KAPE precompilados en `C:\Users\DFIRUser\Kape-Collection`. Durante la investigación se reconstruye la línea de tiempo del incidente a partir de artefactos de Windows: conexión de un dispositivo USB, ejecución de un binario exfiltrador, transferencia en segundo plano con BITS, conexiones RDP a un sistema interno y copias SMB, hasta el borrado del registro de firewall para cubrir el rastro. Los prerrequisitos recomendados son las salas Windows Forensics 1, Windows Forensics 2 y Compromised Windows Analysis.

## Solucionario

### Task 1: Case Briefing / Informe del Caso

**Explicación:** La sala se abre dentro del escenario de THM Security Services (TSS) y presenta el briefing del caso en el TSS Operations Hub (pestaña Active Case). Es una tarea informativa que confirma que el analista revisó el caso y está listo para comenzar la investigación forense. Verifica también los prerrequisitos del caso (Windows Forensics 1 y 2, Compromised Windows Analysis) antes de pasar a la máquina de investigación.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | I have reviewed the active case briefing and I am ready to begin. | `No answer needed` |

### Task 2: The Investigation / La Investigación

**Explicación:** Con la workstation forense ya iniciada (2-3 minutos, vista split-screen o RDP con `DFIRUser:TryH@cKMe1!433`), el objetivo es reconstruir la exfiltración de datos que realizó Turner el día del incidente: dispositivo USB conectado, binario ejecutado, dominio de destino de la transferencia, pivote a un sistema interno por RDP, carpeta de contratos de proveedores y borrado de logs. Las pistas apuntan al índice de Windows Search para la etiqueta del volumen, a los traces de ejecución para el binario, a las transferencias BITS para el dominio, a las conexiones RDP y los traces SMB para el sistema interno y la ruta de copia, y a los filtros de eventos para las eliminaciones. Todas las respuestas dependen de valores concretos del laboratorio. (respuesta sin confirmar: requiere resolver el laboratorio)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | A storage device was connected to Turner's workstation on the day of the incident. What is its serial number? | `-` |
| 2 | What was the name of the storage device Turner connected with the workstation? | `-` |
| 3 | An executable was run on Turner's workstation on the same day. Its name clearly reflects the intent behind running it. What is its name? | `-` |
| 4 | The first attempt failed. Turner then used a Windows-native background transfer mechanism to try again. What domain was he targeting? | `-` |
| 5 | What was the name of the archive Turner prepared to send to that domain? | `-` |
| 6 | Both direct transfer attempts from the workstation failed. Turner then accessed another internal system before moving the data. What is the name of that system? | `-` |
| 7 | The client reported that vendor contracts are missing. Turner browsed the finance directory locally before removing it. What was the name of the folder containing those contracts? | `-` |
| 8 | What was the last interaction time of that restricted folder that Turner accessed? (Format: HH:MM:SS) | `-` |
| 9 | Turner successfully moved the archive to the internal system he accessed. What was the full path of the location he copied it to? | `-` |
| 10 | Turner deleted several files to cover his tracks. When was the firewall log deleted? (Format: HH:MM:SS AM/PM) | `-` |

---

**Metodología:** El flujo sigue una investigación DFIR de exfiltración de datos por insider con Windows Forensics: (1) revisar el briefing del caso y montar la workstation forense con los artefactos KAPE, (2) reconstruir la línea de tiempo del día del incidente a partir de artefactos del sistema (conexión de dispositivos USB, ejecución de binarios, índice de búsqueda de Windows), (3) seguir los intentos de transferencia y el pivote hacia un sistema interno (RDP), y (4) rastrear las copias SMB y el borrado de logs para completar la cadena de evidencia de la exfiltración.

### Cadena de ataque / Attack Chain

```text
Insider threat - Turner exfiltra datos de la empresa (THM Security Services)
  │
  ├─ 1. Conexión de almacenamiento externo
  │      Dispositivo USB en la workstation de Turner (día del incidente)
  │      Serial number + nombre/etiqueta del volumen (Windows Search cache)
  │
  ├─ 2. Ejecución del binario exfiltrador + preparación del archivo
  │      Ejecutable cuyo nombre refleja la intención (traces de ejecución)
  │      Intento 1 directo → falla
  │      Intento 2: transferencia de fondo nativa (BITS) → dominio objetivo
  │      Archivo comprimido preparado para enviar a ese dominio
  │
  ├─ 3. Pivote a sistema interno
  │      Conexiones RDP → nombre del sistema interno
  │      Navegación local en el directorio de finanzas (carpeta de contratos)
  │      Copia del archivo vía SMB → ruta completa en el sistema interno
  │
  └─ 4. Anti-forensia: borrado de rastros
         Eliminación de archivos y del firewall log (timestamp) para cubrir la pista
         Recuperación de la evidencia mediante artefactos KAPE
```

**Learning chain:** Revisión del briefing del caso → línea de tiempo del día del incidente → identificación del dispositivo USB conectado → ejecución del binario exfiltrador → transferencia de fondo (BITS) hacia el dominio objetivo → preparación del archivo comprimido → pivote al sistema interno (RDP) → acceso a la carpeta de contratos → copia SMB → eliminación de logs y anti-forensia.

**Lección:** *Incluso cuando el insider borra archivos y logs para cubrir sus trazas, la evidencia de los artefactos de Windows (conexión USB, ejecución de procesos, índice de búsqueda, traces RDP/SMB y filtros de eventos) permite reconstruir la exfiltración completa y su cadena de movimiento de datos.*

**MITRE ATT&CK:** T1005 (Data from Local System), T1039 (Data from Network Shared Drive), T1078 (Valid Accounts), T1048 (Exfiltration Over Alternative Protocol), T1070.004 (Indicator Removal on Host: File Deletion).

**Fuente:** [TryHackMe - The Clean Exit](https://tryhackme.com/room/thecleanexit)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.