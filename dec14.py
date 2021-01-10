import csv
import re

with open('dec14.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = '\n')
    input = []
    for line in reader:
        input.extend(line)

# print(input[0:6])

def binaryToDecimal(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal*2 + int(digit)
    return decimal

# def decimalToBinary(decimal):
#     binary = ''
#     if decimal > 1:
#         print(decimal)
#         decimalToBinary(decimal // 2)
#     print(decimal % 2, end='')
    # binary = binary + str(decimal % 2)
    # return binary
# print(decimalToBinary(5))

dictMem = {}
for cmd in input:
    if 'mem' in cmd:
        address = int(cmd.split('[')[1].split(']')[0])
        value = int(cmd.split('=')[1].strip())
        dictMem[address] = value

p2 = 0




# result = ['0', '1', '0', '1', '1', '1', '1', '1', '1', '0', '0', '1', '1', '0', '1', '0', 'X', '1', '1', '0', '1', '0', '1', '1', '1', '1', 'X', '1', '0', '1', '0', '1', '1', 'X', 'X', '0']

# ww = ['x','x','x','x']



for cmd in input:
    if 'mask' in cmd: 
        print(cmd)
        mask = cmd.split('=')[1].strip()
        print('Refresh mask:',mask)
    elif 'mem' in cmd:
        print(cmd)
        address = int(cmd.split('[')[1].split(']')[0])
        value = int(cmd.split('=')[1].strip())
        addBinary = list("{0:b}".format(address))
        addBinary36 = ['0' for x in range(36)]
        for i in range(1, len(addBinary)+1):
            addBinary36[-i] = addBinary[-i]
        # print('addBinary36:', addBinary36)
        result = ['0' for x in range(36)]
        
        for i in range(1, 37):
            # print(i)
            # print((template[-i]), (mask[-i]))
            if mask[-i] == '0':
                result[-i] = addBinary36[-i]
            elif mask[-i] == '1':
                result[-i] = '1'
            elif mask[-i] == 'X':
                result[-i] = 'X'
        # print('result:', result)
        
        countX = 0
        for j in result:
            if j == 'X':
                countX += 1
        # print('countX:', countX)
        last = 2 ** countX

        binCombList = []
        for combination in range(last):
            qq = format(combination, 'b')
            binary = list(str(qq))
            if len(binary) < countX:
                temp = ['0' for i in range(countX-len(binary))]
                temp.extend(binary)     
                binCombList.append(temp)      
            binCombList.append(binary)

        for i in binCombList:
            if len(i) < countX:
                binCombList.remove(i)
        # print(binCombList)

        xPos = []
        for i, number in enumerate(result):
            if number == 'X':
                xPos.append(i)
        # print(xPos)

        for j, comb in enumerate(binCombList):
            # print('comb:', comb)
            for i, k in enumerate(comb):
                result[int(xPos[i])] = comb[i]
            # print(result)    
            dictMem[binaryToDecimal(result)] = value

        


for i in dictMem.values():
    p2 += i
print(p2)



# 3412579074999 high








# sample=['mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X', 'mem[8] = 11', 'mem[7] = 101' , 'mem[8] = 0']


# for cmd in input:
#     if 'mask' in cmd: 
#         print(cmd)
#         mask = cmd.split('=')[1].strip()
#         print('Refresh mask:',mask)
#     elif 'mem' in cmd:
#         print(cmd)
#         address = int(cmd.split('[')[1].split(']')[0])
#         value = list("{0:b}".format(int(cmd.split('=')[1].strip())))
#         template = ['0' for x in range(36)]
#         for i in range(1, len(value)+1):
#             template[-i] = value[-i]
#         print('template:',template)
#         result = [0 for x in range(36)]
        
#         for i in range(1, 37):
#             # print(i)
#             # print((template[-i]), (mask[-i]))
#             if mask[-i] == 'X':
#                 result[-i] = template[-i]
#             else: result[-i] = mask[-i] 
        
#         decRes = binaryToDecimal(result)
#         dictMem[address] = decRes
#         print('address:', address)
#         print('value:', value)
#         print('mask:', mask)
#         print('result:',result)
#         print('decRes:', decRes)
#         print(dictMem)
#     print('----------------------------')

# # print(dictMem)

# p1 = 0
# for x in dictMem.values():
#   print(x)
#   p1 += x

# print(p1)

