# Gobuster_ The Basics

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `gobusterthebasics` | [TryHackMe](https://tryhackme.com/room/gobusterthebasics) | 01 Level Easy | THM | Gobuster, Fuzzing, Directorios, Subdominios, Vhosts | Fundamentos de fuzzing web con Gobuster |

---

**Contexto:** Sala que enseña el uso de Gobuster para el fuzzing de directorios y archivos, subdominios y virtual hosts, con los modos `dir`/`dns` y los flags más utilizados en cada caso.

> **ES:** Aprender Gobuster desde cero: modos, flags y casos de uso (directorios, subdominios y vhosts).
> **EN:** Learn Gobuster from scratch: modes, flags and use cases (directories, subdomains and vhosts).

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Presentación de la sala y del objetivo de aprender Gobuster.

No answer needed

### Task 2: Entorno y preparación / Environment and Setup

**Explicación:** Preparación del entorno de trabajo para los ejercicios.

No answer needed

### Task 3: Gobuster: Introducción / Gobuster: Introduction

**Explicación:** Se aprenden los parámetros básicos: el flag `-u` indica la URL objetivo y el modo `dns` se usa para el fuzzing de subdominios.

1. `-u`
2. `dns`

### Task 4: Caso de uso: Enumeración de directorios y archivos / Use Case: Directory and File Enumeration

**Explicación:** Fuzzing de directorios: se usa `--no-tls-validation` para evitar problemas con el certificado, se encuentra el directorio `secret` y se obtiene la bandera del apartado.

1. `--no-tls-validation`
2. `secret`
3. `THM{ReconWasASuccess}`

### Task 5: Caso de uso: Enumeración de subdominios / Use Case: Subdomain Enumeration

**Explicación:** Fuzzing de subdominios en modo `dns` con el flag `-d`; el host devuelve 4 subdominios.

1. `-d`
2. `4`

### Task 6: Caso de uso: Enumeración de vhosts / Use Case: Vhost Enumeration

**Explicación:** Enumeración de virtual hosts; se descubren 4 vhosts.

- `4`

### Task 7: Conclusión / Conclusion

**Explicación:** Cierre y resumen de la sala.

No answer needed

### Tabla unificada de preguntas y respuestas

| Task | Pregunta | Respuesta |
|------|----------|-----------|
| 1 | — | `No answer needed` |
| 2 | — | `No answer needed` |
| 3.1 | ¿Qué flag indica la URL objetivo? | `-u` |
| 3.2 | ¿En qué modo se fuzzean subdominios? | `dns` |
| 4.1 | ¿Qué flag deshabilita la validación TLS? | `--no-tls-validation` |
| 4.2 | ¿Qué directorio se encuentra? | `secret` |
| 4.3 | Bandera del reto | `THM{ReconWasASuccess}` |
| 5.1 | ¿Qué flag se usa para fuzzear subdominios? | `-d` |
| 5.2 | ¿Cuántos subdominios se descubren? | `4` |
| 6 | ¿Cuántos vhosts se descubren? | `4` |
| 7 | — | `No answer needed` |

---

**Metodología:** Uso de Gobuster en sus tres casos de aplicación: fuzzing de directorios/archivos (modo `dir`, flag `--no-tls-validation`), fuzzing de subdominios (modo `dns`, flag `-d`) y enumeración de vhosts, cuantificando los resultados y validando el directorio `secret` con el payload encontrado.

### Cadena de ataque / Attack Chain

```text
Setup -> fuzz de directorios y archivos (modo dir) -> -u + --no-tls-validation -> /secret -> THM{ReconWasASuccess} -> fuzz de subdominios (modo dns, -d) -> 4 -> enumeración de vhosts -> 4
```

**Learning chain:** Gobuster → Directory/file fuzzing → Subdomain fuzzing → Vhost enumeration

**Lección:** *Gobuster acelera la fase de reconocimiento: basta conocer el modo (`dir`/`dns`/`vhost`) y el flag adecuado para mapear superficies de ataque completas.*

**MITRE ATT&CK:** N/A (Room de reconocimiento/fuzzing)

**Fuente:** [TryHackMe - Gobuster_ The Basics](https://tryhackme.com/room/gobusterthebasics)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.