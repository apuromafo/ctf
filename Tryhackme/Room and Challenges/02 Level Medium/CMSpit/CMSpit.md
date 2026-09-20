# CMSpit

| Campo | Valor |
|---|---|
| Dificultad | Medium |
| Tipo | CTF |
| Slug | cmspit |
| Link | https://tryhackme.com/room/cmspit |
| Sección | 02 Level Medium |
| Fuente | TryHackMe |
| Componentes | CMS, CVE, explotación web, metadata |
| Impacto | Compromiso del servidor mediante vulnerabilidades CMS |

---

**Contexto:** CMSpit es una sala de TryHackMe de dificultad media que explota vulnerabilidades en un CMS específico (Cockpit CMS v0.11.1). Cubre enumeración de versiones, análisis de endpoints de autenticación, explotación de CVEs como CVE-2021-22204 y uso de herramientas como djvumake para obtener acceso al servidor y extraer las flags.

## Solucionario

### Task 1: Resolución completa del desafío

**Explicación:** Se resolvieron las 12 preguntas/flags de la sala mediante enumeración del CMS, análisis de endpoints, explotación de CVEs y extracción de datos.

1. cockpit
2. 0.11.1
3. /auth/check
4. 4
5. /auth/resetpassword
6. skidy@tryhackme.fakemail
7. thm{f158bea70731c48b05657a02aaf955626d78e9fb}
8. thm{c3d1af8da23926a30b0c8f4d6ab71bf851754568}
9. thm{c5fc72c48759318c78ec88a786d7c213da05f0ce}
10. CVE-2021-22204
11. djvumake
12. thm{bf52a85b12cf49b9b6d77643771d74e90d4d5ada}

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Nombre del CMS | `cockpit` |
| 2 | Versión | `0.11.1` |
| 3 | Endpoint de verificación | `/auth/check` |
| 4 | Número de pregunta | `4` |
| 5 | Endpoint de reseteo | `/auth/resetpassword` |
| 6 | Email de prueba | `skidy@tryhackme.fakemail` |
| 7 | Flag 1 | `thm{f158bea70731c48b05657a02aaf955626d78e9fb}` |
| 8 | Flag 2 | `thm{c3d1af8da23926a30b0c8f4d6ab71bf851754568}` |
| 9 | Flag 3 | `thm{c5fc72c48759318c78ec88a786d7c213da05f0ce}` |
| 10 | CVE explotado | `CVE-2021-22204` |
| 11 | Herramienta utilizada | `djvumake` |
| 12 | Flag final | `thm{bf52a85b12cf49b9b6d77643771d74e90d4d5ada}` |

---

**Metodología:** Enumeración de CMS, análisis de endpoints, explotación de CVE en metadata, inyección de comandos y obtención de flags.

**Learning chain:** Descubrimiento del CMS → versión identificada → endpoints de autenticación mapeados → CVE-2021-22204 explotado → acceso obtenido → flags extraídas.

**Lección:** *Las vulnerabilidades en la metadata de archivos multimedia pueden servir como vector de compromiso cuando no se validan adecuadamente los archivos subidos.*

**MITRE ATT&CK:** T1190 - Exploit Public-Facing Application, T1059 - Command and Scripting Interpreter

**Fuente:** [TryHackMe - CMSpit](https://tryhackme.com/room/cmspit)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.