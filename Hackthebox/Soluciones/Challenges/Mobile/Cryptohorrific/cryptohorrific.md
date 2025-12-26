# Challenge: Cryptohorrific
Points: 4pts
Status: Solved

## DESCRIPTION:
Secure coding is the keystone of the application security!

The first step was to investigate the challenge.plist file. Running the strings command on it revealed a suspicious base64-encoded string
Ciphertext: Tq+CWzQS0wYzs2rJ+GNrPLP6qekDbwze6fIeRRwBK2WXHOhba7WR2OGNUFKoAvyW7njTCMlQzlwIRdJvaP2iYQ==


Reversing time in ghidra or IDA free

With the knowledge that the decryption process involved a Key and an IV

as the pair for was key:iv , now update:

Key: !A%D*G-KaPdSgVkY
IV: QfTjWnZq4t7w!z%C

Once I had the key and IV, I knew that the base64-encoded string from the challenge.plist file was the ciphertext, and it needed to be decrypted using these values.

Ciphertext: Tq+CWzQS0wYzs2rJ+GNrPLP6qekDbwze6fIeRRwBK2WXHOhba7WR2OGNUFKoAvyW7njTCMlQzlwIRdJvaP2iYQ==
Key: !A%D*G-KaPdSgVkY
IV: QfTjWnZq4t7w!z%C



script:
```
python .\apuromafo_solution.py
=== CONFIGURACIÓN EXTRAÍDA ===
[*] KEY (Clave): !A%D*G-KaPdSgVkY
[*] IV (Vector):  QfTjWnZq4t7w!z%C
[*] Modo:         AES-128-ECB

=== PROCESO DE DESENCRIPTACIÓN Y PADDING ===
[*] 1. Datos desencriptados (con padding):
    Bytes: b'HTB{%SoC00l_H4ckTh3b0xbyBs3cur31stCh4ll3ng3!!Cr4zY%}\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c'
[*] 2. Análisis de Padding detectado:
    - Último byte: 0xc (Indica que hay 12 bytes de relleno)
    - Bytes de relleno: b'\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c'
[*] 3. Datos finales (Padding eliminado):
    Bytes: b'HTB{%SoC00l_H4ckTh3b0xbyBs3cur31stCh4ll3ng3!!Cr4zY%}'

============================================================
FLAG FINAL: HTB{%SoC00l_H4ckTh3b0xbyBs3cur31stCh4ll3ng3!!Cr4zY%}
============================================================
```
