# Task 6: Checks — HackBack2

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF | task6checks | https://tryhackme.com/room/task6checks | 02 Level Medium | TryHackMe | ELF64, ingeniería inversa, análisis estático, parcheo de binarios | Obtención del flag de la tarea |

---

**Contexto:** La tarea **Checks** de HackBack2 entrega un binario ELF64 x86-64 (access-checks, statically linked, not stripped) que aplica varias comprobaciones antes de mostrar el flag: un usuario con `pw_name == "800"`, la variable de entorno `SECRET_REQ=coolenvvar` y la existencia del archivo `secrets.zip`. Al ejecutarlo tal cual crashea (segfault) porque `getpwuid` intenta cargar módulos NSS dinámicos en un binario estático. El análisis estático revela que la función `asvv889a` calcula e imprime el flag de forma independiente (`strtol` de `88ED12AC` → `printf %X`), por lo que basta con parchear `main` para que la llame directamente. El flag es `THM{88ED12AC}`.

## Solucionario

### Task 6: [Medium] [Reverse Engineering] Checks

**Explicación:** El reto pide el flag del binario `access-checks`, un ELF64 x86-64 estático que ejecuta 4 comprobaciones antes de imprimir el flag. El análisis estático muestra la función `asvv889a` que convierte la cadena `88ED12AC` a entero y lo imprime con el formato `Here you go: %X\n`; el `main` ejecuta una secuencia de checks (usuario, variable de entorno, archivo) que impiden llegar hasta ahí. Como el flag NO depende de los checks, se parchea el cuerpo de `main` para que llame directamente a `asvv889a` y se obtiene el flag sin cumplir ninguna condición. Ruta alternativa (Ruta B): en teoría bastaría con un usuario con `pw_name == "800"`, `export SECRET_REQ=coolenvvar` y crear un `secrets.zip`, pero en este entorno `getpwuid` crashea al cargar NSS dinámicos en un binario estático.

**Nivel:** Medium - Reverse Engineering

## Qué era / What it was

Un binario con varias comprobaciones antes de mostrar el flag. El original se caía antes de llegar al flag.

## Cómo se resolvió / How it was resolved

1. Se analizó el binario por dentro (decompilación).
2. Se encontró la función `asvv889a` que convierte `88ED12AC` a mayúsculas y lo imprime.
3. El `main` tenía 4 comprobaciones (usuario, variable de entorno, archivo) que impedían llegar ahí.
4. Se parcheó el `main` para que llamara directo a la función del flag.
5. Con el parche aplicado, el programa imprime el flag.

## Flag / Bandera

THM{88ED12AC}

### Detalle del análisis (del writeup local)

```text
0) Info del binario
- Archivo: access-checks
- Formato: ELF64 x86-64, statically linked, not stripped
- SHA-256: BEF862A5C8C1B7503522D1D5FCAA5665A95C31ABF24E95B6F2D86610AF07C554
- Al ejecutarlo sin tocar nada: Segmentation fault (crash en
  getpwuid -> carga de modulos NSS dinamicos, falla en binario estatico)

Simbolos propios del reto (no libc):
  0000000000400b6d T asvv889a
  0000000000400bd8 T main

1) Analisis estatico
Strings de interes:
  0x49e808  "Here you go: %X\n"      <- formato del flag
  0x49e819  "SECRET_REQ"             <- nombre de env var
  0x49e824  "800"                    <- usuario requerido (pw_name)
  0x49e828  "coolenvvar"             <- valor de la env var
  0x49e833  "secrets.zip"            <- archivo requerido
  0x49e840  "hm you need to do more to get the flag"  <- fallo

asvv889a (0x400b6d):
  - movabs rax, 0x4341323144453838   ; bytes LE: 38 38 45 44 31 32 41 43 = "88ED12AC"
  - strtol(ptr, NULL, 16)  -> 0x88ED12AC
  - printf("Here you go: %X\n", 0x88ED12AC)  ->  88ED12AC

main (0x400bd8):
  Secuencia de checks (de ahi el nombre del reto):
    1) getuid() -> getpwuid(uid)  ; comprueba pw_name == "800"
    2) getenv("SECRET_REQ")       ; debe ser distinta de NULL
    3) strcmp(env, "coolenvvar")  ; debe ser 0
    4) access("secrets.zip", 0)   ; el archivo debe existir
  Si TODOS pasan -> call asvv889a  (imprime el flag)
  Si alguno falla -> printf("hm you need to do more to get the flag")

2) Resolucion
El flag NO depende de los checks: asvv889a calcula e imprime el
resultado directamente (strtol de "88ED12AC" en base 16 -> printf %X).

Ruta A (dinamica, parchear main):
  Reescribir el cuerpo de main para que llame directo a asvv889a
  (bypass de getpwuid + los 3 checks):

  En VA 0x400bd8:
    push   rbp
    mov    rbp,rsp
    sub    rsp,0x10
    mov    eax,0x0
    call   0x400b6d <asvv889a>    ; e8 83 ff ff ff
    mov    eax,0x0
    leave
    ret

  bytes: 55 48 89 e5 48 83 ec 10 b8 00 00 00 00
         e8 83 ff ff ff b8 00 00 00 00 c9 c3

  Ejecucion:
    $ ./access-checks.patched
    Here you go: 88ED12AC

Ruta B (sin parchear, cumpliendo los checks):
  Teoricamente bastaria con:
    1) un usuario con pw_name == "800" (getpwuid devuelve el nombre del uid actual)
    2) export SECRET_REQ=coolenvvar
    3) crear un archivo secrets.zip en el directorio actual
  En este entorno falla antes porque getpwuid crashea al intentar
  cargar NSS dinamicos en un binario estatico.
```

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 6.1 | [+50] What is the flag? | `THM{88ED12AC}` |

---

**Metodología:** Análisis estático del binario (strings + decompilación) para identificar la función del flag y las comprobaciones del `main`, y parcheo binario del cuerpo de `main` (bypass de `getpwuid`, entorno y archivo) para ejecutar directamente `asvv889a` (PTES fase de exploitation, ingeniería inversa).

**Learning chain:** reconocer ELF64 estático → strings ("Here you go: %X") → función asvv889a (88ED12AC → strtol → printf %X) → checks del main (getpwuid/entorno/access) → parcheo de main (e8 83 ff ff ff) → flag.

**Lección:** *Los checks de protección de un binario no siempre protegen el flag: si la función que lo imprime calcula el valor de forma independiente, basta un parche mínimo en main para llegar al resultado sin cumplir ninguna condición.*

**MITRE ATT&CK:** T1480 Execution Guardrails (comprobaciones de ejecución) · T1106 Native API (llamada directa a asvv889a) · T1027 Obfuscated Files or Information (ofuscación/dificultad del análisis).

**Fuente:** [TryHackMe - Task 6: Checks — HackBack2](https://tryhackme.com/room/task6checks)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.