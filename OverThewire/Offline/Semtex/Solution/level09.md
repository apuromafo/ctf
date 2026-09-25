# Semtex Nivel 9 - 10

| Campo | Valor |
|-------|-------|
| **Juego / Game** | Semtex (offline) |
| **Nivel / Level** | 9 - 10 |
| **URL** | https://overthewire.org/wargames/semtex/ |

Semtex Level 9 → Level 10
Hacking szene
Thanks to zaphod and Mush for finding a bugs in this level

Do you know these hacking movies where they push some buttons, then the evil hacker script window turns up and a percentage bar is showing how far the password cracking has gone?

0%....10%....20%....30%....40%....50%....60%....70%....80%....90%....100%
password cracked!
Ever wanted to do it yourself? Here is your chance.\

This level implements a weakness in the authentication scheme used by M$ win95 and win98 for the netbios shares.

There is a TCP daemon on brebera port 24019. It authenticates your password. Once you send the correct password, it echoes it back. Well, let the source speak for itself. As far as brute force may take you, a little brain is never bad :P Perhaps you have heard of pqwak?

Included file: semtex10.c
#define _GNU_SOURCE
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <sys/socket.h>
#include <sys/wait.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <signal.h>


#define LISTENPORT 24019
#define REALPWD "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
#define OLDPWD "XXXXXXXXXXXXXXXX"
#define DROPUID 1998
#define DROPGID 1998

struct query
{
        unsigned char oldpass[20+1];
        unsigned char pass[100+1];
        unsigned int len;
} qry;

struct response
{
        unsigned int result;
        unsigned char pass[100+1];
} rsp;

int main(int argc, char *argv[])
{
        int listenfd, connfd;
        struct sockaddr_in localaddr;
        struct sockaddr_in remoteaddr;
        int sin_size;
        int port=LISTENPORT;

        setresgid(DROPGID, DROPGID, DROPGID);
        setresuid(DROPUID, DROPUID, DROPUID);
        signal(SIGPIPE, SIG_IGN);
        daemon(0,0);

        if ((listenfd = socket(AF_INET, SOCK_STREAM, 0)) == -1)
        {
                perror("socket");
                exit(EXIT_FAILURE);
        }

        localaddr.sin_family = AF_INET;
        localaddr.sin_port = htons(port);
        localaddr.sin_addr.s_addr = INADDR_ANY;
        bzero(&(localaddr.sin_zero), 8);

        if (bind(listenfd, (struct sockaddr *)&localaddr, sizeof(struct sockaddr)) == -1)
        {
                perror("bind");
                exit(EXIT_FAILURE);
        }

        if (listen(listenfd, 20) == -1)
        {
                perror("listen");
                exit(EXIT_FAILURE);
        }

        for (;;)
        {
                sin_size = sizeof(struct sockaddr_in);
                if ((connfd = accept(listenfd, (struct sockaddr *)&remoteaddr, &sin_size)) == -1)
                {
                        perror("accept");
                        continue;
                }

//              printf("connection from %s\n",  inet_ntoa(remoteaddr.sin_addr));

                if (!fork()) //child
                {
                        close(listenfd);

                        for (;;)
                        {
                                memset(&qry, 0, sizeof(struct query));
                                memset(&rsp, 0, sizeof(struct response));

                                if (recv(connfd, &qry, sizeof(struct query), 0)!=sizeof(struct query))
                                {
                                        perror("recv");
                                        close(connfd);
                                        exit(EXIT_FAILURE);
                                }

                                if (strncmp(qry.oldpass, OLDPWD, strlen(OLDPWD)))
                                {
                                        close(connfd);
                                        exit(EXIT_FAILURE);
                                }

                                // validate
                                if (!strncmp(qry.pass, REALPWD, qry.len))
                                        rsp.result=1;

                                if (rsp.result && (qry.len==strlen(REALPWD)))
                                        strcpy(rsp.pass, REALPWD);

//                              printf("-> result=%s\n", rsp.result?"CORRECT":"WRONG");
                                if (send(connfd, &rsp, sizeof(struct response), 0)!=sizeof(struct response))
                                {
                                        perror("send");
                                        close(connfd);
                                        exit(EXIT_FAILURE);
                                }
                        }
                }

                while(waitpid(-1,NULL,WNOHANG) > 0);

                close(connfd);
        }

}

---

## Fuentes / Sources

- OTW: https://overthewire.org/wargames/semtex/ - fecha de acceso: 2026-09-25.
- Autor notas: Apuromafo.

---

## Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a OverTheWire.
> **EN:** Educational and personal use only. Not affiliated with OverTheWire.

_Fecha de edición: 2026-09-25_
