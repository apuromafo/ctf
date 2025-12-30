- Race condition vulnerability in web applications
- Race condition happens when
     1. Two or more actions run at the same time
     2. The result depends on which finishes first
     3. The application lacks proper synchronisation
 
- Types of race conditions
     1. TOCTOU (Time-of-Check to Time-of-Use) : a program checks something first and uses it later, but the data changes in between. This means what was true at the time of the check might no longer be true when the action happens
     2. Shared Resource Race : when multiple users or systems try to change the same data simultaneously without proper control; final result depends on which one finishes last
     3. Atomicity Violation : When parts of a process run separately, another request can sneak in between and cause inconsistent results

- Race conditions exploit timing

## Answers: 
- What is the flag value once the stocks are negative for SleighToy Limited Edition? : `THM WINNER_OF_R@CE007}`
- Repeat the same steps as were done for ordering the SleighToy Limited Edition. What is the flag value once the stocks are negative for Bunny Plush (Blue)? : `THM{WINNER_OF_Bunny_R@ce]` 
