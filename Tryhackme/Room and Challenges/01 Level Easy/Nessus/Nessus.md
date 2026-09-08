# Nessus

| **Dificultad** | Easy |
| **Tipo** | Escaneo de vulnerabilidades (herramienta) |
| **Slug** | `rpnessusredux` |
| **Link** | [TryHackMe](https://tryhackme.com/room/rpnessusredux) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | Nessus / Plantillas de escaneo / Programación / Puertos / Plugin IDs / Análisis de resultados |
| **Impacto** | Sala práctica sobre Nessus, el escáner de vulnerabilidades: instalación y activación, navegación por la interfaz (New Scan, Policies, Plugin Rules), plantillas de escaneo (Host Discovery, Basic Network Scan, Credentialed Patch Audit, Web Application Tests), configuración de escaneos (Schedule, todos los puertos, bandas limitadas, Nessus SYN scanner) y análisis de los resultados de un escaneo web (IDs de plugins, archivos y direcciones expuestas). |

---

**Contexto:** La sala explica Nessus desde cero: primero se despliega el laboratorio y se instala/activa Nessus. Se recorre la interfaz (crear un escaneo, gestionar políticas y reglas de plugins) y se eligen las plantillas adecuadas (descubrimiento de hosts, escaneo de red básico, auditoría de parches con credenciales o pruebas de aplicaciones web). La configuración práctica cubre la programación, el escaneo de todos los puertos, el modo de baja velocidad de enlace y el escáner SYN, hasta completar 6 pasos en la plantilla. Finalmente se importan y analizan los resultados de un escaneo web: plugins, el archivo `.bak`, el `login.php` y el directorio expuesto, identificando una vulnerabilidad de Clickjacking.

## Solucionario

### Task 1: Desplegando el laboratorio

**Explicación:** Se despliega la máquina objetivo (la web que luego se escaneará) y se arranca Nessus en la máquina atacante.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Despliega la máquina objetivo y arranca Nessus. | `No answer needed` |

### Task 2: Primeros pasos con Nessus

**Explicación:** Instalación y activación de Nessus (código de activación), espera de la descarga de plugins, acceso a la interfaz web `https://localhost:8834`, creación de la cuenta admin y ejecución del primer escaneo con la plantilla adecuada.

```bash
sudo dpkg -i Nessus-*.deb
sudo /etc/init.d/nessusd start
# https://localhost:8834
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Instala Nessus en la máquina atacante. | `No answer needed` |
| 2 | Activa Nessus con el código de activación. | `No answer needed` |
| 3 | Espera a que se descarguen los plugins de Nessus. | `No answer needed` |
| 4 | Accede a la interfaz web de Nessus. | `No answer needed` |
| 5 | Configura la cuenta de administrador de Nessus. | `No answer needed` |
| 6 | Crea el primer escaneo. | `No answer needed` |
| 7 | Selecciona la plantilla adecuada. | `No answer needed` |
| 8 | Configura el objetivo del escaneo. | `No answer needed` |
| 9 | Inicia el escaneo. | `No answer needed` |
| 10 | Revisa los resultados del primer escaneo. | `No answer needed` |

### Task 3: Navegando por Nessus

**Explicación:** Elementos de la interfaz: `New Scan` crea escaneos; `Policies` gestiona plantillas personalizadas; `Plugin Rules` define reglas sobre plugins. Plantillas: `Host Discovery` (hosts activos), `Basic Network Scan` (puertos/servicios), `Credentialed Patch Audit` (con credenciales) y `Web Application Tests` (aplicaciones web).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué botón se utiliza para crear un nuevo escaneo? | `New Scan` |
| 2 | ¿Dónde se gestionan las plantillas personalizadas (políticas)? | `Policies` |
| 3 | ¿Qué sección permite gestionar las reglas de los plugins? | `Plugin Rules` |
| 4 | ¿Qué plantilla se usa para descubrir únicamente los hosts activos? | `Host Discovery` |
| 5 | ¿Qué plantilla realiza un escaneo básico de la red (puertos y servicios)? | `Basic Network Scan` |
| 6 | ¿Qué plantilla audita los parches del sistema con credenciales? | `Credentialed Patch Audit` |
| 7 | ¿Qué plantilla está pensada para probar aplicaciones web? | `Web Application Tests` |

### Task 4: Configurando el escaneo

**Explicación:** Configuración del escaneo: pestaña `Schedule` para programarlo, `Port scan (all ports)` para todos los puertos, `Scan low bandwidth links` para redes lentas. Sin root, Nessus usa el `Nessus SYN scanner`. La versión instalada en el laboratorio fue `2.4.41`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué pestaña permite programar la realización del escaneo? | `Schedule` |
| 2 | ¿Qué ajuste indica a Nessus que escanee todos los puertos? | `Port scan (all ports)` |
| 3 | ¿Qué ajuste es útil en redes con ancho de banda limitado? | `Scan low bandwidth links` |
| 4 | Continúa configurando los ajustes del escaneo. | `No answer needed` |
| 5 | ¿Qué escáner de puertos utiliza Nessus si no se ejecuta como root? | `Nessus SYN scanner` |
| 6 | ¿Cuál era la versión de Nessus que se instaló? | `2.4.41` |

### Task 5: Analizando los resultados del escaneo

**Explicación:** Del informe web: el plugin `10107` identifica la versión del servidor HTTP; el escaneo descubrió `login.php`, el archivo `.bak`, el directorio expuesto `/external/phpids/0.6/docs/examples/` y la vulnerabilidad `Clickjacking` en el servidor.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el ID del plugin que identifica la versión del servidor HTTP? | `10107` |
| 2 | ¿Qué página web fue descubierta por el escaneo? | `login.php` |
| 3 | ¿Qué extensión de archivo fue encontrada? | `.bak` |
| 4 | ¿Qué directorio fue expuesto en el servidor? | `/external/phpids/0.6/docs/examples/` |
| 5 | ¿Qué vulnerabilidad está presente en el servidor web? | `Clickjacking` |

---

**Metodología:** Se instala y activa Nessus y se espera la descarga de plugins antes del primer escaneo. Se navega por la interfaz identificando cada sección: creación de escaneos (New Scan), gestión de políticas y reglas de plugins, y las plantillas en función del objetivo (solo descubrimiento, red básica, auditoría de parches con credenciales o aplicación web). En la configuración se programa el escaneo, se escanean todos los puertos, se habilita el modo de baja velocidad y se selecciona el escáner SYN como alternativa sin privilegios de root. Los resultados se interpretan por plugin (10107), archivos descubiertos (`.bak`, `login.php`), directorios expuestos y finalmente la vulnerabilidad de Clickjacking del servidor.

**Learning chain:** instalación → activación → interfaz y plantillas → configuración del escaneo → interpretación de resultados.

**MITRE ATT&CK:** T1595.002 (Active Scanning: Vulnerability Scanning), T1595.001 (Active Scanning: Scanning IP Blocks)

**Fuente:** [TryHackMe - Nessus](https://tryhackme.com/room/rpnessusredux)