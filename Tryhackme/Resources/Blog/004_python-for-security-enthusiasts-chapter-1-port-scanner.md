# Python for Security Enthusiasts Chapter 1: Port Scanner

**ID Original:** 60e84cd565e4000001040837
**Slug:** python-for-security-enthusiasts-chapter-1-port-scanner
--------------------


## Socket Module

This is one of the standard modules that is used for low-level networking interaction.The Python interface is a straightforward transliteration of the Unix system call and library interface for sockets to Python’s object-oriented style: the socket() function returns a socket object whose methods implement the various socket system calls. Parameter types are somewhat higher-level than in the C interface: as with read() and write() operations on Python files, buffer allocation on receive operations is automatic, and buffer length is implicit on send operations.

## Basic Functions

Some of the basic functions that we will use throughout this chapter will have the following:-


* socket.gethostbyname : This will give the host by name of the website provided as an argument and returns the IP of the host.
For example:-

&gt;&gt;&gt; import socket
&gt;&gt;&gt; socket.gethostbyname(&quot;www.google.com&quot;)
'216.58.199.132'


## OOP functions

socket.socket(AF_INET, SOCK_STREAM) : This is a OOP function class, that means you need to provide the object to the class which will process through the data.
Let it be:-

&gt;&gt;&gt; from sockets import *
&gt;&gt;&gt;s = socket(AF_INET, SOCK_STREAM)




* s.connect(host,port) : s is a variable which will be used to call the class function. This will try to connect to port of the specified host.
For example:-


&gt;&gt;&gt; from socket import * # This will let you use function without module prefix
&gt;&gt;&gt; s = socket(AF_INET, SOCK_STREAM)
&gt;&gt;&gt; s.connect(('216.58.199.132',80))




* s.recv : This will recieve data from the host.


## Making Port Scanner

So, now we know what will be used. Let's get started:-

from socket import *

def port_scan(host, port):
    s = socket(AF_INET, SOCK_STREAM) # Setting up TCP protocol
    try: # Exception Handling
        s.connect((host, port)) # Connecting to port
        print(&quot;[+] {} port is open&quot;.format(port))
    except: # If connection fails
        print(&quot;[+] Port is closed&quot;)
        


## How it works

It first import all functions from **socket** module. **def port_scan** is defining function **port_scan** and it takes two argument **host** and **port** then it is setting up TCP protocol then in **try....except** block which will handle the exception. It has a s.connect will try to connect to host's port.

## Making It Better: Part 1

Save it as port_scan.py

from socket import *

def connect_port(host, port):
    s = socket(AF_INET, SOCK_STREAM) # Setting up TCP protocol
    try: # Exception Handling
        s.connect((host, port)) # Connecting to port
        print(&quot;[+] {} port is open&quot;.format(port))
    except: # If connection fails
        print(&quot;[+] Error Occured&quot;)
        
def main():
   host = input(&quot;Enter Host: &quot;)
   port = input(&quot;Enter Port: &quot;)
   port_scan(host, port) # calling port_scan function
   
if __name__ == '__main__':
    main()
        

We added a main function which will ask for host and port and will function **port_scan** and perform operation further.

## Making It Better: Part 2

Now, I'll show you how to add command line argument and take multiple port as input for scanning.

from socket import *
import sys

def port_scan(host): 
    for i in range(1, 1025):
        s = socket(AF_INET, SOCK_STREAM)# Setting up TCP protocol
        res = s.connect_ex((str(host), i))
        if res ==  0: # If connection successful
            print(&quot;Port {} is open.&quot;.format((i)))
        s.close() # Closing the connection

   
if __name__ == '__main__':
    port_scan(sys.argv[1])
        


## How it works

It's same as above one but it has a new s.connec_ex it's same as s.connect but it gives numeric value for result i.e 1 means an error occured while 0 means success. The first two lines are importing sockets and sys. Then we iterate over first 1024 numeric values that will be used as port umbers. Then it's being treated as port. We will have to close the connetion everytime because it'll throw an eception that socket is already binded to host.

Note: sys is imported because it will read command line arguments with sys.argv[1] as 1 is the position of host.


## Using the port_scan.py

Now, you're done. Let's run our script:-

robin@oracle:/Projects$ python3 temp.py 192.168.43.172
Port 22 is open.


Congratulation on making you first ever tool i.e. a port scanner.

## Final Words

This is it for today, we have worked our way through this. Next time, we will be creating a hash cracker and a basic XOR function.
Until then, **try this tool on THM's Online Machines by deploying it**.
Follow me on [twitter](https://twitter.com/d4mianwayne?ref=blog.tryhackme.com) for more content.
