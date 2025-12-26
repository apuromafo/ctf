# Challenge: xorxorxor
Points: 1pts
Status: Solved


## DESCRIPTION:

Challenge Scenario
Who needs AES when you have XOR?

Based from the script, we can conclude that each character will be XOR with each character of the key.
We can assume that the 4 characters is HTB{

H in hex -> 48 (base16)
xor 48 with 13 -> 5b

T -> 54
xor 54 with 4a -> 1e

B -> 42
xor 42 with f6 -> b4

{ -> 7B
xor 7B with e1 -> 9a

I used this online tools to calculate the xor -> https://xor.pw/#

The key is -> 5b1eb49a

dcode.fr for XOR BruteForce.
Got the flag!


script :
```
python .\apuromafo_Solution.py
--- Iniciando Proceso de Desencriptación ---
[+] Hexadecimal extraído: 134af6e1297bc4a96f6a...
[+] Clave recuperada (XOR entre Ciphertext y 'HTB{'):
    Hex: 5b1eb49a | Bytes: b'[\x1e\xb4\x9a'

========================================
RESULTADO: HTB{rep34t3d_x0r_n0t_s0_s3cur3}
========================================
```