import csv

with open('dec08.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = '\n')
    input = []
    for line in reader:
        input.extend(line)

def getStep(instr):
    if '+' in instr:
        step = instr.split('+')[1]
    if '-' in instr:
        step = instr.split('-')[1]
    return step 

def getSign(instr):
    if '+' in instr:
        sign = 1
    if '-' in instr:
        sign = -1
    return sign

def findDuplicate (recordCurrent):
    seen = set()
    uniq = [x for x in recordCurrent if x not in seen and not seen.add(x)]    
    return seen

def changeInstr(instr):
    if 'jmp' in instr:
        newInstr = instr.replace('jmp', 'nop')
    if 'nop' in instr:
        newInstr = instr.replace('nop', 'jmp')
    if 'acc' in instr:
        newInstr = instr
    return newInstr


# def mini(index, newInstr):
#     inputA = []
#     inputA.extend(input)
#     inputA[index] = newInstr
#     print(inputA[index])
#     recordCurrentA = []
#     currentA = 0
#     ansA = 0
#     while (1):
#         instrA = inputA[currentA]
#         # print('current', current)
#         stepA = getStep(instrA)
#         signA = getSign(instrA)
#         if 'acc' in instr:
#             ansA = ansA + int(stepA) * signA
#             print('ansA', ansA)
#             currentA = currentA + 1
#         if 'jmp' in instrA:
#             current = currentA + int(stepA) * signA
#         if 'nop' in instrA:
#             currentA = currentA + 1
#         recordCurrentA.append(currentA)
#         print('recordCurrentA', recordCurrentA)
#         print('***********************')
#         if currentA >= 653:
#             print('terminate at last instruction!')
#             break
#         if ansA > 2519:
#             print('stop when ans in mini > 2519')
#             continue

recordTermAns = []

for currentChange in range(len(input)):
    inputA = []
    inputA.extend(input)
    if 'acc' in input[currentChange]:
        continue   
    inputA[currentChange] = changeInstr(input[currentChange])  
    recordCurrent = []
    current = 0
    ans = 0
    
    while (1):
        instr = inputA[current]
        step = getStep(instr)
        sign = getSign(instr)
        if 'acc' in instr:
            ans = ans + int(step) * sign
            current = current + 1
        if 'jmp' in instr:
            current = current + int(step) * sign
        if 'nop' in instr:
            current = current + 1
        recordCurrent.append(current)
        if ans > 2519:
            print('stop when ans in big > ' ,'. current change:', currentChange)
            print(recordCurrent)
            break
        if ans <0 :
            print('stop', '. current change:', currentChange)
            print(recordCurrent)
            break
        if current < 0:
            print('current<0', '. current change:', currentChange)
            print(recordCurrent)
            break
        if current >= 653:
            recordTermAns.append(ans)
            print('terminate at last instruction!', '. current change:', currentChange)
            print(recordCurrent)
            break
    print('+++++++++++++++++++++++++++++++++++')


print('record term ans:',recordTermAns)







# 446, 447, 448, 449, 6, 256, 222, 58, 59, 60, 61, 62, 302, 605, 326, 327, 461, 462, 192, 193, 194, 388, 574, 575, 576, 577, 133, 134, 135, 136, 137, 305, 306, 307, 308, 309, 553, 322, 323, 376, 377, 124, 125, 471, 472, 473, 474, 475, 641, 642, 643, 568, 399, 400, 401, 402, 260, 261, 380, 381, 382, 455, 456, 457, 458, 459, 184, 185, 186, 187, 188, 239, 240, 511, 512, 513, 502, 503, 504, 505, 506, 275, 276, 277, 278, 279, 597, 598, 599, 600, 68, 69, 432, 433, 434, 435, 436, 330, 331, 294, 295, 296, 297, 21, 22, 23, 166, 167, 264, 265, 250, 251, 252, 253, 369, 370, 371, 372, 373, 34, 35, 36, 37, 38, 582, 583, 584, 585, 491, 492, 493, 494, 495, 318, 319, 160, 161, 466, 467, 391, 392, 393, 394, 49, 50, 12, 13, 14, 15, 617, 618, 619, 620, 621, 73, 74, 75, 76, 335, 336, 337, 127, 128, 129, 130, 40, 41, 42, 43, 632, 633, 634, 635, 636, 282, 283, 284, 285, 286, 107, 108, 109, 110, 111, 559, 560, 561, 562, 563, 153, 154, 155, 452, 271, 89, 90, 91, 92, 93, 538, 539, 540, 541, 542, 99, 100, 101, 102,