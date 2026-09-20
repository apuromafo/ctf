# Phantom Fob

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Medium | challenge | `phantomfob` | [TryHackMe](https://tryhackme.com/room/phantomfob) | 02 Level Medium | TryHackMe | CAN bus, key fob, rolling codes, signal forging | Comprensión y ejecución de un ataque a un key fob de coche sobre el CAN bus con códigos rotativos |

---

**Contexto:** Los coches modernos utilizan una red interna llamada CAN Bus en la que cada componente, desde las puertas hasta el tablero y el motor, se comunica emitiendo pequeños mensajes al cable compartido. En esta sala estás conectado al CAN bus de un vehículo de demostración y dispones de un key fob capaz de Bloquear (Lock) el coche y activar la bocina (Horn), pero sin botón de Desbloqueo (Unlock). El fabricante afirma que el comando de desbloqueo "no puede copiarse". El reto consiste en observar los mensajes del vehículo, deducir cómo se construyen los comandos de puertas y fabricar (forge) el mensaje de Unlock.

## Solucionario

### Task 1: Set up your virtual environment / Configura tu entorno virtual

**Explicación:** Para resolver la sala se inician la AttackBox y la Lab Machine y se conecta la máquina de laboratorio del vehículo. A continuación se capturan los mensajes que circulan por el CAN bus mientras se interactúa con el key fob: se emiten los comandos Lock y Horn y se observa la trama asociada a cada pulsación. Al analizar la estructura de las tramas se identifica un campo de comando acompañado de un contador o código rotatorio (rolling code) que cambia en cada segundo, de modo que un simple replay de una trama capturada no sería válido. Para conseguir la flag se forja el comando Unlock imitando la estructura del comando Lock ya capturado, se ajusta el campo correspondiente y se inyecta la trama forjada en el bus, desbloqueando el vehículo.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag? | `THM{C4r_H4cking_is_kind4_c00l}` |

---

**Metodología:** El procedimiento seguido es: (1) preparar el entorno con la AttackBox y la Lab Machine; (2) realizar sniffing del tráfico CAN mientras se pulsan Lock y Horn con el fob; (3) estudiar el formato de la trama, distinguiendo el campo de comando del código rotatorio (rolling code); (4) verificar que el código cambia cada segundo, lo que invalida el replay; (5) forjar el mensaje de Unlock reutilizando la estructura observada; y (6) enviar la trama forjada al CAN bus para desbloquear el coche y obtener la flag. La descripción pública de la sala resume la idea: "The fob locks but won't unlock. Codes change every second, forge the signal; don't replay it."

### Cadena de ataque / Attack Chain

```text
[ Preparación ] -> Iniciar AttackBox, arrancar la Lab Machine y conectarse al CAN bus
        |
        v
[ Reconocimiento ] -> Sniffing del tráfico CAN mientras se pulsa Lock / Horn con el fob
        |
        v
[ Análisis ] -> Identificar en la trama el campo de comando y el código rotatorio
        |
        v
[ Observación ] -> El código cambia cada segundo: el replay de una trama capturada es inválido
        |
        v
[ Forja ] -> Construir el comando Unlock imitando la estructura del comando Lock
        |
        v
[ Ejecución ] -> Inyectar la trama forjada en el CAN bus -> Vehículo desbloqueado -> FLAG
```

**Learning chain:** CAN Bus (arbitraje y tramas) -> sniffing -> rolling codes (códigos rotativos) -> replay vs forge -> inyección de comandos en la red del vehículo.

**Lección:** *No basta con copiar (replay) la señal de un key fob moderno: los códigos rotativos obligan al atacante a comprender el protocolo y a forjar tramas válidas. La defensa del vehículo depende de autenticar y cifrar los mensajes, no solo de ocultar su formato.*

**MITRE ATT&CK:** La técnica T1204 (User Execution) no aplica en esta sala. El enfoque se centra en T1059 (Command and Scripting Interpreter) y T1040 (Network Sniffing); desde el punto de vista defensivo, la prioridad es endurecer el ecosistema automotriz (CAN bus autenticado, filtrado y validación de tramas, y auditoría de señales).

**Fuente:** [TryHackMe - Phantom Fob](https://tryhackme.com/room/phantomfob)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
