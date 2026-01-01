

Hopper's Origin

se debe ingresar la clave para su acceso.



 Access URL: Hopper's Invitation
 hxxps://static-labs.tryhackme.cloud/apps/hoppers-invitation/ como bien sabemos desde el link de sidequest 1
 
una vez decodificado el contenido con la flag , desde sidequest 1 (paso final ) , se procede a decodificar el contenido del txt indicado en su código de fuente.
analizando el codigo de fuente.
el acceso lo permite 
 
 Hoppers Origins
From HopSec Island, Eggsploits whisper through TBFC - Origins of how SOC-mas became EAST-mas.

Hoppers Origins room info
Room Type  Free Room. Anyone can deploy virtual machines in the room (without being subscribed)!

Created by:   am03bam4n
Created 53 days ago



Task 2

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

Answer format: ***{************************************}

 
AI.VANCHAT.LOC: user.txt

Answer format: ***{************************************}

 
AI.VANCHAT.LOC: root.txt

Answer format: ***{************************************}

 
TBFC.LOC: user.txt

Answer format: ***{************************************}

 
TBFC.LOC: root.txt

Answer format: ***{************************************}

 
VANCHAT.LOC: user.txt

Answer format: ***{************************************}

 
VANCHAT.LOC: root.txt

Answer format: ***{************************************}

 
SERVER1: user.txt

Answer format: ***{************************************}

 
SERVER1: root.txt

Answer format: ***{************************************}

 
SERVER2: user.txt

Answer format: ***{************************************}

 
SERVER2: root.txt

Answer format: ***{************************************}

 
SERVER3: user.txt

Answer format: ***{************************************}

 
SERVER3: root.txt

Answer format: ***{************************************}

 
SERVER4: user.txt

Answer format: ***{************************************}

 
SERVER4: root.txt

Answer format: ***{************************************}
 
Web: user.txt

Answer format: ***{************************************}

 
Web: root.txt

Answer format: ***{************************************}

01.01.2026
 
#solution

Hopper's Origin
 Access URL: Hopper's Invitation
 https://static-labs.tryhackme.cloud/apps/hoppers-invitation/
 
 
 
 i put the key from the end of sidequest 1 or any,  and say in error cors but see the additional file
 
 https://assets.tryhackme.com/additional/aoc2025/files/hopper-origins.txt
 
  content
 `hlRAqw3zFxnrgUw1GZusk+whhQHE0F+g7YjWjoJvpZRSCoDzehjXsEX1wQ6TTlOPyEJ/k+AEiMOxdqywh/86AOmhTaXNyZAvbHUVjfMdTqdzxmLXZJwI5ynI`
 
  i check the info.
 
 
````python

 python .\POC.py
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

when enter have the room 
https://tryhackme.com/room/ho-aoc2025-yboMoPbnEX
````

solution:
https://tryhackme.com/jr/ho-aoc2025-yboMoPbnEX

next steps:

# TUT Hoppers Origins 01.01.2026 
 https://0xb0b.gitbook.io/writeups/tryhackme/2025/advent-of-cyber-25-side-quest/hoppers-origins
 
 
 video
 
 Hoppers Origins - Misión secundaria Advent of Cyber ​​- Parte 1 (Tutorial 2025)
 
 https://www.youtube.com/watch?v=r1cUBw-G2kc
 
 
 Hoppers Origins - Advent of Cyber Side Quest - Part 2- Walkthrough 2025
 
 https://www.youtube.com/watch?v=T-Hfx8VC7Nk
 
 
 
 