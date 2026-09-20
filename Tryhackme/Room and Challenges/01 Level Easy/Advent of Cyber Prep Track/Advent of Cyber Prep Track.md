# Advent of Cyber Prep Track

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough (warm-up AOC 2025) | `adventofcyberpreptrack` | https://tryhackme.com/room/adventofcyberpreptrack | 01 Level Easy | TryHackMe | contraseñas seguras / VirusTotal simulado / AttackBox y CLI / CMD (dir /a) / Linux (ls -la, cat) / brechas / credenciales por defecto / permisos de apps / riesgos de IA (chatbot) / análisis de logs y User-Agents | Serie de 10 mini retos de calentamiento antes del Advent of Cyber 2025: desde crear contraseñas fuertes hasta detectar un User-Agent sospechoso en logs. |

---

**Contexto:** Room de preparación ("Prep Track") previa al Advent of Cyber 2025. En Wareville, la "SOC-mas" está amenazada por King Malhare, y antes del evento principal hay que completar 10 mini-misiones type warming-up que repasan habilidades esenciales: gestión de contraseñas, análisis de malware simulado, CLI de Linux y de Windows (CMD), búsqueda de brechas, credenciales por defecto, permisos de aplicaciones, riesgos de los chatbots de IA y análisis de logs web con User-Agents raros. Cada misión es un pequeño reto interactivo que entrega una flag.

> **ES:** Diez mini-misiones interactivas para calentar antes del Advent of Cyber 2025: passwords, malware, AttackBox, CMD, Linux, brechas, routers, apps, chatbots y logs.
> **EN:** Ten hands-on mini-challenges to warm up before Advent of Cyber 2025: passwords, malware, AttackBox, CMD, Linux, breaches, routers, apps, chatbots and log analysis.

## Solucionario

### Task 1: Bienvenida al Advent of Cyber 2025 / Welcome to Advent of Cyber 2025

**Explicación:** Introducción del evento: la historia en Wareville, el premio acumulado, las reglas de participación (sin cheats ni bots) y el certificado por completar todos los rooms. Solo hay que marcar "Got it!".

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Marca "Got it!". | `No answer needed` |

### Task 2: Cómo usar TryHackMe / How to use TryHackMe

**Explicación:** Explicación de la interfaz: el AttackBox (VM Ubuntu en el navegador), el despliegue de máquinas, la vista dividida y las alternativas VPN/RDP/SSH/VNC. Solo lectura.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Marca "Got it!". | `No answer needed` |

### Task 3: Únete a la comunidad / Join our community

**Explicación:** Invitación a unirse al servidor de Discord de la comunidad y seguir las redes sociales de TryHackMe para recibir novedades y soporte. Solo lectura.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Marca "Got it!". | `No answer needed` |

### Task 4: Introducción / Introduction

**Explicación:** Arranca la narrativa: en la TBFC los sistemas fallan por la interferencia de King Malhare, y antes del gran evento hay 10 misiones de calentamiento. Se explica el botón "View Site" para abrir cada reto. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Pulsa "Warm me up!" para empezar. | `No answer needed` |

### Task 5: Reto 1 - Pandemonio de contraseñas / Challenge 1 - Password Pandemonium

**Explicación:** Al iniciar sesión en el workstation de TBFC aparece un aviso: hay credenciales débiles detectadas. El objetivo es crear una contraseña que supere todos los checks: mínimo 12 caracteres, con mayúsculas, minúsculas, números y símbolos, y que no aparezca en la base de datos de contraseñas filtradas. Al enviar una contraseña válida se obtiene la flag.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What's the flag? / ¿Cuál es la flag? | `THM{StrongStart}` |

### Task 6: Reto 2 - El sospechoso Chocolate.exe / Challenge 2 - The Suspicious Chocolate.exe

**Explicación:** Un USB con la playlist de la fiesta contiene un archivo `chocolate.exe`. Se simula un análisis con una herramienta tipo VirusTotal: se pulsa "Scan", se revisa el informe (49 resultados limpios y 1 malicioso) y se decide correctamente si el archivo es seguro o malicioso para obtener la flag.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What's the flag? / ¿Cuál es la flag? | `THM{NotSoSweet}` |

### Task 7: Reto 3 - Bienvenida al AttackBox / Challenge 3 - Welcome to the AttackBox

**Explicación:** Se presenta el AttackBox y la línea de comandos: los defensores deben sentirse cómodos con la CLI. Con comandos básicos de Linux (`ls` para listar, `cd` para navegar, `cat` para leer) se localiza el archivo `welcome.txt` y se lee el mensaje oculto que entrega la flag.

```bash
ls
cd <carpeta>
cat welcome.txt
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What's the flag? / ¿Cuál es la flag? | `THM{Ready2Hack}` |

### Task 8: Reto 4 - El enigma del CMD / Challenge 4 - The CMD Conundrum

**Explicación:** El workstation de McSkidy muestra señales de manipulación: logs borrados y carpetas sin explicación. Se investiga con el Command Prompt de Windows: `dir` para listar y `dir /a` para revelar archivos ocultos, y `type` para leer el contenido del archivo de flag oculto.

```cmd
dir
dir /a
type <archivo_oculto>
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What's the flag? / ¿Cuál es la flag? | `THM{WhereIsMcSkidy}` |

### Task 9: Reto 5 - Conocimiento de Linux / Challenge 5 - Linux Lore

**Explicación:** Los drones del reparto fallan y la investigación apunta a un login en un servidor Linux. Se busca un mensaje oculto en el home de McSkidy: hay que entrar en la carpeta y usar `ls -la` para ver los "dotfiles" (archivos ocultos como `.secret_message`) y `cat` para leerlos.

```bash
ls -la
cat .secret_message
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What's the flag? / ¿Cuál es la flag? | `THM{TrustNoBunny}` |

### Task 10: Reto 6 - La filtración en la lista / Challenge 6 - The Leak in the List

**Explicación:** Hay rumores de una fuga de datos en TBFC. Se simula una herramienta tipo "Have I Been Pwned": se comprueba el correo `mcskidy@tbfc.com` contra la base de datos de brechas conocidas para ver si la cuenta ha sido comprometida, y eso entrega la flag.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What's the flag? / ¿Cuál es la flag? | `THM{LeakedAndFound}` |

### Task 11: Reto 7 - Problemas de WiFi en Wareville / Challenge 7 - WiFi Woes in Wareville

**Explicación:** Los drones se comportan de forma irregular porque alguien entró al router con credenciales por defecto. Se inicia sesión en el router con `admin`/`admin`, se accede a los ajustes de seguridad y se actualiza la contraseña a una segura para obtener la flag.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What's the flag? / ¿Cuál es la flag? | `THM{NoMoreDefault}` |

### Task 12: Reto 8 - La trampa de la app / Challenge 8 - The App Trap

**Explicación:** La cuenta social de McSkidy publica mensajes extraños por una aplicación de terceros sospechosa. La misión enseña a revisar los permisos de las apps conectadas: se identifica la app conectada con permisos excesivos (como acceso al gestor de contraseñas) y se revoca su acceso, entregando la flag.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What's the flag? / ¿Cuál es la flag? | `THM{AppTrapped}` |

### Task 13: Reto 9 - La confesión del chatbot / Challenge 9 - The Chatbot Confession

**Explicación:** El asistente de IA FestiveBot está filtrando secretos internos. Hay que revisar el historial de la conversación del chatbot para identificar las líneas donde el bot reveló información privada (URLs internas o contraseñas) y reconocer el riesgo de que la IA comparta datos sensibles.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What's the flag? / ¿Cuál es la flag? | `THM{DontFeedTheBot}` |

### Task 14: Reto 10 - El rastro del navegador de Bunny / Challenge 10 - The Bunny's Browser Trail

**Explicación:** Los servidores web soportan mucho tráfico con una entrada de log sospechosa. Se introduce el análisis de logs y las cadenas "User-Agent": hay que distinguir el tráfico de navegadores normales (Chrome, Firefox, Edge) e identificar la entrada que viene de "BunnyOS", el agente sospechoso.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What's the flag? / ¿Cuál es la flag? | `THM{EastmasIsComing}` |

### Task 15: La meta / The Finish Line

**Explicación:** Cierre del Prep Track: se confirma que el usuario ha completado los mini retos y ya domina conceptos de CLI, Linux/Windows, brechas, IoT, permisos de apps, IA y logs para enfrentar el Advent of Cyber 2025. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Pulsa "Bring on Advent of Cyber 2025!". | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What's the flag? (Challenge 1 - Password Pandemonium) | `THM{StrongStart}` |
| 2 | What's the flag? (Challenge 2 - The Suspicious Chocolate.exe) | `THM{NotSoSweet}` |
| 3 | What's the flag? (Challenge 3 - Welcome to the AttackBox) | `THM{Ready2Hack}` |
| 4 | What's the flag? (Challenge 4 - The CMD Conundrum) | `THM{WhereIsMcSkidy}` |
| 5 | What's the flag? (Challenge 5 - Linux Lore) | `THM{TrustNoBunny}` |
| 6 | What's the flag? (Challenge 6 - The Leak in the List) | `THM{LeakedAndFound}` |
| 7 | What's the flag? (Challenge 7 - WiFi Woes in Wareville) | `THM{NoMoreDefault}` |
| 8 | What's the flag? (Challenge 8 - The App Trap) | `THM{AppTrapped}` |
| 9 | What's the flag? (Challenge 9 - The Chatbot Confession) | `THM{DontFeedTheBot}` |
| 10 | What's the flag? (Challenge 10 - The Bunny's Browser Trail) | `THM{EastmasIsComing}` |

---

**Metodología:** Completar en orden las 10 mini-misiones interactivas: crear una contraseña robusta que pase todos los checks, analizar chocolate.exe con el antivirus simulado, usar comandos de Linux y CMD para leer archivos ocultos, comprobar la cuenta en una brecha, cambiar credenciales por defecto del router, revocar permisos de la app maliciosa, revisar el historial del chatbot IA y detectar el User-Agent anómalo (BunnyOS) en los logs. Cada reto entrega su flag al completarlo.

### Cadena de ataque / Attack Chain

```text
Contraseñas fuertes -> análisis de malware (simulado) -> CLI Linux (ls/cd/cat) -> CMD (dir /a, type) -> dotfiles (.secret_message) -> brechas de datos -> router con default creds -> permisos de apps -> chatbot IA (fuga de datos) -> logs web y User-Agent (BunnyOS)
```

**Learning chain:** Password hygiene -> malicia de archivos -> AttackBox/CLI -> Windows CMD -> Linux ocultos -> breach checking -> IoT/default credentials -> OAuth/permissions -> AI data leakage -> log & user-agent review.

**Lección:** *Las defensas del día a día (contraseñas fuertes, cero credenciales por defecto, revisión de permisos, control de la IA y análisis de logs) son lo primero que falla bajo presión.*

**MITRE ATT&CK:** T1110 (Brute Force / credenciales por defecto), T1552 (Unsecured Credentials), T1565 (Data Manipulation), T1555 (Credentials from Password Stores), T1566 (Phishing), T1071 (Application Layer Protocol/logs)

**Fuente:** [TryHackMe - Advent of Cyber Prep Track](https://tryhackme.com/room/adventofcyberpreptrack)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.