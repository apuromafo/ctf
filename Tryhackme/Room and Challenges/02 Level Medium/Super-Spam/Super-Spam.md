# Super-Spam

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Ofensivo / Web | superspam | https://tryhackme.com/room/superspam | 02 Level Medium | TryHackMe | concrete5, Criptografía, Cifrado XOR, Reversing, Cifrado de sesión/cookies | Descifrado de flags cifradas con XOR y recuperación de material cifrado |

---

**Contexto:** La sala **Super-Spam** parte de un sitio construido sobre **concrete5 8.5.2** y se centra en la **criptografía de la aplicación**: el material de la sala llega cifrado y el alumno debe identificar el algoritmo (cifrado **XOR**), recuperar la clave usada (`$$L3qwert30kcool`) y descifrar con ella las dos banderas (flags) entregadas, navegando por la lógica de cifrado del CMS para revertir el proceso.

## Solucionario

### Task 1: Reversión del cifrado XOR
**Explicación:**

Se identifica en primer lugar la versión del CMS que aloja la aplicación y se recibe el material cifrado. A continuación se reconoce el algoritmo de cifrado empleado (XOR), se obtiene la clave del cifrado y se aplica la operación inversa sobre los dos valores cifrados para recuperar las flags.

1. `concrete5 8.5.2`
2. `flag{-eteKc=skineogyls45«ey?t+du8}`
3. `XOR`
4. `$$L3qwert30kcool`
5. `flag{iteeKdbu==hjK6§YuUu7-6N_}`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1.1 | Versión del CMS | `concrete5 8.5.2` |
| 1.2 | Primer valor cifrado | `flag{-eteKc=skineogyls45«ey?t+du8}` |
| 1.3 | Algoritmo de cifrado | `XOR` |
| 1.4 | Clave del cifrado | `$$L3qwert30kcool` |
| 1.5 | Segundo valor cifrado | `flag{iteeKdbu==hjK6§YuUu7-6N_}` |

---

**Metodología:** Fingerprinting del CMS (concrete5), localización del material cifrado, identificación del cifrado XOR, extracción de la clave y descifrado de las dos banderas mediante la operación inversa.

**Learning chain:** Reconocimiento del CMS → identificación del cifrado → recuperación de la clave → operación XOR inversa → flags descifradas.

**Lección:** *El cifrado XOR con clave reutilizada es trivial de revertir si se conoce el par clave/valor; en un CMS auditar siempre cómo se generan y almacenan las claves de cifrado.*

**MITRE ATT&CK:** T1106 Native API · T1005 Data from Local System · T1140 Deobfuscate/Decode Files or Information.

**Fuente:** [TryHackMe - Super-Spam](https://tryhackme.com/room/superspam)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.