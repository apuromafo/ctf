# Reversing ELF

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | challenge | `reversingelf` | https://tryhackme.com/room/reversingelf | 01 Level Easy | TryHackMe | ingeniería inversa / ELF / gdb / strings / base64 / strcmp / crackme | Reto de ingeniería inversa para principiantes: 8 binarios ELF de dificultad creciente que hay que romper para recuperar contraseñas y flags. |

---

**Contexto:** Sala CTF de introducción a la ingeniería inversa compuesta por 8 binarios ELF (crackmes). Cada binario esconde una contraseña o una flag que hay que recuperar por distintas vías: `strings`, `ltrace`/`strace`, descifrado base64, comparaciones hardcodeadas en el disassembly, ofuscación con XOR y análisis con herramientas como radare2/IDA. Sirve de primera toma de contacto con el reversing de binarios Linux.

> **ES:** "Reversing ELF" — 8 crackmes ELF para principiantes: strings, ltrace, base64, disassembly y XOR.
> **EN:** "Reversing ELF" — 8 ELF crackmes for beginners: strings, ltrace, base64, disassembly and XOR.

## Solucionario

### Task 1: Crack 1

**Explicación:** El primer binario es el más sencillo: la flag aparece directamente en texto plano al usar `strings` sobre el ejecutable.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag del crack 1? / What is the flag for crack 1? | `flag{not_that_kind_of_elf}` |

### Task 2: Crack 2

**Explicación:** Con `ltrace` o `strings` se obtiene la contraseña con la que el binario compara la entrada: `super_secret_password`. Al ejecutar el binario con esa contraseña se obtiene la flag.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la contraseña del crack 2? / What is the password for crack 2? | `super_secret_password` |
| 2 | ¿Cuál es la flag del crack 2? / What is the flag for crack 2? | `flag{if_i_submit_this_flag_then_i_will_get_points}` |

### Task 3: Crack 3

**Explicación:** El binario compara la entrada decodificándola en base64. La cadena que se obtiene tras decodificar es la contraseña `f0r_y0ur_5ec0nd_le55on_unbase64_4ll_7h3_7h1ng5`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la contraseña del crack 3? / What is the password for crack 3? | `f0r_y0ur_5ec0nd_le55on_unbase64_4ll_7h3_7h1ng5` |

### Task 4: Crack 4

**Explicación:** El binario ejecuta `strcmp` contra una contraseña almacenada que se obtiene con `strings` o `ltrace`: `my_m0r3_secur3_pwd`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la contraseña del crack 4? / What is the password for crack 4? | `my_m0r3_secur3_pwd` |

### Task 5: Crack 5

**Explicación:** El quinto crackme es ofuscado: el binario modifica la cadena en memoria (XOR). Analizando el flujo con gdb o un debugger, la contraseña final aplicada es `OfdlDSA|3tXb32~X3tX@sX`4tXtz`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la contraseña del crack 5? / What is the password for crack 5? | ``OfdlDSA|3tXb32~X3tX@sX`4tXtz`` |

### Task 6: Crack 6

**Explicación:** El binario compara la entrada desofuscando el valor durante la ejecución; tras seguir la lógica con un debugger la contraseña es `1337_pwd`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la contraseña del crack 6? / What is the password for crack 6? | `1337_pwd` |

### Task 7: Crack 7

**Explicación:** Con `strings` o el disassembly del binario se localiza la flag directamente: `flag{much_reversing_very_ida_wow}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag del crack 7? / What is the flag for crack 7? | `flag{much_reversing_very_ida_wow}` |

### Task 8: Crack 8

**Explicación:** En el último crackme, la flag se extrae de los datos/strings del binario o tras ejecutarlo con el argumento correcto: `flag{at_least_this_cafe_wont_leak_your_credit_card_numbers}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag del crack 8? / What is the flag for crack 8? | `flag{at_least_this_cafe_wont_leak_your_credit_card_numbers}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag del crack 1? / What is the flag for crack 1? | `flag{not_that_kind_of_elf}` |
| 2 | ¿Cuál es la contraseña del crack 2? / What is the password for crack 2? | `super_secret_password` |
| 3 | ¿Cuál es la flag del crack 2? / What is the flag for crack 2? | `flag{if_i_submit_this_flag_then_i_will_get_points}` |
| 4 | ¿Cuál es la contraseña del crack 3? / What is the password for crack 3? | `f0r_y0ur_5ec0nd_le55on_unbase64_4ll_7h3_7h1ng5` |
| 5 | ¿Cuál es la contraseña del crack 4? / What is the password for crack 4? | `my_m0r3_secur3_pwd` |
| 6 | ¿Cuál es la contraseña del crack 5? / What is the password for crack 5? | ``OfdlDSA|3tXb32~X3tX@sX`4tXtz`` |
| 7 | ¿Cuál es la contraseña del crack 6? / What is the password for crack 6? | `1337_pwd` |
| 8 | ¿Cuál es la flag del crack 7? / What is the flag for crack 7? | `flag{much_reversing_very_ida_wow}` |
| 9 | ¿Cuál es la flag del crack 8? / What is the flag for crack 8? | `flag{at_least_this_cafe_wont_leak_your_credit_card_numbers}` |

---

**Metodología:** Empezar por técnicas sencillas (`strings`, `ltrace`) con los primeros crackmes, pasar a la decodificación base64 y las contraseñas hardcodeadas comparadas con `strcmp`, y terminar con los binarios ofuscados (XOR, modificación en memoria) usando gdb y analizando el disassembly para recuperar las contraseñas y flags finales.

### Cadena de ataque / Attack Chain

```text
strings -> ltrace/strace -> base64 -> strcmp (cadenas hardcodeadas) -> gdb/disassembly -> XOR/desofuscación en memoria -> flag
```

**Learning chain:** strings -> ltrace -> base64 -> disassembly/IDA -> ofuscación XOR -> flags.

**Lección:** *El reversing es una escalera: lo que hoy es un simple strings o ltrace se convierte en análisis de ofuscación; cada técnica suma a la siguiente, y el objetivo es siempre recuperar la cadena con la que el binario compara la entrada.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application); referencia genérica a técnicas de análisis local de binarios (strings, gdb, radare2)

**Fuente:** [TryHackMe - Reversing ELF](https://tryhackme.com/room/reversingelf)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.