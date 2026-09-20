# Bash Scripting

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `bashscripting` | [TryHackMe](https://tryhackme.com/room/bashscripting) | 01 Level Easy | TryHackMe | bash / variables / parámetros / arrays / test operators | Automatización de tareas repetitivas de enumeración y explotación mediante scripting en Bash |

---

**Contexto:** Esta sala introduce desde cero los fundamentos del scripting en Bash: el shebang, los comentarios, las variables y su expansión, la entrada del usuario con `read`, los parámetros posicionales, los arrays y los operadores de comprobación de archivos y directorios. Todo el contenido se trabaja de forma interactiva dentro de la propia sala, sin necesidad de comprometer una máquina externa. Dominar estos conceptos permite al pentester automatizar tareas repetitivas de forma rápida y fiable.

> **ES:** La sala guía en la creación de scripts Bash funcionales: variables, entrada de usuario, parámetros, arrays y flags de test, con ejercicios prácticos paso a paso.
> **EN:** This room guides you through writing functional Bash scripts: variables, user input, parameters, arrays and test flags, with hands-on step-by-step exercises.

## Solucionario

### Task 1: Introducción / Get started
**Explicación:** Pregunta introductoria de la sala. No requiere respuesta.

| Pregunta / Question | Respuesta / Answer |
|--------------------|--------------------|
| Pregunta introductoria de la sala | `No answer needed` |

### Task 2: Variables
**Explicación:** Se crea el primer script. En la primera línea se indica el intérprete con el shebang `#!/bin/bash` y, a continuación, un comentario precedido de la almohadilla `#`. El programa ficticio que se escribe como práctica se denomina `BishBashBosh`.

| Pregunta / Question | Respuesta / Answer |
|--------------------|--------------------|
| ¿Con qué símbolo se indica un comentario en Bash? | `#` |
| ¿Cómo se llama el programa ficticio creado en la práctica? | `BishBashBosh` |

### Task 3: Variables (continuación)
**Explicación:** Con las variables definidas (`apt-get install cowsay`, `name=Jammy`, `age=21`, `city` y `country`) se comprueba su comportamiento. La salida del script es `Jammy is 21 years old` y, para visualizar el contenido de cada variable, se usa `echo $city` y `echo $country`.

| Pregunta / Question | Respuesta / Answer |
|--------------------|--------------------|
| ¿Qué salida produce el script con las variables definidas? | `Jammy is 21 years old` |
| ¿Qué comando muestra el contenido de la variable `city`? | `echo $city` |
| ¿Qué comando muestra el contenido de la variable `country`? | `echo $country` |

### Task 4: Parámetros / Parameters
**Explicación:** Se trabaja con los parámetros posicionales y la entrada del usuario. `$#` devuelve el número de argumentos pasados al script, `$0` el nombre del script y `$4` el cuarto argumento. La orden `read test` captura la entrada del usuario y, al proporcionar la entrada `hello aloha`, la variable `test` recibe ese valor.

| Pregunta / Question | Respuesta / Answer |
|--------------------|--------------------|
| ¿Qué variable devuelve el número de argumentos pasados al script? | `$#` |
| ¿Qué variable devuelve el nombre del script? | `$0` |
| ¿Qué variable devuelve el cuarto argumento? | `$4` |
| ¿Qué comando se usa para leer la entrada del usuario en una variable? | `read test` |
| ¿Qué valor recibe la variable con la entrada proporcionada? | `hello aloha` |

### Task 5: Arrays
**Explicación:** Se manipula el array `cars=( 'honda' 'audi' 'bmw' 'ford' 'tesla' )`. La expansión `${cars[1]}` dentro de `echo "${cars[1]}"` imprime `audi`, `unset cars[3]` elimina el elemento indicado y `cars[3]='toyota'` reasigna un nuevo valor a una posición.

| Pregunta / Question | Respuesta / Answer |
|--------------------|--------------------|
| ¿Cómo se imprime el segundo elemento del array `cars`? | `echo "${cars[1]}"` |
| ¿Cómo se elimina un elemento del array? | `unset cars[3]` |
| ¿Cómo se asigna un nuevo valor a un elemento del array? | `cars[3]='toyota'` |

### Task 6: Operadores de test / Test operators
**Explicación:** Se estudian los operadores de comprobación de Bash, que devuelven verdadero o falso según la característica de un archivo o directorio.

| Pregunta / Question | Respuesta / Answer |
|--------------------|--------------------|
| ¿Qué flag comprueba si un archivo existe y es legible? | `-r` |
| ¿Qué flag comprueba si la ruta es un directorio? | `-d` |

### Task 7: Cierre / Outro
**Explicación:** Pregunta final de cierre de la sala. No requiere respuesta.

| Pregunta / Question | Respuesta / Answer |
|--------------------|--------------------|
| Pregunta final de cierre de la sala | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Pregunta introductoria de la sala | `No answer needed` |
| 2 | Símbolo de comentario en Bash | `#` |
| 3 | Programa ficticio de la práctica | `BishBashBosh` |
| 4 | Salida del script con variables | `Jammy is 21 years old` |
| 5 | Contenido de la variable `city` | `echo $city` |
| 6 | Contenido de la variable `country` | `echo $country` |
| 7 | Número de argumentos pasados al script | `$#` |
| 8 | Nombre del script | `$0` |
| 9 | Cuarto argumento | `$4` |
| 10 | Comando para leer la entrada del usuario | `read test` |
| 11 | Valor de la variable con la entrada | `hello aloha` |
| 12 | Imprimir segundo elemento del array | `echo "${cars[1]}"` |
| 13 | Eliminar elemento del array | `unset cars[3]` |
| 14 | Asignar nuevo valor al array | `cars[3]='toyota'` |
| 15 | Flag de archivo legible | `-r` |
| 16 | Flag de directorio | `-d` |
| 17 | Pregunta final de cierre | `No answer needed` |

---

**Metodología:** Se sigue el itinerario guiado de la sala: creación del script con shebang y comentario, definición de variables y comprobación de su salida con `echo`, uso de parámetros posicionales y `read` para la entrada del usuario, manipulación de arrays y, por último, operadores de test sobre archivos y directorios.

### Cadena de ataque / Attack Chain

```text
Shebang #!/bin/bash -> comentario (#) -> variables -> echo $var -> parámetros ($#, $0, $4) -> read -> arrays (${arr[n]}, unset, reasignación) -> test operators (-r, -d)
```

**Learning chain:** bash scripting --> shebang --> comments --> variables --> echo expansion --> positional parameters --> user input (read) --> arrays --> test operators

**Lección:** *El scripting en Bash es una habilidad transversal del pentester: variables, parámetros, arrays y operadores de test permiten automatizar tareas repetitivas, ahorrando tiempo y reduciendo errores manuales.*

**MITRE ATT&CK:** T1059.004 (Command and Scripting Interpreter: Unix Shell)

**Fuente:** [TryHackMe - Bash Scripting](https://tryhackme.com/room/bashscripting)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.