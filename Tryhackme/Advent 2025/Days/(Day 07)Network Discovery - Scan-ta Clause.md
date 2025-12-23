- nmap: port scanning
- 22 -> default SSH port
- netcat: to manually interact with network services
- `dns` port: protocol that connects domain names to IP addresses
- 3306 port -> MySQL database management system  

## Nmap commands
- `nmap -sn <network>` : tells us which machines are live
- `nmap <ip>` : scans the specified host for open ports
- `nmap -p <port> <ip>`: scans specified port

## Transport protocols 
- TCP(Transmission Control Protocol): used in case of web browsing, email, file transfer, SSH; connection based 
- UDP(User Datagram Protocol): is connectionless

## Netcat
- `nc <ip> <port>` : connects to service 


## Answers:
- What evil message do you see on top of the website? : `Pwned by HopSec`
- What is the first key part found on the FTP server? : `3aster_`
- What is the second key part found in the TBFC app? : `15_th3_`
- What is the third key part found in the DNS records? : `n3w_xm45`
- Which port was the MySQL database running on? : `3306`
- Finally, what's the flag you found in the database? : `THM{4ll_s3rvice5_d1sc0vered}`
