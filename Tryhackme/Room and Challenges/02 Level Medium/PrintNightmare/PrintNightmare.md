# PrintNightmare [MEDIUM]

1. No answer needed
2. Services
3. 1. CVE-2021-34527
   2. 07/02/2021
4. THM{SiGBQPMkSvejvmQNEL}
5. 1. C:\Windows\System32\spool\drivers\x64\3\
   2. pcAddPrinterDriverEx()
   3. rpcdump.py
6. 1. svch0st.dll,0x45A
   2. Microsoft-Windows-PrintService/Admin,808
   3. Service Control Manager,7031,1
   4. Microsoft-Windows-Sysmon/Operational,3,4747
   5. 10.10.210.100,ip-10-10-210-100.eu-west-1.compute.internal
   6. C:\Windows\System32\spool\drivers\x64\3\New\svch0st.dll,2021-08-13 17:33:37
7. 1. WIN-1O0UJBNP9G7
   2. printnightmare.local
   3. lowprivlarry
   4. letmein.dll
   5. 10.10.124.236
   6. \\10.10.124.236\sharez
   7. SMB3
8. 1. PowerShell,Group Policy
   2. Computer Configuration/Administrative Templates/Printers
   3. Get-Service -Name Spooler
9. No answer needed

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
