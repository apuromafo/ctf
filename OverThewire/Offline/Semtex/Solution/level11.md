# Semtex Nivel 11 - 12

| Campo | Valor |
|-------|-------|
| **Juego / Game** | Semtex (offline) |
| **Nivel / Level** | 11 - 12 |
| **URL** | https://overthewire.org/wargames/semtex/ |

Semtex Level 11 → Level 12
Authentication Daemon
There is an authentication daemon waiting on brebera port 24012. You connect to it, supply your password and get authenticated. The semtex 12 password will give you user access, the admin password will give you administrator access…

After authentication you connect to the remote file system reader on port 24013. Depending on your access level you can list files and show them. The semtex 13 password has been located in one of the files on this remote file system. Brebera is fast, can you be faster?

Thanks to bk for this level!

Included file: semtex12.authd.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <time.h>
#include <signal.h>
#include <wait.h>


#include "server.h"
#include "sem.h"

#define PATH "/path"
#define SHM_SIZE 4096
#define SHM_KEY 0xbadc0ded
#define AUTH_PORT 24012
#define BUFSIZE 512

int new_connection(unsigned int addr, int pass, struct sharea* auth_array);
int daemonize();

int main(int argc, char **argv)
{
        if(argc > 1) {
                if((argv[1][0] == 'D')) {
                        if((daemonize()) == -1)
                                exit(EXIT_FAILURE);
                }
        }
        
        int                     fd, sockfd, connfd;
        unsigned int            sin_size;
        struct sockaddr_in      my_addr, remote_addr;
        struct sigaction        reap_zombies;

        key_t           key = SHM_KEY;
        int             shmid;
        struct sharea   *auth_array;

        char            sendbuf[BUFSIZE], recvbuf[BUFSIZE], super_pass[BUFSIZE];        

        fd = open(PATH, O_RDONLY);
        if(fd < 0) {
                perror("open");
                exit(EXIT_FAILURE);
        }

        if((read(fd, super_pass, BUFSIZE)) < 0) {
                perror("pass");
                exit(EXIT_FAILURE);
        }
        close(fd);

        /*Set up the shared memory authorization array */

        if((shmid = shmget(key, SHM_SIZE, IPC_CREAT | 0666)) == -1) {
                perror("Shared");
                exit(1);
        }
        
        if((auth_array = shmat(shmid, NULL, 0)) == (void *)-1) {
                perror("Share attach");
                exit(1);
        }

        memset(auth_array, 0, sizeof(*auth_array));
        
        memset(&reap_zombies, 0, sizeof(reap_zombies));
        reap_zombies.sa_flags = SA_NOCLDWAIT;

        if((sigaction(SIGCHLD, &reap_zombies, 0)) == -1) {
                perror("Sighandler");
                exit(1);
        }
        
        /* Lets set up the listening socket */

        if((sockfd = socket(PF_INET, SOCK_STREAM, 0)) == -1) {
                perror("Socket");
                exit(1);
        }
        my_addr.sin_family = AF_INET;
        my_addr.sin_port = htons(AUTH_PORT);
        my_addr.sin_addr.s_addr = htonl(INADDR_ANY);
        memset(&(my_addr.sin_zero), '\0', 8);

        if((bind(sockfd, (struct sockaddr *)&my_addr, sizeof(struct sockaddr))) == -1) {
                perror("Bind");
                exit(1);
        }

        
        listen(sockfd, 5);      /* Error checks... nah! */
        
        while(1) {

                pid_t   pid;
                
                sin_size = sizeof(struct sockaddr_in);
                if((connfd = accept(sockfd, (struct sockaddr*)&remote_addr, &sin_size)) == -1) {
                        perror("Accept");
                        exit(1);
                }
                
                pid = fork();
                if(pid < 0) {
                        perror("fork");
                        exit(EXIT_FAILURE);
                }
                if(pid > 0) {
                        close(connfd);
                        continue;
                }               
                
                strcpy(sendbuf, "Authd login - Send Pass");
                send(connfd, sendbuf, strlen(sendbuf), 0);
                recv(connfd, recvbuf, BUFSIZE - 1, 0);
                recvbuf[BUFSIZE - 1] = '\0';
                
                if(!new_connection(remote_addr.sin_addr.s_addr, strcmp(recvbuf, super_pass), auth_array)) {
                        strcpy(sendbuf, "Failed - try again later");
                        send(connfd, sendbuf, strlen(sendbuf), 0);
                }
                close(connfd);
                exit(EXIT_SUCCESS);
        }
}

int new_connection(unsigned int addr, int super, struct sharea *auth_array)
{
        int i, found = 0;

        /* Insert new entry with correct perms */
        
        down(&auth_array->sem);
        for(i = 0; i < 32; i++) {
                if(auth_array->list[i].token == 0) {
                        found++;
                        auth_array->list[i].token = addr;
                        auth_array->list[i].timestamp = time(NULL);
                        if(super)
                                auth_array->list[i].perms = 1;  /* 1 = ordinary user */
                        break;
                }
                                                
        }
        up(&auth_array->sem);

        /* Expire old connections */
        down(&auth_array->sem);
        for(i = 0; i < 32; i++) {
                if((auth_array->list[i].timestamp + 300) < time(NULL)) 
                        memset(&auth_array->list[i], 0, sizeof(struct auth));
        }
        up(&auth_array->sem);
        
        return found;
}
Included file: semtex12.daemon.c
#include <sys/types.h>
#include <sys/stat.h>
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <errno.h>
#define _GNU_SOURCE
#include <unistd.h>


#define TARGET_UID 1998

int daemonize()
{
        int ret = -1;

        if((daemon(0, 0)) == -1)
                return ret;

        if((setresgid(TARGET_UID, TARGET_UID, TARGET_UID)) == -1)
                return ret;
        if((setresuid(TARGET_UID, TARGET_UID, TARGET_UID)) == -1)
                return ret;

        ret = 0;

        return ret;
        
}
Included file: semtex12.reader.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <dirent.h>
#include <unistd.h>
#include <signal.h>
#include <wait.h>


#include "server.h"
#include "sem.h"

#define PATH "/path"
#define SHM_SIZE 4096
#define SHM_KEY 0xbadc0ded
#define AUTH_PORT 24013
#define BUFSIZE 512

int daemonize();

void list_dir(int fd)
{
        DIR             *dirp;
        struct dirent   *dp;
                
        if((dirp = opendir(PATH)) == NULL)
                        return;
        while((dp = readdir(dirp)) != NULL) {
                send(fd, dp->d_name, strlen(dp->d_name), 0);
        }
        return;
}

void filedump(const char *name, int fd)
{
        FILE            *filp;
        char            buf[2048];
        int             ret;
        
        chdir(PATH);
        if((filp = fopen(name, "rb")) == NULL) {
                strcpy(buf, "File not found.");
                send(fd, buf, strlen(buf), 0);
                return;
        }
        do {
                ret = fread(buf, 1, 2048, filp);
                if(ret > 0)
                        send(fd, buf, ret, 0);
                        send(fd, "\n", 1, 0);
        } while(ret >= 2048);
}

int main(int argc, char **argv)
{

        if(argc > 1) {
                if(argv[1][0] == 'D') {
                        if(daemonize())
                                exit(EXIT_SUCCESS);
                }
        }
        
        int                     sockfd, connfd;
        unsigned int            sin_size;
        struct sockaddr_in      my_addr, remote_addr;

        key_t           key = SHM_KEY;
        int             shmid;
        struct sharea   *auth_array;
        struct sigaction        reap_zombies;
        
        char            sendbuf[BUFSIZE], recvbuf[BUFSIZE], filename[BUFSIZE];

        /*Set up the shared memory authorization array */

        if((shmid = shmget(key, SHM_SIZE, IPC_CREAT | 0666)) == -1) {
                perror("Shared");
                exit(1);
        }

        if((auth_array = shmat(shmid, NULL, 0)) == (void *)-1) {
                perror("Share attach");
                exit(1);
        }

        /* Lets set up the listening socket */

        memset(&reap_zombies, 0, sizeof(reap_zombies));
        reap_zombies.sa_flags = SA_NOCLDWAIT;

        if((sigaction(SIGCHLD, &reap_zombies, 0)) == -1) {
                perror("Sighandler");
                exit(1);
        }

        if((sockfd = socket(PF_INET, SOCK_STREAM, 0)) == -1) {
                perror("Socket");
                exit(1);
        }
        my_addr.sin_family = AF_INET;
        my_addr.sin_port = htons(AUTH_PORT);
        my_addr.sin_addr.s_addr = htonl(INADDR_ANY);
        memset(&(my_addr.sin_zero), '\0', 8);

        if((bind(sockfd, (struct sockaddr *)&my_addr, sizeof(struct sockaddr))) == -1) {
                perror("Bind");
                exit(1);
        }

        listen(sockfd, 5);      /* Error checks... nah! */
        
        while(1) {

                int i, len, pid, found = 0;

                sin_size = sizeof(struct sockaddr_in);
                if((connfd = accept(sockfd, (struct sockaddr*)&remote_addr, &sin_size)) == -1) {
                        perror("Accept");
                        exit(1);
                }
                
                if((pid = fork()) < 0) {
                        perror("fork");
                        exit(EXIT_FAILURE);
                }
                if(pid) {
                        close(connfd);
                        continue;
                }
                
                strcpy(sendbuf, "File Transfer: Enter 'l' for list or type a filename:");
                send(connfd, sendbuf, strlen(sendbuf), 0);
                len = recv(connfd, recvbuf, BUFSIZE - 1, 0);
                
                if(len <= 0)
                        break;
                
                strncpy(filename, recvbuf, len < BUFSIZE ? len : BUFSIZE);
                filename[BUFSIZE - 1] = '\0';

                down(&auth_array->sem); /* Take semaphore for reading auth list */
                for(i = 0; i < 32; i++) {
                        if(auth_array->list[i].token == remote_addr.sin_addr.s_addr) {
                                found++;
                                break;
                        }
                }
                up(&auth_array->sem); /* Release semaphore to wait on user replies next... avoid deadlock */

                if(!found) {
                        strcpy(sendbuf, "Not recognized, use authd first.");
                        send(connfd, sendbuf, strlen(sendbuf), 0);
                        close(connfd);
                        continue;
                }
                
                if(filename[0] == 'l') {
                        list_dir(connfd);
                }
                else {
                        strcpy(sendbuf, "Display file? (y/n)");
                        /*check perm and display file*/
                        
                        send(connfd, sendbuf, strlen(sendbuf), 0);
                        recv(connfd, recvbuf, BUFSIZE - 1, 0);
                        recvbuf[BUFSIZE - 1] = '\0';
                        
                        if(recvbuf[0] == 'y') {
                                down(&auth_array->sem);
                                if(auth_array->list[i].perms == 0) {/* 0 is superuser, 1 is user */
                                        filedump(filename, connfd);
                                }
                                else {
                                        strcpy(sendbuf, "Not Authorized");
                                        send(connfd, sendbuf, strlen(sendbuf), 0);
                                }
                                up(&auth_array->sem);
                        }

                }
                close(connfd);
                exit(EXIT_SUCCESS);
        }
        return 0;
}
Included file: semtex12.sem.c
#include <unistd.h>


/* Get the semaphore and busy wait if held already */

void down(int *sem)
{
retry:
        while(*sem)
                sleep(5);
        (*sem)++;
        if(*sem > 1) {
                (*sem)--;
                goto retry;
        }
        return;
}

/* Try and get the semaphore, but return 0 if held */

int try_down(int *sem)
{
        if(*sem)
                return 0;
        (*sem)++;
        if(*sem > 1) {
                (*sem)--;
                return 0;
        }
        return *sem;
}

/* Release the semaphore */

void up(int *sem)
{
        *sem = 0;
}
Included file: semtex12.sem.h
int down(int *sem);
int try_down(int *sem);
void up(int *sem);
Included file: semtex12.server.h
struct auth {
        unsigned int    token;
        unsigned int    perms;
        unsigned int    timestamp;
};


struct sharea {
        int             sem;
        unsigned int    bitmap;
        struct auth     list[32];
};

---

## Fuentes / Sources

- OTW: https://overthewire.org/wargames/semtex/ - fecha de acceso: 2026-09-25.
- Autor notas: Apuromafo.

---

## Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a OverTheWire.
> **EN:** Educational and personal use only. Not affiliated with OverTheWire.

_Fecha de edición: 2026-09-25_
