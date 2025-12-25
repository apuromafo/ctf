 

# 🛡️ TryHackMe Career Quiz - Python Implementation

Este proyecto es una implementación en Python del popular test de orientación de **TryHackMe**.
 Ayuda a profesionales y estudiantes de ciberseguridad a identificar su rol ideal mediante un análisis de preferencias técnicas y psicológicas.
 Inspirado en el quiz de Inspirado en https://tryhackme.com/careers/quiz

---

## 📊 Perfiles de Carrera Soportados

El script evalúa y categoriza al usuario en uno de los siguientes 5 roles críticos de la industria:

| Rol | Enfoque Principal | Recurso Oficial |
| --- | --- | --- |
| **Penetration Tester** | Descubrir fallas y explotar vulnerabilidades de forma sistemática. | [Ver Carrera](https://tryhackme.com/careers/penetration-tester) |
| **Security Analyst** | Evaluación de redes y recomendación de medidas preventivas. | [Ver Carrera](https://tryhackme.com/careers/cyber-security-analyst) |
| **Security Engineer** | Desarrollo e implementación de soluciones contra amenazas web y de red. | [Ver Carrera](https://tryhackme.com/careers/security-engineer) |
| **Red Teamer** | Emulación de adversarios y prueba de capacidades de detección/respuesta. | [Ver Carrera](https://tryhackme.com/careers/red-teamer) |
| **Incident Responder** | Respuesta en tiempo real y creación de protocolos ante brechas de seguridad. | [Ver Carrera](https://tryhackme.com/careers/incident-responder) |

---

## ⚙️ Características Técnicas

* **Motor de Aleatorización:** Utiliza `random.shuffle` tanto para el orden de las preguntas como para las opciones, eliminando sesgos de posición.
* **Lógica de Puntuación:** Implementa `collections.Counter` para determinar el perfil predominante basado en las respuestas del usuario.
* **Validación de Entrada:** Sistema de control de errores para asegurar que el usuario ingrese valores válidos (1-5).
* **Interfaz CLI:** Diseñada con arte ASCII y banners de advertencia para una experiencia de terminal limpia.

---

## 🚀 Instalación y Uso

### Requisitos

* Python 3.x
* Librerías estándar (`collections`, `random`) — *No requiere dependencias externas.*

### Ejecución

```bash
  
# Ejecutar el test
python quiz.py

```

---

## 🛠 Estructura del Código

El script se divide en tres bloques lógicos principales:

1. **Disclaimer & Header:** Establece el contexto y la advertencia legal de que el test es solo orientativo.
2. **Question Bank:** Un set de 10 preguntas dinámicas que cubren desde habilidades técnicas hasta escenarios de "gadgets de espía".
3. **Result Engine:** Procesa los datos y entrega una descripción detallada junto con una URL de formación específica de TryHackMe.

---

## ⚠️ Aviso Legal

Este test es una herramienta de orientación. Los resultados sugieren roles en ciberseguridad basándose en las preferencias marcadas,
 pero no limitan el potencial del usuario ni garantizan aptitud para dichos roles.

---
 