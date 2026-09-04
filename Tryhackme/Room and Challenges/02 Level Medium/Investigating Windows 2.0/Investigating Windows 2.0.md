# Investigating Windows 2.0 [MEDIUM]

1. 1. HKCU\Environment\UserIntMprLogonScript
   2. procexp64.exe
   3. SELECT * FROM Win32_ProcessStartTrace WHERE ProcessName = 'procexp64.exe'	
   4. VBScript
   5. LaunchBeaconingBackdoor
   6. Motobit Software
   7. http://www.motobit.com, http://motobit.cz
   8. WMIBackdoor.ps1
   9. C:\TMP
   10. mim.exe, powershell.exe
   11. svchost.exe
   12. Process Start
   13. Parent PID, Command line, Current directory, Environment
   14. No process
   15. WMIScan
   16. ProcessStartTrigger
   17. __FilterToConsumerBinding
   18. nbtscan.exe
   19. Known Bad / Dual use classics
   20. p.exe
   21. psexesvc.exe, Sysinternals PsExec
   22. schtasks-backdoor.ps1
   23. xCmd.exe
   24. C:\Users\Public\svchost.exe
   25. C:\Windows\System32
   26. Stuff running where it normally shouldn't
   27. en-US.js
   28. CACTUSTORCH
   29. mim.exe
   30. mk.ps1, mk.exe, v2.0.50727

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
