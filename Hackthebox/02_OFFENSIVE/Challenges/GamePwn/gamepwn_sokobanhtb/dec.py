'''

1. **Basic gameplay reconnaissance**
   Run `SokobanHTB.exe` and observe the mechanics: move the purple player with WASD, push green boxes, and apparently need to place three boxes on the yellow X tiles to win.

2. **Static analysis – find the main game loop**
   Load the binary in **Ghidra**.

   * From `entry` → `FUN_1400b32e0()` → `FUN_1400045f0()`.
   * From the decompilation of `FUN_1400045f0()` we see: asset loading (`player.png`, `X.png`, `box.png`), map initialization, and a `while (running)` game loop that handles input, collision, box movement, win check, and rendering.
   * During map/object setup, functions are called with parameters like `CONCAT44((float)i, (float)j)`, which strongly suggests **positions are stored as `float` coordinates**.

3. **Cheat Engine – locate player coordinates**
   Attach **Cheat Engine** to the process.

   * Scan for **Unknown initial value** with type **Float**.
   * Move the player right → filter with **Increased value**.
   * Move left → filter with **Decreased value**.
   * Stand still → filter with **Unchanged value**.
   * After several iterations only a few addresses remain.
   * Add them to the list and edit values one by one.
   * The address whose change immediately shifts the player horizontally is the **x-coordinate**.
   * `x_addr + 4` (also `Float`) controls the vertical movement → this is the **y-coordinate**.

4. **Find the outer blocks / boundary coordinates (1024)**

   * Manually change the player’s x-coordinate to a large value to push the character outside the map.
   * Through trial and error, notice that around **x = 1024** the player overlaps an outer block and the game logic quickly snaps him back.
   * This indicates that many outer blocks / boundaries use **1024** as one of their coordinates.

5. **Cheat Engine – scan around 1024 to find block/box arrays**

   * In CE, scan for **Exact value = 1024 (Float)**.
   * Use a few rounds of Increased/Decreased/Unchanged filtering.
   * Add the remaining addresses and edit them; some edits move outer blocks.
   * These addresses form the **coordinate array for blocks/boxes**.

6. **Identify the three “real” boxes used in the win condition**

   * Among those coordinates, modify them one by one and watch which green boxes (the pushable ones inside the map) teleport.
   * This lets you map specific memory addresses to the **three boxes that actually participate in the victory check**.

7. **Teleport boxes onto goal tiles**

   * Determine the coordinates of the three yellow `X` goal tiles (by observation or by testing coordinates).
   * For each of the three real boxes, directly overwrite its `(x, y)` in Cheat Engine with the corresponding goal tile’s coordinates.

8. **Trigger the win logic and reveal the flag**

   * After editing, move the player slightly so the main loop re-evaluates the box positions.
   * All boxes are now “on goals”, so the win condition is satisfied and the game displays the flag:

   ```text
   HTB{H4ck_0r_50k084n_7h3_80x_a34fbe06}
   ```

'''
