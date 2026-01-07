'''
Exploitation
Using mgba
Launch the game with mgba Nostalgia.gba -g and connect to GDB using gdb -ex="target remote localhost:2345". Enter the sequence Left Left Z X X X Enter in the game window to reveal the flag.

Using no$gba Debugger
Install no$gba with nocashgba-debuggerand open the ROM. Enter Any arrows 8 times Set a breakpoint at 0200162A cmp r0,4h and press Ctrl in the program window to set r0 = 4h.

When the program reaches 0200162C beq 020016F0 clicking Run Next, change the Z flag to make the branch false. Continue to 02001630 bne 2001660h and change Z again.

At 02001636 cmp r3,0F3h and 0200163B bne 200161Eh, change Z to false one last time. Press [F9] to run the program, and the flag will appear in the game window.

Summary
The Nostalgia Challenge involves exploiting a Game Boy Advance ROM. Using mgba, you can input a specific sequence of controls to reveal the flag. Alternatively, with no$gba debugger, the challenge demonstrates low-level debugging techniques by manipulating CPU flags (Z) to alter the program flow and ultimately reveal the flag in the game window.

HTB{GBA_RuLeZ_DudE}
'''
