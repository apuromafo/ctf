# Introduction to Cryptography

| **Dificultad** | MEDIUM | **Tipo** | Free | **Slug** | `introductiontocryptography` |
| **Link** | [TryHackMe](https://tryhackme.com/room/introductiontocryptography) | **Sección** | 02 Level Medium | **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | Criptografía / XOR / Hashing SHA256 / GPG / RSA / OpenSSL / Cracking de contraseñas | **Impacto** | Repasa fundamentos criptográficos apoyándose en referencias al libro de Miyamoto Musashi, con práctica de cifrado, hashing SHA256 de un corpus, operaciones asimétricas y cracking de contraseña |

---

**Contexto:** Sala que introduce los fundamentos de la criptografía con un hilo conductor tomado del *Libro de los cinco anillos* de Miyamoto Musashi (autor de la cita inicial). Se trabaja con retos de texto (waste/science/understand), operaciones XOR y valores hexadecimales (e7, 27, 4f), claves de 4096 bits, la generación de hashes SHA256 de un corpus y el cracking de la contraseña `qwerty123`, cerrando con dos tareas de revisión.

## Solucionario

### Task 1: Introducción

**Explicación:** Contexto histórico-criptográfico de la sala. Pregunta sobre la obra/autor de referencia:

1. Miyamoto Musashi

### Task 2: Cita del Libro

**Explicación:** Palabras que completan el reto sobre el texto de la obra:

2. 1. waste
   2. science
   3. understand

### Task 3: Reto XOR y Hex

**Explicación:** Resultados intermedios del reto de cifrado (percepción y valores en hexadecimal):

3. 1. Perception
   2. e7
   3. 27

### Task 4: Cifrado de Archivo

**Explicación:** Operaciones de cifrado con claves generadas:

4. 1. 4096
   2. 4f

### Task 5: Hash SHA256

**Explicación:** Hashes SHA256 generados a partir del corpus/texto de la sala:

5. 1. 2c34b68669427d15f76a1c06ab941e3e6038dacdfb9209455c87519a3ef2c660
   2. 11faeec5edc2a2bad82ab116bbe4df0f4bc6edd96adac7150bb4e6364a238466
   3. c7e4de386a09ef970300243a70a444ee2a4ca62413aeaeb7097d43d2c5fac89f

### Task 6: Criptografía Asimétrica (RSA)

**Explicación:** Parámetros de la clave asimétrica usada en la sala:

6. 1. 4096
   2. 2039

### Task 7: Cracking de Contraseña del Archivo

**Explicación:** La contraseña que protege uno de los recursos se obtiene por fuerza bruta/diccionario:

7. qwerty123

### Task 8: Revisión 1

**Explicación:** Apartado de repaso. No se requiere respuesta:

8. No answer needed

### Task 9: Revisión 2

**Explicación:** Apartado final de cierre de la sala. No se requiere respuesta:

9. No answer needed

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Quién escribió la obra referenciada en la introducción? | `Miyamoto Musashi` |
| 2 | Primera palabra del reto de texto | `waste` |
| 3 | Segunda palabra del reto de texto | `science` |
| 4 | Tercera palabra del reto de texto | `understand` |
| 5 | Resultado del reto de percepción | `Perception` |
| 6 | Valor hexadecimal del reto (1) | `e7` |
| 7 | Valor hexadecimal del reto (2) | `27` |
| 8 | Tamaño de clave usado en el cifrado | `4096` |
| 9 | Valor hexadecimal de la clave/operación | `4f` |
| 10 | Hash SHA256 calculado (1) | `2c34b68669427d15f76a1c06ab941e3e6038dacdfb9209455c87519a3ef2c660` |
| 11 | Hash SHA256 calculado (2) | `11faeec5edc2a2bad82ab116bbe4df0f4bc6edd96adac7150bb4e6364a238466` |
| 12 | Hash SHA256 calculado (3) | `c7e4de386a09ef970300243a70a444ee2a4ca62413aeaeb7097d43d2c5fac89f` |
| 13 | Tamaño de la clave RSA/OpenSSL | `4096` |
| 14 | Número asociado a la clave RSA/OpenSSL | `2039` |
| 15 | Contraseña crackeada del archivo | `qwerty123` |
| 16 | Apartado de revisión 1 | `No answer needed` |
| 17 | Apartado de revisión 2 | `No answer needed` |

---

**Metodología:**
1. Identificar la obra y autor de referencia de la sala (Miyamoto Musashi).
2. Resolver el reto de texto con las palabras del libro.
3. Resolver el reto XOR/hexadecimal.
4. Realizar operaciones de cifrado con claves generadas (4096).
5. Calcular los hashes SHA256 del corpus.
6. Analizar la criptografía asimétrica (RSA/OpenSSL).
7. Crackear la contraseña del archivo (`qwerty123`) y cerrar con las tareas de revisión.

**Learning chain:** Musashi → cita del libro (waste/science/understand) → reto XOR (Perception, e7, 27) → cifrado (4096, 4f) → SHA256 del corpus → RSA/OpenSSL (4096, 2039) → crack de contraseña → revisión

**Lección:** *La criptografía real combina conceptos históricos, operaciones XOR, hashing y aritmética de claves grandes; y tal como demuestra la sala, una mala contraseña termina reduciendo todo el esquema a un simple ataque de diccionario.*

**MITRE ATT&CK:** T1059 - Command and Scripting Interpreter (uso de herramientas CLI de cifrado); T1486 - Data Encrypted for Impact (cifrado de archivos); T1114 - Email Collection; la sala es fundamentalmente formativa (crypto fundamentals) y no despliega un TTP ofensivo directo

**Fuente:** [TryHackMe - Introduction to Cryptography](https://tryhackme.com/room/introductiontocryptography)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.