1, port scan
22/tcp ssh
80/tcp http

2,enumerate the web pages
In the original page, there is nothing useful even there is no urls.

So let's use the ffuf to check these resources.
`ffuf -u http://10.10.10.242/FUZZ -w /usr/share/wordlists/dirb/common.txt`
But very sad there is nothing useful and no login or other pages.

So let's check the sub-domain or virtual machines/hosts.
Still very sad, there is no sub-domains.

Let's come to original page and use the burp to catch the package of response.

From the response content, we find something interesting.
`X-Powered-By: PHP/8.1.0-dev`
If there is only `PHP/8.1.0` if would not catch my attention. But `-dev` would be always vulnerable.

Thus we can search the exploits about that version of PHP.
So of course, we can get the poc 
`PHP 8.1.0-dev - 'User-Agentt' Remote Code Execution`
```
An early release of PHP, the PHP 8.1.0-dev version was released with a backdoor on March 28th 2021, but the backdoor was quickly discovered and removed. If this version of PHP runs on a server, an attacker can execute arbitrary code by sending the User-Agentt header. The following exploit uses the backdoor to provide a pseudo shell ont the host.
It would have the backdoor.
```
`https://github.com/flast101/php-8.1.0-dev-backdoor-rce.git`
Just run the exploit script ,we can get the user shell.

2, get the root shell.
Firstly, we can check the List the commands the current user is authorized to execute when using sudo.
`sudo -l`
Then we can find 
```
Matching Defaults entries for james on knife:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User james may run the following commands on knife:
    (root) NOPASSWD: /usr/bin/knife

```
So let's check /usr/bin/knife
the permission of that :
`lrwxrwxrwx 1 root root 31 May  7  2021 /usr/bin/knife -> /opt/chef-workstation/bin/knife`

we found we have the permission of write and exec.(this is a link file)
And also, we found it was a ruby script.
`#!/opt/chef-workstation/embedded/bin/ruby --disable-gems`

In this place, we need to include the background
```
Background
Chef is an automation/infrastructure platform:

Chef Infra is a powerful automation platform that transforms infrastructure into code. Whether you’re operating in the cloud, on-premises, or in a hybrid environment, Chef Infra automates how infrastructure is configured, deployed, and managed across your network, no matter its size.

knife is a command line tool manage Chef. According to the docs, it manages aspects of Chef such as:

Nodes
Cookbooks and recipes
Roles, Environments, and Data Bags
Resources within various cloud environments
The installation of Chef Infra Client onto nodes
Searching of indexed data on the Chef Infra Server

```

And we can found some trick exploitation in GTFOBins.
```
Shell
It can be used to break out from restricted environments by spawning an interactive system shell.

knife exec -E 'exec "/bin/sh"'

Sudo
If the binary is allowed to run as superuser by sudo, it does not drop the elevated privileges and may be used to access the file system, escalate or maintain privileged access.

sudo knife exec -E 'exec "/bin/sh"'
```

So just try them and get our root shell.
