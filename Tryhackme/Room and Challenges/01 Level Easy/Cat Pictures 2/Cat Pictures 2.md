# Cat Pictures 2

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | ctf | `catpictures2` | [TryHackMe](https://tryhackme.com/room/catpictures2) | 01 Level Easy | THM | Lychee, nginx, Gitea, Ansible, EXIF/metadatos, CVE-2021-3156 | Medio |

---

**Contexto:** Secuela de la room "Cat Pictures". La máquina expone una galería Lychee en el puerto 80, nginx en el 8080, Gitea en el 3000, un runner de Ansible en el 1337 y SSH en 22/222. Los metadatos EXIF de una imagen desvelan la ruta a un archivo oculto en nginx con las credenciales de Gitea. En el repositorio Ansible está el Flag 1 y un playbook editable que se ejecuta como bismuth, con el que se lee el Flag 2 y se sustrae la clave privada SSH. El acceso por SSH permitirá escalar a root con CVE-2021-3156 (Baron Samedit) para leer el Flag 3.

> **ES:** Box CTF: extracción de metadatos EXIF → credenciales de Gitea → Flag 1 → inyección de comandos en un playbook de Ansible ejecutado como bismuth → Flag 2 y clave SSH → escalada a root mediante CVE-2021-3156 (Baron Samedit) → Flag 3.

> **EN:** CTF box: EXIF metadata extraction → Gitea credentials → Flag 1 → command injection in an Ansible playbook run as bismuth → Flag 2 and SSH key → privilege escalation to root via CVE-2021-3156 (Baron Samedit) → Flag 3.

## Solucionario

### Task 1: Deploy the VM! / Desplegar la VM!

**Explicación:** Iniciar la máquina y esperar unos minutos a que terminen de arrancar todos los servicios antes de atacarla.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | I have deployed the VM. | `No answer needed` |

### Task 2: Flags! / Flags

**Explicación:** Todas las imágenes del álbum Lychee se descargan y se revisan con exiftool; los metadatos de una de las fotos apuntan a `:8080/764efa883dda1e11db47671c4a3bbd9e.txt`, un archivo en nginx con las credenciales de Gitea (samarium). En el repositorio "ansible" de Gitea está el Flag 1 y un playbook.yaml con `shell: whoami` que el runner de Ansible del puerto 1337 ejecuta como bismuth; editando el comando se lee flag2.txt y después /home/bismuth/.ssh/id_rsa. Con la clave privada se entra por SSH como bismuth y, tras confirmar la versión vulnerable de sudo, se compila CVE-2021-3156 para obtener root y leer /root/flag3.txt.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | What is Flag 1? | `10d916eaea54bb5ebe36b59538146bb5` |
| 2 | What is Flag 2? | `5e2cafbbf180351702651c09cd797920` |
| 3 | What is Flag 3? | `6d2a9f8f8174e86e27d565087a28a971` |

---

**Metodología:** nmap → descarga de las imágenes de la galería Lychee → exiftool → archivo oculto en nginx (8080) → credenciales Gitea → login en Gitea (3000) → Flag 1 → edición del playbook (whoami → ls/cat) → ejecución en el runner de Ansible (1337) → Flag 2 → robo de id_rsa → SSH bismuth → linpeas → sudo vulnerable (1.8.21p2) → compilación de CVE-2021-3156 → root → Flag 3.

### Cadena de ataque / Attack Chain

Reconocimiento → metadatos EXIF → credenciales Gitea → Flag 1 → inyección en el playbook de Ansible → Flag 2 + clave SSH → SSH bismuth → CVE-2021-3156 (Baron Samedit) → root → Flag 3.

**Learning chain:** Enumeración de servicios → extracción de metadatos → acceso a Gitea → abuso de playbooks de Ansible (RCE) → sustracción de credenciales → SSH → vulnerabilidades de sudo → escalada a root.

**Lección:** *Los metadatos de imagen, los playbooks de automatización con comandos editables y un sudo sin parchear son tres eslabones que, encadenados, convierten una galería de gatos en una root shell: la oscuridad no es seguridad y el patch management importa.*

**MITRE ATT&CK:** T1078 (Valid Accounts), T1059 (Command and Scripting Interpreter), T1068 (Exploitation for Privilege Escalation).

**Fuente:** [TryHackMe - Cat Pictures 2](https://tryhackme.com/room/catpictures2)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.