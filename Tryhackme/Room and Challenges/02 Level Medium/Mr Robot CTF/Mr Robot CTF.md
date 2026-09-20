# Mr Robot CTF

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF / Web | mrrobotctf | https://tryhackme.com/room/mrrobotctf | 02 Level Medium | TryHackMe | WordPress, robots.txt, dictionary attack, Hydra, SUID | Compromiso total inspirado en la serie Mr. Robot (3 keys) |

---

**Contexto:** La sala **Mr Robot CTF** está inspirada en la serie *Mr. Robot* y de la estética de *fsociety*. El reto obliga a enumerar el sitio web (robots.txt, WordPress), atacar el panel de login y encontrar las tres *keys* (`key-1-of-3`, `key-2-of-3`, `key-3-of-3`) escondidas en la máquina. Como respuesta hay que entregar el **hash MD5** de cada key recuperada. La cadena típica combina fuerza bruta de contraseña, acceso a WordPress y escalada de privilegios por capacidad/técnicas locales.

## Solucionario

### Task 1: Investigación y fase inicial
**Explicación:**

Enumeración inicial del objetivo: `robots.txt` revela el diccionario de contraseñas y los primeros ficheros, y el sitio corre bajo **WordPress**. Los apartados 1 a 4 cubren la investigación y el arranque del CTF (no requieren una respuesta concreta).

1. `No answer needed`
2. `No answer needed`
3. `No answer needed`
4. `No answer needed`

### Task 2: Keys del CTF
**Explicación:**

Recuperadas las tres *keys* de la máquina (con el diccionario de `robots.txt` para entrar en WordPress mediante fuerza bruta y escalando después por binarios SUID/capacidades como `nmap`), se devuelve el **hash MD5** de cada una:

1. `073403c8a58a1f80d943455fb30724b9`
2. `822c73956184f694993bede3eb39f959`
3. `04787ddef27c3dee1ee161b21670b4e4`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1.1 | Fase inicial de investigación | `No answer needed` |
| 1.2 | Segunda fase de investigación | `No answer needed` |
| 1.3 | Tercera fase de investigación | `No answer needed` |
| 1.4 | Cuarta fase de investigación | `No answer needed` |
| 2.1 | MD5 de la key 1-of-3 | `073403c8a58a1f80d943455fb30724b9` |
| 2.2 | MD5 de la key 2-of-3 | `822c73956184f694993bede3eb39f959` |
| 2.3 | MD5 de la key 3-of-3 | `04787ddef27c3dee1ee161b21670b4e4` |

---

**Metodología:** Enumeración web (robots.txt, WordPress) → fuerza bruta de login → consola de WordPress → RCE → escalada de privilegios vía SUID → recuperación de las 3 keys y cálculo de sus MD5.

**Learning chain:** Reconocimiento → diccionario en robots.txt → ataque al login WordPress → shell → escalada → key-1/2/3 → hashes MD5.

**Lección:** *Una útima 'robots.txt' puede arruinar un sitio: contiene diccionarios y rutas que encadenan el ataque hasta el compromiso total; entrega siempre el hash pedido, no la flag en claro.*

**MITRE ATT&CK:** T1110 Brute Force · T1505.003 Web Shell · T1548.001 Abuse Elevation Control Mechanism: Setuid and Setgid.

**Fuente:** [TryHackMe - Mr Robot CTF](https://tryhackme.com/room/mrrobotctf)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.