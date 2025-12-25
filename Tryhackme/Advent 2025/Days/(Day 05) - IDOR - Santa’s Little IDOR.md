- IDOR(insecure direct object reference): type of vulnerability
- web server should check to ensure you are allowed to view data (ex: `https://awesome.website.thm/TrackPackage?packageID=1001`, you would just have to change the ID to get information that ur not supposed to be able to access)

- Authentication: essentially, verification of who you are 
- Authorization: verification of your permissions

- authentication first, then authorization
- `inspect` a web page to search for vulnerabilities
- UUID (universal unique identifier): [https://www.uuidtools.com/decode](url)


privilege escalation: 
- vertical privilege escalation: gaining access to more features
- horizontal privilege escalation: gain access to features you are authorized to use, but data you are not supposed to have access to (like someone else's details) 


## Answers:
- What does IDOR stand for? : `Insecure Direct Object Reference`
- What type of privilege escalation are most IDOR cases? : `Horizontal`
- Exploiting the IDOR found in the view_accounts parameter, what is the user_id of the parent that has 10 children? : `15`
