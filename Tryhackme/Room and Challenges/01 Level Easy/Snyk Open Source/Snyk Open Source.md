# Snyk Open Source

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | DevSecOps / SCA | snykopensource | https://tryhackme.com/room/snykopensource | 01 Level Easy | TryHackMe | Snyk Open Source, SCA, package.json, dependencias transitivas, CVSS, Orb, ChatOps | Alto |

---

**Contexto:**
> **ES:** Laboratorio de seguridad de código abierto con Snyk Open Source (SCA). Se analizan dependencias, vulnerabilidades transitivas, formato de manifestos, integraciones CI/CD (Orb/YAML) y ChatOps.
> **EN:** An open-source security lab with Snyk Open Source (SCA). Dependencies, transitive vulnerabilities, manifest formats, CI/CD integrations (Orb/YAML) and ChatOps are covered.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:**
No se requiere respuesta; establece el contexto de Snyk Open Source.

```
No answer needed
```

### Task 2: Conceptos básicos / Basics
**Explicación:**
No se requiere respuesta; cubre los fundamentos de la herramienta.

```
No answer needed
```

### Task 3: Dependencias / Dependencies
**Explicación:**
Se identifica el fichero índice de dependencias del proyecto, el número de paquetes y el concepto de dependencias transitivas.

```
1. package.json
2. 5
3. transitive dependencies
```

### Task 4: Autenticación / Authentication
**Explicación:**
Se indica el mecanismo de autenticación empleado.

```
single sign-on
```

### Task 5: Vulnerabilidades / Vulnerabilities
**Explicación:**
Se identifica la versión vulnerable del paquete y el tipo de vulnerabilidad asociada.

```
1. 2.4.2
2. prototype pollution
```

### Task 6: CVSS / Severity
**Explicación:**
Se responde sobre el sistema común de puntuación de vulnerabilidades y sobre una opción de uso.

```
1. common vulnerability scoring system
2. n
```

### Task 7: Integración CI/CD / CI/CD Integration
**Explicación:**
Se identifican los recursos de integración con CircleCI.

```
1. orb
2. yaml
```

### Task 8: ChatOps
**Explicación:**
Se indica la función de ChatOps habilitada por Snyk.

```
chatops
```

### Task 9: Cierre / Wrap-up
**Explicación:**
No se requiere respuesta en la tarea final.

```
No answer needed
```

### Tabla unificada de preguntas/respuestas

| # | Respuesta |
|---|---|
| 1 | `No answer needed` |
| 2 | `No answer needed` |
| 3.1 | `package.json` |
| 3.2 | `5` |
| 3.3 | `transitive dependencies` |
| 4 | `single sign-on` |
| 5.1 | `2.4.2` |
| 5.2 | `prototype pollution` |
| 6.1 | `common vulnerability scoring system` |
| 6.2 | `n` |
| 7.1 | `orb` |
| 7.2 | `yaml` |
| 8 | `chatops` |
| 9 | `No answer needed` |

---

**Metodología:**
1. Revisión del manifest del proyecto (`package.json`).
2. Escaneo de dependencias directas y transitivas con Snyk Open Source.
3. Identificación de la versión vulnerable y del tipo de vulnerabilidad (`prototype pollution`).
4. Interpretación de la puntuación CVSS.
5. Integración del escaneo en el pipeline CI/CD mediante Orb/YAML.
6. Automatización de notificaciones con ChatOps.

### Cadena de ataque / Attack Chain
package.json → Snyk Open Source (SCA) → dependencias transitivas → vulnerabilidad (`2.4.2` / prototype pollution) → CVSS → CI/CD (orb/yaml) → ChatOps.

**Learning chain:**
SCA → manifestos → dependencias transitivas → CVSS → integración CI/CD → automatización.

**Lección:** *El análisis de dependencias de código abierto debe cubrir también las dependencias transitivas para cerrar la superficie de ataque de la cadena de suministro de software.*

**MITRE ATT&CK:**
| Técnica | ID |
|---|---|
| Supply Chain Compromise | T1195 |
| Compromise Software Dependencies and Development Tools | T1195.001 |
| Command and Scripting Interpreter | T1059 |

**Fuente:** [TryHackMe - Snyk Open Source](https://tryhackme.com/room/snykopensource)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.