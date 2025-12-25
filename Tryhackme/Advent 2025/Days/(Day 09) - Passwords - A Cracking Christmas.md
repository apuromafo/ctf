- Ways of guessing the password that protects a file
     1. Dictionary Attacks: Use a predefined list of potential passwords (AKA wordlist); useful in case of weak or common passwords
     2. Mask Attacks: Basically, a Brute-force attack, but limits gueasses to a specific format to make it faster
     3. Brute-force Attacks: systematically tries every possible combination of characters until the right one is found

- Common wordlists
     1. rockyou.txt
     2. common-passwords.txt

- You can use GPU-accelerated cracking when possible (in cases such as MD5, SHA-1, SHA-256, NTLM)
- Tools to Use (pick one based on file type)
  1. PDF: pdfcrack, john (via pdf2john)
  2. ZIP: fcrackzip, john (via zip2john)
  3. General: john (very flexible) and hashcat (GPU acceleration, more advanced)

- Tools and indicators for password cracking:
    1. Binaries and aliases: john, hashcat, fcrackzip, pdfcrack, zip2john, pdf2john.pl, 7z, qpdf, unzip, 7za, perl invoking pdf2john.pl.
    2. Command‑line traits: --wordlist, -w, --rules, --mask, -a 3, -m in Hashcat, references to rockyou.txt, SecLists, zip2john, pdf2john.
    3. Potfiles and state: ~/.john/john.pot, .hashcat/hashcat.potfile, john.rec.
 
- Steps to take when suspicious activity or a possible password-cracking on a machine is detected:
    1. Isolate the system if real malicious activity is suspected; ignore or suppress alerts if it’s just a lab or training machine.
    2. Collect evidence early (running processes, memory, GPU usage, open files, and the protected file involved).
    3. Preserve cracking artefacts like the working folder, wordlists, hash files, and command history.
    4. Check impact by seeing which files or passwords were successfully cracked and whether there was further access or data theft.
    5. Decide intent by identifying who ran the activity and whether it was authorised; escalate if it wasn’t.
    6. Fix and prevent by changing compromised passwords/keys, enforcing MFA, and educating users to keep such tools only in approved lab environments.

## Answers: 
- What is the flag inside the encrypted PDF? : `THM{Cr4ck1ng_PDFs_1s_34$y}`
- What is the flag inside the encrypted zip file? : `THM{Cr4ck1n6_z1p$_1s_34$yyyy}`
