# Obfuscation - The Egg Shell File

| **Dificultad** | Easy | **Tipo** | walkthrough | **Slug** | `day18obfuscationtheeggshellfile` |
| **Link** | [TryHackMe](https://tryhackme.com/room/adventofcyber25) |
| **Sección** | Advent of Cyber Tryhackme |
| **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | obfuscation / ROT ciphers / ROT1 / ROT13 / XOR obfuscation / CyberChef / C2 URL / API key |
| **Impacto** | Ofuscar y desofuscar contenido (C2 URL y API key) para evadir o vencer filtros basados en keywords |

---

**Contexto:** Día 18 del Advent of Cyber 2025. La **ofuscación** hace que los datos sean difíciles de leer o analizar: permite a los atacantes evadir la detección, retrasar el análisis y saltarse herramientas de seguridad simples basadas en keywords. Se repasan dos técnicas básicas para decodificar con CyberChef: los **ROT ciphers** (ROT1 desplaza cada letra 1 posición; ROT13 las desplaza 13) y la **ofuscación XOR** (cada byte se combina con una clave). Con eso se desofusca una URL de C2 y se ofusca una API key ejecutando el script Egg Shell.

## Solucionario

### Día 18: Obfuscation - The Egg Shell File

**Explicación:**

- Obfuscation -> makes data hard to read or analyze; allows attackers to evade detection, delay analysis, Bypass simple keyword-based security tools
- Basic Obfuscation Techniques (Use cyberChef to decode)
     1. ROT Ciphers: ROT1: Shifts each letter forward by 1; ROT13: Shifts letters by 13
     2. XOR Obfuscation: Each byte is XOR’ed with a key

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the first flag you get after deobfuscating the C2 URL and running the script? | `THM{C2_De0bfuscation_29838}` |
| 2 | What is the second flag you get after obfuscating the API key and running the script again? | `THM{API_Obfusc4tion_ftw_0283}` |

---

**Metodología:** Se tomó la URL de C2 ofuscada del script Egg Shell y se decodificó con CyberChef (ROT y/o XOR según la técnica detectada). Se ejecutó el script con la URL desofuscada y se obtuvo el primer flag. Después se ofuscó la API key aplicando la técnica correspondiente y se volvió a ejecutar el script para obtener el segundo flag.
**Learning chain:** obfuscation (ROT1/ROT13/XOR) -> CyberChef decode -> C2 URL desofuscada -> ejecutar Egg Shell -> flag 1 -> ofuscar API key -> ejecutar de nuevo -> flag 2

Cadena de ataque / Attack Chain:
```
egg file -> C2 URL ofuscada (ROT/XOR) -> CyberChef decode -> THM{C2_De0bfuscation_29838} -> API key ofuscada -> ejecutar script -> THM{API_Obfusc4tion_ftw_0283}
```

**Lección:** *La ofuscación es una carrera bilateral: los atacantes la usan para evadir detección por keywords y los analistas la vencen con transformaciones simples (ROT, XOR, base64) encadenadas en CyberChef.*

**MITRE ATT&CK:** T1027 - Obfuscated Files or Information, T1140 - Deobfuscate/Decode Files or Information

**Fuente:** [TryHackMe - Obfuscation - The Egg Shell File](https://tryhackme.com/room/adventofcyber25)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.