 

# Tutorial Definitivo: Explotación de SokobanHTB

## Ingeniería Inversa y Manipulación de Memoria para CTF

Este tutorial cubre el proceso desde el reconocimiento inicial hasta la manipulación de la memoria para extraer la Flag del reto **SokobanHTB**.

---

## 1. Reconocimiento y Análisis de Superficie

Antes de abrir herramientas técnicas, es fundamental entender el funcionamiento del objetivo:

* **Mecánica:** Juego de "Sokoban" donde un personaje púrpura debe empujar 3 cajas verdes sobre 3 marcas `X` amarillas.
* **Controles:** WASD o flechas de dirección.
* **Objetivo de Explotación:** Alterar el estado del juego para satisfacer la condición de victoria sin completar el puzzle manualmente.

---

## 2. Análisis Estático (Ghidra)

Para entender cómo el juego gestiona los datos, realizamos ingeniería inversa sobre el binario.

### Localización del Bucle Principal

1. Carga el ejecutable en **Ghidra** y analiza las funciones de entrada.
2. Sigue el flujo: `entry` → `FUN_1400b32e0()` → **`FUN_1400045f0()`**.
3. Identificamos `FUN_1400045f0()` como la **función principal** del motor del juego.

### Hallazgos del Código Descompilado

Al analizar el bucle principal, observamos la carga de activos (`player.png`, `box.png`) y la inicialización de objetos. Un detalle crítico aparece en la función de posicionamiento:

* Uso de `CONCAT44((float)i, (float)j)`.
* **Conclusión técnica:** El motor utiliza **flotantes de 4 bytes (Single Precision Float)** para las coordenadas `X` e `Y`. Esto descarta la búsqueda de valores enteros (`Integer`) en la memoria.

---

## 3. Localización de Coordenadas en Memoria (Cheat Engine)

Con el conocimiento de que las posiciones son `Floats`, procedemos a la búsqueda dinámica.

### Paso A: Encontrar al Jugador

1. Abre **Cheat Engine** y selecciona el proceso `SokobanHTB.exe`.
2. Configura `Value Type` a **Float**.
3. Realiza un **"Unknown initial value"** scan.
4. Mueve al personaje y filtra:
* Derecha → **Increased value**
* Izquierda → **Decreased value**
* Sin movimiento → **Unchanged value**


5. Una vez localizada la dirección de la coordenada **X**, la coordenada **Y** estará casi siempre en `X + 4`.

### Paso B: El valor de límite "1024"

1. Modifica manualmente la X del jugador a un valor muy alto.
2. Notarás que el mapa tiene límites definidos. Mediante pruebas, descubrimos que muchos bloques externos y colisiones están anclados al valor **1024.0**.
3. Realiza un nuevo escaneo en CE buscando el valor exacto **1024** (tipo Float). Esto nos dará acceso al **arreglo de objetos** (paredes y cajas).

---

## 4. Identificación de Cajas y Teletransportación

No todas las direcciones con valor 1024 son útiles; debemos encontrar las tres cajas verdes vinculadas a la victoria.

### Mapeo de Objetos

1. De la lista de direcciones obtenidas en el paso anterior, modifica los valores uno por uno.
2. Observa qué caja verde "salta" o desaparece en la pantalla del juego.
3. Anota las direcciones de memoria de las **3 cajas verdes participantes**.

### Ejecución del "Warp-to-Win"

1. Identifica las coordenadas visuales de las metas (`X` amarillas). Puedes mover al jugador sobre una de ellas y copiar sus coordenadas `(X, Y)`.
2. En **Cheat Engine**, sobrescribe las coordenadas de las 3 cajas verdes con las coordenadas de las metas.
3. **Acción final:** Realiza un pequeño movimiento con el jugador. Esto fuerza al motor a ejecutar el "Win Check".

---

## 5. Resultado y Obtención de la Flag

Si los datos en memoria coinciden con la validación del código estático, el juego desplegará el trofeo y la cadena de texto de la Flag.

### Flag Final

```text
HTB{H4ck_0r_50k084n_7h3_80x_a34fbe06}

```

---

## Resumen de Direccionamiento Técnico

| Objeto | Tipo de Dato | Estructura Sugerida |
| --- | --- | --- |
| Jugador | Float (4 bytes) | `[Base + Offset_X]`, `[Base + Offset_Y]` |
| Cajas | Float (4 bytes) | Arreglo de estructuras `(x, y)` |
| Límite Mapa | Float (4 bytes) | Constante `1024.0` |

---
 Nota:
Español: Además, si solo vas a copiarlos en HTB , no los pegues de inmediato, ya que HTB los baneará, chicos intenten resolverlo y aqui lo dejo a modo de respaldo solamente .

English: Also, if you're just going to copy them, don't instant paste it as HTB will ban you, guys.