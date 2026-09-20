# Dodge

| **Dificultad** | Medium |
| **Tipo** | CTF |
| **Slug** | `dodge` |
| **Link** | [TryHackMe](https://tryhackme.com/room/dodge) |
| **Sección** | 02 Level Medium |
| **Fuente** | thmrevenant (GitHub) |
| **Componentes** | Enumeración / Linux / explotación / escalada de privilegios / flags |
| **Impacto** | Compromiso completo de la máquina Dodge: enumeración, acceso inicial, escalada de privilegios y captura de dos flags |

---

**Contexto:** Dodge es una sala CTF de nivel medio centrada en el compromiso completo de una máquina. El flujo de resolución pasa por la enumeración de servicios, la explotación de una vulnerabilidad para lograr el acceso inicial, la escalada de privilegios hasta el máximo nivel y la captura de las flags que acreditan cada fase. Las respuestas documentadas son las dos flags finales del reto.

## Solucionario

### Task 1: Flags del reto

**Explicación:** Al completar la explotación y la escalada de privilegios se obtienen las dos flags del reto: la primera **THM{0649b2285e507b38b10620e57f9c8610}** y la segunda **THM{7b88ac4f52cd8723a8d0c632c2d930ba}**, asociadas a las etapas de acceso y compromiso total.

1. THM{0649b2285e507b38b10620e57f9c8610}
2. THM{7b88ac4f52cd8723a8d0c632c2d930ba}

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la primera flag del reto? | `THM{0649b2285e507b38b10620e57f9c8610}` |
| 2 | ¿Cuál es la segunda flag del reto? | `THM{7b88ac4f52cd8723a8d0c632c2d930ba}` |

---

**Metodología:**

1. Enumerar la máquina: nmap para descubrir los servicios abiertos y las versiones.
2. Enumerar la aplicación o servicio vulnerable y buscar un vector de explotación.
3. Obtener el acceso inicial (shell) sobre la máquina.
4. Escalar privilegios mediante técnicas de escalada en Linux.
5. Capturar las dos flags una vez se alcanzan los niveles requeridos.

**Learning chain:** Reconocimiento -> Enumeración de servicios -> Explotación -> Acceso inicial -> Escalada de privilegios -> Flag 2 -> Flag 1

**Lección:** *Un CTF de compromiso completo se resuelve encadenando enumeración, explotación y escalada: cada flag valida una etapa del proceso.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1068 (Exploitation for Privilege Escalation)

**Fuente:** [TryHackMe - Dodge](https://tryhackme.com/room/dodge)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.