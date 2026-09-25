# Semtex Nivel 8 - 9

| Campo | Valor |
|-------|-------|
| **Juego / Game** | Semtex (offline) |
| **Nivel / Level** | 8 - 9 |
| **URL** | https://overthewire.org/wargames/semtex/ |

Semtex Level 8 → Level 9
Tunneling your firewall
How do you get data through a firewall that is blocking any tcp connection? You just don’t use a tcp connection, but instead other packets, that might not be filtered. For example network maintenance protocols like ICMP.

There is a raw socket open on a yet unknown host that listens for icmp packets and forwards them to a tcp server that you cannot reach. Your job is to create a client that communicates with this icmp “server”. If everything works, you find yourself in a shell on an unknown system, and can search for the password.

The protocol and the server, that is used by the ICMP tunnel is described in your home directory. If you manage to blackbox analyze it, then you can jump directly from semtex0 to semtex10 :)

You will have to use /rdx/rawwrapper.

Included file: semtex9.rawwrapper.c
#ifndef _GNU_SOURCE
#define _GNU_SOURCE
#endif
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <netinet/ip_icmp.h>
#include <string.h>


#define DROPUID 1009
#define DROPGID 1009

// rawwrapper, aton 2004

int main(int argc, char *argv[])
{
        int rfd;
        char *argv0, *argv1;

        if (argc<2)
        {
                printf("usage: rawwrapper <program>\n");
                printf("argv[1] will be the raw socket\n");
                exit(EXIT_FAILURE);
        }

        //open raw socket
        if ((rfd = socket(PF_INET, SOCK_RAW, IPPROTO_ICMP))<0)
        {
                perror("socket");
                return EXIT_FAILURE;
        }

        //drop priviledges
        setresgid(DROPGID, DROPGID, DROPGID);
        setresuid(DROPUID, DROPUID, DROPUID);

        argv0=malloc(strlen(argv[0])+1);
        strcpy(argv0, argv[0]);
        argv1=malloc(strlen(argv[1])+1);
        strcpy(argv1, argv[1]);

        // fill in new argv
        argv[0]=argv1;
        sprintf(argv[1], "%d", rfd);

        //execute the client program
        execve(argv[0], argv, NULL);
        return EXIT_SUCCESS;
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
