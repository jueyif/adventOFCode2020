import fileinput
import re
import numpy as np
import itertools
import math
from decimal import Decimal

sq = 0.5 * math.sqrt(3)
hf = 0.5
sq = round(sq, 3)

input = [line.strip('\n') for line in (fileinput.input(files ='dec24.txt'))]
newInput = []

for line in input:
    newline = []
    i = 0
    while (i < len(line)):
        if line[i] == 'e':
            char = line[i]
            i += 1
        elif line[i] == 'w':
            char = line[i]
            i += 1
        elif line[i] == 's':
            if line[i+1] == 'e':
                char = 'se'
                i += 2 
            else:
                char = 'sw'
                i += 2
        elif line[i] == 'n':
            if line[i+1] == 'w':
                char = 'nw'
                i += 2
            else:
                char = 'ne'
                i += 2
        newline.append(char)
    newInput.append(newline)

endCoor = []
for line in newInput:
    x, y = 0, 0
    for dire in line:
        if dire == 'e':
            x += 1
        elif dire == 'ne':
            x += hf
            y += sq
        elif dire == 'nw':
            x -= hf
            y += sq
        elif dire == 'w':
            x -= 1
        elif dire == 'sw':
            x -= hf
            y -= sq
        elif dire == 'se':
            x += hf
            y -= sq
    x = round(x, 3)
    y = round(y, 3)
    endCoor.append((x,y))

unique = []
multi = []
for coor in endCoor:
    if coor not in unique:
        unique.append(coor)
    else:
        unique.remove(coor)


for coor in endCoor:
    if coor not in unique:
        multi.append(coor)

ans = len(unique)

for coor in multi:
    count = 0
    for countCoor in multi:
        if countCoor == coor:
            count += 1
    if count % 2 == 1:
        ans += 1

# part 1
print('Part 1: ', ans)




