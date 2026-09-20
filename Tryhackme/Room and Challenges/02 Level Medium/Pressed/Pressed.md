# Pressed

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF / Challenge | pressed | https://tryhackme.com/room/pressed | 02 Level Medium | TryHackMe | Base64, Decodificación de datos | Recuperación de la flag del reto |

---

**Contexto:** La sala **Pressed** es un challenge CTF en el que la flag acreditativa no se entrega de forma directa. La respuesta aparece fragmentada en varios bloques codificados en base64 que, concatenados en orden, reconstruyen la flag completa. El reto obliga a reconocer la codificación, decodificar cada pieza y ensamblarlas, aunque una de las partes ya se proporciona en claro para validar el resultado.

## Solucionario

### Task 1: Flag fragmentada en base64 / Flag split in base64
**Explicación:**

La flag se presenta en cuatro partes. Los tres primeros bloques están codificados en base64 (`VEhNe0...` decodifica a `THM{`) y deben concatenarse con la última pieza, que ya está en texto claro, para obtener la flag definitiva del reto.

```
1. VEhNe0FfQzJfTUF5Xw==
2. RWx1RDNfWTB1X1doM25fWW91Xw==
3. QXJlX1ByZSRzM2RfNF9UaW0zfQ==
4. THM{A_C2_MAy_EluD3_Y0u_Wh3n_You_Are_Pre$s3d_4_Tim3}
```

Respuesta: `THM{A_C2_MAy_EluD3_Y0u_Wh3n_You_Are_Pre$s3d_4_Tim3}`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Fragmento 1 de la flag (base64) | `VEhNe0FfQzJfTUF5Xw==` |
| 2 | Fragmento 2 de la flag (base64) | `RWx1RDNfWTB1X1doM25fWW91Xw==` |
| 3 | Fragmento 3 de la flag (base64) | `QXJlX1ByZSRzM2RfNF9UaW0zfQ==` |
| 4 | Flag completa | `THM{A_C2_MAy_EluD3_Y0u_Wh3n_You_Are_Pre$s3d_4_Tim3}` |

---

**Metodología:** Identificar que la respuesta es una flag fragmentada, reconocer los bloques base64, decodificarlos y concatenarlos en orden, y validar el resultado contra el fragmento en claro final.

### Cadena de ataque / Attack Chain

```
Flag fragmentada en bloques base64
        │
        ▼
Decodificar cada fragmento (base64 → ASCII)
        │
        ▼
Concatenar los fragmentos en orden
        │
        ▼
THM{A_C2_MAy_EluD3_Y0u_Wh3n_You_Are_Pre$s3d_4_Tim3}
```

**Learning chain:** Reconocimiento de codificación → decodificación base64 → concatenación → flag.

**Lección:** *Las flags pueden ocultarse en múltiples capas de codificación; antes de buscar otra vía conviene comprobar si los bloques codificados encajan entre sí.*

**MITRE ATT&CK:** T1059 Command and Scripting Interpreter · T1027 Obfuscated Files or Information.

**Fuente:** [TryHackMe - Pressed](https://tryhackme.com/room/pressed)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.