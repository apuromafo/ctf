# Challenge: BabyEncryption
Points: 1pts
Status: Solved

## DESCRIPTION:
You are after an organised crime group which is responsible for the illegal weapon market in your country. 
As a secret agent, you have infiltrated the group enough to be included in meetings with clients. 
During the last negotiation, you found one of the confidential messages for the customer. 
It contains crucial information about the delivery. Do you think you can decrypt it?
## HINT:
- NONE
## STEPS:
1. First, unzip the `.zip` file given.


## SOLUTION OUTPUT
python solution.py 

```bash
python .\apuromafo_Solution.py

[+] Datos cargados. Iniciando análisis de transformación:

 IDX  |  HEX   |  DEC  |      ECUACIÓN (paso a paso)      |  RES  | CHAR
-------------------------------------------------------------------------
  0   |  0x6e  |  110  |      (110 - 18) * 179 % 256      |   84  |   T
  1   |  0x0a  |   10  |      ( 10 - 18) * 179 % 256      |  104  |   h
  2   |  0x93  |  147  |      (147 - 18) * 179 % 256      |   51  |   3
  3   |  0x72  |  114  |      (114 - 18) * 179 % 256      |   32  |
  4   |  0xec  |  236  |      (236 - 18) * 179 % 256      |  110  |   n
  5   |  0x49  |   73  |      ( 73 - 18) * 179 % 256      |  117  |   u
  6   |  0xa3  |  163  |      (163 - 18) * 179 % 256      |   99  |   c
  7   |  0xf6  |  246  |      (246 - 18) * 179 % 256      |  108  |   l
  8   |  0x93  |  147  |      (147 - 18) * 179 % 256      |   51  |   3
  9   |  0x0e  |   14  |      ( 14 - 18) * 179 % 256      |   52  |   4
 10   |  0xd8  |  216  |      (216 - 18) * 179 % 256      |  114  |   r
 11   |  0x72  |  114  |      (114 - 18) * 179 % 256      |   32  |
 12   |  0x3f  |   63  |      ( 63 - 18) * 179 % 256      |  119  |   w
 13   |  0x9d  |  157  |      (157 - 18) * 179 % 256      |   49  |   1
 14   |  0xf6  |  246  |      (246 - 18) * 179 % 256      |  108  |   l
 15   |  0xf6  |  246  |      (246 - 18) * 179 % 256      |  108  |   l
 16   |  0x72  |  114  |      (114 - 18) * 179 % 256      |   32  |
 17   |  0x0e  |   14  |      ( 14 - 18) * 179 % 256      |   52  |   4
 18   |  0xd8  |  216  |      (216 - 18) * 179 % 256      |  114  |   r
 19   |  0xd8  |  216  |      (216 - 18) * 179 % 256      |  114  |   r
                                    ...

============================================================
MANTRA / FLAG DESCRIPTO:
------------------------------------------------------------
Th3 nucl34r w1ll 4rr1v3 0n fr1d4y.
HTB{l00k_47_y0u_r3v3rs1ng_3qu4710n5_c0ngr475}
============================================================
```