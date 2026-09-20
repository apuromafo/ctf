# Jupyter 101

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `jupyter101` | https://tryhackme.com/room/jupyter101 | 01 Level Easy | TryHackMe | Jupyter Notebook / Python / pandas (Series, DataFrames) / matplotlib | Introducción a Jupyter Notebook: celdas, kernels, atajos, manejo de datos con pandas (read_csv, head, tail, shape) y visualización básica con matplotlib. |

---

**Contexto:** Sala introductoria de la ruta de data science de TryHackMe. Explica qué es Jupyter Notebook, cómo se ejecutan las celdas (Interpreter/Shift + Enter), el manejo de datos con pandas (Series y DataFrames, `read_csv`, `head`, `tail`, `shape`) y la visualización con `plot()`, etiquetas y colores de matplotlib.

> **ES:** Sala de iniciación a Jupyter Notebook: celdas e interpretación, pandas (Series/DataFrames) y gráficos con matplotlib.
> **EN:** Jupyter Notebook intro room: cells and interpretation, pandas (Series/DataFrames) and plotting with matplotlib.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Lectura de la introducción a Jupyter Notebook y a la sala. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la room. / Read the room introduction. | `No answer needed` |

### Task 2: Fundamentos / Fundamentals

**Explicación:** Conceptos básicos del cuaderno: celdas de código y de markdown. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee los fundamentos de la tarea. / Read the task fundamentals. | `No answer needed` |

### Task 3: Entorno / Environment

**Explicación:** Configuración del entorno de trabajo con los notebooks. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee el contenido de la tarea. / Read the task content. | `No answer needed` |

### Task 4: Celdas / Cells

**Explicación:** Se explican los tipos de celda del notebook. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee el contenido de la tarea. / Read the task content. | `No answer needed` |

### Task 5: Ejecución de celdas / Running Cells

**Explicación:** Las celdas de un notebook se ejecutan con un intérprete (kernel) activo. La forma de ejecutar la celda actual (`Shift + Enter`) ejecuta y avanza a la siguiente celda; con el atajo combinado se mantiene la selección. El número de kernel activo en el ejercicio es `1` y el código devuelve `2` como salida.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué componente interpreta el código del notebook? / Which component interprets the notebook code? | `Interpreter` |
| 2 | Número de kernel activo. / Active kernel number. | `1` |
| 3 | Atajo para ejecutar la celda y avanzar. / Shortcut to run the cell and move on. | `Shift + Enter` |
| 4 | Salida del código del ejercicio. / Output of the exercise code. | `2` |

### Task 6: Workflow / Flujo de trabajo

**Explicación:** Tarea de lectura sobre el flujo de trabajo habitual en un notebook. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee el contenido de la tarea. / Read the task content. | `No answer needed` |

### Task 7: pandas / Series y DataFrames / pandas: Series and DataFrames

**Explicación:** La librería pandas trabaja con **Series y DataFrames**. Los datos se cargan con `read_csv`, y para inspeccionarlos se usan `head` (primeras filas), `tail` (últimas filas) y `shape` (dimensiones del DataFrame).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Estructuras principales de pandas. / Main pandas structures. | `Series and Dataframes` |
| 2 | Función para cargar un CSV. / Function to load a CSV. | `read_csv` |
| 3 | Método para mostrar las primeras filas. / Method to show the first rows. | `head` |
| 4 | Método para mostrar las últimas filas. / Method to show the last rows. | `tail` |
| 5 | Atributo con las dimensiones del DataFrame. / Attribute with the DataFrame dimensions. | `shape` |

### Task 8: Visualización / Visualization

**Explicación:** Para graficar se usa `plot()`. Los ejes se etiquetan con `xlabel` e `ylabel`, el gráfico se titula con `title`, y se personaliza con `color` y el parámetro `zlabel` del ejemplo.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Función para generar el gráfico. / Function to generate the plot. | `plot()` |
| 2 | Etiqueta del eje X. / X-axis label. | `xlabel` |
| 3 | Etiqueta del eje Y. / Y-axis label. | `ylabel` |
| 4 | Título del gráfico. / Plot title. | `title` |
| 5 | Atributo de color del gráfico. / Plot color attribute. | `color` |
| 6 | Parámetro adicional del ejemplo. / Additional parameter of the example. | `zlabel` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la room. | `No answer needed` |
| 2 | Lee los fundamentos de la tarea. | `No answer needed` |
| 3 | Lee el contenido de la tarea. | `No answer needed` |
| 4 | Lee el contenido de la tarea. | `No answer needed` |
| 5 | ¿Qué componente interpreta el código del notebook? | `Interpreter` |
| 6 | Número de kernel activo. | `1` |
| 7 | Atajo para ejecutar la celda y avanzar. | `Shift + Enter` |
| 8 | Salida del código del ejercicio. | `2` |
| 9 | Lee el contenido de la tarea. | `No answer needed` |
| 10 | Estructuras principales de pandas. | `Series and Dataframes` |
| 11 | Función para cargar un CSV. | `read_csv` |
| 12 | Método para mostrar las primeras filas. | `head` |
| 13 | Método para mostrar las últimas filas. | `tail` |
| 14 | Atributo con las dimensiones del DataFrame. | `shape` |
| 15 | Función para generar el gráfico. | `plot()` |
| 16 | Etiqueta del eje X. | `xlabel` |
| 17 | Etiqueta del eje Y. | `ylabel` |
| 18 | Título del gráfico. | `title` |
| 19 | Atributo de color del gráfico. | `color` |
| 20 | Parámetro adicional del ejemplo. | `zlabel` |

---

**Metodología:** Seguir el flujo de un notebook: lanzar el kernel (Interpreter), ejecutar celdas con `Shift + Enter`, cargar datos con pandas (`read_csv`), inspeccionarlos con `head`/`tail`/`shape` y, finalmente, graficar con `plot()` añadiendo etiquetas y títulos.

### Cadena de ataque / Attack Chain

```text
Arrancar kernel -> ejecutar celdas (Shift + Enter) -> pandas (read_csv/head/tail/shape) -> matplotlib (plot/xlabel/ylabel/title/color)
```

**Learning chain:** Jupyter -> celdas -> kernel -> pandas (Series/DataFrames) -> visualización.

**Lección:** *Jupyter Notebook combina un intérprete por células con pandas y matplotlib: aprender los atajos de ejecución y las funciones básicas de pandas (read_csv, head, tail, shape) es suficiente para empezar a analizar datos.*

**MITRE ATT&CK:** N/A (room de fundamentos de data science)

**Fuente:** [TryHackMe - Jupyter 101](https://tryhackme.com/room/jupyter101)
---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.