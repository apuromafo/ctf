# DVWA

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `dvwa` | [TryHackMe](https://tryhackme.com/room/dvwa) | 01 Level Easy | TryHackMe | DVWA / Web Hacking / laboratorio de práctica | Practicar ataques web clásicos en un laboratorio local (Damn Vulnerable Web Application). |

> **Objeto:** Desplegar y explotar el laboratorio DVWA (Damn Vulnerable Web Application) para practicar las vulnerabilidades web clásicas: SQL Injection, XSS, Command Injection, File Upload, CSRF y escalada de dificultad en cada módulo.

---

**Contexto:** DVWA es una aplicación web deliberadamente vulnerable que sirve como laboratorio de entrenamiento para probar técnicas de hacking web en un entorno controlado. La room la despliega y guía al alumno en su uso.

> **ES:** Room de introducción a DVWA: se despliega el laboratorio y se practica la explotación de los módulos típicos (SQLi, XSS, command injection, file upload, CSRF) a distintos niveles de seguridad. No contiene preguntas con respuesta: todo es "No answer needed" con la práctica guiada.
> **EN:** Intro to DVWA: the lab is deployed to practise classic web exploitation (SQLi, XSS, command injection, file upload, CSRF) at different security levels. It has no answerable questions: everything is "No answer needed" guided practice.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:** Se despliega la máquina de la room y se accede a la aplicación DVWA. El contenido es práctico y guiado: no hay preguntas que responder (No answer needed).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed. / Sin respuesta necesaria. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed. / Sin respuesta necesaria. | `No answer needed` |

---

**Metodología:** Desplegar el laboratorio DVWA, iniciar sesión y practicar de forma guiada los módulos de vulnerabilidades (SQL Injection, Reflected/Stored XSS, Command Injection, File Upload, CSRF), subiendo el nivel de seguridad del aplicativo para aumentar la dificultad.

### Cadena de ataque / Attack Chain

```text
Despliegue de DVWA -> login -> práctica guiada de módulos (SQLi, XSS, Command Injection, File Upload, CSRF) -> subida de nivel de seguridad
```

**Learning chain:** Introducción a DVWA → práctica de módulos de vulnerabilidades web → niveles de seguridad.

**Lección:** *DVWA ofrece un entorno seguro y aislado para entrenar la explotación web: probar los mismos payloads en distintos niveles de seguridad enseña a entender cómo funcionan los filtros y las mitigaciones.*

**MITRE ATT&CK:** N/A (laboratorio de práctica de vulnerabilidades web)

**Fuente:** [TryHackMe - DVWA](https://tryhackme.com/room/dvwa)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.