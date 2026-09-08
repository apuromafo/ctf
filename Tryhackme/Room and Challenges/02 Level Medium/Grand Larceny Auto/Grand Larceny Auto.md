# Grand Larceny Auto

| **Dificultad** | MEDIUM | **Tipo** | CTF | **Slug** | `grandlarcenyauto` |
| **Link** | [TryHackMe](https://tryhackme.com/room/grandlarcenyauto) | **Sección** | 02 Level Medium | **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | Game Hacking / .NET Reverse Engineering / Control-Flow Flattening / dnSpy | **Impacto** | Evalúa la capacidad de reutilizar lógica ofuscada de una DLL .NET para extraer la flag real sin descifrar el flujo |

---

**Contexto:** Sala de **game hacking de Windows** (.NET) de dificultad Media. Se recibe el juego **Grand Larceny Auto** y el objetivo es obtener la flag real de la bóveda. La DLL `GrandLarcenyAuto.dll` está ofuscada con **control-flow flattening**, pero se puede **reutilizar la lógica** desde un pequeño programa .NET: basta con instanciar un `PlayerState` con 6 estrellas y llamar a `SafehouseVault.TryOpen()` para "sellar la bóveda" y obtener la flag de la salida. Usar Windows, no el AttackBox. **Windows game hacking** room (.NET) of Medium difficulty. You get the game **Grand Larceny Auto** and the goal is to obtain the real vault flag. The `GrandLarcenyAuto.dll` is obfuscated with **control-flow flattening**, but the logic can be **reused** from a small .NET program: just instantiate a `PlayerState` with 6 stars and call `SafehouseVault.TryOpen()` to "unseal the vault" and get the flag from the output. Use Windows, not the AttackBox.

## Solucionario

### Task 1: Find the Flag

**Explicación:** 1 tarea (descargable). Abrir `GrandLarcenyAuto.dll` (.NET) en **dnSpy**. En el espacio de nombres `GrandLarcenyAuto`: `CheatConsole.Submit` tiene un código hardcodeado (flag señuelo/decoy), `CryptoUtil` contiene las claves, `GameController`, `PlayerState` (`WantedStars`, `Cash`, `X`, `Y`, `InCar`) y `SafehouseVault`. `SafehouseVault.TryOpen()` está ofuscado con control-flow flattening (un switch gigante) y exige **`WantedStars >= 6`**. Vía dinámica: parchear la DLL y jugar hasta abrir la bóveda. Vía estática (la demostrada): proyecto consola .NET 8 con `<Reference HintPath="GrandLarcenyAuto.dll">`; `var player = new PlayerState { WantedStars = 6 }; new SafehouseVault(player).TryOpen();` y `dotnet run` → salida `VAULT UNSEALED` + flag. 1 pregunta. En inglés: 1 task (downloadable). Open `GrandLarcenyAuto.dll` (.NET) in **dnSpy**. In namespace `GrandLarcenyAuto`: `CheatConsole.Submit` has hardcoded code (decoy flag), `CryptoUtil` holds the keys, `GameController`, `PlayerState` (`WantedStars`, `Cash`, `X`, `Y`, `InCar`) and `SafehouseVault`. `SafehouseVault.TryOpen()` is obfuscated with control-flow flattening (a giant switch) and requires **`WantedStars >= 6`**. Dynamic route: patch the DLL and play until the vault opens. Static route (the demonstrated one): a .NET 8 console project with `<Reference HintPath="GrandLarcenyAuto.dll">`; `var player = new PlayerState { WantedStars = 6 }; new SafehouseVault(player).TryOpen();` and `dotnet run` → output `VAULT UNSEALED` + flag. 1 question.

Nota: La salida de `SafehouseVault.TryOpen()` imprime `VAULT UNSEALED` seguido de `THM{...}`; el valor exacto no está publicado por los walkthroughs. Aquí no se compila la flag real (decoy ni original); se documenta el método que la imprime. English: The output of `SafehouseVault.TryOpen()` prints `VAULT UNSEALED` followed by `THM{...}`; the exact value is not published by walkthroughs. No real flag (decoy or original) is compiled here; the method that prints it is documented.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag? | `THM{...redacted...}` |

---

**Metodología:**
1. Abrir `GrandLarcenyAuto.dll` (.NET) en **dnSpy** (o ILSpy). Explorar el espacio `GrandLarcenyAuto`.
2. Recon del juego: `CheatConsole.Submit` contiene el código de la cheatsheet: introducirlo en la consola del juego "funciona" pero devuelve un flag **señuelo** (decoy). `CryptoUtil` gestiona claves/cifrado, `GameController` orquesta el juego y `PlayerState` modela `WantedStars`, `Cash`, `X`, `Y`, `InCar`.
3. Targeting `SafehouseVault`: `SafehouseVault.TryOpen()` está ofuscado con **control-flow flattening** (un `switch` con muchas variables de estado). El requisito clave es `WantedStars >= 6`.
4. Ruta dinámica (opcional): Parchear la DLL (forzar estrellas/cash/direcciones) y jugar hasta conseguir el estado necesario y abrir la bóveda en el juego real.
5. Ruta estática (demostrada): Crear un proyecto consola **.NET 8** con referencia directa a la DLL:
   `<Reference HintPath="...\GrandLarcenyAuto.dll" />` (si el resolver da problemas, usar la referencia fuerte/de assembly load desde el propio proyecto).
6. Explotar la lógica: en el Main del proyecto consola `var player = new PlayerState { WantedStars = 6 }; new SafehouseVault(player).TryOpen();` — se llama exactamente al método que valida y cifra la flag.
7. `dotnet run` → la salida muestra `VAULT UNSEALED` seguida del `THM{...}` real.

**Learning chain:** GrandLarcenyAuto.dll (.NET) → dnSpy → análisis de espacio GrandLarcenyAuto → identificación de SafehouseVault.TryOpen() → ruta estática con proyecto consola .NET 8 → dotnet run → `VAULT UNSEALED` + THM{...}

**Lección:** *La ofuscación por control-flow flattening impide leer el flujo pero no impide **reutilizar la lógica**: si el método de validación existe y es público, llamarlo desde tu propio programa con los datos correctos (`WantedStars = 6`) obtiene el flag sin descifrar el switch. La flag real está en `SafehouseVault.TryOpen()`, no en la "cheatshell" del juego.*

**MITRE ATT&CK:** T1622 - Debugger Evasion; T1656 - Impair Defenses (ofuscación); CWE-693 - Protection Mechanism Failure

**Fuente:** [TryHackMe - Grand Larceny Auto](https://tryhackme.com/room/grandlarcenyauto)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
