1, enumerate the port (nmap)
22/tcp ssh
80/tcp http
3000/tcp GenericLines

2, check the websites.
it is clear of the versions 
`[admin](http://greenhorn.htb/login.php) | powered by [pluck](http://www.pluck-cms.org)`
`<meta name="generator" content="pluck 4.7.18" />`

Of course, we can get the exploits about this version!
`Pluck v4.7.18 - Remote Code Execution (RCE)`
`https://www.exploit-db.com/exploits/51592`

and from the url we can guess it is about "File traversal"
`http://greenhorn.htb/?file=welcome-to-greenhorn`

then just run the exploit scripts then we can get shell.

3, get the user shell
Enumerate the config.php
then we get a pass.php
`$ww = 'd5443aef1b64544f3685bf112f6c405218c573c7279a831b1fe9612e3a4d770486743c5580556c0d838b51749de15530f87fb793afdcc689b6b39024d7790163';`

So try to hash crack it .
then we get password
`d5443aef1b64544f3685bf112f6c405218c573c7279a831b1fe9612e3a4d770486743c5580556c0d838b51749de15530f87fb793afdcc689b6b39024d7790163:iloveyou1`

So we need to try to login something
`junior:x:1000:1000::/home/junior:/bin/bash
this user would be interesting.
Very lucky, we successfully login in.

From the user file, we get a funny pdf file
`Using OpenVAS.pdf`
And this file include the masked password, so we need to crack it.

It’s have sudo privilege password , But it’s hidden
Let’s try convert it to image using pdfimages.

`pdfimages "./Using OpenVAS.pdf" greenhorn`
It is a pixelated image containing a password.
There tool called Depix.
Depix is a PoC for a technique to recover plaintext from pixelized screenshots.
then we get root password
`sidefromsidetheothersidesidefromsidetheotherside`

