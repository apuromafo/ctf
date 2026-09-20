# Develpy

| Campo | Valor |
|-------|-------|
| **Dificultad** | Medium |
| **Tipo** | CTF / Web + Python |
| **Slug** | develpy |
| **Link** | https://tryhackme.com/room/develpy |
| **Sección** | 02 Level Medium |
| **Fuente** | TryHackMe |
| **Componentes** | Python, Debug, Web, Hash Analysis |
| **Impacto** | Medio — Análisis de una aplicación Python con contraseñas expuestas |

---

**Contexto:** Develpy es un reto CTF centrado en una aplicación desarrollada en Python. El reto trabaja con credenciales y contraseñas en forma de hash que se obtienen analizando la aplicación y su proceso de desarrollo.

## Solucionario

### Task 1: Análisis de la aplicación

**Explicación:** Se analiza la aplicación Python y se obtienen los hashes de las credenciales del entorno.

1. 1. cf85ff769cfaaa721758949bf870b019
   2. 9c37646777a53910a347f387dce025ec

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1.1 | Hash contraseña 1 | `cf85ff769cfaaa721758949bf870b019` |
| 1.2 | Hash contraseña 2 | `9c37646777a53910a347f387dce025ec` |

---

**Metodología:** Enumeración de la aplicación → Análisis del código Python → Extracción de hashes → Cracking o validación de credenciales.

**Learning chain:** Application enumeration → Source code review → Credential extraction → Hash analysis

**Lección:** *Las credenciales con hash de producción nunca deben filtrarse en el código de la aplicación.*

**MITRE ATT&CK:**
- T1552.001 — Unsecured Credentials: Credentials In Files
- T1110 — Brute Force

**Fuente:** [TryHackMe - Develpy](https://tryhackme.com/room/develpy)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.