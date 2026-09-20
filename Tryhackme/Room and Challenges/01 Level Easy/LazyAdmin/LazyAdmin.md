# LazyAdmin

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | challenge | `lazyadmin` | [TryHackMe](https://tryhackme.com/room/lazyadmin) | 01 Level Easy | TryHackMe | SweetRice CMS, fuerza bruta, credenciales, escalada de privilegios, script en /usr/bin | Compromiso de una caja Linux a través del CMS SweetRice, recuperación de credenciales y escalada a root mediante sudo. |

---

**Contexto:** LazyAdmin es una máquina Linux (nivel easy/fácil) que expone un servidor web con el CMS SweetRice. La idea es enumerar la web, descubrir una copia de seguridad de la base de datos que contiene credenciales, romper el hash de la contraseña del administrador, entrar en el panel de administración de SweetRice y explotar una vulnerabilidad para obtener una shell. La escalada a root se hace aprovechando un script con permisos sudo (`/usr/bin/backup.pl`), que ejecuta un script propio sin usar rutas absolutas.

> **ES:** Caja CTF "LazyAdmin": enumeración web -> CMS SweetRice -> dump de my.cnf -> hash de admin crackeado -> login en panel -> shell www-data -> sudo backup.pl -> root. Flags de usuario y de root recuperadas.
> **EN:** "LazyAdmin" CTF box: web enumeration -> SweetRice CMS -> my.cnf dump -> cracked admin hash -> admin panel login -> www-data shell -> sudo backup.pl -> root. User and root flags recovered.

## Solucionario

### Task 1: Flags / Flags
**Explicación:** Con los exploits de SweetRice se obtiene acceso como `www-data` en la máquina, se lee el `user.txt` del usuario y mediante el abuso del script `/usr/bin/backup.pl` con sudo se eleva a root y se lee el `root.txt`. Las flags son `THM{63e5bce9271952aad1113b6f1ac28a07}` y `THM{6637f41d0177b6f37cb20d775124699f}`.

```text
1. 1. THM{63e5bce9271952aad1113b6f1ac28a07}
   2. THM{6637f41d0177b6f37cb20d775124699f}
```

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | User flag | `THM{63e5bce9271952aad1113b6f1ac28a07}` |
| 1 | Root flag | `THM{6637f41d0177b6f37cb20d775124699f}` |

---

**Metodología:** La caja se resolvió enumerando el sitio web y encontrando una copia de seguridad del CMS SweetRice. La base de datos incluía las credenciales del administrador con un hash que se pudo romper. Con esas credenciales se accedió al panel de administración y, explotando la funcionalidad del CMS, se obtuvo una shell como `www-data`. Para la escalada se aprovechó que el usuario podía ejecutar `/usr/bin/backup.pl` con sudo: el script hacía referencia a su ejecutable sin ruta absoluta, por lo que se sustituyó con un script malicioso a través de un directorio controlado y se obtuvo una shell interactiva como root.

### Cadena de ataque / Attack Chain

```text
Enumeración web -> SweetRice CMS -> copia de seguridad de MySQL -> hash del admin -> crack del hash -> login en el panel -> explotación de SweetRice -> shell www-data -> sudo /usr/bin/backup.pl -> script malicioso -> shell root -> user.txt -> root.txt
```

**Learning chain:** web enumeration -> CMS fingerprinting -> credential dump -> hash cracking -> admin panel access -> RCE -> www-data shell -> sudo misconfiguration (backup.pl) -> PATH/relative path abuse -> root shell -> user/root flags

**Lección:** *Las copias de seguridad y los dangling file permissions son vectores habituales de credenciales filtradas; y un script con sudo que depende de la variable PATH permite suplantar el binario y escalar privilegios.*

**MITRE ATT&CK:** T1078 (Valid Accounts), T1552 (Unsecured Credentials), T1110 (Brute Force), T1059.004 (Command and Scripting Interpreter: Unix Shell), T1068 (Exploitation for Privilege Escalation), T1574.007 (Dynamic Linker Hijacking: PATH)

**Fuente:** [TryHackMe - LazyAdmin](https://tryhackme.com/room/lazyadmin)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.