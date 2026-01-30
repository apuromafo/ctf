# Python for Security Enthusiasts Chapter 2: Requests Module

**ID Original:** 60e84cd565e4000001040839
**Slug:** python3-requests
--------------------


## Requests Module

Dealing with HTTP requests is not an easy task in any programming language. If we talk about Python, it comes with two built-in modules, urllib and urllib2, to handle HTTP related operation. Both modules come with a different set of functionalities and many times they need to be used together. The main drawback of using urllib is that it is confusing (few methods are available in both urllib, urllib2), the documentation is not clear and we need to write a lot of code to make even a simple HTTP request.
To make these things simpler, one easy-to-use third-party library, known as requests, is available and most developers prefer to use it instead or urllib/urllib2. It is an Apache2 licensed HTTP library powered by urllib3 and httplib.

## Installation

Since, this series uses python3 for development I'll be using pip3 for installing 3rd party modules.
Type the following in your terminal:-
sudo pip3 install requests
Doing that pip will install the requests module on your system and you'll be ready to go!

## Basics of requests

To start using python's requests module you need to import it first. Following are the commands which will be used for creating a script that will scrape data from a website or API.


* requests.get(url) : This will make a GET request to the website.

* requests.post(url, data) : This will make a POST requests to the URL and data of the post body can be passed as a dictionary format.


Note: Other request method will be made in a same way like requests.head, requests.put etc.

For a request object you can use following:-
For the ease of understanding let's take a example of requests object:-
&gt;&gt;&gt;import requests
&gt;&gt;&gt;r = requests.get(&quot;https://google.com&quot;)



* r.status_code : This will return the response code that has been recieved from request like 200, 404, 301 etc.

* r.text : This will return the data that has been recieved from a website.

* r.json : This will make the response in json object.

Arguments for requests methods:-


* timeout : This will be used to set timeout for a request.

* allow_redirects : This can be used to specify that redirects can be allowed or not like allow_redirects=True will let the request to redirect.

* r.encoding : This will show the encoding of the data recieved.

* cookies : This will pass the cookie to the requested session. It must be given in a dictionary format.

* headers : This will use the header provided for the requests session.

For now, this got you covered. I won't be explaining advanced content, if you want to have a advance post let me know by making a requests on THM discord server or contacting me at [twitter](https://twitter.com/d4mianwayne?ref=blog.tryhackme.com)

## Project 1: IP-Lookup

So, let's make a simple request to an **IP-Lookup** API that will gather the information for our target.

Note: This will a very basic request, but nonetheless it'll help you in understanding how we can gather data using Python.
I'm using [this](http://ip-api.com/json?ref=blog.tryhackme.com) API to get the general information about an IP Address.

Let's write a program to get data about an IP address:
import requests
import json  # Need to parse recieved data

def iplookup(public_ip):
    r = requests.get(&quot;http://ip-api.com/&quot;+public_ip) 
    if r.status_code == 200: # If success 
        data = json.loads(r.text) # Load the recieved data in json object
        for key, value in (data).items(): # This will iterate over dictionary
            print(&quot;{}:{}&quot;.format(key, value))
    else:  # If error occurs
        print(&quot;Error Occured while making request&quot;)

if __name__ == &quot;__main__&quot;:
    try:
        ip = input(&quot;Enter IP: &quot;)
        iplookup(ip)
    except:
        print(&quot;Error Occured!&quot;)     


## How it works

On first and second line we imported requests and json. After that we create a function named iplookup which will take an argument i.e. public_ip after that we make a request to the API and see if it returns the success code via r.status_code, then loads our recieved data into a json format and by iterating over this, we print the recieved information. I added a try...except block to handle any error that might occur. For more information on exception handling please see introductory course I've written on this blog!

## Project 2: Directory Buster

Now, let's take on a more complicated, yet very useful tool, a **directory buster**. So, before we move on I'll explain how to reading and writing files in Python.

## File Handling: Read &amp; Write

We need to read files to do directory bust'ing using a dictionary attack. In python, we use the open function which is a builtin function which returns a file object and can be used to open a file in different ways such as **read**, **write** and **append**.
Let's take an example:
#!/usr/bin/python3

f = open(&quot;new.txt&quot;, &quot;r&quot;) # opens the file for reading
print(f.read()) # reads the content of file

new = open(&quot;new1.txt&quot;,&quot;w&quot;) # opens the file for writing
data = f.read() 
new.write(data) # write data file new1.txt
new.close() # close the file

We use open function and pass two arguments, a file path and the mode of opening. In above example file.txt is file path and r is the mode i.e. read mode and then we open a file new1.txt for read purpose which will be used to writte

## Different file modes



* r  : Read mode.

* w  : Write mode.

* a  : Append mode.

* r+ : Read and Write mode.


Note: Appending b to a mode will open the file in binary mode of operation i.e. all the contents of file will be considered as byte object like f = open(&quot;new.txt&quot;, &quot;rb&quot;) which will reads the file in binary mode.

Let's get started:-
import requests

def dirb(url, dict):
    try:
        wordlist = open(dict,&quot;rb&quot;)
        for path in wordlist.readlines():
            path = path.strip().decode(&quot;utf-8&quot;)
            urlpath = url+&quot;/&quot;+path
            r = requests.get(urlpath)
            if r.status_code != 404:
                print(&quot;{} -&gt; {}&quot;.format(r.status_code, urlpath))
    except: # Catching exceptions
        print(&quot;Error Occured!&quot;)

if __name__ == &quot;__main__&quot;:
    dirb(&quot;http://10.0.0.210&quot;, &quot;all.txt&quot;)    # MrRobot room IP


## How it works

We created a function named dirb with arguments url and dict which will be our file containing our directory list to brute force on the site. Then we have a try...except block. I then opened the dict file using readlines and started to loopi through the list of the words from our file, then we strip the string and decode then append it to our specified urls then we add the urls and path together with &quot;/&quot; to route them. After that we make a GET request to the generated url and print the output of a requests as long as response code is not equal to 404 (which means &quot;Not Found&quot;).
That being said, I use this script to hack a machine on TryHackMe [MrRobotCTF](https://tryhackme.com/room/mrrobot?ref=blog.tryhackme.com) and here was the output:-
robin@oracle:~$ python3 temp.py
200 -&gt; http://10.0.0.210/admin
403 -&gt; http://10.0.0.210/.htaccess
200 -&gt; http://10.0.0.210/readme.html
200 -&gt; http://10.0.0.210/image
--snip--

You can also deploy the MrRobot machine and use this script to get the directories of the website!

## Final Words

This will give you enough of an idea on how to make your own tools using Python3. But in our second project, you might observe that the script is very time consuming. For that to resolve we can use threads or multiprocessing. I have not added that functionality in because it will require some more modules and an understanding of their workflows. You can look at a multithreaded directory script here: [dirbrute.py](https://github.com/D4mianWayne/Alfred/blob/master/alfred/dirbrute.py?ref=blog.tryhackme.com). Once I am finished with series, I will most probably cover the details of every module later.
Follow me on [twitter](https://twitter.com/D4mianWayne?ref=blog.tryhackme.com).
