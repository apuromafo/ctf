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