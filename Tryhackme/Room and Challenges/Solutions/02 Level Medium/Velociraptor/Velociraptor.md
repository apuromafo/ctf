1. No answer needed
2. velociraptor.exe gui
3. 1. THM-VELOCIRAPTOR.eu-west-1.compute.internal
   2. 2021-04-11T22:11:10Z
   3. LET Generic_Client_Info_Users_0_0=SELECT Name, Description, Mtime AS LastLogin FROM Artifact.Windows.Sys.Users()
   4. Stdout
   5. powershell -ExecutionPolicy Unrestricted -encodedCommand ZwBlAHQALQBkAGEAdABlAA==
4. 1. Ubuntu on Windows Subsystem for Linux
   2. 19
5. 1. ntfs accessor
   2. registry accessor
   3. desktop.ini
   4. THM{VkVMT0NJUkFQVE9S}
6. 1. Column Selectors
   2. VQL Plugin
   3. Filter expression
   4. ?
   5. execve()
7. 1. parse_mft
   2. IsDir
8. 1. Windows.Detection.PrintNightmare
   2. SELECT "C:/" + FullPath AS Full_Path,FileName AS File_Name,parse_pe(file="C:/" + FullPath) AS PE
   3. nightmare.dll
   4. C:\Users\caleb\source\repos\nightmare\x64\Release\nightmare.pdb
9. No answer needed
