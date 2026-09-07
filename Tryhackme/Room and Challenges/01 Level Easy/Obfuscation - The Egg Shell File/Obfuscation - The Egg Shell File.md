# Obfuscation - The Egg Shell File

| **Dificultad** | Medium |
| **Tipo** | walkthrough |
| **Slug** | `obfuscation-aoc2025-e5r8t2y6u9` |
| **Link** | [TryHackMe](https://tryhackme.com/r/room/obfuscation-aoc2025-e5r8t2y6u9) |
| **Sección** | Advent of Cyber 2025 |
| **Componentes** | Obfuscation, C2 URL, API keys, encoding |
| **Impacto** | N/A |

---

**Contexto:** En esta sala del Advent of Cyber 2025 (Día 18), se desofusca una URL de C2 y se ofusca una API key en un script malicioso. Se utiliza un pie de claves de descodificación para aplicar codificaciones inversas y revelar los flags ocultos.

## Solucionario

### Task 1: Day 18 - Obfuscation

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the first flag after deobfuscating the C2 URL? | `THM{C2_De0bfuscation_29838}` |
| 2 | What is the second flag after obfuscating the API key? | `THM{API_Obfusc4tion_ftw_0283}` |

---

**Metodología:** Se utilizó una tabla de claves de descodificación para revertir la ofuscación de la URL C2 (reversal, desplazamiento de caracteres, XOR) y revelar el primer flag. Luego se aplicó la ofuscación inversa a la API key para obtener el segundo flag.

**Learning chain:** obfuscation techniques → C2 URL deobfuscation → API key obfuscation → encoding tables → flag extraction

**MITRE ATT&CK:** T1027 - Obfuscated Files or Information, T1071.001 - Application Layer Protocol: Web Protocols

**Fuente:** [TryHackMe - Obfuscation - The Egg Shell File](https://tryhackme.com/r/room/obfuscation-aoc2025-e5r8t2y6u9)