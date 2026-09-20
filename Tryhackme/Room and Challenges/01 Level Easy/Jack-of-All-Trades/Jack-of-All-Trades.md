# Jack-of-All-Trades

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | challenge (boot2root) | `jackofalltrades` | [TryHackMe](https://tryhackme.com/room/jackofalltrades) | 01 Level Easy | TryHackMe | boot2root, CTF, enumeración web, esteganografía, escalada de privilegios, Securi-Tay 2020 | Resolver la máquina de extremo a extremo (boot-to-root) combinando enumeración web, artefactos ocultos y escalada de privilegios. |

---

**Contexto:** Desafío boot-to-root diseñado originalmente para la conferencia Securi-Tay 2020 (Boot-to-root originally designed for Securi-Tay 2020). La narrativa del reto presenta a Jack, un hombre de muchos talentos contratado por el zoo para capturar a los pingüinos; la máquina exige ver a través de su fachada de anciano juguetero olvidadizo y derribar al lunático. El resumen original comenzaba con la URL de la sala (https://tryhackme.com/room/jackofalltrades) y contenía la historia de Task 1 con sus dos flags.

> **ES:** Explotar la máquina del zoo: encontrar la entrada oculta tras la fachada de Jack, obtener el User Flag y escalar privilegios hasta el Root Flag para capturar al lunático.
> **EN:** Exploit the zoo box: find the hidden way in behind Jack's facade, obtain the User Flag and escalate privileges to the Root Flag to stop the lunatic.

## Solucionario

### Task 1: Flags

**Explicación:** Se presenta la historia del desafío tal y como aparece en el enunciado original: Jack, el hombre de los muchos talentos, ha sido contratado por el zoo para capturar a los pingüinos por su experiencia domando pingüinos, pero no todo es lo que parece. Hay que ver a través de su fachada de anciano juguetero olvidadizo y derribar a este lunático. El reto pide responder las preguntas de abajo ("Answer the questions below") para obtener el User Flag y el Root Flag.

> Jack is a man of a great many talents. The zoo has employed him to capture the penguins due to his years of penguin-wrangling experience, but all is not as it seems... We must stop him! Can you see through his facade of a forgetful old toymaker and bring this lunatic down?

> Answer the questions below

> User Flag

> Root Flag

1. securi-tay2020_{p3ngu1n-hunt3r-3xtr40rd1n41r3}
2. securi-tay2020_{6f125d32f38fb8ff9e720d2dbce2210a}

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | User Flag | `securi-tay2020_{p3ngu1n-hunt3r-3xtr40rd1n41r3}` |
| 2 | Root Flag | `securi-tay2020_{6f125d32f38fb8ff9e720d2dbce2210a}` |

---

**Metodología:** Enumerar la máquina para descubrir el punto de entrada oculto, seguir las pistas de la fachada del anciano juguetero, obtener el User Flag y escalar privilegios hasta conseguir el Root Flag, completando el desafío boot-to-root diseñado para Securi-Tay 2020.

### Cadena de ataque / Attack Chain

```text
reconocimiento inicial -> descubrimiento de la entrada oculta -> User Flag (securi-tay2020_{p3ngu1n-hunt3r-3xtr40rd1n41r3}) -> escalada de privilegios -> Root Flag (securi-tay2020_{6f125d32f38fb8ff9e720d2dbce2210a})
```

**Learning chain:** CTF boot2root -> enumeración -> explotación web -> User Flag -> escalada de privilegios -> Root Flag.

**Lección:** *En un boot-to-root cada pista cuenta: la aparente fachada del objetivo guarda el acceso inicial, y combinar enumeración, explotación y escalada de privilegios permite encadenar el camino hasta el root.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1059 (Command and Scripting Interpreter), T1003 (OS Credential Dumping), T1036 (Masquerading)

**Fuente:** [TryHackMe - Jack-of-All-Trades](https://tryhackme.com/room/jackofalltrades)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.