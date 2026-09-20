# AV Evasion_ Shellcode

| Campo | Valor |
|-------|-------|
| Dificultad | Medium |
| Tipo | Room |
| Slug | avevasionshellcode |
| Link | https://tryhackme.com/room/avevasionshellcode |
| Sección | 02 Level Medium |
| Fuente | TryHackMe |
| Componentes | Shellcode, AV Evasion, PE Analysis, Windows Defender |
| Impacto | Alto |

---

**Contexto:** Sala enfocada en la evasión de antivirus mediante shellcode y técnicas de ofuscación. Se aprende a generar shellcode, analizar archivos PE, identificar firmas de detección y desarrollar técnicas para evadir Windows Defender y otros productos de seguridad. Incluye análisis estático de binarios y práctica de generación de payloads evasivos.

## Solucionario

### Task 1: Introduccion a AV Evasion
**Explicación:** Conceptos fundamentales de evasión de antivirus y por qué es necesaria en pruebas de penetración y CTF.

1. No answer needed

### Task 2: Windows Defender
**Explicación:** Comprensión del funcionamiento de Windows Defender y sus mecanismos de detección. Identificación del antivirus instalado y configuración de la máquina virtual.

2. 1. Windows Defender
   2. av-victim
   3. THM{H3ll0-W1nD0ws-Def3nd3r!}

### Task 3: Analisis Estatico de PE
**Explicación:** Análisis estático de archivos PE (Portable Executable) para entender su estructura, incluyendo cabecera DOS, secciones y metadatos relevantes para la evasión.

3. 1. 530949
   2. 5A4D
   3. 12E4
   4. 7
   5. .flag
   6. THM{PE-N3w-s3ction!}

### Task 4: Generacion de Shellcode
**Explicación:** Generación de shellcode utilizando herramientas como msfvenom para crear payloads que evadan la detección antivirus.

4. THM{y0ur-1s7-5h311c0d3}

### Task 5: Comprension del Shellcode
**Explicación:** Análisis y comprensión del shellcode generado, entendiendo su功能 y cómo interactúa con el sistema operativo.

5. No answer needed

### Task 6: Analisis de Firma
**Explicación:** Análisis de firmas antivirus y cómo los productos de seguridad detectan código malicioso basado en patrones conocidos.

6. 1. nay
   2. nay
   3. yea
   4. No answer needed

### Task 7: Ofuscacion Basica
**Explicación:** Técnicas básicas de ofuscación para modificar el shellcode y evadir la detección basada en firmas.

7. 1. nay
   2. nay
   3. yea

### Task 8: Tecnica Avanzada
**Explicación:** Implementación de técnicas avanzadas de evasión que combinan múltiples métodos de ofuscación.

8. No answer needed

### Task 9: Evasion Activa
**Explicación:** Evasión activa de antivirus en tiempo de ejecución, incluyendo bypass de monitoreo y detección en vivo.

9. 1. yea
   2. yea
   3. yea
   4. No answer needed

### Task 10: Validacion
**Explicación:** Validación de las técnicas de evasión implementadas verificando que los payloads evadan la detección correctamente.

10. 1. nay
    2. yea

### Task 11: Conclusion
**Explicación:** Revisión final de las técnicas aprendidas y cierre de la actividad.

11. No answer needed

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Task 1 | No answer needed |
| 2 | Task 2.1 | Windows Defender |
| 2 | Task 2.2 | v-victim |
| 2 | Task 2.3 | THM{H3ll0-W1nD0ws-Def3nd3r!} |
| 3 | Task 3.1 | 530949 |
| 3 | Task 3.2 | 5A4D |
| 3 | Task 3.3 | 12E4 |
| 3 | Task 3.4 | 7 |
| 3 | Task 3.5 | .flag |
| 3 | Task 3.6 | THM{PE-N3w-s3ction!} |
| 4 | Task 4 | THM{y0ur-1s7-5h311c0d3} |
| 5 | Task 5 | No answer needed |
| 6 | Task 6.1 | 
ay |
| 6 | Task 6.2 | 
ay |
| 6 | Task 6.3 | yea |
| 6 | Task 6.4 | No answer needed |
| 7 | Task 7.1 | 
ay |
| 7 | Task 7.2 | 
ay |
| 7 | Task 7.3 | yea |
| 8 | Task 8 | No answer needed |
| 9 | Task 9.1 | yea |
| 9 | Task 9.2 | yea |
| 9 | Task 9.3 | yea |
| 9 | Task 9.4 | No answer needed |
| 10 | Task 10.1 | 
ay |
| 10 | Task 10.2 | yea |
| 11 | Task 11 | No answer needed |

---

**Metodología:** Evasión de antivirus (AV Evasion) mediante shellcode, análisis estático de PE y técnicas de ofuscación progresivas.

**Learning chain:** Análisis PE -> Generación de shellcode -> Análisis de firmas -> Ofuscación -> Evasión activa -> Validación

**Lección:** _La evasión de antivirus requiere comprender tanto la detección estática como la dinámica para desarrollar payloads efectivos._

**MITRE ATT&CK:** T1027 (Obfuscated Files or Information), T1055 (Process Injection), T1059.001 (PowerShell), T1211 (Exploitation for Defense Evasion), T1036 (Masquerading)

**Fuente:** [TryHackMe - AV Evasion_ Shellcode](https://tryhackme.com/room/avevasionshellcode)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
