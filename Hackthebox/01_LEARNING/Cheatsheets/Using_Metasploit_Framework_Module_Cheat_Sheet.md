# Using the Metasploit Framework — Cheat Sheet

> **Fuente / Source:** [m4riio21/HTB-Academy-Cheatsheets](https://github.com/m4riio21/HTB-Academy-Cheatsheets) (`metasploit.md`) — fecha de acceso: 2026-09-24. Módulo HTB Academy: Using the Metasploit Framework.
> **Autor notas:** Apuromafo (curaduría local).

---

## MSFconsole Commands

| **Command**        | **Description**                                                  |
| :--------------- | :----------------------------------------------------------- |
| `show exploits` | Show all exploits within the Framework.                      |
| `show payloads`  | Show all payloads within the Framework.                      |
| `show auxiliary` | Show all auxiliary modules within the Framework.             |
| `search <name>` | Search for exploits or modules within the Framework.         |
| `info`         | Load information about a specific exploit or module.         |
| `use <name>` | Load an exploit or module (example: use windows/smb/psexec). |
| `use <number>` | Load an exploit by using the index number displayed after the search <name> command. |
| `LHOST`        | Your local host's IP address reachable by the target, often the public IP address when not on a local network. Typically used for reverse shells. |
| `RHOST`        | The remote host or the target. |
| `set <function>` | Set a specific value (for example, LHOST or RHOST). |
| `setg <function>` | Set a specific value globally (for example, LHOST or RHOST). |
| `show options` | Show the options available for a module or exploit.          |
| `show targets` | Show the platforms supported by the exploit.                 |
| `set target <number>` | Specify a specific target index if you know the OS and service pack. |
| `set payload <payload>` | Specify the payload to use. |
| `set payload <number>` | Specify the payload index number to use after the show payloads command. |
| `show advanced` | Show advanced options. |
| `set autorunscript migrate -f` | Automatically migrate to a separate process upon exploit completion. |
| `check` | Determine whether a target is vulnerable to an attack. |
| `exploit` | Execute the module or exploit and attack the target. |
| `exploit -j` | Run the exploit under the context of the job. (This will run the exploit in the background.) |
| `exploit -z` | Do not interact with the session after successful exploitation. |
| `exploit -e <encoder>` | Specify the payload encoder to use (example: exploit –e shikata_ga_nai). |
| `exploit -h` | Display help for the exploit command. |
| `sessions -l` | List available sessions (used when handling multiple shells). |
| `sessions -l -v` | List all available sessions and show verbose fields, such as which vulnerability was used when exploiting the system. |
| `sessions -s <script>` | Run a specific Meterpreter script on all Meterpreter live sessions. |
| `sessions -K` | Kill all live sessions. |
| `sessions -c <cmd>` | Execute a command on all live Meterpreter sessions. |
| `sessions -u <sessionID>` | Upgrade a normal Win32 shell to a Meterpreter console. |
| `db_nmap` | Use Nmap and place results in a database. (Normal Nmap syntax is supported, such as –sT –v –P0.) |

----
## Meterpreter Commands

| **Command**                                                     | **Description**                                                  |
| :---------------------------------------------------------- | :----------------------------------------------------------- |
| `help`                                                      | Open Meterpreter usage help.                                 |
| `run <scriptname>`                                        | Run Meterpreter-based scripts; for a full list check the scripts/meterpreter directory. |
| `sysinfo`                                                   | Show the system information on the compromised target.       |
| `ls`                                                        | List the files and folders on the target.                    |
| `use priv`                                                  | Load the privilege extension for extended Meterpreter libraries. |
| `ps`                                                        | Show all running processes and which accounts are associated with each process. |
| `migrate <proc. id>`                                      | Migrate to the specific process ID (PID is the target process ID gained from the ps command). |
| `use incognito`                                             | Load incognito functions. (Used for token stealing and impersonation on a target machine.) |
| `list_tokens -u`                                            | List available tokens on the target by user.                 |
| `list_tokens -g`                                            | List available tokens on the target by group.                |
| `impersonate_token <DOMAIN_NAME\USERNAME>`               | Impersonate a token available on the target.                 |
| `steal_token <proc. id>`                                  | Steal the tokens available for a given process and impersonate that token. |
| `drop_token`                                                | Stop impersonating the current token.                        |
| `getsystem`                                                 | Attempt to elevate permissions to SYSTEM-level access through multiple attack vectors. |
| `shell`                                                     | Drop into an interactive shell with all available tokens.    |
| `execute -f <cmd.exe> -i`                                 | Execute cmd.exe and interact with it.                        |
| `execute -f <cmd.exe> -i -t`                              | Execute cmd.exe with all available tokens.                   |
| `execute -f <cmd.exe> -i -H -t`                           | Execute cmd.exe with all available tokens and make it a hidden process. |
| `rev2self`                                                  | Revert back to the original user you used to compromise the target. |
| `reg <command>`                                           | Interact, create, delete, query, set, and much more in the target's registry. |
| `screenshot`                                                | Take a screenshot of the target's screen.                    |
| `upload <filename>`                                       | Upload a file to the target.                                 |
| `download <filename>`                                     | Download a file from the target.                             |
| `keyscan_start`                                             | Start sniffing keystrokes on the remote target.              |
| `keyscan_dump`                                              | Dump the remote keys captured on the target.                 |
| `keyscan_stop`                                              | Stop sniffing keystrokes on the remote target.               |
| `getprivs`                                                  | Get as many privileges as possible on the target.            |
| `background`                                                | Run your current Meterpreter shell in the background.        |
| `hashdump`                                                  | Dump all hashes on the target.                               |
| `clearev`                                                   | Clear the event log on the target machine.                   |
| `timestomp`                                                 | Change file attributes, such as creation date (antiforensics measure). |
| `reboot`                                                    | Reboot the target machine.                                   |

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox.

_Fecha de edición: 2026-09-24_
