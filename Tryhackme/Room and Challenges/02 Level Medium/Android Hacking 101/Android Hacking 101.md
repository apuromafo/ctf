# Android Hacking 101

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Mobile Security | androidhacking101 | https://tryhackme.com/room/androidhacking101 | 02 Level Medium | TryHackMe | APK, adb, dex2jar, smali, Android Studio | Compromiso de apps móviles / datos sensibles |

---

**Contexto:** La sala **Android Hacking 101** introduce el pentesting de aplicaciones Android sobre un emulador. El alumno configura el entorno ADB, instala una APK de muestra (la app de la conferencia Black Hat 2014 volcada fuera del sandbox de la conferencia), extrae el paquete del dispositivo, descompila el binario con herramientas como `dex2jar`/`d2j-dex2smali`, localiza credenciales y librerías, e identifica componentes expuestos (activities exportadas y permisos peligrosos como `SEND_SMS`) en apps de propósito educativo como InsecureBankv2. Cada tarea avanza de la configuración al análisis del código descompilado.

## Solucionario

### Task 1: Configuración del entorno
**Explicación:**

Se instala y verifica el entorno de desarrollo Android y la herramienta ADB sobre el laboratorio.

Respuesta: `No answer needed`

### Task 2: Conexión con el emulador
**Explicación:**

Se conecta el host con el emulador/dispositivo mediante ADB y se comprueba el estado de la sesión.

Respuesta: `No answer needed`

### Task 3: Instalación de la APK objetivo
**Explicación:**

Se instala la aplicación de muestra en el emulador, preparada para su análisis.

Respuesta: `No answer needed`

### Task 4: Identificación del paquete
**Explicación:**

Se lista la aplicación instalada y se obtiene el nombre del paquete que servirá como identificador único en los comandos ADB.

Respuesta: `com.swapcard.apps.android.blackhat`

### Task 5: Extracción de la APK
**Explicación:**

Se localiza y extrae el binario instalado desde la partición de datos del emulador. Se documenta la herramienta usada para convertir el paquete (opción `d2j-dex2smali`), la respuesta seleccionada en el análisis, la ruta física de la APK y el comando ADB que la trae al host.

1. `d2j-dex2smali`
2. `b`
3. `/data/app/com.swapcard.apps.android.blackhat-1/base.apk`
4. `adb pull /data/app/com.swapcard.apps.android.blackhat-1/base.apk`

### Task 6: Reconocimiento del código
**Explicación:**

Se examina el proyecto/código descompilado en busca de metadatos y componentes sensibles: el nombre del repositorio, la activity exportada que permite invocar el cambio de contraseña y el permiso peligroso declarado por la app.

1. `swapcard-android-app-2014`
2. `com.android.insecurebankv2.ChangePassword`
3. `android.permission.SEND_SMS`

### Task 7: Análisis estático de librerías
**Explicación:**

Se revisan las librerías nativas y dependencias del paquete buscando rutas de ataque adicionales.

Respuesta: `No answer needed`

### Task 8: Requisitos del sistema
**Explicación:**

Se identifican los elementos del sistema Android que la aplicación espera y que condicionan el análisis dinámico.

Respuesta: `No answer needed`

### Task 9: Hardware y firmware
**Explicación:**

Se comparan las características del dispositivo virtual con las exigencias de la app objetivo.

Respuesta: `No answer needed`

### Task 10: Instrumentación dinámica
**Explicación:**

Se aplica Frida u otro mechanismo de instrumentación para manipular el comportamiento de la app en tiempo de ejecución.

Respuesta: `No answer needed`

### Task 11: Cierre
**Explicación:**

Se consolidan los hallazgos del análisis de la aplicación móvil.

Respuesta: `No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Configuración del entorno | `No answer needed` |
| 2 | Conexión con el emulador | `No answer needed` |
| 3 | Instalación de la APK | `No answer needed` |
| 4 | Nombre del paquete de la app | `com.swapcard.apps.android.blackhat` |
| 5.1 | Herramienta seleccionada en el análisis | `d2j-dex2smali` |
| 5.2 | Opción elegida en el laboratorio | `b` |
| 5.3 | Ruta física de la APK en el dispositivo | `/data/app/com.swapcard.apps.android.blackhat-1/base.apk` |
| 5.4 | Comando ADB de extracción | `adb pull /data/app/com.swapcard.apps.android.blackhat-1/base.apk` |
| 6.1 | Repositorio del código descompilado | `swapcard-android-app-2014` |
| 6.2 | Activity exportada vulnerable | `com.android.insecurebankv2.ChangePassword` |
| 6.3 | Permiso peligroso solicitado | `android.permission.SEND_SMS` |
| 7 | Análisis de librerías | `No answer needed` |
| 8 | Requisitos del sistema | `No answer needed` |
| 9 | Hardware y firmware | `No answer needed` |
| 10 | Instrumentación dinámica | `No answer needed` |
| 11 | Cierre del análisis | `No answer needed` |

---

**Metodología:** Pentest móvil guiado (OWASP MASTG): identificación de paquete, extracción de APK vía adb, descompilación (dex2jar/smali), análisis de código descompilado (activities exportadas), revisión de permisos y librerías.

**Learning chain:** Entorno ADB → instalación → fingerprint del paquete → extracción del binario → descompilación → hallazgos en código → permisos → instrumentación → reporte.

**Lección:** *Una app móvil se analiza antes de ejecutarse: el nombre del paquete y un `adb pull` son el inicio de todo el proceso de revenimiento.*

**MITRE ATT&CK:** T1401 App Process Discovery (Mobile) · T1622 Debugger Evasion · T1574 Hijack Execution Flow (Library/Path) en contexto móvil.

**Fuente:** [TryHackMe - Android Hacking 101](https://tryhackme.com/room/androidhacking101)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.