# Linux Backdoors

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `linuxbackdoors` | [TryHackMe](https://tryhackme.com/room/linuxbackdoors) | 01 Level Easy | TryHackMe | Persistencia, backdoors, cron, ssh, técnicas ofensivas | Conocer y crear backdoors en Linux: SSH (claves y `-i`), tareas cron y otras técnicas de persistencia. |

---

**Contexto:** La sala "Linux Backdoors" (módulo de técnica/pentesting) enseña a dejar persistencia en un sistema Linux tras obtener acceso. Se cubren las principales técnicas: backdoors a través de SSH (añadir la clave pública del atacante a `.ssh` y conectarse usando `-i` con la clave privada), programación de tareas cron (con periodos de `minute` y `hour`) y otras variantes de backdoors que se comprueban con pregunta/respuesta a lo largo de la sala.

> **ES:** Técnicas de persistencia/backdoors en Linux: claves SSH en `.ssh`, conexión con `-i`, tareas cron cada `minute`/`hour` y comprobación de otras técnicas.
> **EN:** Linux persistence/backdoor techniques: SSH keys in `.ssh`, connecting with `-i`, cron jobs every `minute`/`hour`, and verification of other techniques.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:** Introducción a la persistencia con backdoors. No requiere respuesta.

```text
1. No answer needed
```

### Task 2: Backdoor SSH / SSH backdoor
**Explicación:** Se configura el backdoor SSH: el atacante añade su clave pública al directorio del usuario (`/home/*/.ssh`) y después se conecta usando el parámetro `-i` para indicar la clave privada.

```text
2. 1. .ssh
   2. -i
```

### Task 3: Comprobación del backdoor SSH / SSH backdoor check
**Explicación:** Se verifica el backdoor SSH. No requiere respuesta.

```text
3. No answer needed
```

### Task 4: Tareas cron / Cron jobs
**Explicación:** Se deja un backdoor mediante tareas cron; las unidades de tiempo empleadas son el `minute` y la `hour`.

```text
4. 1. minute
   2. hour
```

### Task 5: Práctica de cron / Cron practice
**Explicación:** Ejercicio práctico sobre las tareas cron. No requiere respuesta.

```text
5. No answer needed
```

### Task 6: Cierre / Wrap-up
**Explicación:** Tareas finales de cierre. No requieren respuesta.

```text
6. 1. No answer needed
   2. No answer needed
```

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Introducción | `No answer needed` |
| 2 | Directorio donde se deposita la clave SSH | `.ssh` |
| 2 | Flag de conexión SSH con clave privada | `-i` |
| 3 | Comprobación del backdoor SSH | `No answer needed` |
| 4 | Unidad de tiempo cron de menor tamaño | `minute` |
| 4 | Unidad de tiempo cron de mayor tamaño | `hour` |
| 5 | Práctica de cron | `No answer needed` |
| 6 | Cierre (1) | `No answer needed` |
| 6 | Cierre (2) | `No answer needed` |

---

**Metodología:** La práctica consistió en preparar la persistencia de un sistema Linux: se generó un par de claves, se colocó la pública en el `.ssh` del usuario objetivo y se comprobó la conexión remota con el parámetro `-i`. Después se configuraron tareas cron en distintos intervalos (minuto y hora) para mantener un re-conexión periódica, y se cerró revisando el resto de técnicas de backdoors.

### Cadena de ataque / Attack Chain

```text
Acceso inicial -> generar par de claves -> key log-ita en .ssh -> conexión SSH con -i -> persistencia vía cron (minute/hour) -> acceso mantenido
```

**Learning chain:** initial access -> keygen -> public key in .ssh -> ssh -i -> cron persistence -> maintained access

**Lección:** *La persistencia en Linux suele ser trivial si se tiene acceso de escritura al `.ssh` del usuario o a las tareas cron; detectarla requiere revisar claves autorizadas y los cron jobs sospechosos.*

**MITRE ATT&CK:** T1098 (Account Manipulation: SSH Authorized Keys), T1053.003 (Scheduled Task/Job: Cron), T1021.004 (Remote Services: SSH)

**Fuente:** [TryHackMe - Linux Backdoors](https://tryhackme.com/room/linuxbackdoors)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.