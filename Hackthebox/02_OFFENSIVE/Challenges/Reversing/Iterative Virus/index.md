# Iterative Virus [verificar]

> **ES:** Challenge de Reversing (dificultad oficial por verificar): un PE de Windows (`iterative_virus.exe`) con una sección personalizada `.ivir` cifrada; hay que invertir la rutina de descifrado iterativo, descifrar y parchear el binario para leer la flag en claro (`HTB{...}`).
> **EN:** Reversing challenge (official difficulty to verify): a Windows PE (`iterative_virus.exe`) with a custom encrypted `.ivir` section; reverse the iterative decryption routine, decrypt and patch the binary to read the flag in cleartext (`HTB{...}`).

| Campo | Valor |
|-------|-------|
| **Categoría** | Reversing |
| **Dificultad** | [verificar] (oficial no hallada en 3 intentos de búsqueda) |
| **Estado** | Retired (inferido: existen decryptor y binario públicos; [verificar] estado actual en plataforma) |
| **URL** | https://app.hackthebox.com/challenges/ (slug `Iterative Virus`; pendiente de verificar ID exacto) |
| **Archivos** | `iterative_virus.exe` (descarga con contraseña `hackthebox`) [verificar nombre exacto del zip] |
| **Fecha de resolución** | 2026-09-25 (documentación; resuelto previamente según stub local) |
| **Puntos** | [verificar] |

---

## 🎯 Objetivo / Goal

> **ES:** Extraer el contenido cifrado de la sección `.ivir`, invertir el descifrado iterativo con las claves halladas por ingeniería inversa, parchear el PE y leer la flag en claro (`HTB{...}`) con un desensamblador.
> **EN:** Extract the encrypted content of the `.ivir` section, invert the iterative decryption with the keys found by reverse engineering, patch the PE, and read the flag in cleartext (`HTB{...}`) with a disassembler.

---

## 🛠️ Herramientas usadas / Tools used

- [ ] `file` + `strings` (triaje del PE)
- [ ] Desensamblador/decompilador (Ghidra / IDA / x64dbg) para hallar claves y rutina
- [ ] Python + `pefile` + `binascii` (extracción, descifrado y parcheo del PE)
- [ ] Visor de secciones (`pefile`/CFF Explorer/pe-bear) para confirmar `.ivir`

---

## 📋 Pasos / Steps

### Paso 1 — Análisis inicial / Triage

> **ES:** Se confirma que es un PE de Windows y se detecta la sección no estándar `.ivir`, que concentra los datos cifrados.
> **EN:** Confirm it is a Windows PE and spot the non-standard `.ivir` section holding the encrypted data.

```bash
unzip iterative_virus.zip   # contraseña: hackthebox
file iterative_virus.exe
strings -n 6 iterative_virus.exe | head -n 60
python3 -c "import pefile; pe=pefile.PE('iterative_virus.exe'); print([ (s.Name, hex(s.VirtualAddress), hex(s.SizeOfRawData)) for s in pe.sections ])"
```

**Resultado / Result:** PE con sección `.ivir` presente; las cadenas no muestran la flag en claro porque los datos útiles están cifrados (paráfrasis del README de kaixeb).

### Paso 2 — Ingeniería inversa de la rutina y claves / Reverse routine and keys

> **ES:** Al invertir el binario se encuentra una rutina que descifra por multiplicaciones iteradas con varias claves de 64 bits sobre bloques de 8 bytes en little-endian, aplicada a un rango concreto de la sección.
> **EN:** Reversing the binary reveals a routine that decrypts via iterated multiplications with several 64-bit keys over 8-byte little-endian blocks, applied to a specific range of the section.

```bash
# Sin comando único: en Ghidra/IDA buscar referencias a ".ivir",
# la constante de dirección base y el bucle de multiplicación.
# Resultado del análisis (constantes del decryptor de kaixeb, no son la flag):
#   claves = 0x6E2368B9C685770B, 0xEB7FD64E061C1A3D,
#            0xCB8FF2D53D7505A1, 0x0F1EF554206DCE4D
#   inicio codificado ~ 0x14001C7E4, tamaño 408 bytes
```

**Resultado / Result:** Claves y ventana de datos identificadas (4 claves de 64 bits, 408 bytes desde la dirección indicada, en bloques little-endian de 8 bytes). La operación es multiplicación con máscara a 64 bits (`& 0xFFFFFFFFFFFFFFFF`) aplicada iterativamente por cada clave (paráfrasis del script citado, no copiado literal).

### Paso 3 — Descifrar y parchear el PE / Decrypt and patch PE

> **ES:** Se replica la lógica en Python con `pefile`: extraer `.ivir`, recortar la ventana cifrada, convertir a enteros little-endian, multiplicar por cada clave, reconvertir a bytes y parchear el binario resultante.
> **EN:** Replicate the logic in Python with `pefile`: extract `.ivir`, slice the encrypted window, convert to little-endian integers, multiply by each key, convert back to bytes, and patch the resulting binary.

```bash
pip install pefile
python3 iterative_virus_decryptor.py
ls -l iterative_virus_decrypted.exe
strings -n 6 iterative_virus_decrypted.exe | grep -i "HTB" | head
# Nota: el script de referencia usa una ruta absoluta local en `filename`;
# adaptarla al directorio de trabajo antes de ejecutar.
```

**Resultado / Result:** Se genera `iterative_virus_decrypted.exe` ("Patching the binary was successful" en el script de referencia); al abrirlo en el desensamblador/decompilador la flag ya aparece en claro con formato `HTB{...}` (no se reproduce aquí por integridad del contenido; challenge retirado).

---

## 🧠 Lo aprendido / Learned

- [ ] Secciones PE personalizadas (`.ivir`) como contenedor de datos cifrados: hay que leer `VirtualAddress`/`SizeOfRawData` y calcular el offset real (`ImageBase` + RVA).
- [ ] Endianness importa: los bloques de 8 bytes se interpretan en little-endian antes de operar.
- [ ] Descifrado "iterativo" = aplicar la misma operación (multiplicación mod 2⁶⁴) en cascada con varias claves; replicarlo en Python evita depurar el malware en vivo.
- [ ] Parchear el PE con `pefile` (`set_bytes_at_offset` + `write`) permite reutilizar el flujo normal de análisis estático sobre el binario ya descifrado.
- [ ] Dificultad oficial de este reto no documentada en fuentes consultadas: queda como pendiente explícito.

---

## 📚 Fuentes y Referencias / Sources

- **Decryptor de referencia (lógica parafraseada, no copiada):** [HTBIterativeVirus](https://github.com/kaixeb/HTBIterativeVirus) — kaixeb (README: extrae contenido cifrado de `iterative_virus.exe`, lo descifra con claves halladas por ingeniería inversa, parchea el PE como `iterative_virus_decrypted.exe` y permite hallar la flag en claro; script `iterative_virus_decryptor.py` con sección `.ivir`, 4 claves, dirección `0x14001C7E4`, 408 bytes, bloques LE de 8 bytes y multiplicación `& 0xFFFFFFFFFFFFFFFF`)
- **Nota local previa:** stub raíz `Soluciones/Challenges/iterative_virus.md` ("# Solved Challenge: Iterative Virus / Points: 0pts") migrado a esta plantilla (los "0pts" eran marcador local, no puntuación oficial; categoría Reversing inferida por la evidencia de ingeniería inversa sobre un PE)
- **Fecha de acceso:** 2026-09-25
- **Autor de este walkthrough:** Apuromafo (síntesis propia parafraseada a partir de la fuente citada)

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. Challenge retirado (inferido); no se publican flags literales.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Retired challenge (inferred); no literal flags published.

_Fecha de edición: 2026-09-25_
