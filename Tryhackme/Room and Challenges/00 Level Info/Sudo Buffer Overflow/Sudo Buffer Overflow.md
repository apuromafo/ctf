# Sudo Buffer Overflow

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Info | Walkthrough | `sudovulnsbof` | https://tryhackme.com/room/sudovulnsbof | 00 Level Info | TryHackMe | sudo / buffer overflow / escalada de privilegios / Linux | Escalada de privilegios en Linux explotando un buffer overflow en una versión antigua de sudo |

---

**Contexto:** La sala practica la explotación de un buffer overflow en `sudo` como vía de escalada de privilegios local en Linux. Se trabaja sobre una versión vulnerable de la utilidad y, abusando del desbordamiento, se obtiene una shell de root en la máquina, momento en el que se lee la flag.

> **ES:** Se identifican las versiones usadas de sudo y su dependencia, se explota el buffer overflow y se escala a root para capturar la flag.
> **EN:** Identify the sudo versions in use and its dependency, exploit the buffer overflow and escalate to root to capture the flag.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** La tarea presenta la sala y el motivo del reto: explotar un buffer overflow en sudo para escalar privilegios. Solo se despliega la máquina y se lee la información.

```text
1. No answer needed
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Desplegar la máquina y leer la información. / Deploy the machine and read the information. | No answer needed |

### Task 2: Explotación del buffer overflow / Buffer overflow exploitation

**Explicación:** Se comprueba la versión vulnerable de `sudo` y su binario de apoyo, se descarga y compila el exploit de buffer overflow y se ejecuta para obtener una shell de root. La flag se lee una vez escalado.

```text
2. 1. No answer needed
   2. THM{buff3r_0v3rfl0w_rul3s}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Compilar y ejecutar el exploit del buffer overflow. / Compile and run the buffer overflow exploit. | No answer needed |
| 2 | ¿Cuál es la flag de la sala? / What is the room flag? | `THM{buff3r_0v3rfl0w_rul3s}` |

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Desplegar la máquina y leer la información. / Deploy the machine and read the information. | No answer needed |
| 2 | Compilar y ejecutar el exploit del buffer overflow. / Compile and run the buffer overflow exploit. | No answer needed |
| 3 | ¿Cuál es la flag de la sala? / What is the room flag? | `THM{buff3r_0v3rfl0w_rul3s}` |

---

**Metodología:** Desplegar la máquina, confirmar la versión de sudo vulnerable y su biblioteca asociada, compilar y ejecutar el exploit de buffer overflow para corromper la pila y, al escalar a root, leer la flag.

### Cadena de ataque / Attack Chain

```text
Acceso a la máquina -> sudo vulnerable -> compilar exploit buffer overflow -> ejecutar exploit -> corrupción de pila -> shell root -> cat flag -> THM{buff3r_0v3rfl0w_rul3s}
```

**Learning chain:** Linux -> sudo -> buffer overflow -> pila -> escalada de privilegios local -> root -> flag

**Lección:** *Un buffer overflow en un binario con privilegios como sudo convierte un defecto de memoria en acceso root; verificar y actualizar sudo, además de mitigaciones de pila, es la defensa principal frente a estas vulnerabilidades.*

**MITRE ATT&CK:** T1068 (Exploitation for Privilege Escalation), T1059.004 (Unix Shell)

**Fuente:** [TryHackMe - Sudo Buffer Overflow](https://tryhackme.com/room/sudovulnsbof)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.