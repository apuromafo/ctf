# Getting Started

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `gettingstarted` | [TryHackMe](https://tryhackme.com/room/gettingstarted) | 01 Level Easy | THM | Deploy, Information Disclosure, Default Credentials, Admin page | Fundamentos de explotación web básica |

---

**Contexto:** Sala introductoria de TryHackMe que enseña a desplegar la primera máquina y a resolver los primeros retos prácticos: descubrir una página de administración oculta mediante information disclosure, probar credenciales por defecto y contar los usuarios registrados en la aplicación.

> **ES:** Desplegar la máquina, descubrir la admin page oculta, explotar credenciales por defecto `admin:admin` y recapitular lo aprendido.
> **EN:** Deploy the machine, discover the hidden admin page, exploit the default `admin:admin` credentials and recap.

## Solucionario

### Task 1: Divulgación de información / Information Disclosure

**Explicación:** Se despliega la máquina y se inspecciona el sitio web. El probing inicial revela una página de administración oculta.

1. `/test-admin`

### Task 2: Credenciales por defecto / Default Credentials

**Explicación:** La admin page es accesible con credenciales por defecto. Se autentica con `admin:admin` y se determina el número de usuarios registrados en la aplicación.

1. `admin:admin`
2. `3`

### Task 3: Recapitulación / Recap

**Explicación:** Cierre de la sala repasando los conceptos vistos.

No answer needed

### Tabla unificada de preguntas y respuestas

| Task | Pregunta | Respuesta |
|------|----------|-----------|
| 1 | ¿Cuál es la página de administración oculta? | `/test-admin` |
| 2.1 | ¿Cuáles son las credenciales por defecto? | `admin:admin` |
| 2.2 | ¿Cuántos usuarios hay registrados? | `3` |
| 3 | — | `No answer needed` |

---

**Metodología:** Desplegar la máquina, realizar reconocimiento del sitio web, descubrir la página de administración oculta (`/test-admin`), autenticarse con credenciales por defecto (`admin:admin`) y enumerar los usuarios de la aplicación.

### Cadena de ataque / Attack Chain

```text
Deploy de la máquina -> recon del sitio -> information disclosure (/test-admin) -> login con credenciales por defecto (admin:admin) -> enumeración de usuarios (3) -> recap
```

**Learning chain:** Deploy → Recon → Information Disclosure → Default Credentials → Enumeration

**Lección:** *Comprobar siempre la presencia de páginas ocultas y de credenciales por defecto en cualquier auditoría inicial: son la puerta de entrada más simple a muchos sistemas.*

**MITRE ATT&CK:** N/A (Room introductoria)

**Fuente:** [TryHackMe - Getting Started](https://tryhackme.com/room/gettingstarted)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.