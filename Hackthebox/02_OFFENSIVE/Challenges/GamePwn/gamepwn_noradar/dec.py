import struct,math
with open('./noradar','rb') as f:
    data=f.read()
    
start=20512
length=191
coords=[struct.unpack('<dd',data[start+i*16:start+i*16+16]) for i in range(length)]
points=coords[3:]
# group
groups=[]
cur=[]
for x,y in points:
    if (x,y)==(0.0,0.0):
        if cur:
            groups.append(cur)
            cur=[]
    else:
        cur.append((int(x), int(y)))
if cur:
    groups.append(cur)
print('number of glyphs',len(groups))

# function to draw ascii
from itertools import pairwise


def draw(group):
    # 8x8 grid from (1..7) maybe; we will allocate 8x8 index 0..7 for x and y; but points may use 1..7 inclusive; we'll map 1->0 etc.
    grid=[[' ' for _ in range(8)] for __ in range(8)]
    prev=None
    for (x,y) in group:
        if prev is not None:
            x0,y0=prev; x1,y1=x,y
            # draw line inclusive; handle horizontal or vertical or diagonal?; we assume horizontal or vertical lines
            if x0==x1:
                # vertical line from y0 to y1
                step=1 if y1>=y0 else -1
                for yy in range(y0,y1+step,step):
                    xx=x0; # mark
                    if 1<=xx<=7 and 1<=yy<=7:
                        grid[7-yy][xx]= '#'
            elif y0==y1:
                step=1 if x1>=x0 else -1
                for xx in range(x0,x1+step,step):
                    yy=y0
                    if 1<=xx<=7 and 1<=yy<=7:
                        grid[7-yy][xx]='#'
            else:
                # diagonal? we handle step of 1 along x and y simultaneously
                stepx=1 if x1>=x0 else -1
                stepy=1 if y1>=y0 else -1
                xx=x0; yy=y0
                while True:
                    if 1<=xx<=7 and 1<=yy<=7:
                        grid[7-yy][xx]='#'
                    if (xx,yy)==(x1,y1):
                        break
                    xx+=stepx; yy+=stepy
        prev=(x,y)
    return grid


# draw each glyph and print ascii lines plus index
for idx,g in enumerate(groups):
    grid=draw(g)
    print('Glyph',idx)
    for row in grid:
        print(''.join(row[1:8]))
    print()

#HTB{GR33N_CUB3_ST4LKER}
