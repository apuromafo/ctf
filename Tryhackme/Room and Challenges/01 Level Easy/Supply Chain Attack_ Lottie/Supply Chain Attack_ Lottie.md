# Supply Chain Attack_ Lottie

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | Supply Chain | supplychainattacklottie | https://tryhackme.com/room/supplychainattacklottie | 01 Level Easy | TryHackMe | Paquete malicioso, Lottie, form-validator.bundle.js, Dominio C2, puerto 9090 | Crítico |

---

**Contexto:**
> **ES:** Laboratorio centrado en un ataque a la cadena de suministro de software. Un paquete malicioso se publica y, al ser consumido por la aplicación, contacta con un servidor externo tras la sustitución de un bundle legítimo por uno malicioso.
> **EN:** A lab focused on a software supply chain attack. A malicious package is published and, once consumed by the application, reaches out to an external server after a legitimate bundle is replaced by a malicious one.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:**
No se requiere respuesta; presenta el escenario del ataque a la cadena de suministro.

```
No answer needed
```

### Task 2: Identificación del paquete / Package Identification
**Explicación:**
Se identifica la opción correcta del paquete malicioso y el dominio del servidor de comando y control.

```
1. a
2. castleservices01[.]com
```

### Task 3: Elementos del ataque / Attack Elements
**Explicación:**
Se detallan la versión del paquete, el puerto de escucha, el bundle malicioso que sustituye al legítimo y la flag del lab.

```
1. 1.1.0
2. 9090
3. form-validator.bundle.js
4. THM{MALICIOUS_PACKAGE_UPLOADED007}
```

### Task 4: Persistencia / Persistence
**Explicación:**
No se requiere respuesta.

```
No answer needed
```

### Task 5: Cierre / Wrap-up
**Explicación:**
No se requiere respuesta en la tarea final.

```
No answer needed
```

### Tabla unificada de preguntas/respuestas

| # | Respuesta |
|---|---|
| 1 | `No answer needed` |
| 2.1 | `a` |
| 2.2 | `castleservices01[.]com` |
| 3.1 | `1.1.0` |
| 3.2 | `9090` |
| 3.3 | `form-validator.bundle.js` |
| 3.4 | `THM{MALICIOUS_PACKAGE_UPLOADED007}` |
| 4 | `No answer needed` |
| 5 | `No answer needed` |

---

**Metodología:**
1. Publicación de un paquete malicioso en el registro de paquetes.
2. Análisis de las dependencias consumidas por la aplicación.
3. Localización del bundle sustituido (`form-validator.bundle.js`).
4. Identificación del dominio C2 (`castleservices01[.]com`) y del puerto de escucha (`9090`).
5. Validación del compromiso con la flag.

### Cadena de ataque / Attack Chain
Publicación del paquete malicioso (v`1.1.0`) → Instalación como dependencia → Sustitución de `form-validator.bundle.js` → C2 (`castleservices01[.]com:9090`) → Flag.

**Learning chain:**
Cadena de suministro → paquetes maliciosos → bundles de frontend → C2 → detección.

**Lección:** *El envenenamiento de paquetes en la cadena de suministro convierte un componente de confianza en el vector de compromiso inicial; verificar integridad y procedencia es imprescindible.*

**MITRE ATT&CK:**
| Técnica | ID |
|---|---|
| Supply Chain Compromise | T1195 |
| Compromise Software Dependencies and Development Tools | T1195.001 |
| Ingress Tool Transfer | T1105 |
| Command and Control | T1071 |
| Application Layer Protocol | T1071.001 |

**Fuente:** [TryHackMe - Supply Chain Attack_ Lottie](https://tryhackme.com/room/supplychainattacklottie)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.