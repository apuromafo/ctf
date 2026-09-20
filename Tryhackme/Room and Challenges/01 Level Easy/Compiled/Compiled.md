# Compiled

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | reto de ingeniería inversa | `compiled` | https://tryhackme.com/room/compiled | 01 Level Easy | TryHackMe | ELF / Ghidra / strings / scanf / strcmp / anti-reversing (cadena-trampa "StringsIsForNoobs") | Descubrir la contraseña de un binario ELF que comprueba la entrada con `strcmp`, y recuperar el input correcto que imprime "Correct!". |

---

**Contexto:** Reto de reversing de la categoría Easy. Se entrega un binario ELF (`Compiled.Compiled`) que pide una contraseña e imprime "Correct!" o "Try again!". El programa construye a propósito una cadena llamativa ("StringsIsForNoobs") para despistar a quien ejecute `strings`, y luego usa `scanf("DoYouEven%sCTF", ...)` seguido de comparaciones con `__dso_handle` (blocklist) y `_init` (la comprobación real). La contraseña correcta, introducida como `DoYouEven_init`, hace que `local_28` sea `_init`.

> **ES:** "Simple Reversing Challenge": descarga el binario, descompila su `main` (por ejemplo con Ghidra) y descubre la contraseña que hace que el programa imprima "Correct!". ¡Ten cuidado, puede haber medidas anti-reversing!
> **EN:** "Simple Reversing Challenge": download the binary, decompile its `main` (e.g. with Ghidra) and discover the password that makes the program print "Correct!". Beware, there may be anti-reversing measures in place!

## Solucionario

### Task 1: Bienvenida / Welcome

**Explicación:** Se descarga el fichero de la tarea (también está en el AttackBox en `/root/Rooms/Compiled/`). El binario pide "Password:" y captura la entrada con `scanf("DoYouEven%sCTF", local_28)`. El primer `strcmp` rechaza exactamente `__dso_handle` (es una pista falsa) y el segundo exige que `local_28` sea `_init`. Como `%s` se detiene en el primer espacio o en el fin de la entrada, y el `CTF` final del formato no es obligatorio, la contraseña ganadora es `DoYouEven_init` (introducir `DoYouEven_initCTF` falla, porque `%s` se come el `CTF` como parte del buffer).

```c
undefined8 main(void) {
  int iVar1;
  char local_28 [32];
  fwrite("Password: ", 1, 10, stdout);
  __isoc99_scanf("DoYouEven%sCTF", local_28);
  iVar1 = strcmp(local_28, "__dso_handle");
  if ((-1 < iVar1) && (iVar1 = strcmp(local_28, "__dso_handle"), iVar1 < 1)) {
    printf("Try again!");
    return 0;
  }
  iVar1 = strcmp(local_28, "_init");
  if (iVar1 == 0) { printf("Correct!"); }
  else { printf("Try again!"); }
  return 0;
}
```

```bash
strings Compiled.Compiled      # aparece "DoYouEven%sCTF", "__dso_handle", "_init" y la trampa "StringsIsForNoobs"
./Compiled.Compiled
Password: DoYouEven_init
Correct!
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la contraseña? / What is the password? | `DoYouEven_init` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la contraseña? / What is the password? | `DoYouEven_init` |

---

**Metodología:** Probar el binario con contraseñas incorrectas, inspeccionar la cadena de formato `"DoYouEven%sCTF"` con `strings`/`ltrace` y descompilar la función `main` con Ghidra. Se identifica una blocklist (`__dso_handle`) y la comparación real con `_init`, y se deduce la contraseña completa `DoYouEven_init`, respetando el comportamiento de `scanf` con `%s`.

### Cadena de ataque / Attack Chain

```text
Descargar binario -> ejecutar (Try again!) -> strings/ltrace -> Ghidra (decompilación de main) -> entender scanf("DoYouEven%sCTF") -> blocklist __dso_handle -> strcmp(_init) -> password: DoYouEven_init -> Correct!
```

**Learning chain:** Ejecución inicial -> strings/ltrace -> decompilación con Ghidra -> análisis del formato scanf -> strcmp/blocklist -> construcción de la contraseña.

**Lección:** *No basta con `strings`: las cadenas de formato de `scanf` y los `strcmp` parciales esconden la lógica real, y el comportamiento de `%s` (que no exige los literales finales del formato) es la clave para obtener la contraseña ganadora.*

**MITRE ATT&CK:** N/A (reto de ingeniería inversa de un binario local)

**Fuente:** [TryHackMe - Compiled](https://tryhackme.com/room/compiled)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.