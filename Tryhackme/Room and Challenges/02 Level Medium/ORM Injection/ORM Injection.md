# ORM Injection [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM
* **Tipo / Type:** Walkthrough (Premium)
* **Slug:** `orminjection`
* **Link:** https://tryhackme.com/room/orminjection
* **Sección / Section:** Web / Injection
* **Fuente / Source:** Writeup de thmrevenant (GitHub)

---

## Solucionario de Tareas / Task Solutions

> **ES:** Aprendizaje y explotación de vulnerabilidades de inyección en ORM (Object-Relational Mapping), cubriendo Active Record, Eloquent y Hibernate, con prácticas de SQL injection a través de métodos ORM.
> **EN:** Learning and exploiting ORM (Object-Relational Mapping) injection vulnerabilities, covering Active Record, Eloquent, and Hibernate, with SQL injection practices through ORM methods.

---

### Task 1 — Fundamentos de ORM

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the default ORM for Ruby on Rails applications? | `Active Record` |
| Which of the following is NOT a feature of ORM? | `c` |
| What is the method used in our Laravel code snippet to define the structure of the users table? | `up()` |
| What is the file name usually used to store database credentials in Laravel? | `.env` |
| What is the path in the DOCUMENT_ROOT variable? | `C:\Users\Administrator\Downloads\orminjection\public` |
| What is the ORM library for the Spring framework? (The one mentioned in this task) | `Hibernate` |

---

### Task 2 — Explotación de ORM Injection

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Once you have reviewed the cookies to identify the ORM, what is the cookie's name that is responsible for maintaining the session in the attached application? | `laravel_session` |
| What email is associated with the name Jane Doe? | `jane@thm.com` |
| What is the name of the vulnerable Eloquent method that is used in this task? | `whereRaw()` |
| What is the flag value after submitting the payload in the secure input field? | `THM{SECURED_001}` |
| What is the total number of rows in the users table? | `5` |
| What is the password for the email john@thm.com? | `THM{101}` |

---

### Task 3 — Prevención y Buenas Prácticas

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Is it a good practice to write raw SQL queries in ORM? (yea/nay) | `nay` |
| Which side should input validation be carried out? Write the correct option only. | `c` |

---

## Metodología / Methodology

1. **Paso / Step:** Comprender los ORM principales (Active Record para Rails, Eloquent para Laravel, Hibernate para Spring) y sus funcionalidades / Understand the main ORMs (Active Record for Rails, Eloquent for Laravel, Hibernate for Spring) and their features.
2. **Paso / Step:** Identificar el ORM utilizado en la aplicación examinando las cookies de sesión (laravel_session) / Identify the ORM used in the application by examining session cookies (laravel_session).
3. **Paso / Step:** Localizar archivos de configuración (.env) y DOCUMENT_ROOT para entender la estructura del proyecto / Locate configuration files (.env) and DOCUMENT_ROOT to understand the project structure.
4. **Paso / Step:** Identificar el método vulnerable (whereRaw()) y diseñar payloads de inyección SQL a través del ORM / Identify the vulnerable method (whereRaw()) and craft SQL injection payloads through the ORM.
5. **Paso / Step:** Explotar la inyección para extraer datos de la tabla users (emails, contraseñas, flags) / Exploit the injection to extract data from the users table (emails, passwords, flags).
6. **Paso / Step:** Evaluar el campo de entrada seguro y determinar las mejores prácticas de prevención / Evaluate the secure input field and determine prevention best practices.

### Cadena de ataque / Attack Chain

```
Reconocimiento: identificar ORM (laravel_session cookie)
  -> Localizar DOCUMENT_ROOT y configuración (.env)
    -> Identificar método vulnerable: whereRaw()
      -> Inyección SQL a través del ORM para extraer datos
        -> Obtención de emails, contraseñas y flags
          -> Verificación de campo seguro con payload entregado
            -> Conclusión: evitar whereRaw() y usar consultas parametrizadas
```

**Lección:** Los ORM no son inmunes a inyección SQL. Métodos como `whereRaw()` en Laravel permiten consultas directas que pueden ser explotadas. La validación de entrada debe realizarse en el lado del servidor y las consultas deben usar bindings parametrizados en lugar de concatenación directa.

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
