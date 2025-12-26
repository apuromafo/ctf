Semtex
2022-08-16 - semtex offline
Semtex is offline.
Wargame?
This network is a legal environment where you can learn coding/hacking techniques without destroying anything. You have to solve Semtex 0 to get a username/password for login. Once logged in, you have to make your way from one level to the next, each one containing a small security hole/feature that has been installed for you. Your mission is to find out how to exploit the weakness and to cause interesting behavior :)

Rules?
Well you can do anything you want on this box, code, hack, learn, … its all there for gaining knowledge. Please refrain from DOS attacks of any kind, it ruins the fun of you and of others. As long as you behave, everything is possible.

Contribute?
This wargame is from the community for the community. If you want to contribute, send a level plus exploit to aton at packetdropped dot org.

Network programming, reverse engineering, buffer overflows and combinatorial analysis.

Contact : aton at packetdropped dot org



Semtex Level 0
Get a shell
semtex.labs.overthewire.org

x86/elf:	Connect to port 24000
amd64/elf:	Connect to port 24001
ppc/mach-O:	Connect to port 24002
Receive data until the port is closed.

Every second byte you receive is trash, ignore it. The other bytes are an executable that shows you the password.

Then login to semtex1@semtex.labs.overthewire.org on port 2229

Thanks to mrx for the amd64 and ppc binaries!

Reading Material
Beej’s guide to network programming



Semtex Level 1 → Level 2
Dynamic tricks
This program checks your user ID.

Perhaps you can trick it, so that it thinks you have a different one.

Think dynamically.

Reading Material
Link

https://www.google.com/search?q=linux+function+interception




Semtex Level 2 → Level 3
Number-Lock Action
You are almost on Semtex 3, there is just one big door before you. It is locked with a number lock. Analyze and use the locks in /semtex/semtex3 to adjust all the numbers in the correct way. They will open your way to the next level.

Tip : If you are not good at math, you should consider brute force. Rewrite the program and try all possible combinations of the locks. It wont take more than a few seconds ;)


Semtex Level 3 → Level 4
Ptrace your way
Pass prints the password for the level you are on. Try to make it print the next level’s password. This time it is not so easy:

/semtex/semtex4: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), statically linked, for GNU/Linux 2.6.15, stripped
Tip :

Pass uses geteuid() to get its information.
Read man ptrace



Semtex Level 4 → Level 5
Random Networking
Make 10 connections to port 24027 from different IP’s. On each connection you will receive a string of 10 ASCII characters. XOR this string with the Semtex5 password, character by character. Then send back the 10 characters followed by another string of exactly 10 characters which identifies you (can be anything within A-Z, a-z, 0-9). The first 10 characters that you send, are different on every connection, the last 10 have to be the same. If you do not send the correct string back within 5 seconds you are disconnected. Once connected with at least 10 different IP’s You will receive the password on one connection, chosen randomly.

**Note: Your connections time out in 2 minutes and you cannot connect from an IP that is still connected. May the sockets be with you. **

Reading Material
Socks5 Request For Comment


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




Semtex Level 6 → Level 7
Multi-vitamin
Getting out of the restricted shell shouldn’t take you more than five minutes. Then have a look at /rdx/multivitamin. Try to analyse the algorithm very carefully. There is a weakness that really speeds up your quest…\

Multiplication is easy, and so is division…? You might want to look at http://gmplib.org/ if you use c.

Included file: semtex7.c
/*
 *      multivitamin.c 2006 by aton@packetdropped.org
 *
 *      rules: no patching.
 *      compile: gcc multivitamin.c -o multivitamin -lgmp
 *
 *      -> multiplication is simple, and so is division...?
 */


#define _GNU_SOURCE
#include <unistd.h>
#include <string.h>
#include <stdio.h>
#include <gmp.h>

#define ADDVALUE 27137

int main(int argc, char *argv[])
{
        mpz_t longjohn, mul, cmpval;
        char userstr[512+1];
        int n=0;

        mpz_init(longjohn);
        mpz_set_ui(longjohn, 1);
        mpz_init(mul);
        mpz_init(cmpval);
        mpz_set_str(cmpval, "insert-here-the-password-hash-from-your-home-directory-on-semtex-7", 10);

        if (argc<2)
        {
                printf("%s <string>\n", argv[0]);
                return -1;
        }

        strncpy(userstr, argv[1], 512);

        for (n=0;n<strlen(userstr);n++)
        {
                mpz_set_ui(mul, (unsigned long)(userstr[n]+ADDVALUE));
                mpz_mul(longjohn, longjohn, mul);
        }

        if (!(n=mpz_cmp(longjohn, cmpval)))
        {
                setresuid(geteuid(), geteuid(), geteuid());
                execlp("/bin/bash", "bash", NULL);
        }
        else
                printf("err... booom!\n");

        return 0;
}


Semtex Level 7 → Level 8
Non-sniffable data
This level is about some very simple covert channel, about transferring information that cannot possibly be sniffed. There is a socket file in /rdx/nature. It is a local Unix socket. Receive data from it until EOF and save it to a file.

Watch the time between the received bytes. Certain delays mean certain bytes that have been left out (have not been sent).

0-1 s : no special data
1-2 s : 'Q'
2-3 s : 'L'
3-4 s : 'A'
4-5 s : 'V'
you have to take these “unsent” data into your output file too, exactly at the places where they occur.

Thus you are receiving data while not receiving anything.

The output file is a .jpg image :)




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



Semtex Level 10 → Level 11
Deja vue
/rdx/vl1b is vortex semtex1 with a slight modification to make things a little bit harder.

Thanks to andrewg for inspiration.

Suggested reading
manpages: popen, dup2

Included file: semtex11.c
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <stdio.h>


// code by andrewg, modified by aton

#define e(); if(((unsigned int)ptr & 0xff000000)==0xca000000) { setresuid(geteuid(), geteuid(), geteuid()); execlp("/bin/sh", "sh", "-i", NULL); }

void print(unsigned char *buf, int len)
{
        int i;

        printf("[ ");
        for(i=0; i < len; i++) printf("%x ", buf[i]);
        printf(" ]\n");
}

int main()
{
        unsigned char buf[512];
        unsigned char *ptr = buf + (sizeof(buf)/2);
        unsigned int x;

        while((x = getchar()) != EOF) {
                switch(x) {
                        case '\n': print(buf, sizeof(buf)); continue; break;
                        case '\\': ptr--; break;
                        default: e(); if(ptr > buf + sizeof(buf)) continue; ptr++; break;
                }
        }
        printf("All done\n");
}




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


