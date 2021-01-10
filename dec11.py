import csv

with open('dec11.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = '\n')
    input = []
    for line in reader:
        input.extend(line)

# row:97 col: 98 
# sample: 10, 10
rowInput = len(input)
# print(rowInput)
# qq = input[0]
# print(qq)
colInput = len(input[0])
print('row:', len(input))
print('col:',len(input[0]))



def getPos(row, col):
    pos =[]
    # any
    if row in range(1,rowInput-1) and col in range(1, colInput-1):
        pos = [(row-1, col),(row, col-1),(row+1, col),(row, col+1),(row-1, col-1),(row+1, col+1),(row+1, col-1),(row-1, col+1)]
    # first row
    if row == 0 and col in range(1,colInput-1):
        pos = [(row, col-1),(row+1, col),(row, col+1),(row+1, col+1),(row+1, col-1)]   
    # first col
    if row in range(1,rowInput-1) and col == 0:
        pos = [(row, col+1),(row+1, col),(row-1, col),(row+1, col+1),(row-1, col+1)]
    # last row 
    if row == rowInput-1 and col in range(1,colInput-1):
        pos = [(row, col-1),(row, col+1),(row-1, col-1),(row-1, col+1),(row-1, col)]
    # last col
    if row in range(1,rowInput-1) and col == colInput-1:
        pos = [(row, col-1),(row+1, col),(row-1, col),(row+1, col-1),(row-1, col-1)]    
    # first row first col
    if row == 0 and col == 0:
        pos = [(1, 0),(0, 1),(1, 1)]
    # last row last col
    if row == rowInput-1 and col == colInput-1:
        pos = [(row-1, col),(row, col-1),(row-1, col-1)]
    # first row last col
    if row == 0 and col == colInput-1:
        pos = [(1, colInput-1),(1, rowInput-1),(0, rowInput-1)]
    # last row first col
    if row == rowInput-1 and col == 0:
        pos = [(row-1, col),(row, 1),(row-1, 1)]
    return pos

def emptyToOccu(pos, matrix):
    countEmpty = 0
    for (r,c) in pos:
        if matrix[r][c] == '#':
            countEmpty += 1
    if countEmpty == 0:
        return True
    else:
        return False

def occuToEmpty(pos, matrix):
    countOccu = 0
    for (r,c) in pos:
        if matrix[r][c] == '#':
            countOccu = countOccu + 1
    if countOccu >= 4:
        return True
    else:
        return False

def loop(layout):
    record = [[0 for i in range(colInput)] for j in range(rowInput)]
    for i in range(rowInput):
        for j in range(colInput):
            pos = getPos(i,j)
            if layout[i][j] == 'L':
                if emptyToOccu(pos, layout):
                    record[i][j] = 1
                else: 
                    record[i][j] = 0
            if layout[i][j] == '#':
                if occuToEmpty(pos, layout):
                    record[i][j] = 1
                else: 
                    record[i][j] = 0 
    newLayout = [[0 for i in range(colInput)]  for j in range(rowInput)]
    for i in range(rowInput):
        for j in range(colInput):
            if record[i][j] == 1 and layout[i][j] == 'L':
                newLayout[i][j] = '#'
            if record[i][j] == 1 and layout[i][j] == '#':
                newLayout[i][j] = 'L'
            if record[i][j] == 0:
                newLayout[i][j] = layout[i][j]
    print(newLayout)
    print('-------------------')
    return loop(newLayout)


# loop(input)
    

with open('dec11sult.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = '\n')
    result = []
    for line in reader:
        result.extend(line)

# print(result[0])

p1= 0
for i in result[0]:
    if i == '#':
        p1 += 1

print(p1)



# ww = [[0 for i in range(colInput)] for j in range(rowInput)]
# for i in range(colInput):
#     for j in range(rowInput):
#         pos = getPos(i,j)
#         if input[i][j] == 'L':
#             if emptyToOccu(pos, input):
#                 ww[i][j] = 1
#             else: 
#                 ww[i][j] = 0
#         if input[i][j] == '#':
#             if occuToEmpty(pos, input):
#                 ww[i][j] = 1
#             else: 
#                 ww[i][j] = 0    

# firRound = [[0 for i in range(colInput)]  for j in range(rowInput)]
# for i in range(rowInput):
#     for j in range(colInput):
#         if ww[i][j] == 1 and input[i][j] == 'L':
#             firRound[i][j] = '#'
#         if ww[i][j] == 1 and input[i][j] == '#':
#             firRound[i][j] = 'L'
#         if ww[i][j] == 0:
#             firRound[i][j] = input[i][j] 

# print(firRound)

# ww2 = [[0 for i in range(colInput)] for j in range(rowInput)]
# for i in range(colInput):
#     for j in range(rowInput):
#         pos = getPos(i,j)
#         if firRound[i][j] == 'L':
#             if emptyToOccu(pos, firRound):
#                 ww2[i][j] = 1
#             else: 
#                 ww2[i][j] = 0
#         if firRound[i][j] == '#':
#             if occuToEmpty(pos, firRound):
#                 ww2[i][j] = 1
#             else: 
#                 ww2[i][j] = 0            


# secRound = [[0 for i in range(colInput)]  for j in range(rowInput)]
# for i in range(rowInput):
#     for j in range(colInput):
#         if ww[i][j] == 1 and firRound[i][j] == 'L':
#             secRound[i][j] = '#'
#         if ww[i][j] == 1 and firRound[i][j] == '#':
#             secRound[i][j] = 'L'
#         if ww2[i][j] == 0:
#             secRound[i][j] = firRound[i][j]

# print('----------------------')
# print(secRound)

