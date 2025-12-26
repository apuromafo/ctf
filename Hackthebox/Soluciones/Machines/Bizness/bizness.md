# 🛡️ Machine: Bizness

**Flags obtenidas:** system, user

**Estado:** Pwned

**Info:** 26.12.2025

## ##Área de Interés

* Aplicación Web
* Aplicaciones Comunes
* Bases de Datos

## ##Vulnerabilidad

* Credenciales Débiles
* Ejecución Remota de Comandos (RCE)
* Configuración Incorrecta
* Diseño Inseguro

## ##Lenguaje

* Python
* Java

## ##Tecnología

* NGINX
* Apache OFBiz

## ##Técnica

* Reconocimiento
* Descubrimiento de Estructura de Sitio Web
* Análisis de Configuración
* Reutilización de Contraseñas
* Cracking de Contraseñas

---

## 📝 Descripción

Bizness es una máquina Linux fácil que presenta una ejecución remota de comandos (RCE) pre-autenticación en Apache OFBiz, clasificada como [CVE-2023-49070](https://nvd.nist.gov/vuln/detail/CVE-2023-49070). El exploit se aprovecha para obtener una shell en la máquina, donde la enumeración de la configuración de OFBiz revela un hash de contraseña en la base de datos Derby del servicio. A través de la investigación y una pequeña revisión de código, el hash se transforma en un formato más común que puede ser crackeado por herramientas estándar de la industria. La contraseña obtenida se utiliza para iniciar sesión en la máquina como usuario root.

## 📑 Registro de Cambios de la Máquina

**Última actualización:** hace 2 años

**Marzo, 2024** `[~] Cambio`

`Parche CVE-2024-1086`

`Se actualizó la caja para eliminar la vulnerabilidad a CVE-2024-1086.`

**Enero, 2024** `[~] Cambio`

`Eliminado Artefacto de Prueba`

`Se eliminó un artefacto de prueba del directorio personal del usuario que causaba confusión y llevaba a los usuarios a un callejón sin salida (rabbit hole).`

---
 