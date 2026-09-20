# ToolsRus

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `toolsrus` | [TryHackMe - ToolsRus](https://tryhackme.com/room/toolsrus) | 01 Level Easy | THM | Enumeración web, Apache Tomcat, hash cracking, TFTP | Pentest de servicios web y descifrado de credenciales |

---

**Contexto:** Máquina de enumeración: descubrimiento de recursos web (guías y directorios ocultos), abuso de Apache Tomcat y de un servicio de transferencia de archivos, y descifrado de un hash para obtener acceso privilegiado.

> **ES:** Pentest donde se enumeran recursos web, se explotan Apache Tomcat/2.4.18 y TFTP, y se descifra un hash para escalar a root.
> **EN:** Pentest where web resources are enumerated, Apache Tomcat/2.4.18 and TFTP are exploited, and a hash is cracked to escalate to root.

## Solucionario

### Task 1: Respuestas / Answers

**Explicación:** Solución de las preguntas de la máquina ToolsRus: guía de Tomcat, credenciales, versiones de los servicios y flag final.

1. 1. guidelines
   2. bob
   3. protected
   4. bubbles
   5. 1234
   6. Apache Tomcat/7.0.88
   7. 5
   8. Apache/2.4.18
   9. 1.1
   10. root
   11. ff1fc4a81affcc7688cf89ae7dc6e0e1

### Tabla unificada de preguntas / Unified Q&A

| # | Respuesta / Answer |
|---|---|
| 1 | `guidelines` |
| 2 | `bob` |
| 3 | `protected` |
| 4 | `bubbles` |
| 5 | `1234` |
| 6 | `Apache Tomcat/7.0.88` |
| 7 | `5` |
| 8 | `Apache/2.4.18` |
| 9 | `1.1` |
| 10 | `root` |
| 11 | `ff1fc4a81affcc7688cf89ae7dc6e0e1` |

---

**Metodología:** Se enumeraron los recursos web (incluida la guía `guidelines`), se obtuvieron las credenciales de Tomcat (`bob` / `protected`), se identificaron las versiones de los servicios (Apache Tomcat/7.0.88, Apache/2.4.18) y se explotó el servicio de transferencia para recuperar un archivo con el hash de `root`, que se descifró (`ff1fc4a81affcc7688cf89ae7dc6e0e1`) para acceder al sistema.

### Cadena de ataque / Attack Chain

1. Enumeración web y descubrimiento de la guía `guidelines`.
2. Obtención de credenciales de Tomcat (`bob` / `protected`).
3. Identificación de las versiones de Apache Tomcat/7.0.88 y Apache/2.4.18.
4. Abuso del servicio de transferencia para recuperar el hash de `root`.
5. Descifrado del hash y acceso privilegiado.

**Learning chain:** Web enumeration → Tomcat credentials → service versioning → TFTP abuse → hash cracking

**Lección:** *La información pública (como una guía con credenciales filtradas) y los servicios de transferencia sin control pueden exponer hashes o datos que permiten la escalada a root.*

**MITRE ATT&CK:** T1083 - File and Directory Discovery, T1110.002 - Brute Force: Password Cracking, T1190 - Exploit Public-Facing Application

**Fuente:** [TryHackMe - ToolsRus](https://tryhackme.com/room/toolsrus)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.