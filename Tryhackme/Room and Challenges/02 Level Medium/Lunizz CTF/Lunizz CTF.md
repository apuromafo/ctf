# Lunizz CTF

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF | lunizzctf | https://tryhackme.com/room/lunizzctf | 02 Level Medium | TryHackMe | Reversing, ingeniería inversa, tracing de procesos, scripts, variables de entorno | Análisis dinámico y estático de un binario para la obtención de flags |

---

**Contexto:** **Lunizz CTF** es un reto de ingeniería inversa donde se examina un binario y un script, se inspeccionan procesos y strings (como `proct`), se descubre una contraseña y se explota la lógica del programa para obtener dos flags cifradas.

## Solucionario

### Task 1: Reversing / Ingeniería inversa
**Explicación:**

Se analiza el binario y el script del reto: se localiza la contraseña en el código, se observa el proceso y sus argumentos (comando `run`, proceso `proct`) y se descifran las dos flags a partir de los datos extraídos.

1. `CTF_script_cave_changeme`
2. `run`
3. `proct`
4. `northern lights`
5. `thm{23cd53cbb37a37a74d4425b703d91883}`
6. `thm{ad23b9c63602960371b50c7a697265db}`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1.1 | Contraseña encontrada en el script | `CTF_script_cave_changeme` |
| 1.2 | Comando usado para ejecutar el binario | `run` |
| 1.3 | Proceso observado durante la ejecución | `proct` |
| 1.4 | Phrase / clave asociada a la lógica del programa | `northern lights` |
| 1.5 | Primera flag del reto | `thm{23cd53cbb37a37a74d4425b703d91883}` |
| 1.6 | Segunda flag del reto | `thm{ad23b9c63602960371b50c7a697265db}` |

---

**Metodología:** Ingeniería inversa mixta: análisis estático del script (extracción de contraseña) y análisis dinámico del binario (tracing de proceso y argumentos con `run`/`proct`), correlacionando los datos para descifrar ambas flags.

**Learning chain:** Análisis del script → identificación de la contraseña → ejecución del binario → observación del proceso (proct) → extracción de datos → descifrado de flags.

**Lección:** *La combinación de análisis estático y dinámico es la que resuelve un reto de reversing: el script revela datos que solo la ejecución del binario permite interpretar.*

**MITRE ATT&CK:** T1106 Native API · T1059 Command and Scripting Interpreter · T1005 Data from Local System · T1140 Deobfuscate/Decode Files or Information.

**Fuente:** [TryHackMe - Lunizz CTF](https://tryhackme.com/room/lunizzctf)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.