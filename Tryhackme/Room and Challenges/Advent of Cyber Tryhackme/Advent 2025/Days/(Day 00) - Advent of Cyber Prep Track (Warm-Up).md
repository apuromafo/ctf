# Advent of Cyber Prep Track (Warm-Up)

| **Dificultad** | Easy | **Tipo** | CTF (Free Room) | **Slug** | `day00adventofcyberpreptrackwarmup` | | **Link** | [TryHackMe](https://tryhackme.com/room/adventofcyber25) | | **Sección** | Advent of Cyber Tryhackme | | **Fuente** | texto oficial THM + anotaciones propias | | **Componentes** | Warm-Up / Passwords / Malware / AttackBox / Linux CLI / Phishing / Wi-Fi / App Permissions / Chatbot / Browser Trail | | **Impacto** | Día 00 (warm-up) del AoC 2025: 10 mini-retos introductorios de conceptos básicos de seguridad que entregan una flag cada uno |

---

**Contexto:** Día 00 del calendario Advent of Cyber 2025 ("Advent of Cyber Prep Track (Warm-Up)"). Es un calentamiento de 10 mini-retos muy sencillos que repasan: generación de contraseñas, detección de malware, uso de la AttackBox, terminal CMD y Linux, phishing, Wi-Fi, permisos de apps, chatbots y rastro del navegador. Documentación original bilingüe (ES/EN); se conservan ambos idiomas y las flags exactas.

---

## Solucionario

### Task 1: Generar una contraseña aleatoria / Make a random password

**Explicación:** Ejercicio de higiene: generar una contraseña aleatoria en lugar de usar una predecible.

```
make a random password
```

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | Make a random password | `THM{StrongStart}` |

### Task 2: El Chocolate Sospechoso.exe / The Suspicious Chocolate.exe

**Explicación:** Un ejecutable llamado "chocolate" resultó ser malware; se identifica la naturaleza maliciosa del fichero.

```
malicious
```

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 2 | ¿Qué tipo de fichero es El Chocolate Sospechoso.exe? / What type of file is The Suspicious Chocolate.exe? | `THM{NotSoSweet}` |

### Task 3: ¡Bienvenido a la AttackBox! / Welcome to the AttackBox!

**Explicación:** Primer contacto con la AttackBox de TryHackMe: leer el fichero de bienvenida de los retos.

```
cat challenges/welcome.txt
```

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 3 | Welcome to the AttackBox! | `THM{Ready2Hack}` |

### Task 4: El Enigma de CMD / The CMD Conundrum

**Explicación:** Navegar con el CMD de Windows hasta carpeta misteriosa y leer la flag oculta.

```
cd into mystery_data type hidden_flag.txt
```

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 4 | The CMD Conundrum | `THM{WhereIsMcSkidy}` |

### Task 5: Leyendas de Linux / Linux Lore

**Explicación:** En Linux, navegar hasta el usuario indicado y leer la flag oculta con cat.

```
got to user, cat hidden flag
```

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 5 | Linux Lore | `THM{TrustNoBunny}` |

### Task 6: La Filtración en la Lista / The Leak in the List

**Explicación:** Un correo entregado en una web comprometida; se introduce el email y se comprueba que la credencial ha sido filtrada.

```
put in email and click on compromised site
```

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 6 | The Leak in the List | `THM{LeakedAndFound}` |

### Task 7: Problemas WiFi en Wareville / WiFi Woes in Wareville

**Explicación:** Acceder a una red Wi-Fi con credenciales por defecto y cambiarla por una contraseña propia.

```
login and make another password
```

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 7 | WiFi Woes in Wareville | `THM{NoMoreDefault}` |

### Task 8: La Trampa de la App / The App Trap

**Explicación:** Revisar los permisos de las apps: la tercera app pide permisos excesivos; se revoca su acceso a la contraseña.

```
go to third app and revoke password access
```

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 8 | The App Trap | `THM{AppTrapped}` |

### Task 9: La Confesión del Chatbot / The Chatbot Confession

**Explicación:** Un chatbot recopila información sensible; se marcan las casillas con la información que un chatbot no debería pedir.

```
check the boxes with sensitive info
```

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 9 | The Chatbot Confession | `THM{DontFeedTheBot}` |

### Task 10: La Ruta del Navegador del Conejo / The Bunny’s Browser Trail

**Explicación:** Revisar el historial/rastro del navegador para encontrar al bot responsable (Easter Bunny del "Eastmas").

```
find the bot
```

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 10 | The Bunny’s Browser Trail | `THM{EastmasIsComing}` |

---

**Metodología:**

1. Generar contraseñas aleatorias (higiene básica)

2. Reconocer malware y reaccionar ante él

3. Familiarizarse con la AttackBox y las CLI (CMD y Linux)

4. Reconocer phishing, contraseñas por defecto y permisos excesivos de apps

5. Concienciación sobre chatbots y rastro del navegador

**Learning chain:** Warm-Up -> Fundamentos (Passwords/CLI) -> Concienciación (Phishing/Wi-Fi/Apps/Chatbot)

**Lección:** *El warm-up del AoC 2025 repasa hábitos básicos de seguridad (contraseñas, permisos, phishing y OSINT del navegador) que serán la base de los retos diarios del calendario.*

**MITRE ATT&CK:**

- T1110 - Brute Force (contraseñas por defecto)

- T1566.001 - Spearphishing Attachment (phishing inicial)

- T1204 - User Execution (ejecutar ficheros sospechosos/malware)

- T1078 - Valid Accounts (credenciales filtradas y permisos)

**Fuente:** [TryHackMe - Advent of Cyber Prep Track (Warm-Up)](https://tryhackme.com/room/adventofcyber25)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.