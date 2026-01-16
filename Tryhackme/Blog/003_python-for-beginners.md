# Python for Beginners

**ID Original:** 60e84cd565e4000001040836
**Slug:** python-for-beginners
--------------------


## Overview

Python is a multi-purpose interpreted programming language that has now made its mark on the world of Computer Science and most importantly to the cyber security.
It's not a standalone post that will just explain what python is and introduce to some basic command. This post will be a start for a series named **Python For Security Enthusiasts** that will explain you how to use python libraries and builtin functions for ease of your work. I will use Python3 throughout this course on Ubuntu 18.04.

## First Steps

Python can be installed from standard apt repository of linux by typing sudo apt-get install python3 that will install python3 in your machine. To use command prompt, you just have to type python in your terminal which will land you to python interactive shell.
robin@python:~$ python3
Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type &quot;help&quot;, &quot;copyright&quot;, &quot;credits&quot; or &quot;license&quot; for more information.
&gt;&gt;&gt; 


## Basics

Starting off with the basics, I will explain different concept that will be used to get idea of what you're doing and will help you in debugging the program as well.

## Variables

A variable points to data stored in a memory location. A memory can typically contains strigs, real numbers, Boolean Values, integers or more complex data types like sets, lists, dictionary.
Note: In Python, you don't have to explicitly define a data type like C/C++.
Note: Python's string can be in single as well as double quotes they don't differ like PHP/Perl.
Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type &quot;help&quot;, &quot;copyright&quot;, &quot;credits&quot; or &quot;license&quot; for more information.
&gt;&gt;&gt; a_string = &quot;Hello&quot; # A string in duble quotations
&gt;&gt;&gt; a_string
'Hello'
&gt;&gt;&gt; a_string = 'Hello' # A string in single quotations
&gt;&gt;&gt; a_string
'Hello'
&gt;&gt;&gt; num = 5 # A integer value
&gt;&gt;&gt; num
5
&gt;&gt;&gt; float = 1.34 # A float value
&gt;&gt;&gt; float
1.34
&gt;&gt;&gt; Boolean = True # A boolean value
&gt;&gt;&gt; Boolean
True
&gt;&gt;&gt; 

Above, we declared different types of variables without explicitly defining it.

## Strings

A string is a immutable object in python that means once created you cannot change it's content. As told before it doesn't matter if you use single quotations or double quotations, a string will be a string. A builtin functon len is used to get the length of a corrseponding string provided as argument.
&gt;&gt;&gt; var = &quot;Hello, this is a string&quot;
&gt;&gt;&gt; var
'Hello, this is a string'
&gt;&gt;&gt; new_var = 'Hello, this is a string'
&gt;&gt;&gt;new_var
'Hello, this is a string'


## Integers and Floats

A python integer can either be in negative or postive since it doesn't require any pre-declarations of variable data type like C's unsingned and signed integers, it can be very useful.
&gt;&gt;&gt; a_int = 5
&gt;&gt;&gt; a_int
5
&gt;&gt;&gt; a_float = 1.43
&gt;&gt;&gt; a_float
1.43

As you can see, there is no variable declaration is needed we can save a lot of time and quickly use the objects.

## Lists, Sets and Dictionaries


## Lists

A list is a collection of homogenous or hetergenous data type that means we can store either single or differnet datas at a same time in a single list. A list can contain duplicate. For accessing data of the list you can use index i.e. position of the element in the list.
&gt;&gt;&gt; lists
[&quot;A&quot;,&quot;B&quot;,&quot;C&quot;,&quot;D&quot;]
&gt;&gt;&gt; lists[0] # value atposition zero
'A'


## Sets

A set on the other hand is a mutable data type which can be used to store different data types but it doesn't contain duplicates.
&gt;&gt;&gt; lists = [&quot;A&quot;,&quot;B&quot;,&quot;C&quot;,&quot;D&quot;,&quot;A&quot;,&quot;B&quot;]
&gt;&gt;&gt; set(lists)
[&quot;A&quot;,&quot;B&quot;,&quot;C&quot;,&quot;D&quot;]


## Dictionary

A dictionary is a hash table containing keys and their corresponding values. It has **O(1)** access time that means a constant time for retrieving data from that dictionary.
A dictionary item can be accessed from keys, below is the example.
&gt;&gt;&gt; dictionary
{'Foo': 'Bar', 'Bacon': 'Fish'}
&gt;&gt;&gt; dictionary['Foo']
'Bar'
&gt;&gt;&gt; dictionary['Bacon']
'Fish'


## Input

The input syntax is used for taking a input from the user from command line. It is by default take strings as input but with a data type prefix to it would take input as the data i.e. int for integers or float for float value.
#!/usr/bin/env python3

name = input(&quot;Enter Name: &quot;) # This will ask for input
age = int(input(&quot;Enter age:&quot; )) # This will take a integer input
height = float(input(&quot;Enter height: &quot;)

First, the name variable will take input as a string and age will take input as a integer while height variable will take float as input.
If any other type of object will ebe entered it'll result in **Exception**.

## Operators



* + : This is used to concatenate two strings or add two integers or float.

* - : This is used to subtarct a integer from a integer.

* = : This is used for variable assignments.

* == : This is used to compare two similar variable of same data types.

* != : This is a not equal to synatx that is used for comapring **if value is not equal to &lt; variable &gt;**.

* % : This is used to get remainder of a number.

* * : This is used for multiply a value. It also works for strings that provide recurrence of the strings.

* &gt;= and &lt;= : They are used for greater than or equal to and less than or equal to respectively.

* and : This is boolean AND.

* or : This is used for boolean OR.

* not: This is used for boolean NOT.


## Control Flow


## The if, elif and else statements

These statements are called conditional statements. This is used to check a condition then perform the processing of data later.
As of now, let's take a example:-

user = input(&quot;Enter Username: &quot;)
password = input(&quot;Enter Password: &quot;)

if user == &quot;admin&quot; and password == &quot;123&quot;:
    print(&quot;Welcome Admin&quot;)
elif user == &quot;guest&quot; and password == &quot;guest&quot;:
    print(&quot;Welcome Guest&quot;)
else:             
    print(&quot;Wrong credentials&quot;) 

The **user** and **password** are both variables and input syntax sill take input from user when the script will be run. On line 6 we have if which will check if user is equal to string &quot;admin&quot; and password will be comapared to string &quot;123&quot;. The and statement is used to check two variables simulatenously. On line 8 we are checking if user and password will be equal to &quot;guest&quot;. On line 10 we can see that there is a else which will be executed if either of them are wrong.

## for statement

The for..in statement is another looping statement which iterates over a sequence of objects i.e. go through each item in a sequence.

num = 5
for i in range(num):
    print(i) # Will print 0,1,2,3,4

On line 4, there is a for..in statement using a builtin object range which takes a integer and iterates over them. A for loop can be used to iterate over different kind of data type like list, strngs etc.

## while statement

The while statement allows you to repeatedly execute a block of statements as long as a condition is true. A while statement is an example of what is called a looping statement.
For example:-
while num &lt; 10:
    num += 1
print(num)

On line 1 we have a variable named num assigned 0 as value. Line 2 has a while statement which will be run until num value will be equal to or more than 10. On line 4 we have 1 being incremented to the num, everytime it's been incremented the value will be overwritten. Hence on line 5 we get a value 10.

## Functions

Functions are reusable pieces of programs. They allow you to give a name to a block of statements, allowing you to run that block using the specified name anywhere in your program and any number of times. This is known as calling the function. We have already used many built-in functions such as len and range.
Function structure:-
    -- your code --
    return result

A function contains a def at start which defines a function. func_name will be the name of function. arg will be the argument and return will gives the final result. A function **must** have a return statement.

## Exception

Exceptions occur when exceptional situations occur in your program. For example, what if you are going to read a file and the file does not exist? Or what if you accidentally deleted it when the program was running? Such situations are handled using exceptions.
Consider a simple print function call. What if we misspelt print as Print? Note the capitalization. In this case, Python raises a syntax error.
Traceback (most recent call last):
  File &quot;&lt;stdin&gt;&quot;, line 1, in &lt;module&gt;
NameError: name 'Print' is not defined
&gt;&gt;&gt; print(&quot;Hello World&quot;)
Hello World


## Handling Exceptions

We can handle exceptions using the try..except statement. We basically put our usual statements within the try-block and put all our error handlers in the except-block.
try:
    text = input('Enter something --&gt; ')
except EOFError:
    print('Why did you do an EOF on me?')
except KeyboardInterrupt:
    print('You cancelled the operation.')
else:
    print('You entered {}'.format(text))

We put all the statements that might raise exceptions/errors inside the try block and then put handlers for the appropriate errors/exceptions in the except clause/block. The except clause can handle a single specified error or exception, or a parenthesized list of errors/exceptions. If no names of errors or exceptions are supplied, it will handle all errors and exceptions.

## Modules

You have seen how you can reuse code in your program by defining functions once. What if you wanted to reuse a number of functions in other programs that you write? As you might have guessed, the answer is modules.
A module can be imported by another program to make use of its functionality. This is how we can use the Python standard library as well. First, we will see how to use the standard library modules.
import sys

print('The command line arguments are:')
for i in sys.argv:
    print(i)

print('\n\nThe PYTHONPATH is', sys.path, '\n')

First, we import the sys module using the import statement. Basically, this translates to us telling Python that we want to use this module. The sys module contains functionality related to the Python interpreter and its environment i.e. the system.
When Python executes the import sys statement, it looks for the sys module. In this case, it is one of the built-in modules, and hence Python knows where to find.

## Final Notes



* **Objects** : Python refers to anything as objects.

* **Text Editor** : Use of a good text editor like Sublime Editor or VS Code Studio throughout this course would be considered a plus.

