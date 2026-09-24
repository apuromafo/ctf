# Android Application Static Analysis


---
## Page 1

Extracting and Enumerating APK Files
Command
Description
adb install myapp.apk
Install an application.
adb shell pm path com.example.myapp
adb shell pm list packages
adb pull /data/app/com.example.myapp-1/base.apk .
Extract the APK from the device.
apktool d myapp.apk
Disassembling an APK
Analyzing Application's Source Code
Command
Description
sudo apt install jadx
jadx-gui /full/path/to/myapp.apk
Analyze app with JADX.
curl -o- https://raw.githubusercontent.com/nvm-
sh/nvm/v0.40.2/install.sh | bash
source ~/.bashrc
nvm install node
npm -g install js-beautify
apktool d myapp.apk
js-beautify myapp/assets/index.android.bundle -o
beautified_index.android.bundle.js
Beautify the content of the minified JS
code.
pip3 install --upgrade git+https://github.com/P1sec/hermes-dec
hbc-decompiler index.android.bundle output.js
Decompile Hermes JavaScript bytecode.
ANDROID APPLICATION STATIC ANALYSIS
CHEAT SHEET

---
## Page 2

Command
Description
wget https://github.com/giacomoferretti/paranoid-
deobfuscator/archive/refs/tags/v2.0.1.zip
unzip v2.0.1.zip
cd paranoid-deobfuscator-2.0.1
python -m venv .venv
source .venv/bin/activate
pip install "numpy==1.26.0"
apktool d myapp.apk
python -m paranoid_deobfuscator -v myapp
Deobfuscate apps obfuscated with
Paranoid/LSParanoid
Analyzing Native Libraries
Command
Description
wget
https://raw.githubusercontent.com/x41sec/tools/master/Mobile/Xamarin/Xamarin_XALZ_decompress.py
python Xamarin_XALZ_decompress.py myapp/unknown/assemblies/Myapp.dll myapp_decompressed.dll
Decompress
special
Xamarin
files.
sudo pip3 install git+https://github.com/jakev/pyxamstore.git
pyxamstore unpack -d myapp/unknown/assemblies/
Extract
assemblies
from .blob
files.
Application Patching
Command
Description
adb connect 10.11.1.1:5001
adb install mybank.apk
adb uninstall mynotes.apk
Connect to remote device, install and
uninstall apps.
apktool b myapp
echo -e "password\npassword\njohn
doe\ntest\ntest\ntest\ntest\ntest\nyes" > params.txt
cat params.txt | keytool -genkey -keystore key.keystore -validity
1000 -keyalg RSA -alias john
zipalign -p -f -v 4 myapp/dist/myapp.apk myapp_aligned.apk
echo password | apksigner sign --ks key.keystore myapp_aligned.apk
adb uninstall com.hackthebox.myapp
adb install myapp_aligned.apk
Recompile an APK, sign it, uninstall the old
one, and install the patched one.