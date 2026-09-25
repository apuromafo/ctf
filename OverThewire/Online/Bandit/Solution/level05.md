# SSH Command
ssh bandit5@bandit.labs.overthewire.org -p 2220
# Username
bandit5
# Password
[omitida - ver Rules.md]
# Method of Solve
Use the Find command to locate the file, then read it
```
find . -size 1033c ! -executable
cat ./maybehere07/.file2
```
