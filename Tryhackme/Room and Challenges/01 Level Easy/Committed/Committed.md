# Committed

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | reto forense (git) | `committed` | https://tryhackme.com/room/committed | 01 Level Easy | TryHackMe | Git forensics / git log / git show / git diff / ramas / commit history / credenciales filtradas | Localizar en el historial de Git la credencial (flag) que un desarrollador filtró por accidente en un repositorio. |

---

**Contexto:** Reto de forensia sobre Git: un desarrollador "filtró por accidente" código sensible (una contraseña/flag hardcodeada) en un repositorio y después intentó borrarla en un commit posterior ("Oops"). Como Git conserva todo el historial, la flag sigue accesible en los commits antiguos y en otras ramas. Hay que inspeccionar el historial, las ramas y los diffs del repositorio en `/home/ubuntu/commited` para recuperarla.

> **ES:** "Oh no, otra vez no": uno de nuestros desarrolladores subió código sensible al repositorio de GitHub sin querer... el problema es que no recordamos qué ni dónde. ¿Puedes localizar lo que se filtró por accidente? Descubre la flag en el repositorio.
> **EN:** "Oh no, not again!": one of our developers accidentally committed some sensitive code to our GitHub repository... the problem is, we don't remember what or where. Can you track down what we accidentally committed? Discover the flag in the repository!

## Solucionario

### Task 1: Descubre la flag en el repositorio / Discover the flag in the repository

**Explicación:** Se descomprime el fichero `commited.zip` y se entra en el repositorio (`/home/ubuntu/commited/commited`). Con `git log --all`, `git branch -a` y `git diff` se revisan todos los commits de ambas ramas (`master` y `dbint`). El commit con mensaje "Oops" (`c56c470...`) muestra cómo se borró la contraseña, pero un commit anterior de la rama `dbint` todavía contiene la flag hardcodeada como contraseña de MySQL en `main.py`. `git show c56c470...` revela el diff donde la flag `flag{a489a9dbf8eb9d37c6e0cc1a92cda17b}` aparece reemplazada por una cadena vacía.

```bash
cd /home/ubuntu/commited && unzip commited.zip
cd commited/commited
git log --all --oneline
git branch -a                       # master y dbint
git checkout dbint
git show c56c470a2a9dfb5cfbd54cd614a9fdb1644412b5
# diff main.py:  password="flag{a489a9dbf8eb9d37c6e0cc1a92cda17b}"  ->  password=""
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Descubre la flag en el repositorio. / Discover the flag in the repository. | `flag{a489a9dbf8eb9d37c6e0cc1a92cda17b}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Descubre la flag en el repositorio. / Discover the flag in the repository. | `flag{a489a9dbf8eb9d37c6e0cc1a92cda17b}` |

---

**Metodología:** Descomprimir el ZIP, identificar el directorio `.git`, inspeccionar el historial con `git log --all`, descubrir la segunda rama con `git branch -a`, revisar los commits con `git show`/`git diff` y localizar el commit donde la flag estaba hardcodeada como contraseña de MySQL en `main.py`.

### Cadena de ataque / Attack Chain

```text
unzip commited.zip -> git log --all -> git branch -a (rama dbint) -> git show c56c470 (commit "Oops") -> diff main.py -> flag hardcodeada
```

**Learning chain:** Git forensics -> commit history -> ramas -> git show/git diff -> credenciales filtradas.

**Lección:** *Git nunca olvida: borrar un secreto en un commit posterior no lo elimina del historial; mientras exista el commit original, la credencial sigue recuperable, por lo que hardcodear credenciales y depender de borrarlas después es una pésima práctica.*

**MITRE ATT&CK:** T1552.001 - Unsecured Credentials (Credentials in Files)

**Fuente:** [TryHackMe - Committed](https://tryhackme.com/room/committed)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.