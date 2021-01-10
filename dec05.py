import csv
import math

with open('dec05.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = '\n')
    input = []
    for row in reader:
        input.extend(row)
length = len(input)

seatList = []

for s in input:
    binaryRow  = s.replace('F','0').replace('B','1')[0:7]
    decimalRow = 0
    for digit in binaryRow:
        decimalRow = decimalRow*2 + int(digit)
    binaryCol  = s.replace('L','0').replace('R','1')[7:10]
    decimalCol = 0
    for digit in binaryCol:
        decimalCol = decimalCol*2 + int(digit)
    seatID = decimalRow * 8 + decimalCol
    seatList.append(seatID)

print('Part 1 Answer:', max(seatList))

seatList.sort()

qq = range(40,941)

ans = [x for x in qq if x not in seatList]
print('Part 2 Answer:', ans)



