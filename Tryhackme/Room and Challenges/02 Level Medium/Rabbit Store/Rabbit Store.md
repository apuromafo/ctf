# Rabbit Store

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF / Challenge | rabbitstore | https://tryhackme.com/room/rabbitstore | 02 Level Medium | TryHackMe | Hash / MD5, Enumeración, Web | Obtención de hashes / flags del reto |

---

**Contexto:** La sala **Rabbit Store** es un challenge CTF web en el que la resolución pasa por enumerar la aplicación y extraer los dos valores hash que actúan como respuesta acreditativa del laboratorio.

## Solucionario

### Task 1: Hashes del reto / Challenge hashes
**Explicación:**

La secuencia de respuestas son los dos hashes (formato MD5) que se obtienen durante la resolución del reto web.

```
1. 98d3a30fa86523c580144d317be0c47e
2. eabf7a0b05d3f2028f3e0465d2fd0852
```

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Hash 1 del reto | `98d3a30fa86523c580144d317be0c47e` |
| 2 | Hash 2 del reto | `eabf7a0b05d3f2028f3e0465d2fd0852` |

---

**Metodología:** Enumeración de la aplicación web, identificación de los puntos de datos expuestos y extracción de los hashes que responden la sala.

### Cadena de ataque / Attack Chain

```
Enumeración de la aplicación web
        │
        ▼
Localización de datos sensibles
        │
        ▼
Extracción de los valores hash
```

**Learning chain:** Reconocimiento web → enumeración → extracción de hashes → respuestas.

**Lección:** *Las aplicaciones expuestas suelen colar datos en bruto (hashes, IDs) en recursos aparentemente inocuos; la enumeración metódica de la web es la clave del reto.*

**MITRE ATT&CK:** T1580 Cloud Infrastructure Discovery · T1041 Exfiltration Over C2 Channel (contexto de extracción de datos) · T1083 File and Directory Discovery.

**Fuente:** [TryHackMe - Rabbit Store](https://tryhackme.com/room/rabbitstore)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.