# Soupedecode 01

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|------------|------|------|------|---------|--------|-------------|---------|
| Easy | walkthrough | `soupedecode01` | [TryHackMe](https://tryhackme.com/room/soupedecode01) | 01 Level Easy | TryHackMe | Reverse Engineering, Code Analysis, Hash Identification | Technical — Deobfuscation and code analysis challenges |

---

**Contexto:** Este room presenta desafíos de ingeniería inversa y análisis de código ofuscado. Se requiere identificar hashes, analizar código y resolver ejercicios de "Soupedecode" que ponen a prueba las habilidades de análisis de seguridad.

## Solucionario

### Task 1: Soupedecode Challenge

**Explicación:** Se Identifican los hashes MD5 generados a partir del código ofuscado presentado en el challenge.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the MD5 hash of the first value? | `28189316c25dd3c0ad56d44d000d62a8` |
| 2 | What is the MD5 hash of the second value? | `27cb2be302c388d63d27c86bfdd5f56a` |

---

**Metodología:** Se Aplican técnicas de ingeniería inversa y análisis de código para identificar hashes y valores ofuscados en ejercicios de código malicioso.

### Cadena de ataque / Attack Chain

**Learning chain:** Code Analysis → Obfuscation Detection → Hash Identification → Deobfuscation → Value Extraction

**Lección:** *La capacidad de analizar código ofuscado y identificar hashes es fundamental para el análisis de malware y la ingeniería inversa en ciberseguridad.*

**MITRE ATT&CK:** T1027 — Obfuscated Files or Information; T1140 — Deobfuscate/Decode Files

**Fuente:** [TryHackMe - Soupedecode 01](https://tryhackme.com/room/soupedecode01)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.