# Hashing Basics

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `hashingbasics` | [TryHackMe](https://tryhackme.com/room/hashingbasics) | 01 Level Easy | THM | Hashing, SHA, Hashcat, Rainbow Tables, Encoding | Fundamentos de hashing y cracking de hashes |

---

**Contexto:** Sala del principiante sobre hashing: tipos y longitud de hashes (por ejemplo SHA-256 con 256 bits), cómo hashear palabras, el papel de las rainbow tables, el cracking de hashes con hashcat y el manejo de encoding/decoding de cadenas.

> **ES:** Comprender qué son los hashes, generar y reconocer SHA-256, usar rainbow tables y crackear con hashcat.
> **EN:** Understand what hashes are, generate and recognise SHA-256, use rainbow tables and crack with hashcat.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Presentación de la sala y de los conceptos de hash.

No answer needed

### Task 2: Tipos de hash / Hash Types

**Explicación:** Se calcula un hash SHA-256 de ejemplo y se repasan sus propiedades (longitud y número de bits).

1. `77148c6f605a8df855f2b764bcc3be749d7db814f5f79134d2aa539a64b61f02`
2. `16`
3. `256`

### Task 3: Hashear una palabra / Hashing a Word

**Explicación:** Se aplica el hashing a una palabra concreta para comprobar que un mismo texto produce siempre el mismo hash.

- `qwerty`

### Task 4: Tablas rainbow / Rainbow Tables

**Explicación:** Se explora el uso de rainbow tables para reutilizar hashes de contraseñas comunes y las limitaciones de la técnica.

1. `inS3CyourP4$$`
2. `tryhackme`
3. `Nay`

### Task 5: Hashcat / Hashcat

**Explicación:** Se practica el cracking de hashes con hashcat: valores de configuración y modos de funcionamiento.

1. `256`
2. `2410`
3. `scrypt`

### Task 6: Cracking / Cracking

**Explicación:** Se rompen los hashes propuestos hasta recuperar las contraseñas originales.

1. `85208520`
2. `halloween`
3. `spaceman`
4. `funforyou`

### Task 7: Reto / Challenge

**Explicación:** Reto conjunto de hashing y cracking que combina la generación del hash y su posterior recuperación.

1. `09120c9867ce7f2081d6aaa1775386b98c2f2f246135761aae47d81f58685b9c`
2. `1750`

### Task 8: Codificación / Encoding

**Explicación:** Se diferencia hashing de encoding y se resuelven las cadenas codificadas del apartado.

1. `ENcodeDEcode`
2. `No answer needed`

### Tabla unificada de preguntas y respuestas

| Task | Pregunta | Respuesta |
|------|----------|-----------|
| 1 | — | `No answer needed` |
| 2.1 | Hash SHA-256 calculado | `77148c6f605a8df855f2b764bcc3be749d7db814f5f79134d2aa539a64b61f02` |
| 2.2 | Longitud del valor | `16` |
| 2.3 | Bits del SHA-256 | `256` |
| 3 | Palabra hasheada | `qwerty` |
| 4.1 | Contraseña de la rainbow table | `inS3CyourP4$$` |
| 4.2 | Contraseña encontrada | `tryhackme` |
| 4.3 | Limitación de rainbow tables | `Nay` |
| 5.1 | Valor de hashcat | `256` |
| 5.2 | Modo de hashcat | `2410` |
| 5.3 | Tipo de función | `scrypt` |
| 6.1 | Contraseña 1 | `85208520` |
| 6.2 | Contraseña 2 | `halloween` |
| 6.3 | Contraseña 3 | `spaceman` |
| 6.4 | Contraseña 4 | `funforyou` |
| 7.1 | Hash del reto | `09120c9867ce7f2081d6aaa1775386b98c2f2f246135761aae47d81f58685b9c` |
| 7.2 | Modo de cracking | `1750` |
| 8.1 | Cadena codificada | `ENcodeDEcode` |
| 8.2 | — | `No answer needed` |

---

**Metodología:** Reconocer y generar hashes (SHA-256), comprobar la determinismo del hashing, plantear rainbow tables para contraseñas comunes, romper los hashes con hashcat (modo/parámetros) y distinguir encoding de hashing para resolver el reto final.

### Cadena de ataque / Attack Chain

```text
Introducción -> generar SHA-256 -> hashear palabra -> rainbow tables -> hashcat (modo 2410, scrypt) -> cracking -> reto (1750) -> encoding
```

**Learning chain:** Hash basics → SHA-256 → Rainbow tables → Hashcat → Cracking → Encoding

**Lección:** *Un hash es un cálculo determinista que no debería poder revertirse; por eso las contraseñas débiles caen con rainbow tables y hashcat, y por eso los catálogos de hashes siguen siendo decisivos en auditorías.*

**MITRE ATT&CK:** N/A (Room de hashing)

**Fuente:** [TryHackMe - Hashing Basics](https://tryhackme.com/room/hashingbasics)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.