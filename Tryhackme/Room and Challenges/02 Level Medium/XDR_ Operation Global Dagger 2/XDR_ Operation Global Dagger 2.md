# XDR_ Operation Global Dagger 2 [MEDIUM]

Room: https://tryhackme.com/room/xdroperationglobaldagger2

1. No answer needed
2. No answer needed
3. 1. Suspicious service registration
   2. 3
   3. RegistryModification
   4. cdb58d0bcabe76afc60428f364834463
   5. DisableRealtimeMonitoring
   6. reg  add "HKLM\Software\Policies\Microsoft\Windows Defender\Real-Time Protection" /v "DisableRealtimeMonitoring" /t REG_DWORD /d "1" /f 
   7. WMIC.exe
   8. Discovery, Execution
   9. THM{PZ874JC89DR5NZ1DAF6MS2KH}

#source https://medium.com/@Sle3pyHead/xdr-operation-global-dagger-2-ctf-notes-tryhackme-e85eaa8daab3

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
