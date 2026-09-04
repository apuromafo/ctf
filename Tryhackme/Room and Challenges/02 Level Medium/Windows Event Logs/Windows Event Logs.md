# Windows Event Logs [MEDIUM]

1. No answer needed
2. 1. No answer needed
   2. 40961
   3. whoami
   4. Execute a Remote Command
   5. Pipeline Execution Details
3. 1. 1071
   2. event log, log file, structured query
   3. /lf:true
   4. Xpath query
   5. No answer needed
   6. Application
   7. Event read direction
   8. Maximum number of events to read
4. 1. No answer needed
   2. OpenSSH/Admin,OpenSSH/Operational
   3. Microsoft-Windows-PowerShell-DesiredStateConfiguration-FileDownloadManager
   4. 192
   5. -MaxEvents
   6. 4
5. 1. Get-WinEvent -LogName Application -FilterXPath '*/System/Provider[@Name="WLMS"] and */System/TimeCreated[@SystemTime="2020-12-15T01:09:08.940277500Z"]'
   2. Get-WinEvent -LogName Security -FilterXPath '*/EventData/Data[@Name="TargetUserName"]="Sam" and */System/EventID=4720'
   3. 2
   4. A user account was created
   5. 12/17/2020 1:57:14 PM
   6. Microsoft-Windows-Security-Auditing
6. No answer needed
7. 1. 400
   2. 12/18/2020 7:50:33 AM
   3. 27736
   4. PC01.example.corp
   5. $Va5w3n8
   6. 8/25/2020 10:09:28 PM
   7. 6620
   8. S-1-5-32-544
   9. 4799
8. No answer needed

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
