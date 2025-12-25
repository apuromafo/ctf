
- **XSS** is a web application vulnerability that lets attackers inject malicious code (usually JavaScript) into input fields that reflect content viewed by other users
     1. Reflected XSS: when the injection is immediately projected in a response; exploited via phishing; targets individual victims 
     2. Stored XSS: malicious script is saved on the server and then loaded for every user who views the affected page

- Protection against XSS
     1. Use textContent instead of inner HTML
     2. Make cookies inaccessible to JS
     3. Sanitise input/output and encode

  
  

## Answers: 
- Which type of XSS attack requires payloads to be persisted on the backend? : `stored`
- What's the reflected XSS flag? : `THM{Evil_Bunny}`
- What's the stored XSS flag? : `THM{Evil_Stored_Egg}`
