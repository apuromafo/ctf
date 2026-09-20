# PrintNightmare, thrice!

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF / Walkthrough | printnightmarethrice | https://tryhackme.com/room/printnightmarethrice | 02 Level Medium | TryHackMe | Impresión (Print Spooler), SMB, Mimikatz, PrintNightmare | Escalada a SYSTEM / admin en servidor Windows |

---

**Contexto:** La sala **PrintNightmare, thrice!** es un walkthrough guiado sobre la explotación de la impresión de Windows (Print Spooler). Se identifica el servidor de impresión objetivo, se enumeran los recursos y named pipes (`IPC$`, `srvsvc`, `spoolss`), se localizan los puntos de montaje `print$` con las DLL por arquitectura, se registra una impresora maliciosa que carga el driver DLL explotable y se concluye con la escalada de privilegios mediante el comando de persistencia sobre el grupo de administradores locales.

## Solucionario

### Task 1: Explotación guiada de PrintNightmare / Guided PrintNightmare exploitation
**Explicación:**

La secuencia de respuestas recorre todo el ataque: dirección IP del host de impresión, credenciales de acceso SMB (dominio\usuario), sesión de invitado, named pipes expuestos, rutas UNC del driver malicioso por arquitectura (`x64` y `W32X86`), directorios locales de drivers, ruta del servidor de spool remoto, nombre de la impresora maliciosa, puerto del servicio y proceso (`spoolsv.exe`), y el comando final para añadir al usuario `rjones` al grupo de administradores.

```
1. 20.188.56.147
2. THM-PRINTNIGHT0\rjones
3. THM-PRINTNIGHT0/gentilguest
4. \\printnightmare.gentilkiwi.com\IPC$,srvsvc,spoolss
5. \\printnightmare.gentilkiwi.com\print$,\x64\3\mimispool.dll,\W32X86\3\mimispool.dll
6. C:\Windows\system32\spool\drivers\X64\3,C:\Windows\system32\spool\drivers\W32X86\3
7. C:\Windows\System32\spool\SERVERS\printnightmare.gentilkiwi.com
8. Kiwi Legit Printer
9. 5408,spoolsv.exe
10. net localgroup administrators rjones /add
```

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué host se identifica como servidor de impresión objetivo? | `20.188.56.147` |
| 2 | ¿Qué usuario de dominio se usa en el acceso SMB? | `THM-PRINTNIGHT0\rjones` |
| 3 | ¿Qué cuenta/identificador se utiliza para la sesión de invitado? | `THM-PRINTNIGHT0/gentilguest` |
| 4 | ¿Qué named pipes quedan expuestos en el IPC? | `\\printnightmare.gentilkiwi.com\IPC$,srvsvc,spoolss` |
| 5 | ¿Qué rutas UNC bajo `print$` apuntan al driver malicioso? | `\\printnightmare.gentilkiwi.com\print$,\x64\3\mimispool.dll,\W32X86\3\mimispool.dll` |
| 6 | ¿Qué directorios locales contienen los drivers de impresión? | `C:\Windows\system32\spool\drivers\X64\3,C:\Windows\system32\spool\drivers\W32X86\3` |
| 7 | ¿Qué ruta usa el servidor de spool remoto? | `C:\Windows\System32\spool\SERVERS\printnightmare.gentilkiwi.com` |
| 8 | ¿Qué nombre recibe la impresora maliciosa? | `Kiwi Legit Printer` |
| 9 | ¿Qué puerto y proceso se asocian al servicio? | `5408,spoolsv.exe` |
| 10 | ¿Qué comando se ejecuta para escalar al grupo de administradores? | `net localgroup administrators rjones /add` |

---

**Metodología:** Enumeración del servicio de impresión y SMB, identificación de named pipes y recursos `print$`, preparación del driver DLL por arquitectura, registro de la impresora maliciosa contra el spooler remoto y escalada de privilegios vía `net localgroup`.

### Cadena de ataque / Attack Chain

```
Identificar host de impresión (20.188.56.147)
        │
        ▼
Autenticación SMB (rjones / gentilguest)
        │
        ▼
Enumerar IPC$ → srvsvc, spoolss
        │
        ▼
Mapear print$\x64\3\mimispool.dll y \W32X86\3\mimispool.dll
        │
        ▼
Registrar impresora "Kiwi Legit Printer" (spoolsv.exe : 5408)
        │
        ▼
net localgroup administrators rjones /add
```

**Learning chain:** Reconocimiento del spooler → abuso de privilegios de impresión → carga de DLL maliciosa → escalada a administrador.

**Lección:** *Un recurso de impresión mal configurado (PrintNightmare, CVE-2021-34527) permite convertir una impresora legítima en un vehículo de escalada remota; hay que restringir los cambios de drivers por parte de no administradores.*

**MITRE ATT&CK:** T1068 Exploitation for Privilege Escalation · T1543.003 Create or Modify System Process (Windows Service) · T1078 Valid Accounts.

**Fuente:** [TryHackMe - PrintNightmare, thrice!](https://tryhackme.com/room/printnightmarethrice)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.