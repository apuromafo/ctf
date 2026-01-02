
Sidequest 2
https://tryhackme.com/room/sq2-aoc2025-JxiOKUSD9R


 What is the flag hidden in the file?

Answer format: ***{*******_**_***_********_*******}
 
What is the content of foothold.txt?

Answer format: ***{******_***_****_**_***_***_*****}
 
What is the content of user.txt?

Answer format: Answer format: ***{******_********_**_***_*****_****_******_****}
 
What is the content of root.txt?

Answer format: Answer format: ***{**********_************}

 
01.01.2026 
 
Step 1:  
start egg decode

 `tit_for_tat`
 
 
ya podremos continuar con mmap y otros
```
sudo nmap -sV -p22,80,9004,21337 -sS -T4 --min-rate 2000 -n -Pn 10.66.147.238
Starting Nmap 7.95 ( https://nmap.org ) at 2025-12-22 01:44 -03
Nmap scan report for 10.66.147.238
Host is up (0.12s latency).

PORT      STATE SERVICE VERSION
22/tcp    open  ssh     OpenSSH 9.6p1 Ubuntu 3ubuntu13.11 (Ubuntu Linux; protocol 2.0)
80/tcp    open  http    Apache httpd 2.4.58 ((Ubuntu))
9004/tcp  open  unknown
21337/tcp open  http    Werkzeug httpd 3.0.1 (Python 3.12.3)
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port9004-TCP:V=7.95%I=7%D=12/22%Time=6948CC97%P=x86_64-pc-linux-gnu%r(N
SF:ULL,46,"Payload\x20Storage\x20Malhare's\nVersion\x204\.2\.0\n\[1\]\x20C
SF::\n\[2\]\x20U:\n\[3\]\x20D:\n\[4\]\x20E:\n>>")%r(JavaRMI,55,"Payload\x2
SF:0Storage\x20Malhare's\nVersion\x204\.2\.0\n\[1\]\x20C:\n\[2\]\x20U:\n\[
SF:3\]\x20D:\n\[4\]\x20E:\n>>Invalid\x20option\n")%r(GenericLines,46,"Payl
SF:oad\x20Storage\x20Malhare's\nVersion\x204\.2\.0\n\[1\]\x20C:\n\[2\]\x20
SF:U:\n\[3\]\x20D:\n\[4\]\x20E:\n>>")%r(GetRequest,55,"Payload\x20Storage\
SF:x20Malhare's\nVersion\x204\.2\.0\n\[1\]\x20C:\n\[2\]\x20U:\n\[3\]\x20D:
SF:\n\[4\]\x20E:\n>>Invalid\x20option\n")%r(HTTPOptions,55,"Payload\x20Sto
SF:rage\x20Malhare's\nVersion\x204\.2\.0\n\[1\]\x20C:\n\[2\]\x20U:\n\[3\]\
SF:x20D:\n\[4\]\x20E:\n>>Invalid\x20option\n")%r(RTSPRequest,55,"Payload\x
SF:20Storage\x20Malhare's\nVersion\x204\.2\.0\n\[1\]\x20C:\n\[2\]\x20U:\n\
SF:[3\]\x20D:\n\[4\]\x20E:\n>>Invalid\x20option\n")%r(RPCCheck,55,"Payload
SF:\x20Storage\x20Malhare's\nVersion\x204\.2\.0\n\[1\]\x20C:\n\[2\]\x20U:\
SF:n\[3\]\x20D:\n\[4\]\x20E:\n>>Invalid\x20option\n")%r(DNSVersionBindReqT
SF:CP,55,"Payload\x20Storage\x20Malhare's\nVersion\x204\.2\.0\n\[1\]\x20C:
SF:\n\[2\]\x20U:\n\[3\]\x20D:\n\[4\]\x20E:\n>>Invalid\x20option\n")%r(DNSS
SF:tatusRequestTCP,55,"Payload\x20Storage\x20Malhare's\nVersion\x204\.2\.0
SF:\n\[1\]\x20C:\n\[2\]\x20U:\n\[3\]\x20D:\n\[4\]\x20E:\n>>Invalid\x20opti
SF:on\n")%r(Help,55,"Payload\x20Storage\x20Malhare's\nVersion\x204\.2\.0\n
SF:\[1\]\x20C:\n\[2\]\x20U:\n\[3\]\x20D:\n\[4\]\x20E:\n>>Invalid\x20option
SF:\n")%r(SSLSessionReq,55,"Payload\x20Storage\x20Malhare's\nVersion\x204\
SF:.2\.0\n\[1\]\x20C:\n\[2\]\x20U:\n\[3\]\x20D:\n\[4\]\x20E:\n>>Invalid\x2
SF:0option\n")%r(TerminalServerCookie,55,"Payload\x20Storage\x20Malhare's\
SF:nVersion\x204\.2\.0\n\[1\]\x20C:\n\[2\]\x20U:\n\[3\]\x20D:\n\[4\]\x20E:
SF:\n>>Invalid\x20option\n")%r(TLSSessionReq,55,"Payload\x20Storage\x20Mal
SF:hare's\nVersion\x204\.2\.0\n\[1\]\x20C:\n\[2\]\x20U:\n\[3\]\x20D:\n\[4\
SF:]\x20E:\n>>Invalid\x20option\n")%r(Kerberos,55,"Payload\x20Storage\x20M
SF:alhare's\nVersion\x204\.2\.0\n\[1\]\x20C:\n\[2\]\x20U:\n\[3\]\x20D:\n\[
SF:4\]\x20E:\n>>Invalid\x20option\n");
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 19.46 seconds
```
 
 
 Step 2:
 Nmap and continue with fuzz
 
 
 there are a dev folder-> puerto 80 `/dev` 
```
 ./beacon.bin
Enter key: EastMass
Hello EastMass!
Access granted! Starting socket server...
Socket server listening on port 4444...
```

lectura de strings tienes la flag 1 

 
 about tmp in strings can use as pattern for enter a folder...
 the folder have other binary `/7ln6Z1X***`  , and file for flag 2 
 
 
 the next is pwn step in local and post in remote.
 ```
 int banner()
{
  return puts("Payload Storage Malhare's\nVersion 4.2.0");
  
  int __fastcall main(int argc, const char **argv, const char **envp)
{
  int opt; // [rsp+Ch] [rbp-4h]

  setup(argc, argv, envp);
  banner();
  while ( 1 )
  {
    menu();
    opt = read_opt();
    if ( opt == 4 )
    {
      puts("Bye");
      _exit(1337);
    }
    if ( opt > 4 )
      break;
    if ( opt == 3 )
    {
      delete();
    }
    else
    {
      if ( opt > 3 )
        break;
      if ( opt == 1 )
      {
        create();
      }
      else
      {
        if ( opt != 2 )
          break;
        update();
      }
    }
  }
  puts("Invalid option");
  return 0;
}

exit
// attributes: thunk
void __noreturn _exit(int status)
{
  exit(status);
  
  update

__int64 update()
{
  unsigned int opt; // [rsp+8h] [rbp-8h]
  unsigned int v2; // [rsp+Ch] [rbp-4h]

  puts("idx:");
  opt = read_opt();
  if ( opt <= 0xF8 && chunks[opt] )
  {
    puts("offset:");
    v2 = read_opt();
    if ( (unsigned __int64)v2 < sizes[opt] )
    {
      puts("data:");
      read(0, (void *)(chunks[opt] + v2), sizes[opt] - v2);
      return 0;
    }
    else
    {
      puts("Offset too large!");
      return 1;
    }
  }
  else
  {
    puts("Invalid idx");
    return 0xFFFFFFFFLL;
  }
  
  
  delete
__int64 delete()
{
  unsigned int opt; // [rsp+Ch] [rbp-4h]

  puts("idx:");
  opt = read_opt();
  if ( opt <= 0xF8 && chunks[opt] )
  {
    free((void *)chunks[opt]);
    puts("deleted successfully");
    return 0;
  }
  else
  {
    puts("Invalid idx");
    return 0xFFFFFFFFLL;
  }
}

__int64 create()
{
  int opt; // eax
  __int64 v2; // rbx
  __int64 v3; // rax
  size_t size; // [rsp+8h] [rbp-18h]

  if ( (unsigned __int64)idx <= 0xFF )
  {
    puts("size: ");
    opt = read_opt();
    size = opt;
    if ( opt )
    {
      v2 = idx;
      chunks[v2] = malloc(opt);
      v3 = idx++;
      sizes[v3] = size;
      return 0;
    }
    else
    {
      puts("Size should be non-zero!");
      return 1;
    }
  }
  else
  {
    puts("You cannot allocate any more!");
    return 1;
  }
}


int menu()
{
  puts("[1] C:");
  puts("[2] U:");
  puts("[3] D:");
  return printf("[4] E:\n>>");
}
 ```
 


 
 


# Answer the questions below
What is the flag hidden in the file?

`THM{Welcom3_to_th3_eastmass_pwnland}`

 What is the content of foothold.txt?
`THM{byp4ss_and_pack_is_pwn_you_n33d}`
 

 What is the content of user.txt?

Answer format: `THM{theres_someth1g_in_th3_w4t3r_that_cannot_l3ak}`

 
What is the content of root.txt?

Answer format: `THM{final-boss_defeat3d-yay}`

 

 
  https://corgi.rip/posts/leakless_heap_1/  
  https://github.com/corgeman/leakless_research/   
  
  
 
 tutorial:
 https://jaxafed.github.io/posts/tryhackme-aoc2025_sidequest_two/
 https://github.com/djalilayed/tryhackme/tree/main/Advent_of_Cyber_Side_Quest_2025/Scheme_Catcher
 
 
 
 
tuts in youtube:
video
Djalil Ayed  TryHackMe Scheme Catcher - Advent of Cyber Side Quest - Full Walkthrough 2025

https://www.youtube.com/watch?v=x_s0IofEiAQ


 atached a solution from id root
 

