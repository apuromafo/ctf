- Windows Registry -> brain of the OS
- It stores
    1. System configuration
    2. Installed programs
    3. User activity
    4. Startup behavior
    5. Hardware and security settings

- Registry data is stored in multiple binary files called Hives.
  <img width="1233" height="686" alt="Screenshot 2025-12-23 at 6 36 54 PM" src="https://github.com/user-attachments/assets/d2e6cd4b-904e-48f3-a013-b8e5459c0b42" />
<img width="1233" height="244" alt="Screenshot 2025-12-23 at 6 37 14 PM" src="https://github.com/user-attachments/assets/14cef1ff-faf9-483c-aa74-5eb21b72b9a8" />

- Registry editor -> views registry on a live system; can't safely analyze compromised systems; can't open offline hives

  ![Screenshot 2025-12-23 at 6 38 46 PM](https://github.com/user-attachments/assets/118b25ee-758a-4fbc-ae43-441775781c02)
<img width="1236" height="680" alt="Screenshot 2025-12-23 at 6 39 44 PM" src="https://github.com/user-attachments/assets/94cd5f72-4b9e-4cfb-94ae-d077c93b6bb8" />
<img width="1236" height="295" alt="Screenshot 2025-12-23 at 6 39 53 PM" src="https://github.com/user-attachments/assets/3471c1a5-d26b-455c-889a-c53f0f3a21c9" />

- **Registry explorer**

## Answers: 
- What application was installed on the dispatch-srv01 before the abnormal activity started? : `DroneManager Updater`
- What is the full path where the user launched the application (found in question 1) from? : `C:\Users\dispatch.admin\Downloads\DroneManager_Setup.exe`
- Which value was added by the application to maintain persistence on startup? : `*C:\Program Files\DroneManager\dronehelper.exe* --background`
