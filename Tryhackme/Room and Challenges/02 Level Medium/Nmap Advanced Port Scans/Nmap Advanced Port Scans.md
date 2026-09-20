# Nmap Advanced Port Scans

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
| Medium | Módulo / Laboratorio | nmapadvancedportscans | https://tryhackme.com/room/nmapadvancedportscans | Red Network Security / Nmap | TryHackMe | Nmap, TCP Flags, RFC 793, escaneo avanzado | Medium |

> **Objeto:** Aprender las técnicas avanzadas de escaneo de puertos con Nmap: escaneos NULL/FIN/Xmas, su detección según las respuestas TCP (RFC 793), la artimaña del bit reservado, escaneo ACK, opciones de spoofing (`-S`, `-D`), idle scan (`-sI`) y el cálculo de TTL.

---

**Contexto:**

Esta sala del módulo de Nmap profundiza en los escaneos de puertos más sofisticados. Se repasa cómo se forman los flags TCP y se usa la herramienta interactiva que simula las respuestas del kernel de la máquina objetivo. Se estudia el escaneo TCP Null, FIN y Xmas con sus códigos de respuesta (0, 1, 3, 9), el bit reservado, el escaneo ACK para filtrar el estado de los puertos, el spoofing de IP (`-S 10.10.10.11`) y de origen múltiple (`-D 10.10.20.21,10.10.20.28,ME`), y el idle scan con `-sI 10.10.5.5`.

> **ES:** Con los ejercicios interactivos se determina cómo responde el objetivo a cada escaneo (números 0, 1, 3, 9, etc.), se aprende a fijar IP de origen (`-S 10.10.10.11`), a enmascarar el origen con decoys (`-D 10.10.20.21,10.10.20.28,ME`), a usar el idle scan (`-sI 10.10.5.5`) y a reconocer el flag `syn-ack`.

> **EN:** With the interactive exercises it is determined how the target responds to each scan (numbers 0, 1, 3, 9, etc.), you learn to set the source IP (`-S 10.10.10.11`), to mask the source with decoys (`-D 10.10.20.21,10.10.20.28,ME`), to use the idle scan (`-sI 10.10.5.5`) and to recognize the `syn-ack` flag.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:**

Se presenta la sala y el objetivo de aprender los escaneos de puertos avanzados con Nmap.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1 | `No answer needed` |

### Task 2: TCP Null Scan, FIN Scan y Xmas Scan / TCP Null Scan, FIN Scan and Xmas Scan
**Explicación:**

Se interactúa con el simulador que emula las respuestas del objetivo según el escaneo. Se responden los códigos de respuesta observados: para el puerto abierto, el puerto cerrado y el puerto filtrado (valores `0`, `1`, `3` y `9` según respuesta RST o ningún paquete).

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. Respuesta del objetivo | `0` |
| 2. Respuesta del objetivo | `1` |
| 3. Respuesta del objetivo | `3` |
| 4. Respuesta del objetivo | `9` |
| 5. Respuesta del objetivo | `9` |

### Task 3: TCP Maimon Scan / TCP Maimon Scan
**Explicación:**

Se comprueba qué tipo de escaneo usa los flags FIN y ACK simultáneamente según RFC 793.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 3. Escaneo FIN+ACK | `2` |

### Task 4: El artilugio del bit reservado / The Reserved Bit Trick
**Explicación:**

Se practica con el escaneo que anula el bit reservado del paquete TCP: la respuesta del objetivo, el tipo de respuesta, el número de puertos esperados, el puerto abierto/filtrado y la columna de confirmación.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. Valor esperado | `1` |
| 2. Tipo de respuesta | `RST` |
| 3. Número de puertos | `4` |
| 4. Puerto abierto | `443` |
| 5. ¿Respuesta esperada? / N | `N` |

### Task 5: Spoofing de IP / IP Spoofing
**Explicación:**

Se aprenden las opciones de Nmap para falsificar el origen: especificar una IP de origen falsa (`-S 10.10.10.11`) o usar múltiples orígenes falsos (`-D 10.10.20.21,10.10.20.28,ME`).

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. Opción IP origen falsa | `-S 10.10.10.11` |
| 2. Opción de decoys | `-D 10.10.20.21,10.10.20.28,ME` |

### Task 6: Escaneo ACK / ACK Scan
**Explicación:**

Se determina cuántos puertos abiertos reporta la regla del firewall según el escaneo ACK.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 6. Número de puertos | `4` |

### Task 7: Escaneo Idle / Idle Scan
**Explicación:**

Se usa el escaneo idle (zombie) indicando la IP de la máquina zombi con `-sI`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 7. Comando de idle scan | `-sI 10.10.5.5` |

### Task 8: Respuestas de Nmap / Nmap Responses
**Explicación:**

Se identifica la respuesta esperada de un puerto abierto al escaneo idle/zombie.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 8. Respuesta del puerto abierto | `syn-ack` |

### Task 9: Conclusión / Conclusion
**Explicación:**

Cierre de la sala de escaneos avanzados.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 9 | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Task 1 | `No answer needed` |
| 2 | 1. Respuesta | `0` |
| 2 | 2. Respuesta | `1` |
| 2 | 3. Respuesta | `3` |
| 2 | 4. Respuesta | `9` |
| 2 | 5. Respuesta | `9` |
| 3 | Escaneo FIN+ACK | `2` |
| 4 | 1. Valor esperado | `1` |
| 4 | 2. Tipo de respuesta | `RST` |
| 4 | 3. Número de puertos | `4` |
| 4 | 4. Puerto abierto | `443` |
| 4 | 5. ¿Respuesta? | `N` |
| 5 | 1. Spoofing origen | `-S 10.10.10.11` |
| 5 | 2. Decoys | `-D 10.10.20.21,10.10.20.28,ME` |
| 6 | Puertos en ACK | `4` |
| 7 | Idle scan | `-sI 10.10.5.5` |
| 8 | Respuesta puerto abierto | `syn-ack` |
| 9 | Task 9 | `No answer needed` |

---

**Metodología:**

1. Ejercicio interactivo de respuestas TCP (RFC 793) para escaneos NULL/FIN/Xmas y del bit reservado.
2. Aprendizaje del escaneo Maimon (FIN+ACK) y del escaneo ACK para conocer el filtrado del firewall.
3. Uso de opciones de origen falso (`-S`) y decoys (`-D`).
4. Configuración del idle scan con `-sI` y reconocimiento de la respuesta `syn-ack`.

### Cadena de ataque / Attack Chain

```
Aprender los flags TCP y el RFC 793 (simulador interactivo)
        |
        v
TCP Null / FIN / Xmas scans --> códigos de respuesta (0, 1, 3, 9)
        |
        v
Bit reservado / Maimon (FIN+ACK) --> respuesta RST en puertos abiertos
        |
        v
Evasión: -S 10.10.10.11, -D 10.10.20.21,10.10.20.28,ME
        |
        v
Reconocimiento pasivo: idle scan -sI 10.10.5.5 --> syn-ack = abierto
```

**Learning chain:**

- ¿Por qué los escaneos NULL/FIN/Xmas dependen estrictamente de la implementación RFC 793 del objetivo?
- ¿Cómo distingue el escaneo ACK entre puertos filtrados y sin filtrar?
- ¿Cómo se ejecutan y diferencian el spoofing (`-S`) de los decoys (`-D`)?
- ¿En qué se basa el idle scan y qué respuestas da un puerto abierto?

**Lección:**

*Cuanto más particular es un escaneo, más depende de la implementación TCP del objetivo: entender el RFC 793 y las respuestas de cada técnica evita conclusiones falsas y es la base de toda evasión de firewalls.*

**MITRE ATT&CK:**

- T1046 (Network Service Discovery)
- T1595.002 (Active Scanning: Vulnerability Scanning)
- T1036 (Masquerading) — contexto de spoofing

**Fuente:** [TryHackMe - Nmap Advanced Port Scans](https://tryhackme.com/room/nmapadvancedportscans)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.