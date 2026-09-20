# Anti-Reverse Engineering

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Malware Analysis / Defensivo | antireverseengineering | https://tryhackme.com/room/antireverseengineering | 02 Level Medium | TryHackMe | Anti-debugging, Anti-VM, WinDbg, Python | Protección de malware frente a analistas |

---

**Contexto:** La sala **Anti-Reverse Engineering** estudia las técnicas que los malware emplean para dificultar su análisis: detección de debuggers (`IsDebuggerPresent`), verificación de procesos y ventanas con nombre (`EnumWindows`), detección de entornos virtualizados (servicios como `vboxservice` y `amazon-ssm-agent`, MAC `00:50:56`), consultas WMI a sensores térmicos, manipulación del registro (EIP) y cadenas ofuscadas en BASE64. El alumno aprende a identificar cada evasión, comprender qué mide y decidir cómo neutralizarla en un laboratorio de análisis.

## Solucionario

### Task 1: Introducción
**Explicación:**

Se plantea el escenario de análisis y por qué los autores de malware tratan de impedir la ingeniería inversa.

Respuesta: `No answer needed`

### Task 2: Detección de debuggers
**Explicación:**

Se identifica la primera llamada de la API de Windows que el malware usa para saber si está bajo un depurador.

Respuesta: `IsDebuggerPresent`

### Task 3: Detección de procesos y ventanas
**Explicación:**

Se analiza la técnica que recorre las ventanas del sistema buscando nombres asociados a herramientas de análisis: la API implicada, el conteo de iteraciones y la instrucción ensamblador que ajusta la pila tras el bucle.

1. `EnumWindows`
2. `90`
3. `add esp,8`

### Task 4: Detección de virtualización
**Explicación:**

Se reconocen los indicadores de máquina virtual presentes en la muestra: el servicio de VirtualBox detectado, el prefijo OUI de VMware en la dirección MAC y el servicio de análisis en la nube AWS que también se comprueba.

1. `vboxservice`
2. `00:50:56`
3. `amazon-ssm-agent.exe`

### Task 5: Consultas WMI y registro
**Explicación:**

Se documenta la consulta WMI usada para leer la temperatura de los sensores térmicos (señuelo de entorno físico), junto con los registros involucrados: el registro/instrucción al que se apunta (EIP) y su valor de memoria.

1. `SELECT * FROM MSAcpi_ThermalZoneTemperature`
2. `EIP`
3. `0019FF1C`

### Task 6: Ofuscación de cadenas
**Explicación:**

Se identifica la técnica de ocultación del texto plano de la muestra, codificado en BASE64.

Respuesta: `This is a BASE64 encoded string.`

### Task 7: Firmas de herramientas
**Explicación:**

Se comparan las versiones de las herramientas de análisis presentes en el entorno de laboratorio.

1. `14.16`
2. `2.006`

### Task 8: Bypass de las protecciones
**Explicación:**

Se aplica el parche manual al binario para neutralizar las comprobaciones anti-análisis y poder analizarlo bajo el debugger.

Respuesta: `No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Introducción a la sala | `No answer needed` |
| 2 | Detección de debugger empleada | `IsDebuggerPresent` |
| 3.1 | API de recorrido de ventanas | `EnumWindows` |
| 3.2 | Número de iteraciones/procesos detectados | `90` |
| 3.3 | Instrucción que equilibra la pila | `add esp,8` |
| 4.1 | Servicio de VirtualBox presente | `vboxservice` |
| 4.2 | OUI de VMware en la MAC | `00:50:56` |
| 4.3 | Servicio de AWS presente | `amazon-ssm-agent.exe` |
| 5.1 | Consulta WMI de temperatura | `SELECT * FROM MSAcpi_ThermalZoneTemperature` |
| 5.2 | Registro/contador apuntado | `EIP` |
| 5.3 | Valor de memoria asociado | `0019FF1C` |
| 6 | Cadena ofuscada de la muestra | `This is a BASE64 encoded string.` |
| 7.1 | Versión detectada 1 | `14.16` |
| 7.2 | Versión detectada 2 | `2.006` |
| 8 | Bypass de las protecciones | `No answer needed` |

---

**Metodología:** Ingeniería inversa defensiva de malware: detección de anti-debugging/anti-VM en el binario, análisis de consultas WMI y registro, decodificación de cadenas y parcheo para continuar el análisis.

**Learning chain:** Detección de debugger → ventanas y procesos → indicadores de VM (servicios y MAC) → señuelos WMI → ofuscación BASE64 → fingerprints → bypass.

**Lección:** *Todo check anti-análisis es una firma: saber leerlo permite, primero, entender al adversario y, después, anularlo.*

**MITRE ATT&CK:** T1622 Debugger Evasion · T1497 Virtualization/Sandbox Evasion · T1614 System Location Discovery.

**Fuente:** [TryHackMe - Anti-Reverse Engineering](https://tryhackme.com/room/antireverseengineering)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.