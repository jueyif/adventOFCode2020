import csv

with open('dec03.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    input = []
    for row in reader:
        input.append(row)

for row in input:
    row[0] = list(row[0])

inputHeight = len(input)
inputWidth = len(input[0][0])

for i in range(inputHeight):
    for j in range(10):
        input[i][0].extend(input[i][0])

# Right 3, down 1
countA = 0
for row in range(inputHeight):
    for c in input[row][0][3*row]:
        if c == '#':
            countA = countA + 1
print('Part 1 answer:', countA)

# Right 1, down 1
countB = 0
for row in range(inputHeight):
    for c in input[row][0][row]:
        if c == '#':
            countB = countB + 1
print(countB)

# Right 5, down 1
countC = 0
for row in range(inputHeight):
    for c in input[row][0][5*row]:
        if c == '#':
            countC = countC + 1
print(countC)

# Right 7, down 1
countD = 0
for row in range(inputHeight):
    for c in input[row][0][7*row]:
        if c == '#':
            countD = countD + 1
print(countD)

# Right 1, down 2
countE = 0
for row in range(int(inputHeight/2+1)):
    for c in input[2*row][0][row]:
        if c == '#':
            countE = countE + 1
print(countE)

print('Part 2 Answer:', countA*countB*countC*countD*countE)