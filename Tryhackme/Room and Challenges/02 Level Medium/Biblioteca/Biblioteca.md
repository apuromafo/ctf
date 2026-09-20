# Biblioteca

| Campo | Valor |
|-------|-------|
| Dificultad | Medium |
| Tipo | Room |
| Slug | biblioteca |
| Link | https://tryhackme.com/room/biblioteca |
| Sección | 02 Level Medium |
| Fuente | TryHackMe |
| Componentes | Web Exploitation, SQL Injection, Python Library Hijacking |
| Impacto | Alto |

---

**Contexto:** Sala de explotación web que combina inyección SQL con hijacking de bibliotecas Python. Se presenta una aplicación web vulnerable donde el participante debe explotar una debilidad SQL para obtener acceso y luego manipular el entorno Python para escalar privilegios y obtener las flags de las dos partes del desafío.

## Solucionario

### Task 1: Inyeccion SQL y Library Hijacking
**Explicación:** Explotación de la vulnerabilidad de inyección SQL en la aplicación web para obtener acceso inicial, seguido de la manipulación de bibliotecas Python (library hijacking) para escalar privilegios y completar ambos desafíos.

1. 1. THM{G0Od_OLd_SQL_1nj3ct10n_&_w3@k_p@sSw0rd$}
   2. THM{PytH0n_LiBr@RY_H1j@acKIn6}

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Task 1.1 | THM{G0Od_OLd_SQL_1nj3ct10n_&_w3@k_p@sSw0rd$} |
| 1 | Task 1.2 | THM{PytH0n_LiBr@RY_H1j@acKIn6} |

---

**Metodología:** Explotación web con inyección SQL y Python library hijacking. Obtención de acceso through SQLi y escalamiento through manipulación de dependencias.

**Learning chain:** SQL Injection -> Acceso a base de datos -> Escalamiento de privilegios -> Python Library Hijacking -> Flags

**Lección:** _La combinación de vulnerabilidades web y manipulación de entornos de ejecución puede conducir a compromisos completos del sistema._

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1195.002 (Compromise Software Supply Chain), T1554 (Compromise Client Software Binary), T1078 (Valid Accounts)

**Fuente:** [TryHackMe - Biblioteca](https://tryhackme.com/room/biblioteca)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
