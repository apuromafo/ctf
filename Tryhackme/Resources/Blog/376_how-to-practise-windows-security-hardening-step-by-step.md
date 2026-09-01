# How to Practise Windows Security Hardening (Step by Step)

**ID Original:** no disponible
**Slug:** how-to-practise-windows-security-hardening-step-by-step
--------------------

Windows installs with a lot of legacy protocols still enabled. SMBv1, LLMNR, NetBIOS, RC4 encryption for Kerberos, NTLMv1 authentication - features that made sense in the 1990s and early 2000s but which attackers now exploit routinely. The CIS Benchmarks for Windows document runs to over a thousand pages because there are hundreds of settings that need attention. For someone learning security, that is an overwhelming place to start.
This guide takes a different approach. Rather than a compliance checklist, it walks through hardening in a logical sequence: understand the attack surface, apply the highest-impact controls, enable the logging that lets defenders see what is happening, and verify the changes actually worked. Each step includes the relevant commands and Group Policy paths, plus a TryHackMe room to practise in a safe environment before touching production systems.
The steps below are ordered from highest-impact to more advanced. If you only complete the first four, you will have addressed the majority of the attack chains covered in most real-world Windows penetration tests.
Step 1 - Audit what is running before you harden anything
Hardening without understanding what is on the system is how you break things. The first step is always reconnaissance on your own environment: what services are running, which protocols are active, and what the current patch state looks like.
Run these in an elevated PowerShell session:
# Check SMBv1 status
Get-WindowsOptionalFeature -Online -FeatureName smb1protocol
# Check LLMNR status via registry
Get-ItemProperty "HKLM:\Software\Policies\Microsoft\Windows NT\DNSClient" -Name EnableMulticast -ErrorAction SilentlyContinue
# List all running services
Get-Service | Where-Object {$_.Status -eq 'Running'} | Sort-Object DisplayName
# Check Windows Update / patch status
Get-HotFix | Sort-Object InstalledOn -Descending | Select-Object -First 10
Why it matters You cannot harden what you cannot see. An audit log of the baseline state also gives you a before/after comparison to verify that changes took effect.
Practise on TryHackMe Windows Fundamentals 1 and Windows Fundamentals 2
Step 2 - Disable legacy protocols: SMBv1, LLMNR, and NetBIOS
These three protocols are responsible for a disproportionate share of real-world Windows attacks. SMBv1 was the attack vector for WannaCry and NotPetya. LLMNR and NetBIOS enable Responder -style credential poisoning attacks that require no prior access. All three should be disabled in any environment that does not have a specific legacy dependency on them.
# Disable SMBv1
Disable-WindowsOptionalFeature -Online -FeatureName smb1protocol -NoRestart
# Disable LLMNR via registry
$path = "HKLM:\Software\Policies\Microsoft\Windows NT\DNSClient"
if (!(Test-Path $path)) { New-Item -Path $path -Force }
Set-ItemProperty -Path $path -Name "EnableMulticast" -Type DWord -Value 0
# Disable NetBIOS over TCP/IP
$interfaces = "HKLM:\SYSTEM\CurrentControlSet\Services\NetBT\Parameters\Interfaces"
Get-ChildItem $interfaces | ForEach-Object {
Set-ItemProperty -Path $_.PSPath -Name "NetbiosOptions" -Type DWord -Value 2
}
The Group Policy path for LLMNR is: Computer Configuration > Administrative Templates > Network > DNS Client > Turn off Multicast Name Resolution. Set it to Enabled.
Why it matters LLMNR poisoning with Responder is one of the first things a pentester tries on an internal network. Disabling it removes the attack surface entirely, with no impact on modern DNS-based name resolution.
Practise on TryHackMe Breaching Active Directory — run the LLMNR poisoning lab before and after disabling the protocol to see the difference.
Step 3 Enforce NTLMv2 only and enable SMB signing
NTLM is a legacy authentication protocol that supports multiple versions. NTLMv1 is trivially crackable and should never be used. NTLMv2 is significantly stronger but still vulnerable to relay attacks without SMB signing. The combination of enforcing NTLMv2-only and requiring SMB signing closes both gaps.
# Set LAN Manager authentication to NTLMv2 only (via registry)
$key = "HKLM:\SYSTEM\CurrentControlSet\Control\Lsa"
Set-ItemProperty -Path $key -Name 'LmCompatibilityLevel' -Type DWord -Value 5
# Enable SMB signing (required, not just supported)
Set-SmbServerConfiguration -RequireSecuritySignature $true -Force
Set-SmbClientConfiguration -RequireSecuritySignature $true -Force
The Group Policy path for LAN Manager authentication level is: Computer Configuration > Windows Settings > Security Settings > Local Policies > Security Options > Network security: LAN Manager authentication level. Set to 'Send NTLMv2 response only. Refuse LM and NTLM'.
Why it matters Without SMB signing, an attacker who captures an NTLM authentication can relay it to another server, authenticating as the victim without ever cracking the hash. SMB signing makes every authentication cryptographically tied to the connection, preventing relay.
Step 4 - Enable Credential Guard and protect LSASS
Credential Guard uses hardware-backed virtualisation (VBS) to protect credential material in memory. Without it, tools like Mimikatz can extract NTLM hashes and plaintext credentials from LSASS memory. Enabling it requires a machine with Secure Boot and TPM 2.0 enabled, which covers most hardware from 2016 onwards. The Microsoft Credential Guard documentation covers prerequisites in detail.
# Enable Credential Guard via registry (requires reboot)
$key = "HKLM:\SYSTEM\CurrentControlSet\Control\DeviceGuard"
if (!(Test-Path $key)) { New-Item -Path $key -Force }
Set-ItemProperty -Path $key -Name 'EnableVirtualizationBasedSecurity' -Type DWord -Value 1
Set-ItemProperty -Path $key -Name 'RequirePlatformSecurityFeatures' -Type DWord -Value 1
# Enable LSA Protection (protects LSASS from memory reads)
$lsa = "HKLM:\SYSTEM\CurrentControlSet\Control\Lsa"
Set-ItemProperty -Path $lsa -Name 'RunAsPPL' -Type DWord -Value 1
In Group Policy: Computer Configuration > Administrative Templates > System > Device Guard > Turn On Virtualization Based Security. Enable it with the Secure Boot and DMA Protection platform settings.
Why it matters Pass-the-Hash attacks depend on reading credential hashes from LSASS memory. Credential Guard moves those credentials into a hardware-isolated container that the operating system itself cannot read directly, breaking the attack chain.
Practise on TryHackMe Windows Fundamentals 3 then Windows Privilege Escalation
Step 5 - Deploy LAPS for unique local administrator passwords
By default, Windows machines often have the same local administrator password across the entire fleet, set during imaging and never changed. If an attacker compromises one machine and dumps the local admin hash, they can authenticate to every other machine on the network using Pass-the-Hash. Microsoft LAPS (Local Administrator Password Solution) solves this by generating a unique, automatically rotated password for the local administrator account on each machine, storing it in Active Directory where only authorised users can retrieve it.
LAPS is now built into Windows since the April 2023 cumulative updates (replacing the legacy standalone LAPS client). To enable it:
# Verify LAPS is available (Windows Server 2019+ / Win 10 22H2+)
Get-Command Get-LapsADPassword
# Update AD schema for LAPS (run once, requires Schema Admin rights)
Update-LapsADSchema
# Configure policy via Group Policy:
# Computer Configuration > Administrative Templates
#   > System > LAPS > Configure password backup directory
# Set to: Active Directory
Why it matters LAPS transforms Pass-the-Hash lateral movement from a domain-wide attack into a single-machine problem. Even if an attacker dumps credentials from one workstation, the hash is useless everywhere else.
Step 6 Configure Attack Surface Reduction rules in Defender
Step 6 - Configure Attack Surface Reduction rules in Defender
Windows Defender includes 17 Attack Surface Reduction (ASR) rules that block specific attack behaviours: Office macros spawning child processes, script interpreters running executable content, credential dumping from LSASS, and more. Most are not enabled by default. The recommended approach is to deploy them in Audit mode first to see what would be blocked, then switch to Block mode once you have confirmed no legitimate applications are affected.
# Enable ASR rules in Audit mode first (see what would fire)
# Block Office apps from creating child processes
Add-MpPreference -AttackSurfaceReductionRules_Ids d4f940ab-401b-4efc-aadc-ad5f3c50688a \
-AttackSurfaceReductionRules_Actions AuditMode
# Block credential stealing from LSASS
Add-MpPreference -AttackSurfaceReductionRules_Ids 9e6c4e1f-7d60-472f-ba1a-a39ef669e4b0 \
-AttackSurfaceReductionRules_Actions AuditMode
# Block execution of potentially obfuscated scripts
Add-MpPreference -AttackSurfaceReductionRules_Ids 5beb7efe-fd9a-4556-801d-275e5ffc04cc \
-AttackSurfaceReductionRules_Actions AuditMode
# Check current ASR rule status
Get-MpPreference | Select-Object AttackSurfaceReductionRules_Ids, AttackSurfaceReductionRules_Actions
Why it matters ASR rules block the specific techniques attackers use in commodity malware and ransomware, not just the malicious files themselves. They interrupt the attack chain before execution, rather than detecting malware after the fact.
Step 7 - Enable PowerShell logging and Windows Event auditing
Hardening reduces the attack surface, but no configuration is impenetrable. The controls that give defenders visibility into what is happening on a system are just as important as the controls that block attacks. PowerShell script block logging captures every script that runs, even if it is obfuscated. Windows Event ID 4688 with command line auditing records every process that starts, including its full command line arguments.
# Enable PowerShell Script Block Logging
$sb = "HKLM:\Software\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging"
if (!(Test-Path $sb)) { New-Item -Path $sb -Force }
Set-ItemProperty -Path $sb -Name "EnableScriptBlockLogging" -Value 1
# Enable PowerShell Module Logging
$ml = "HKLM:\Software\Policies\Microsoft\Windows\PowerShell\ModuleLogging"
if (!(Test-Path $ml)) { New-Item -Path $ml -Force }
Set-ItemProperty -Path $ml -Name "EnableModuleLogging" -Value 1
# Enable process creation auditing with command line (Event ID 4688)
auditpol /set /subcategory:"Process Creation" /success:enable /failure:enable
The Group Policy paths are: Computer Configuration > Administrative Templates > Windows Components > Windows PowerShell for logging, and Computer Configuration > Windows Settings > Security Settings > Advanced Audit Policy Configuration > System Audit Policies for process creation. The full Advanced Audit Policy reference is on Microsoft Learn.
Why it matters Without logging, an attacker can run a PowerShell payload, move laterally, and exfiltrate data with no trace in the event log. Script block logging means that even heavily obfuscated scripts are captured in their decoded form at the point of execution.
Practise on TryHackMe Windows Internals — walks through the Windows event log and what to look for during an incident.
Step 8 Verify your hardening actually worked
Step 8 - Verify your hardening actually worked
The final step is verification. Configuration drift is real: updates can re-enable settings, new software installs can add services, and Group Policy can conflict in unexpected ways. Checking that the controls you applied are still in effect should be a regular practice, not a one-time event.
# Verify SMBv1 is disabled
Get-WindowsOptionalFeature -Online -FeatureName smb1protocol | Select-Object State
# Verify LLMNR is off
Get-ItemProperty "HKLM:\Software\Policies\Microsoft\Windows NT\DNSClient" -Name EnableMulticast
# Verify SMB signing is required
Get-SmbServerConfiguration | Select-Object RequireSecuritySignature
Get-SmbClientConfiguration | Select-Object RequireSecuritySignature
# Verify LSA Protection is active
Get-ItemProperty "HKLM:\SYSTEM\CurrentControlSet\Control\Lsa" -Name RunAsPPL
# Check ASR rules are in expected state
Get-MpPreference | Select-Object AttackSurfaceReductionRules_Actions
For a more structured approach, Microsoft Security Baselines provide a policy package you can deploy via Group Policy that applies Microsoft's recommended settings across all the categories above, with documentation for each choice. The CIS Benchmarks cover the same ground but are more conservative and compliance-focused.
What this sequence covers
Working through these eight steps addresses the most commonly exploited Windows configuration weaknesses: the legacy protocols that enable credential harvesting, the default settings that allow Pass-the-Hash lateral movement, the missing controls that let attackers dump credentials from memory, and the absence of logging that lets attacks go undetected.
None of these steps require a security product purchase. Everything above uses native Windows functionality, Group Policy, and built-in Defender features. The gap between a default Windows installation and a reasonably hardened one is almost entirely a configuration gap, not a technology gap.
Practise these skills on TryHackMe's Windows Fundamentals module builds the foundation needed to understand the controls above, and the rooms linked throughout this guide put them into practice in a browser-based lab environment.

---
**Fuente / Source:** [how-to-practise-windows-security-hardening-step-by-step](https://tryhackme.com/resources/blog/how-to-practise-windows-security-hardening-step-by-step)
