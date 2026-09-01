# CTF Category Deep-Dive: Forensics

**ID Original:** no disponible
**Slug:** ctf-category-deep-dive-forensics
--------------------

Of all the categories you will encounter in a Jeopardy-style Capture The Flag competition, forensics is arguably the broadest. A forensics challenge might ask you to pull author metadata from a Word document, detect an image hidden inside an audio file's spectrogram, reconstruct what happened on a compromised system from a memory dump, or reassemble a transferred file from a packet capture. The only thing every challenge has in common is that the answer is already there; you just need to know how to look.
That breadth is what makes forensics so valuable to learn. The techniques map directly onto real incident response work, and the toolset crosses over almost entirely with what professional analysts use in actual investigations. This guide covers the major forensics sub-categories you will encounter in CTFs, the core tools and concepts each one requires, and the TryHackMe rooms that build the skills most efficiently.
What forensics actually covers in a CTF
The forensics category is defined loosely across different competition formats, but most challenges fall into one of five areas: file analysis and metadata, steganography (data hidden inside other data), memory forensics, network forensics and packet analysis, and disk or file system forensics. Some challenges combine multiple areas, requiring you to chain techniques before the flag reveals itself.
What forensics does not usually include, despite some overlap in tools, is live exploitation or privilege escalation. The defining characteristic is that you are given static data - a file, a dump, a capture - and must extract or reconstruct information from it. The challenge is analytical rather than interactive.
Forensics is the CTF category that most directly reflects what blue team analysts do professionally. The tools, methodology, and habits of mind you develop here carry directly into SOC and DFIR roles.
File analysis and metadata
Every file carries information beyond its visible content. Timestamps, embedded author data, GPS coordinates, software version strings, creation tools, and comment fields are all routinely preserved in file metadata, and they are frequently where CTF challenge designers hide flags or critical clues. Equally common is the technique of mismatching file extensions; a file named image.jpg that is actually a PNG, ZIP, or something else entirely at the byte level.
File analysis is almost always the first step in any forensics challenge. Before applying any specialised tool, establishing what a file actually is and what it contains is essential.
Core tools  |  exiftool · file · strings · binwalk
exiftool reads and displays metadata from virtually any file format, making it the standard first pass on any file you receive in a challenge. The file command identifies a file's true type from its magic bytes rather than its extension. strings extracts human-readable text embedded in binary files — useful when a flag or clue has been appended as plain text. binwalk scans files for embedded content and known file signatures, and can automatically extract nested files. A JPEG with a ZIP archive appended to it is a classic forensics challenge structure; binwalk will find and carve it out.
Start here: Intro to Digital Forensics (includes metadata analysis with exiftool and pdfinfo)
Pro tip: When you receive any challenge file, run all four tools immediately: file to confirm the type, exiftool for metadata, strings for embedded text, and binwalk for hidden nested content. Many flags are found in under two minutes this way.
Steganography
Steganography is the practice of hiding data inside other data. In CTFs it appears constantly, far more than in real-world security work, because it produces puzzles that are satisfying to solve. The cover file is most commonly an image or audio file, but anything that tolerates redundant or encoded data can serve as a carrier.
The challenge with steganography is that unlike encryption, which announces itself, a steganographically modified file may look and behave completely normally. Detection requires methodically trying different tools and techniques until something surfaces.
Image steganography  |  steghide · zsteg · stegoveritas · exiftool
Image-based stego challenges typically use one of several embedding techniques. LSB (least significant bit) encoding hides data in the low-order bits of pixel colour values, invisible to the eye but detectable by tools like zsteg (for PNG and BMP files) and stegoveritas. Password-protected content embedded with steghide is extracted with the correct passphrase, which may itself require finding first — often in EXIF metadata. The TryHackMe Steganography room (CC: Stego) covers the core toolset including steghide, zsteg, exiftool, and stegoveritas across both image and audio formats.
Practice room: CC: Steganography
Audio steganography  |  Sonic Visualiser · steghide · Morse analysis
Audio files carry their own steganographic possibilities. The most common CTF technique is spectrogram stego, where data (often an image or text) is encoded into the frequency spectrum of an audio file and becomes visible when the waveform is viewed as a spectrogram. Sonic Visualiser is the standard tool for this: adding a spectrogram layer to a WAV or MP3 file will reveal hidden images, QR codes, or text patterns that are completely inaudible on playback. The Musical Stego room chains several techniques: finding a spectrogram-encoded QR code, extracting audio content from that link, decoding Morse code, and then using the recovered passphrase with steghide to retrieve the final flag. It is an excellent example of how forensics challenges layer steps.
Practice room: Musical Stego
Multi-layer stego puzzles  |  Full technique chains
Harder stego challenges combine multiple techniques sequentially, requiring you to work through encoding layers before the flag appears. The Cicada 3301 Vol. 1 room recreates the famous puzzle format: an audio file hides a spectrogram image, which reveals text that unlocks further extraction. The c4ptur3-th3-fl4g room works through encoding recognition (binary, Base64, hexadecimal, ROT13, ROT47, Morse), spectrogram analysis, and steganography extraction in sequence, building the recognition patterns you need for competition forensics.
Practice rooms: Cicada 3301 Vol. 1 | c4ptur3-th3-fl4g
Pro tip: When stuck on an image stego challenge, work through tools in order: exiftool (metadata), strings (embedded text), binwalk (nested files), zsteg (LSB for PNG/BMP), and steghide with common passwords. For audio, always open in Sonic Visualiser and check the spectrogram before anything else.
File header and format manipulation
A significant subset of forensics challenges involves files that have been deliberately corrupted or disguised by modifying their header bytes. Since operating systems and most tools identify file types from the first few bytes (the file signature or 'magic bytes') rather than the extension, changing a file's extension or corrupting its signature is a common puzzle mechanism.
Reading and editing file headers with a hex editor is a foundational forensics skill. Knowing the magic bytes for common formats, JPEG (FF D8 FF), PNG (89 50 4E 47), ZIP (50 4B 03 04), PDF (25 50 44 46), lets you identify disguised files and restore their structure.
Key room  |  hexeditor · exiftool · file
The Madness room is an excellent example of this class of challenge. An image file is presented with a JPEG extension but PNG magic bytes — it takes hex editing to restore the correct header before steghide can extract the embedded content. Recognising the mismatch between what exiftool reports and what the file command shows is the key initial step, and a pattern that appears in CTF forensics regularly.
Practice room: Madness
Memory forensics
Memory forensics challenges provide a RAM dump from a compromised or running system and ask you to extract artefacts from it. In competition settings, this typically means identifying running processes, network connections, executed commands, or recovering specific files or strings from memory.
The technique crosses directly into professional DFIR work. Memory forensics is where evidence of fileless malware, injected code, and credential theft often lives, and the CTF format is an effective way to build the Volatility workflows that field investigators rely on.
Volatility  |  Core tool for all memory forensics challenges
Volatility is the standard tool for CTF memory forensics. In Volatility 3, the workflow starts by running windows.info to confirm the OS version, then applying plugins systematically: windows.pslist or windows.pstree to list processes and identify suspicious parent-child relationships, windows.cmdline to see what commands were run, windows.netscan for network activity, and windows.malfind to detect injected code. The TryHackMe Volatility room walks through exactly this workflow against a compromised Windows memory dump, building the muscle memory that makes competition memory forensics challenges feel familiar.
Practice room: Volatility | Memory Forensics (CTF room)
Pro tip: In Volatility 3, the syntax changed significantly from version 2. Plugins now follow the format windows.pluginname rather than --profile plus plugin name. If you are working through older CTF writeups, be aware that commands will differ.
Network forensics and PCAP analysis
Network forensics challenges provide a packet capture file and ask you to extract transferred data, identify credentials, find encoded payloads, or reconstruct what happened during a session. The flag is typically embedded in the traffic itself: in an HTTP response body, transferred over FTP, encoded in DNS queries, or hidden in the payload of an unusual protocol.
Wireshark workflow  |  Core PCAP analysis tool
Wireshark is the primary tool for PCAP-based forensics. The standard CTF workflow begins with Statistics > Protocol Hierarchy to understand the shape of the traffic, then follows interesting conversations using Follow TCP Stream or Follow HTTP Stream. For file extraction, File > Export Objects > HTTP will pull any files transferred over HTTP. DNS-based challenges often encode data in query subdomains; sorting by DNS queries and looking for unusual or Base64-like subdomain strings is the tell. TryHackMe's three-part Wireshark sequence covers this comprehensively: Wireshark: The Basics for interface and filter fundamentals, Wireshark: Packet Operations for statistical analysis and display filtering, and Wireshark: Traffic Analysis for anomaly detection and applied investigation.
Practice rooms: Wireshark: The Basics | Wireshark: Traffic Analysis
Pro tip: For PCAP challenges without an obvious starting point, run tshark -r capture.pcap -z conv,tcp to list all TCP conversations by byte volume. The largest conversation often contains the transferred file or the flag payload.
Disk and file system forensics
Disk forensics challenges are less common in CTF settings but appear in more advanced competitions and in the DFIR-oriented rooms on TryHackMe. They involve analysing a disk image to recover deleted files, reconstruct user activity, identify installed software, or surface evidence of malicious behaviour.
Autopsy  |  Disk image analysis in a CTF context
Autopsy automates much of the artefact extraction that would otherwise require manual file system parsing. In the context of both CTF challenges and the TryHackMe Disk Analysis room , the investigation pattern is consistent: load the disk image, let the ingest modules run, then work through Operating System Information, User Accounts, Recent Documents, Browser History, and Installed Programs to answer the challenge questions. Autopsy's keyword search also makes it possible to scan the entire image for specific strings, which is often the most direct route to a flag.
Practice room: Disk Analysis and Autopsy
Room reference
A curated starting list for building CTF forensics skills on TryHackMe.
Room
Difficulty
Sub-category
Key tools
Intro to Digital Forensics
Easy
File analysis
exiftool, pdfinfo, strings
CC: Steganography
Easy
Image & audio stego
steghide, zsteg, stegoveritas
c4ptur3-th3-fl4g
Easy
Encoding + stego
Base64, hex, ROT, spectrograms
Musical Stego
Medium
Audio stego
Sonic Visualiser, steghide
Cicada 3301 Vol. 1
Medium
Multi-layer stego
Sonic Visualiser, steghide
Madness
Easy
File header analysis
hexeditor, exiftool, steghide
Memory Forensics
Easy
Memory forensics CTF
Volatility
Volatility
Medium
Memory forensics
Volatility 2 & 3
Wireshark: The Basics
Easy
Network forensics
Wireshark
Wireshark: Traffic Analysis
Medium
Network forensics
Wireshark
Disk Analysis and Autopsy
Medium
Disk forensics
Autopsy
How to build a forensics methodology
Experienced CTF players approach forensics challenges systematically rather than trying tools at random. The methodology matters because forensics challenges rarely announce what technique they use, and working from a consistent checklist ensures you do not miss the obvious answer while searching for something complex.
For any unknown file: confirm the file type with the file command, read metadata with exiftool, search for readable text with strings, and scan for embedded content with binwalk. This takes under a minute and eliminates most easy forensics challenges immediately. For images, add zsteg and try steghide with an empty passphrase before assuming a password is required. For audio files, open in Sonic Visualiser and check the spectrogram first.
For PCAP files: check the protocol hierarchy, follow the largest TCP stream, export HTTP objects, and look for anything encoded in DNS queries. For memory dumps: run windows.info, list processes with windows.pslist, review network connections with windows.netscan, then dig into command history.
CyberChef ( gchq.github.io/CyberChef ) is essential for forensics challenges involving encoding. It supports Base64, hex, ROT variants, XOR, and hundreds of other transformations, and its 'Magic' operation will try to auto-detect and decode an unknown encoding. Keep it open in a tab during every competition.
From CTF forensics to professional work
CTF forensics is not a perfect simulation of professional investigation. Competition puzzles tend toward steganography and encoding more than real incidents do, and real DFIR work involves much more procedural and legal context than a timed challenge. But the tool proficiency transfers almost completely.
Analysts who can work efficiently with Volatility, Wireshark, Autopsy, and file analysis tools are exactly what hiring managers look for at the entry and mid levels. TryHackMe's DFIR module and the Advanced Endpoint Investigations path bridge the gap between CTF-style forensics practice and professional investigation work, applying the same tools to realistic incident scenarios rather than designed puzzles.
The habits built through forensics competition practice - working systematically, documenting what you tried, understanding why a technique did or did not work - are precisely the habits that experienced investigators consider essential and which are hard to teach through any other format.
Build the methodology. Learn the tools. Capture the flag.