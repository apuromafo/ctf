# Breaking Crypto the Simple Way

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `breakingcryptothesimpleway` | [TryHackMe](https://tryhackme.com/room/breakingcryptothesimpleway) | 01 Level Easy | TryHackMe | criptografía, RSA, modos de cifrado, descifrado | Comprensión práctica de cómo implementaciones criptográficas inseguras pueden romperse |

---

**Contexto:** Sala introductoria de criptografía aplicada. Repasa los fundamentos teóricos y muestra ataques prácticos a RSA y a modos de cifrado, demostrando que una implementación descuidada permite "romper" lo que parecía seguro. El resumen original conserva únicamente las respuestas posicionales del room, sin los enunciados de las preguntas.

## Solucionario

### Task 1: Criptografía básica / Basic Cryptography

**Explicación:** Se repasan los fundamentos teóricos de la criptografía (preguntas sin respuesta) y se practica con RSA, identificando los primos utilizados y sus saltos entre modos de cifrado, hasta capturar las flags de los distintos retos.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `No answer needed` |
| 2 | *(Pregunta 2 no especificada en el original)* | `THM{Psssss_4nd_Qsssssss}` |
| 3 | *(Pregunta 3 no especificada en el original)* | `sunshine` |
| 4 | *(Pregunta 4 no especificada en el original)* | `THM{3nD_2_3nd_is_n0t_c0mpl1c4ted}` |
| 5 | *(Pregunta 5 no especificada en el original)* | `THM{flip_n_flip}` |
| 6 | *(Pregunta 6 no especificada en el original)* | `No answer needed` |

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `No answer needed` |
| 2 | *(Pregunta 2 no especificada en el original)* | `THM{Psssss_4nd_Qsssssss}` |
| 3 | *(Pregunta 3 no especificada en el original)* | `sunshine` |
| 4 | *(Pregunta 4 no especificada en el original)* | `THM{3nD_2_3nd_is_n0t_c0mpl1c4ted}` |
| 5 | *(Pregunta 5 no especificada en el original)* | `THM{flip_n_flip}` |
| 6 | *(Pregunta 6 no especificada en el original)* | `No answer needed` |

---

**Metodología:** Revisión de los fundamentos teóricos → explotación de RSA con parámetros débiles (identificación de los primos) → análisis de los modos de cifrado y de operaciones como el bit flipping → obtención de las flags.

### Cadena de ataque / Attack Chain

```text
Fundamentos de criptografía → RSA (identificación de p·q) → modos de cifrado → bit flipping → flags
```

**Learning chain:** Fundamentos de criptografía → RSA → modos de cifrado → criptoanálisis práctico → flags

**Lección:** *La criptografía solo es segura si se implementa correctamente: parámetros débiles, modos mal utilizados y operaciones encadenadas sin integridad permiten romper el cifrado sin conocer la clave.*

**MITRE ATT&CK:** T1140 (Deobfuscate/Decode Files or Information), T1573 (Encrypted Channel)

**Fuente:** [TryHackMe - Breaking Crypto the Simple Way](https://tryhackme.com/room/breakingcryptothesimpleway)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.