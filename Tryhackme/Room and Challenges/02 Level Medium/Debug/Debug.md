# Debug

| Campo | Valor |
|-------|-------|
| **Dificultad** | Medium |
| **Tipo** | CTF / Web Exploitation |
| **Slug** | debug |
| **Link** | https://tryhackme.com/room/debug |
| **Sección** | 02 Level Medium |
| **Fuente** | TryHackMe |
| **Componentes** | Debugging, Hash Analysis, Web, Forensic |
| **Impacto** | Medio — Análisis de hashes asociados al proceso de depuración |

---

**Contexto:** Esta sala aborda el proceso de depuración de una aplicación web. El aprendiz debe analizar archivos de logging y depuración para obtener hashes que posteriormente se utilizan para acceder a recursos o validar credenciales comprometidas.

## Solucionario

### Task 1: Análisis del entorno

**Explicación:** Se introduce el entorno de depuración y se comienza el análisis.

1. No answer needed

### Task 2: Obtención de hashes

**Explicación:** Se extraen los hashes de los archivos de depuración analizados.

2. 1. 7e37c84a66cc40b1c6bf700d08d28c20
   2. 3c8c3d0fe758c320d158e32f68fabf4b

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Entorno | `No answer needed` |
| 2.1 | Hash 1 | `7e37c84a66cc40b1c6bf700d08d28c20` |
| 2.2 | Hash 2 | `3c8c3d0fe758c320d158e32f68fabf4b` |

---

**Metodología:** Reconocimiento del entorno → Análisis de logs y archivos de depuración → Extracción de hashes → Validación.

**Learning chain:** Environment recon → Log analysis → Hash extraction → Validation

**Lección:** *Los archivos de depuración accesibles públicamente filtran hashes y credenciales sin cifrar.*

**MITRE ATT&CK:**
- T1552.001 — Unsecured Credentials: Credentials In Files

**Fuente:** [TryHackMe - Debug](https://tryhackme.com/room/debug)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.