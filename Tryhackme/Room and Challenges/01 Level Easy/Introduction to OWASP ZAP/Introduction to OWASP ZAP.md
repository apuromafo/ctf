# Introduction to OWASP ZAP

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `introductiontoowaspzap` | [TryHackMe](https://tryhackme.com/room/introductiontoowaspzap) | 01 Level Easy | TryHackMe | OWASP ZAP, proxy de interceptación, spidering, escaneo activo y pasivo, fuerza bruta, alertas | Aprender a usar OWASP ZAP como Zed Attack Proxy: interceptar tráfico, explorar aplicaciones web y automatizar la detección de vulnerabilidades. |

---

**Contexto:** Sala introductoria dedicada a OWASP ZAP (Zed Attack Proxy), el escáner de seguridad web de código abierto de la OWASP. El room recorre su papel como proxy de interceptación, la instalación y configuración en Kali, la expedición del certificado para tráfico HTTPS, el spidering, el escaneo activo y pasivo, la fuerza bruta de formularios de login y la lectura de las alertas generadas. El resumen original conserva únicamente las respuestas posicionales del room, sin los enunciados de las preguntas.

> **ES:** Configurar el navegador para que apunte al proxy de ZAP en 127.0.0.1, instalar el certificado para ver el tráfico HTTPS, explorar la aplicación, lanzar los escaneos y forzar el formulario de login hasta obtener la contraseña.
> **EN:** Point the browser at the ZAP proxy on 127.0.0.1, install the certificate to see the HTTPS traffic, spider the application, run the scans and brute-force the login form until the password is obtained.

## Solucionario

### Task 1: Fundamentos de ZAP / ZAP Fundamentals
**Explicación:** Se presenta el rol de ZAP dentro de las pruebas de seguridad de aplicaciones web y su nombre completo como Zed Attack Proxy.

1. Zed Attack Proxy
2. No answer needed

### Task 2: Proxy de interceptación / Intercepting Proxy
**Explicación:** Se practica la activación del proxy de interceptación para capturar y modificar las peticiones del navegador.

1. No answer needed

### Task 3: Certificados HTTPS / HTTPS Certificates
**Explicación:** Para inspeccionar tráfico HTTPS, ZAP genera y expone su propio certificado raíz que debe ser instalado y confiado por el navegador.

1. No answer needed
2. No answer needed

### Task 4: Exploración con el spider / Spidering
**Explicación:** El spider de ZAP rastrea la aplicación automáticamente, recorriendo enlaces y formularios para descubrir contenido.

1. No answer needed

### Task 5: Configuración del proxy local / Local Proxy Configuration
**Explicación:** El proxy de ZAP escucha de forma local y el navegador debe dirigirse hacia esa dirección.

1. 127.0.0.1

### Task 6: ZAP en Kali Linux / ZAP on Kali Linux
**Explicación:** ZAP viene preinstalado en Kali; se identifica cómo lanzarlo desde la línea de comandos.

1. No answer needed

### Task 7: Escaneo activo / Active Scanning
**Explicación:** El escáner activo lanza ataques contra la aplicación para probar vulnerabilidades conocidas como inyecciones.

1. No answer needed

### Task 8: Fuerza bruta de formularios / Brute Force (password)
**Explicación:** ZAP incluye un atacante de fuerza bruta que prueba contraseñas sobre formularios de autenticación hasta encontrar la válida.

1. password

### Task 9: Alertas y resultados / Alerts and Results
**Explicación:** Los hallazgos se clasifican como alertas con niveles de riesgo que conviene revisar y exportar.

1. No answer needed

### Task 10: Práctica final / Hands-on Practice
**Explicación:** Ejercicio final que integra el flujo completo de análisis de una aplicación web con ZAP.

1. No answer needed

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué significa ZAP? / What does ZAP stand for? | `Zed Attack Proxy` |
| 2 | (Pregunta 2 no especificada en el original) | `No answer needed` |
| 3 | (Pregunta 3 no especificada en el original) | `No answer needed` |
| 4 | (Pregunta 4 no especificada en el original) | `No answer needed` |
| 5 | (Pregunta 5 no especificada en el original) | `No answer needed` |
| 6 | (Pregunta 6 no especificada en el original) | `No answer needed` |
| 7 | Dirección del proxy local / Local proxy address | `127.0.0.1` |
| 8 | (Pregunta 8 no especificada en el original) | `No answer needed` |
| 9 | (Pregunta 9 no especificada en el original) | `No answer needed` |
| 10 | Contraseña encontrada por fuerza bruta / Password found by brute force | `password` |
| 11 | (Pregunta 11 no especificada en el original) | `No answer needed` |
| 12 | (Pregunta 12 no especificada en el original) | `No answer needed` |

---

**Metodología:** Configurar el proxy de ZAP en 127.0.0.1, instalar el certificado raíz para inspeccionar HTTPS, dejar que el spider recorra la aplicación, ejecutar el escaneo activo, lanzar la fuerza bruta sobre el formulario de login y revisar las alertas para extraer la credencial.

### Cadena de ataque / Attack Chain

```text
proxy ZAP (127.0.0.1) -> certificado HTTPS -> spidering -> escaneo activo/pasivo -> fuerza bruta del login -> alertas -> credencial
```

**Learning chain:** OWASP ZAP -> proxy de interceptación -> certificado HTTPS -> spidering -> escaneo activo -> fuerza bruta -> análisis de alertas.

**Lección:** *Un proxy de interceptación como ZAP convierte la navegación normal en una sesión de pruebas visibles; automatizar spider, escáner y fuerza bruta multiplica la superficie descubierta y reduce el esfuerzo manual del analista.*

**MITRE ATT&CK:** T1595 (Active Scanning), T1592 (Gather Victim Host Information), T1059 (Command and Scripting Interpreter), T1110 (Brute Force)

**Fuente:** [TryHackMe - Introduction to OWASP ZAP](https://tryhackme.com/room/introductiontoowaspzap)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.