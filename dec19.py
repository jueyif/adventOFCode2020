import fileinput
import re
import numpy as np
import itertools

input = [line.strip('\n') for line in (fileinput.input(files ='dec19.txt'))]

rulestr = input[:132]
mes = input[134:]

rules = {}

for rule in rulestr:
    id = int(rule.split(':')[0])
    if '|' in rule:
        rule1 = rule.split(': ')[1].split(' | ')[0].split(' ')
        rule2 = rule.split(' | ')[1].split(' ')
        rules[id] = []
        rule11 = []
        rule22 = []
        for i in rule1:
            rule11.append(int(i))
        for i in rule2:
            rule22.append(int(i))
        rules[id].append(rule11)
        rules[id].append(rule22)
    elif 'a' in rule or 'b' in rule:
        rule1 = rule.split(': ')[1].strip('"')
        rules[id] = rule1
    else:
        rule1 = rule.split(': ')[1].split(' ')
        rules[id] = []
        rule11 = []
        for i in rule1:
            rule11.append(int(i))
        rules[id].append(rule11)
    

ida, idb = 0, 0
for x, y in rules.items():
    if y == 'a':
        ida = x   # 54
    if y == 'b':
        idb = x   # 20

def dp(record):
    tempRecord = record.copy()
    for x, y in rules.items():
        count = 0
        for i in y:
            for m in record.keys():
                if i == m:
                    count += 1
        if count == len(y):
            tempRecord[x] = y   
    if 8 in tempRecord.keys():
        return tempRecord
    else:
        return dp(tempRecord)


# xx = np.array(rules[110])
# print(xx)
# print(xx.shape)
# print(xx.shape[1])

# gg = np.array(rules[84])
# print(gg)
# print(gg.shape)
# print(gg.shape[1])

# ff = np.array(rules[49])
# print(ff)
# print(ff.shape)
# print(ff.shape[1])

record = {54:[54], 20:[20]}
possMess = {54:{0: 'a'},20:{0:'b'}}
rules.pop(54)
rules.pop(20)

# print(len(possMess[54]))

# print(5, possMess[5])
# print(96, possMess[96])

while (42 not in possMess.keys()):
    # print(possMess.keys())
    for id, rule in rules.items():
        if np.array(rule).shape == (1,2):
            if rule[0][0] in possMess.keys() and rule[0][1] in possMess.keys():
                possMess[id] = {}
                for i, num in enumerate(rule[0]):
                    possMess[id][num] = possMess[num]
        if np.array(rule).shape == (2,2):
            count = 0
            for numSet in rule:
                if numSet[0] in possMess.keys() and numSet[1] in possMess.keys():
                    count += 1
            if count == 2:
                possMess[id] = {}
                for i, numSet in enumerate(rule):
                    for num in numSet:
                        possMess[id][num] = possMess[num]
        if np.array(rule).shape == (2,1):
            possMess[id] = {}
            if rule[0][0] in possMess.keys() and rule[1][0] in possMess.keys():
                possMess[id][rule[0][0]] = possMess[rule[0][0]]
                possMess[id][rule[1][0]] = possMess[rule[1][0]]

    
# print(0, rules[0])
# print(8, rules[8])
# print(11, rules[11])
# print(31, rules[31])

print(42, rules[42])
print(72, rules[72])
print(60, rules[60])
print(70, rules[70])
print(122, rules[122])
print(22, rules[22])
# print(80, rules[80])
print(99, rules[99])
# print(110, rules[110])
# print(80, possMess[80])

messeger = {54:'a', 20:'b'}

messeger[80] = [possMess[80][20][0]+possMess[80][54][0],possMess[80][54][0]+possMess[80][20][0]]
# print(messeger[80])

messeger[11] = ['a', 'b']
messeger[99] = [possMess[99][20][0]+possMess[99][110][20][0]]

# print('----------------------')

# for id, rule in rules.items():
#     if np.array(rule).shape == (1,2):
#         if rule[0][0] in possMess.keys() and rule[0][1] in possMess.keys():
#             possMess[id] = {}
#             for i, num in enumerate(rule[0]):
#                 possMess[id][num] = possMess[num]
#     if np.array(rule).shape == (2,2):
#         count = 0
#         for numSet in rule:
#             if numSet[0] in possMess.keys() and numSet[1] in possMess.keys():
#                 count += 1
#         if count == 2:
#             possMess[id] = {}
#             for i, numSet in enumerate(rule):
#                 for num in numSet:
#                     possMess[id][num] = possMess[num]
#     if np.array(rule).shape == (2,1):
#         possMess[id] = {}
#         if rule[0][0] in possMess.keys() and rule[1][0] in possMess.keys():
#             possMess[id][rule[0][0]] = possMess[rule[0][0]]
#             possMess[id][rule[1][0]] = possMess[rule[1][0]]

 
# print(possMess)



# for id, rule in rules.items():
#     if np.array(rule).shape == (1,2):
#         if rule[0][0] in possMess.keys() and rule[0][1] in possMess.keys():
#             if len(possMess[rule[0][0]]) == 1 and  len(possMess[rule[0][1]]) == 1:
#                 possMess[id] = possMess[rule[0][0]][0] + possMess[rule[0][1]][0]
#     if np.array(rule).shape == (2,2):
#         count = 0
#         for numSet in rule:
#             if  numSet[0] in possMess.keys() and numSet[1] in possMess.keys():
#                 count += 1
#         if count == 2:
#             possMess[id] = []
#             for numSet in rule:
#                 numSetDimen = (len(possMess[numSet[0]]), len(possMess[numSet[1]]))
#                 if numSetDimen == (1,1):
#                     possMess[id].append(possMess[numSet[0]][0] + possMess[numSet[1]][0])
#                 if  numSetDimen == (2,1):
#                     possMess[id].append(possMess[numSet[0]][0] + (possMess[numSet[1]][0]))
#                     possMess[id].append(possMess[numSet[0]][1] + (possMess[numSet[1]][0]))
#                 if  numSetDimen == (1,2):
#                     possMess[id].append(possMess[numSet[0]][0] + (possMess[numSet[1]][0]))
#                     possMess[id].append(possMess[numSet[0]][0] + (possMess[numSet[1]][1]))
           

# # print(possMess)

# print(2, rules[2])
# print(5, rules[5])
# print(5, possMess[5])

# print(96, possMess[96])


# print('------------------------')

# for id, rule in rules.items():
#     if np.array(rule).shape == (1,2):
#         if rule[0][0] in possMess.keys() and rule[0][1] in possMess.keys():
#             if len(possMess[rule[0][0]]) == 1 and  len(possMess[rule[0][1]]) == 1:
#                 possMess[id] = possMess[rule[0][0]][0] + possMess[rule[0][1]][0]
#     if np.array(rule).shape == (2,2):
#         count = 0
#         for numSet in rule:
#             if  numSet[0] in possMess.keys() and numSet[1] in possMess.keys():
#                 count += 1
#         if count == 2:
#             possMess[id] = []
#             for numSet in rule:
#                 numSetDimen = (len(possMess[numSet[0]]), len(possMess[numSet[1]]))
#                 if numSetDimen == (1,1):
#                     possMess[id].append(possMess[numSet[0]][0] + possMess[numSet[1]][0])
#                 if  numSetDimen == (2,1):
#                     possMess[id].append(possMess[numSet[0]][0] + (possMess[numSet[1]][0]))
#                     possMess[id].append(possMess[numSet[0]][1] + (possMess[numSet[1]][0]))
#                 if  numSetDimen == (1,2):
#                     possMess[id].append(possMess[numSet[0]][0] + (possMess[numSet[1]][0]))
#                     possMess[id].append(possMess[numSet[0]][0] + (possMess[numSet[1]][1]))
           

# print(possMess)




