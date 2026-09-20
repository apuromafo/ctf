# Brute Force Heroes

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `bruteforceheroes` | [TryHackMe](https://tryhackme.com/room/bruteforceheroes) | 01 Level Easy | TryHackMe | ffuf, hydra, hashcat, fuerza bruta, máscaras | Compromiso de credenciales mediante fuzzing, fuerza bruta y cracking de hashes |

---

**Contexto:** Sala centrada en las tres grandes técnicas de fuerza bruta: descubrimiento de contenido (ffuf), fuerza bruta de credenciales (hydra) y cracking de hashes con máscaras (hashcat). El resumen original conserva únicamente las respuestas posicionales del room, sin los enunciados de las preguntas.

## Solucionario

### Task 1: Preparación / Preparation

**Explicación:** Preguntas de contextualización previas a los ataques, sin respuesta que introducir.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `No answer needed` |
| 2 | *(Pregunta 2 no especificada en el original)* | `No answer needed` |

### Task 2: Descubrimiento de contenido / Content Discovery

**Explicación:** Se lanza el fuzzing sobre el sitio para descubrir rutas y archivos, configurando ffuf para ignorar los redireccionamientos a la página de login e identificar los recursos relevantes.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `Found` |
| 2 | *(Pregunta 2 no especificada en el original)* | `Location Response Header`<br>`Nay` |

### Task 3: Fuerza bruta de login / Login Brute Force

**Explicación:** Se fuerza la autenticación del servicio con hydra y diccionarios, filtrando candidatos y completando el acceso con las credenciales encontradas.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `-x ignore:fgrep='Location: login.php'`<br>`1qaz@WSX` |
| 2 | *(Pregunta 2 no especificada en el original)* | `buster`<br>`rhymes` |
| 3 | *(Pregunta 3 no especificada en el original)* | `tommyboy1`<br>`1qaz@WSX__`<br>`URL` |

### Task 4: Cracking de contraseñas / Password Cracking

**Explicación:** Se identifica el tipo de hash, se selecciona el modo de hashcat correspondiente (1800: sha512crypt), se elige el diccionario y la máscara adecuada para obtener la contraseña en claro.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `crackme`<br>`1800`<br>`cr4ck`<br>`?l?l?d?l?l` |
| 2 | *(Pregunta 2 no especificada en el original)* | `No answer needed` |

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Task 1, Pregunta 1 no especificada en el original)* | `No answer needed` |
| 2 | *(Task 1, Pregunta 2 no especificada en el original)* | `No answer needed` |
| 3 | *(Task 2, Pregunta 1 no especificada en el original)* | `Found` |
| 4 | *(Task 2, Pregunta 2 no especificada en el original)* | `Location Response Header`<br>`Nay` |
| 5 | *(Task 3, Pregunta 1 no especificada en el original)* | `-x ignore:fgrep='Location: login.php'`<br>`1qaz@WSX` |
| 6 | *(Task 3, Pregunta 2 no especificada en el original)* | `buster`<br>`rhymes` |
| 7 | *(Task 3, Pregunta 3 no especificada en el original)* | `tommyboy1`<br>`1qaz@WSX__`<br>`URL` |
| 8 | *(Task 4, Pregunta 1 no especificada en el original)* | `crackme`<br>`1800`<br>`cr4ck`<br>`?l?l?d?l?l` |
| 9 | *(Task 4, Pregunta 2 no especificada en el original)* | `No answer needed` |

---

**Metodología:** Descubrimiento de contenido con ffuf → filtrado de redirecciones a `login.php` → fuerza bruta del login con hydra → obtención de credenciales → identificación del hash → cracking con hashcat (modo 1800) mediante diccionario y máscara → captura de las flags.

### Cadena de ataque / Attack Chain

```text
ffuf (Content Discovery) → identificación de rutas/recursos → hydra (fuerza bruta login) → credenciales válidas → hashcat (modo 1800, diccionario + máscara ?l?l?d?l?l) → contraseña en claro → flags
```

**Learning chain:** fuzzing (ffuf) → fuerza bruta de login (hydra) → cracking de hashes (hashcat con máscaras) → accesos y flags

**Lección:** *La fuerza bruta exitosa no depende solo de las herramientas, sino de configurarlas bien: filtrar falsos positivos, elegir el modo de hash correcto y diseñar máscaras adecuadas al objetivo.*

**MITRE ATT&CK:** T1046 (Network Service Discovery), T1110 (Brute Force), T1110.001 (Password Guessing)

**Fuente:** [TryHackMe - Brute Force Heroes](https://tryhackme.com/room/bruteforceheroes)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.