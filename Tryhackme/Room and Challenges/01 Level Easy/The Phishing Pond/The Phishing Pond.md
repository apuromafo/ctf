
# The Phishing Pond [EASY]
> **Room URL:** [The Phishing Pond — Catch the phish before the phish catches you.](https://tryhackme.com/room/phishingpond)

## 📝 Descripción del Lab / Lab Description

**Phishing Pond** es una sala diseñada para entrenar la capacidad de identificación de correos maliciosos. El objetivo es analizar diferentes escenarios de comunicación y determinar si se trata de un intento de **Phishing** o una comunicación legítima.
 
 
---

## 🚀 Proceso de Resolución / Resolution Process

### Introducción / Introduction

Al iniciar la máquina virtual y acceder a la URL proporcionada, nos encontramos con la interfaz del juego donde debemos clasificar los correos.
<div align="center">
<img width="600" alt="Phishing Pond Room" src="./IMG/welcome.png" />

## 📧 Walkthrough de Niveles / Level Walkthrough
 
---

## <div align="center">[The Phishing Pond — TryHackMe Walkthrough](https://tryhackme.com/room/phishingpond)</div>

<div align="center">
<img width="600" alt="Phishing Pond Room" src="./IMG/room.png" />
</div>

## 📝 Introducción al Laboratorio / Laboratory Introduction

El lab **Phishing Pond** es un desafío interactivo donde debemos actuar como analistas de seguridad para identificar correos electrónicos maliciosos. El objetivo es detectar patrones de ataque comunes y obtener la flag final tras superar 10 niveles de dificultad progresiva.

 

## 🎣 Phishing: El Arte del Engaño / Phishing: The Art of Deception

> El **Phishing** es un tipo de estafa en la que los atacantes abusan de tu confianza para engañarte y obtener información personal, contraseñas o dinero. 
Al dirigirse directamente a las personas en lugar de intentar hackear sistemas complejos, se ha convertido en uno de los métodos más efectivos para el robo de datos.

### 🚩 Estrategias Comunes de los Atacantes / Common Attacker Strategies

Para identificar una campaña de phishing, es fundamental reconocer las tácticas psicológicas y técnicas que utilizan:

* **⚠️ Urgencia y tácticas de miedo:** Asuntos como *"Acción inmediata requerida"* diseñados para presionarte a actuar sin pensar.
* **🌐 Direcciones de remitente similares (Typosquatting):** Dominios falsos con cambios casi imperceptibles (ej. `rnicrosoft.com` en lugar de `microsoft.com`).
* **👤 Suplantación de nombre de pantalla:** El nombre del remitente parece familiar, pero la dirección de correo electrónico real no coincide.
* **📎 Adjuntos maliciosos:** Archivos (`.doc`, `.xls`, `.zip`) que solicitan "habilitar macros" o contienen malware directamente.
* **🔓 Cuentas reales comprometidas:** Correos enviados desde cuentas hackeadas que parecen legítimas pero realizan solicitudes inusuales.
* **🎁 Ofertas demasiado buenas para ser verdad:** Premios falsos, reembolsos o vacantes de empleo que requieren tus datos personales de antemano.

---
### Tácticas Identificadas / Identified Tactics:

* **Urgency & Scare Tactics**: Presión mediante límites de tiempo.
* **Look-alike domains**: Dominios visualmente similares (ej. `rnicrosoft.com`).
* **Display name impersonation**: Nombres conocidos con direcciones falsas.
* **Malicious attachments**: Archivos con macros o malware (.doc, .xls, .zip).

## 🚀 Proceso de Resolución / Resolution Process

### Inicio del Challenge / Challenge Start

Al acceder a la máquina, se nos presenta la pantalla de bienvenida que explica la dinámica del juego de clasificación.

---

### Análisis de los 10 Niveles / Analysis of the 10 Levels

#### Nivel 1

Analizamos el primer correo donde se observa una técnica de impersonación de un ejecutivo.

* **Resultado**: Phishing.
* **Razón**: Urgencia y solicitud de transferencia bancaria.
<div align="center">
<img width="600" alt="Phishing Pond Room" src="./IMG/level1.png" />
</div>

#### Nivel 2

* **Resultado**: Legítimo.
<div align="center">
<img width="600" alt="Phishing Pond Room" src="./IMG/level2.png" />

#### Nivel 3

* **Resultado**: Legítimo.
<div align="center">
<img width="600" alt="Phishing Pond Room" src="./IMG/level3.png" />

#### Nivel 4

* **Resultado**: Legítimo.
<div align="center">
<img width="600" alt="Phishing Pond Room" src="./IMG/level4.png" />

#### Nivel 5

En este nivel detectamos un vector de ataque clásico basado en documentos ofimáticos.

* **Resultado**: Phishing.
* **Razón**: El correo solicita explícitamente habilitar macros en un archivo adjunto.
<div align="center">
<img width="600" alt="Phishing Pond Room" src="./IMG/level5.png" />

#### Nivel 6

* **Resultado**: Phishing.
* **Razón**: Enlace a una encuesta externa de procedencia dudosa.
<div align="center">
<img width="600" alt="Phishing Pond Room" src="./IMG/level6.png" />

#### Nivel 7

* **Resultado**: Phishing.
* **Razón**: Promesa de recompensas a cambio de información sensible.
<div align="center">
<img width="600" alt="Phishing Pond Room" src="./IMG/level7.png" />

#### Nivel 8

* **Resultado**: Phishing.
* **Razón**: Redirección a un portal falso de cambio de credenciales.
<div align="center">
<img width="600" alt="Phishing Pond Room" src="./IMG/level8.png" />

#### Nivel 9

* **Resultado**: Phishing.
* **Razón**: El enlace utiliza un dominio "typosquatted" que imita una pasarela de pago real.
<div align="center">
<img width="600" alt="Phishing Pond Room" src="./IMG/level9.png" />

#### Nivel 10

El reto final consolida lo aprendido con un adjunto malicioso.

* **Resultado**: Phishing.
* **Razón**: Reitera la técnica de macros maliciosas.
<div align="center">
<img width="600" alt="Phishing Pond Room" src="./IMG/level10.png" />

 

### resumen / summary

En esta primera etapa, identificamos desde fraudes de CEO hasta archivos con macros.

| Nivel | Captura de Pantalla | Análisis y Resultado |
| --- | --- | --- |
| **01** |  | **🚩 Phishing**: Impersonación de ejecutivo y solicitud de transferencia urgente. |
| **02** |  | **✅ Legítimo**: Comunicación interna estándar. |
| **03** |  | **✅ Legítimo**: Notificación de sistema sin adjuntos ni links sospechosos. |
| **04** |  | **✅ Legítimo**: Correo auténtico de servicio al cliente. |
| **05** |  | **🚩 Phishing**: Archivo adjunto que solicita habilitar macros. |
| **06** |  | **🚩 Phishing**: Contiene un link a una encuesta de terceros sospechosa. |
| **07** |  | **🚩 Phishing**: Oferta de premios que requiere datos bancarios. |
| **08** |  | **🚩 Phishing**: Link de restablecimiento de contraseña falso. |
| **09** |  | **🚩 Phishing**: Dominio engañoso imitando un portal de pagos. |
| **10** |  | **🚩 Phishing**: Intento de entrega de malware vía macros en adjunto. |

---

### Captura de la Flag / Flag Capture

Tras completar correctamente todos los niveles, el sistema valida las respuestas y muestra la flag

> **Flag**: `THM{i_phish_you_not}`
<div align="center">
<img width="600" alt="Phishing Pond Room" src="./IMG/flag.png" />

## 🏁 Finalización y Flag / Completion and Flag

Tras enviar la flag se termina la sala
<div align="center">
<img width="600" alt="Phishing Pond Room" src="./IMG/End.png" />

---

## 🛠️ Técnicas de Análisis Utilizadas / Analysis Techniques Used

1. **Inspección de Hyperlinks**: Verificación de la URL real al pasar el mouse sobre botones (hovering).
2. **Análisis de Headers**: Verificación del dominio del remitente (`From:`) contra el dominio real de la empresa.
3. **Evaluación de Contexto**: Identificación de solicitudes inusuales de credenciales o transferencias monetarias.

---

*Documentación para propósitos educativos y registro de CTF.*

 