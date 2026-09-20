# MD2PDF

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|-------------|---------|
| Easy | walkthrough | `md2pdf` | [TryHackMe](https://tryhackme.com/room/md2pdf) | 01 Level Easy | THM | Markdown, PDF, conversor, generación de documentos | Conversión de Markdown a PDF y obtención de la flag del reto |

> **Objeto:** Interactuar con un conversor Markdown a PDF para generar documentos y recuperar la flag del reto.

---

**Contexto:** Sala centrada en un servicio que convierte documentos Markdown en PDF. Se exploran las funciones del conversor y, tras completar el ejercicio de conversión, se obtiene la flag del reto.

> **ES:** Sala sobre un conversor de Markdown a PDF: práctica de conversión de documentos y obtención de la flag final.
> **EN:** Room about a Markdown-to-PDF converter: practicing document conversion and getting the final flag.

## Solucionario

### Task 1: Conversión y flag / Conversion and flag
**Explicación:** Se utiliza el conversor MD2PDF para generar el documento solicitado y se obtiene la flag del reto.

1. flag{1f4a2b6ffeaf4707c43885d704eaee4b}

### Tabla unificada de preguntas y respuestas

| Task | Pregunta | Respuesta |
|------|----------|-----------|
| 1.1 | Flag del reto | `flag{1f4a2b6ffeaf4707c43885d704eaee4b}` |

---

**Metodología:** Exploración de la interfaz del conversor MD2PDF, generación del documento a partir del Markdown solicitado y captura de la flag mostrada al completar la conversión.

### Cadena de ataque / Attack Chain

Interfaz del conversor → envio del Markdown → generación del PDF → flag del reto.

**Learning chain:** MD2PDF → conversión Markdown → PDF → flag

*Lección:* Los servicios de conversión de documentos deben revisarse tanto por su salida como por los datos que pueden llegar a procesar o exponer.

**MITRE ATT&CK:** N/A.

**Fuente:** [TryHackMe - MD2PDF](https://tryhackme.com/room/md2pdf)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.

**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.

**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).

**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.