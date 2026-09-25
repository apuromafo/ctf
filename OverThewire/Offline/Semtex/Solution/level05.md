# Semtex Nivel 5 - 6

| Campo | Valor |
|-------|-------|
| **Juego / Game** | Semtex (offline) |
| **Nivel / Level** | 5 - 6 |
| **URL** | https://overthewire.org/wargames/semtex/ |

Semtex Level 5 → Level 6
ICMP forging
Send a special ICMP packet to an unknown host. Add the correct payload to it, to make sure you can receive the password. Spoof your origin address and make semtex believe, the packet is really coming from some government server (*.gov) Make sure this server you are sending from has a reverse DNS entry, otherwise you will not receive an answer.

You find more specific information in your home directory. ** Note: You will have to use /semtex/semtexraw. Take a look at the source**

Reading Material
ICMP Request For Comment
Mixter’s raw socket tutorial
Included file: semtex6.rawwrapper.c
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
