# Learn Rust

| **Dificultad** | Easy |
| **Tipo** | Programación (lenguaje Rust) |
| **Slug** | `rust` |
| **Link** | [TryHackMe](https://tryhackme.com/room/rust) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | Cargo / Rustup / Variables y tipos / Funciones / Bucles / Rayon / Manejo de errores |
| **Impacto** | Curso introductorio de programación en Rust: desde la instalación de la toolchain y la creación de proyectos con Cargo hasta variables, mutabilidad, tipos de datos, funciones, bucles, paralelismo con Rayon y manejo de errores con Result, terminando con una bandera final. |

---

**Contexto:** La sala es un curso interactivo de Rust. Empieza con los orígenes del lenguaje (C++, comunidad en Discord, Cargo como gestor) y la instalación con Rustup. Después se crean proyectos con `cargo init` y se compila/ejecuta con `cargo run` y `cargo build --release`. El núcleo cubre variables (mutabilidad y shadowing), tipos de datos (Signed, u32, i16, &str, String), funciones y bucles, incluyendo los mensajes de error del compilador (E0308). Por último se introduce el paralelismo con la librería Rayon y el manejo de errores con `Result` y `unwrap`, y se resuelve un reto final.

## Solucionario

### Task 1: Introducción a Rust

**Explicación:** Orígenes de Rust: inspirado en `C++`, con una comunidad que empezó en `Discord`, alto deseo de continuidad entre desarrolladores (`70%`) y `Cargo` como gestor/compilador oficial.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué lenguaje inspiró el diseño de Rust? | `C++` |
| 2 | ¿En qué plataforma se desarrolló inicialmente la comunidad de Rust? | `Discord` |
| 3 | ¿Qué porcentaje de desarrolladores desea seguir utilizando Rust? | `70%` |
| 4 | ¿Cuál es la herramienta oficial de gestión de paquetes y de compilación de Rust? | `Cargo` |

### Task 2: Herramientas de Rust

**Explicación:** `Rustup` gestiona las toolchains; para instalar herramientas de la comunidad se usa `cargo install rustscan`; `cargo fmt` formatea el código automáticamente.

```bash
rustup update
cargo install rustscan
cargo fmt
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la herramienta para instalar las toolchains de Rust? | `Rustup` |
| 2 | ¿Qué comando instala la herramienta RustScan? | `cargo install rustscan` |
| 3 | ¿Qué comando formatea automáticamente el código de Rust? | `cargo fmt` |

### Task 3: Creando un proyecto

**Explicación:** `cargo init` crea el proyecto: archivo principal `main.rs` y manifiesto `cargo.toml`. Las macros llevan `!` (`println!`); `cargo run` compila y ejecuta; `cargo build --release` compila en modo release dejando los binarios en `target/release/`. El proyecto se compiló `4` veces en total.

```bash
cargo init
cargo run
cargo build --release
ls target/release/
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué comando inicializa un nuevo proyecto de Rust en el directorio actual? | `cargo init` |
| 2 | ¿Qué símbolo se utiliza tras el nombre de una macro (como en println!)? | `!` |
| 3 | ¿Cómo se llama el archivo principal de código por defecto? | `main.rs` |
| 4 | ¿Cómo se llama el archivo de manifiesto con la configuración del proyecto? | `cargo.toml` |
| 5 | ¿Qué comando compila y ejecuta el proyecto? | `cargo run` |
| 6 | ¿Qué comando compila el proyecto en modo release? | `cargo build --release` |
| 7 | ¿En qué directorio se guardan los binarios compilados? | `target/release/` |
| 8 | ¿Cuántas veces se compiló el proyecto en total? | `4` |

### Task 4: Variables - Data Types

**Explicación:** Algunas declaraciones/atribuciones de tipo son inválidas (`F`); el compilador reporta fallos de tipo con el error `E0308`. Reasignar una variable inmutable da `cannot assign twice to immutable variable`.

```rust
let x = 5;
x = 6; // E0308 / cannot assign twice to immutable variable
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿La siguiente declaración de variable es correcta en Rust? (T/F) | `F` |
| 2 | ¿Cuál es el código de error del compilador para los fallos de tipo? | `E0308` |
| 3 | ¿Esta asignación de tipo es válida en Rust? (T/F) | `F` |
| 4 | ¿Cuál es el mensaje de error al reasignar un valor a una variable inmutable? | `cannot assign twice to immutable variable` |

### Task 5: Variables - Constantes y Shadowing

**Explicación:** Las constantes se declaran con `const` y no pueden usar `mut` (`F`). Redeclarar una variable con el mismo nombre se llama `shadowed` y no cambia el tipo original (`F`). La longitud de un texto se obtiene con `word.len();`.

```rust
const MAX: u32 = 100;
let word = "thm".to_string();
println!("{}", word.len());
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Crea una variable siguiendo las indicaciones de la sala. | `No answer needed` |
| 2 | ¿Qué palabra clave se utiliza para definir constantes? | `const` |
| 3 | ¿Una constante puede declararse con la palabra clave "mut"? (T/F) | `F` |
| 4 | ¿Cómo se llama la técnica de declarar una nueva variable con el mismo nombre que una anterior? | `shadowed` |
| 5 | ¿El shadowing cambia el tipo de la variable original? (T/F) | `F` |
| 6 | ¿Qué método se utiliza para obtener la longitud de un texto en Rust? | `word.len();` |

### Task 6: Data Types

**Explicación:** Tipos de Rust: enteros `Signed` (positivos y negativos), sin signo de 32 bits (`u32`), con signo de 16 bits (`i16`), slices de texto (`&str`) y `String`. Declaraciones: `let mut tryhackme: u32 = 9;` y `x: String`.

```rust
let mut tryhackme: u32 = 9;
let x: String = String::from("thm");
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué tipo de entero puede representar valores negativos y positivos? | `Signed` |
| 2 | ¿Qué tipo de dato es un entero sin signo de 32 bits? | `u32` |
| 3 | ¿Qué tipo de dato es un entero con signo de 16 bits? | `i16` |
| 4 | ¿Cómo se declara una variable mutable de tipo u32 llamada "tryhackme"? | `let mut tryhackme: u32 = 9;` |
| 5 | ¿Qué tipo de dato representa un slice de texto (referencia a string)? | `&str` |
| 6 | ¿Cómo se declara una variable de tipo String llamada "x"? | `x: String` |

### Task 7: Funciones

**Explicación:** Funciones en Rust: no pueden mutar globales (`F`), los parámetros no se pasan siempre por valor (`F`), devuelven `&str` para string slices, no devuelven varios valores sin tupla (`F`), un cuerpo no solo puede tener println! (`F`), la última expresión se devuelve implícitamente (`T`) aunque también existe `return`, y pueden llamarse antes de definirse (`T`).

```rust
fn saludo() -> &'static str {
    "hola"
}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Las funciones en Rust pueden mutar variables globales? (T/F) | `F` |
| 2 | ¿Los parámetros de una función se pasan siempre por valor? (T/F) | `F` |
| 3 | ¿Qué tipo de retorno se usa cuando una función devuelve un string slice? | `&str` |
| 4 | ¿Una función puede devolver varios valores a la vez sin una tupla? (T/F) | `F` |
| 5 | ¿El cuerpo de una función puede contener println! sin devolver nada? (T/F) | `F` |
| 6 | ¿La última expresión de una función se devuelve implícitamente? (T/F) | `T` |
| 7 | ¿Qué palabra clave devuelve explícitamente un valor de una función? | `return` |
| 8 | ¿Las funciones en Rust pueden llamarse antes de su definición? (T/F) | `T` |

### Task 8: Bucles

**Explicación:** `break` detiene un bucle; `loop` es infinito hasta que se detiene; un array se recorre con `a.iter()` y el bucle `for` también itera sobre rangos numéricos (`T`).

```rust
for x in 0..10 { println!("{}", x); }
loop { break; }
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué palabra clave detiene la ejecución de un bucle? | `break` |
| 2 | ¿Qué tipo de bucle se ejecuta de forma infinita hasta que se detiene? | `loop` |
| 3 | ¿Cómo se itera sobre los elementos de un array llamado "a"? | `a.iter()` |
| 4 | ¿El bucle for puede iterar sobre un rango de números? (T/F) | `T` |

### Task 9: Desafío de ownership

**Explicación:** El ownership puede transferirse entre funciones (`T`); una variable movida ya no puede usarse (`F`); y las referencias no se copian automáticamente al pasarlas (`F`).

```rust
fn main() { let s = String::from("thm"); tomar(s); }
fn tomar(s: String) {}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Implementa el desafío propuesto en la sala. | `No answer needed` |
| 2 | ¿El ownership puede transferirse entre funciones? (T/F) | `T` |
| 3 | ¿Se puede usar una variable después de mover su ownership? (T/F) | `F` |
| 4 | ¿La referencia a un valor se copia automáticamente al pasarla? (T/F) | `F` |

### Task 10: Rayon - Paralelismo

**Explicación:** `Rayon` añade paralelismo a los iteradores; las dependencias se declaran en `cargo.toml`; la iteración paralela se hace con `a.par_iter()` y las crates se publican en `crates.io`.

```toml
[dependencies]  rayon = "1"
```

```rust
use rayon::prelude::*;
a.par_iter().for_each(|x| println!("{}", x));
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué librería de Rust añade paralelismo a los iteradores? | `Rayon` |
| 2 | ¿En qué archivo del proyecto se declaran las dependencias? | `cargo.toml` |
| 3 | ¿Qué método se utiliza para iterar en paralelo sobre un array "a"? | `a.par_iter()` |
| 4 | ¿Cuál es el registro oficial de librerías de Rust? | `crates.io` |

### Task 11: Desafío

**Explicación:** La premisa de la sala es correcta (`T`): Rust convierte problemas de gestion de memoria en errores en tiempo de compilación.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿La previa de esta sala es correcta? (T/F) | `T` |

### Task 12: Manejo de errores

**Explicación:** Errores recuperables con el enum `Result` (firma `Result<T, E>`), propagación automática con el operador `?` y extracción directa con `unwrap` (que entra en pánico si hay error).

```rust
fn f() -> Result<i32, std::io::Error> { let n = algo()?; Ok(n) }
let v = f().unwrap();
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué enum de Rust se utiliza para manejar errores recuperables? | `Result` |
| 2 | ¿Cuál es la firma de Result con un tipo de valor "T" y un tipo de error "E"? | `Result T, E>` |
| 3 | ¿Qué operador propaga automáticamente los errores de una función? | `?` |
| 4 | ¿Qué método devuelve el valor de un Result o entra en pánico si hay error? | `unwrap` |

### Task 13: Bandera final

**Explicación:** Tras completar los retos del curso se obtiene la bandera final de la sala.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la bandera final de la sala? | `THM{Rust}` |

### Task 14: Conclusión

**Explicación:** Cierre del curso: resumen de lo aprendido (toolchain, Cargo, tipos, ownership, Rayon, Result) y siguientes pasos.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la conclusión de la sala. | `No answer needed` |

---

**Metodología:** Se instala la toolchain con Rustup y se crea el proyecto con `cargo init`, compilando y ejecutando con `cargo run`. A lo largo de los ejercicios se declaran variables y constantes, se manejan los errores del compilador (E0308, "cannot assign twice to immutable variable"), se practican tipos de datos (Signed, u32, i16, &str, String), funciones, bucles (break, loop, iteradores) y el shadowing. Por último se integra la librería Rayon para paralelizar iteradores y se manejan errores con `Result`, el operador `?` y `unwrap`, resolviendo el reto final que entrega la bandera.

**Learning chain:** instalación → creación de proyectos → variables y tipos → funciones y bucles → shadowing → paralelismo con Rayon → manejo de errores → bandera final.

**MITRE ATT&CK:** N/A (sala formativa de programación sin objetivos de ataque)

**Fuente:** [TryHackMe - Learn Rust](https://tryhackme.com/room/rust)