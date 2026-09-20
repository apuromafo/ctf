# L2 MAC Flooding & ARP Spoofing

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `l2macfloodingarpspoofing` | [TryHackMe](https://tryhackme.com/room/l2macfloodingarpspoofing) | 01 Level Easy | TryHackMe | MAC flooding, ARP spoofing, bettercap, Wireshark, tcpdump, escucha de credenciales, man-in-the-middle, HTTP | Compromiso de una red local de nivel 2 mediante MAC flooding y ARP spoofing para interceptar el tráfico de las víctimas y capturar credenciales. |

---

**Contexto:** La sala reproduce un escenario de red con tres máquinas (Alice, Bob y Mallory) para demostrar ataques de nivel 2: el MAC flooding inunda la tabla CAM del switch para forzar el envío de tramas por todos los puertos (rellenando la tabla con direcciones MAC aleatorias), y el ARP spoofing envenena las cachés ARP de las víctimas para convertirse en man-in-the-middle. Con bettercap y Wireshark se captura el tráfico HTTP de la víctima, se recuperan credenciales en claro, se ejecuta una reverse shell y se obtiene la flag final.

> **ES:** Ataques de capa 2: primero se llena la tabla CAM del switch (MAC flooding, respuesta "Yay"), luego se realiza ARP spoofing de Alice y Bob, y se captura el tráfico HTTP para obtener credenciales (`admin:s3cr3t_P4zz`), una reverse shell y las flags `root.txt` y `THM{...}`.
> **EN:** Layer 2 attacks: first the switch CAM table is flooded (MAC flooding, "Yay" answer), then ARP spoofing of Alice and Bob is performed, and HTTP traffic is captured to recover credentials (`admin:s3cr3t_P4zz`), a reverse shell and the flags `root.txt` and `THM{...}`.

## Solucionario

### Task 1: Configuración / Setup
**Explicación:** Preparación del entorno de red. La pregunta corresponde a la comprobación inicial y no requiere respuesta.

```text
1. No answer needed
```

### Task 2: MAC Flooding / MAC Flooding
**Explicación:** Se envenena la tabla CAM del switch rellenándola con direcciones MAC aleatorias para que las tramas se transmitan por todos los puertos. El comando funciona correctamente.

```text
2. Yay
```

### Task 3: Verificación / Verification
**Explicación:** Se identifica la máquina sobre la que se trabaja (192.168.12.66), la máscara de red (/24), el número de equipos a atacar (2) y el usuario de la escena (`alice`).

```text
3. 1. 192.168.12.66
   2. /24
   3. 2
   4. alice
```

### Task 4: ARP Spoofing / ARP Spoofing
**Explicación:** Se lanza el ataque ARP spoofing contra las víctimas. El ataque tiene éxito ("Yay"); el usuario que se hace pasar por víctima es `Bob`, el protocolo involucrado es `ICMP` y se observa el puerto `666`.

```text
4. 1. Yay
   2. Bob
   3. ICMP
   4. 666
```

### Task 5: Intercepción / Interception
**Explicación:** Se confirma el tráfico interceptado: el protocolo capturado es `ICMP` y el puerto en uso es `1337`.

```text
5. 1. ICMP
   2. 1337
```

### Task 6: Eficacia del ataque / Attack effectiveness
**Explicación:** Se confirma el comportamiento del ataque: primero no se observa la comunicación esperada ("Nay") y después sí se logra ("Yay").

```text
6. 1. Nay
   2. Yay
```

### Task 7: Captura de credenciales / Credential capture
**Explicación:** Se intercepta el tráfico HTTP de la víctima. Las direcciones IP de la escena son 192.168.12.10 y 192.168.12.20; la víctima del ataque es 192.168.12.20 en el puerto 80. Se capturan las credenciales en claro (`admin:s3cr3t_P4zz`), el hostname (`www.server.bob`), el archivo solicitado (`test.txt`), la respuesta HTTP (`OK`), la flag `THM{wh0s_$n!ff1ng_0ur_cr3ds}`. Se restaura la red haciendo "RE-ARPing the victims", después se abre una reverse shell y se ejecutan los comandos `whoami, pwd, ls`, recuperando el archivo final `root.txt`.

```text
7. 1. 192.168.12.10, 192.168.12.20
   2. 192.168.12.20
   3. 80
   4. Nay
   5. Nay
   6. Yay
   7. alice
   8. www.server.bob
   9. test.txt
   10. OK
   11. admin:s3cr3t_P4zz
   12. RE-ARPing the victims
   13. Yay
   14. THM{wh0s_$n!ff1ng_0ur_cr3ds}
   15. reverse shell
   16. whoami, pwd, ls
   17. root.txt
```

### Task 8: Flag final / Final flag
**Explicación:** Se obtiene la flag final del ejercicio de Man-in-the-Middle.

```text
8. THM{wh4t_an_ev1l_M!tM_u_R}
```

### Task 9: Conclusión / Conclusion
**Explicación:** Tarea final de reflexión. No requiere respuesta.

```text
9. No answer needed
```

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Configuración inicial | `No answer needed` |
| 2 | ¿Funciona el MAC flooding? | `Yay` |
| 3 | Dirección IP de la máquina | `192.168.12.66` |
| 3 | Máscara de red | `/24` |
| 3 | Número de equipos a atacar | `2` |
| 3 | Usuario de la escena | `alice` |
| 4 | ¿Funciona el ARP spoofing? | `Yay` |
| 4 | Usuario víctima | `Bob` |
| 4 | Protocolo capturado | `ICMP` |
| 4 | Puerto | `666` |
| 5 | Protocolo de la intercepción | `ICMP` |
| 5 | Puerto | `1337` |
| 6 | Primera comprobación | `Nay` |
| 6 | Segunda comprobación | `Yay` |
| 7 | Direcciones IP de la escena | `192.168.12.10, 192.168.12.20` |
| 7 | Dirección IP de la víctima | `192.168.12.20` |
| 7 | Puerto del servicio | `80` |
| 7 | Respuesta 1 | `Nay` |
| 7 | Respuesta 2 | `Nay` |
| 7 | Respuesta 3 | `Yay` |
| 7 | Usuario | `alice` |
| 7 | Hostname | `www.server.bob` |
| 7 | Archivo solicitado | `test.txt` |
| 7 | Respuesta HTTP | `OK` |
| 7 | Credenciales capturadas | `admin:s3cr3t_P4zz` |
| 7 | Método de restauración de la red | `RE-ARPing the victims` |
| 7 | ¿Se restauró la red? | `Yay` |
| 7 | Flag de la tarea | `THM{wh0s_$n!ff1ng_0ur_cr3ds}` |
| 7 | Tipo de ataque final | `reverse shell` |
| 7 | Comandos ejecutados | `whoami, pwd, ls` |
| 7 | Archivo final recuperado | `root.txt` |
| 8 | Flag final | `THM{wh4t_an_ev1l_M!tM_u_R}` |
| 9 | Conclusión | `No answer needed` |

---

**Metodología:** Primero se realizó un ataque de MAC flooding sobre la tabla CAM del switch para degradar la segmentación de nivel 2. Después se ejecutó el ARP spoofing con bettercap para envenenar las cachés ARP de Alice y Bob y convertirse en man-in-the-middle. Con Wireshark se capturó el tráfico HTTP en claro, recuperando credenciales, identificando el host, el archivo solicitado y la flag de la tarea. Finalmente se restauró la ARP ("RE-ARPing the victims") y se explotó una reverse shell para recuperar `root.txt`.

### Cadena de ataque / Attack Chain

```text
MAC flooding (tabla CAM llena) -> ARP spoofing de Alice y Bob -> MITM -> captura de tráfico HTTP -> credenciales admin:s3cr3t_P4zz -> flag THM{...} -> RE-ARPing los hechos -> reverse shell -> whoami/pwd/ls -> root.txt -> flag final THM{wh4t_an_ev1l_M!tM_u_R}
```

**Learning chain:** MAC flooding -> bettercap -> ARP spoofing -> MITM -> Wireshark -> HTTP plaintext credential capture -> RE-ARPing -> reverse shell -> root.txt

**Lección:** *Los protocolos de nivel 2 asumen confianza por diseño: saturar la tabla CAM o envenenar la caché ARP convierte el switch en un hub lógico, permitiendo interceptar tráfico y capturar credenciales en claro.*

**MITRE ATT&CK:** T1557 (Adversary-in-the-Middle: ARP Cache Poisoning), T1557.001 (ARP Cache Poisoning), T1040 (Network Sniffing), T1055 - vehículos del MITM, T1059.004 (Command and Scripting Interpreter: Unix Shell)

**Fuente:** [TryHackMe - L2 MAC Flooding & ARP Spoofing](https://tryhackme.com/room/l2macfloodingarpspoofing)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.