import fileinput
import re
import numpy

input = [line.strip('\n') for line in (fileinput.input(files ='dec16.txt'))]

yourTicket = input[22].split(',')
nearby = input[25:len(input)]
rules = input[:20]

ran = []
for i in rules:
    text = re.findall(r'\d{1,3}\-\d{1,3}', i)
    ran.append(text[0].split('-'))
    ran.append(text[1].split('-'))


invalid = []

# for i in yourTicket:
#     count = 0
#     for j, x in enumerate(ran):
#         x[1] = int(x[1]) 
#         x[0] = int(x[0])
#         if x[0] <= int(i) and int(i) <= x[1]:
#             print('PASS!', i, x, count)
#             break
#         else:
#             count += 1
#             print(i, x, count)
#             if count == len(ran):
#                 print(i, x)
#                 invalid.append(i)


newNear = []
for i, nn in enumerate(nearby):
    nearby[i] = nearby[i].split(',')
    for j, oo in enumerate(nearby[i]):
        nearby[i][j] = int(oo)
    newNear.append(nearby[i])
    # newNear.extend(int(x) for x in nearby[i])
    

# newNear1 = []
# for i, nn in enumerate(nearby):
#     nearby[i] = nearby[i].split(',')
#     newNear.extend(int(x) for x in nearby[i])
#     # newNear.append(nearby[i])

# print(newNear)

valid = newNear

for j, listt in enumerate(newNear):
    for i, nn in enumerate(listt):
        count = 0   
        for k, x in enumerate(ran):
            x[1] = int(x[1]) 
            x[0] = int(x[0])
            if x[0] <= nn and nn <= x[1]:
                # print('PASS!', nn, x, count)
                break
            else:
                count += 1
                # print(nn, x, count)
                if count == len(ran):
                    valid[j].remove(nn)
                    # print(nn, x)
                    invalid.append(nn)


for line in valid:
    if len(line) < 20:
        line.append(0)

# print(len(valid))
# # print((valid[0]))
# print(len(valid[0]))



# colValid = numpy.transpose(valid)


colValid = [[0 for x in range(283)] for y in range(20)]


# 

for row in range(len(valid)):
    for col in range(len(valid[0])):
        # print('row:', row, 'col:', col)
        # print(valid[row][col])
        colValid[col][row] = valid[row][col]


# print(colValid[0])
# print(ran[0:2])

# for xx, line in enumerate(colValid):
#     # print('xx:', xx, 'line:', line)
#     for yy in range(238):
#         count = 0   
#         for k, x in enumerate(ran[(2*xx) : (2*xx+2)]):
#             # print(ran[(2*xx): (2*xx+2)], x)
#             x[1] = int(x[1]) 
#             x[0] = int(x[0])
#             if colValid[xx][yy] != 0:
#                 if x[0] <=  colValid[xx][yy] and  colValid[xx][yy] <= x[1]:
#                     # print('PASS!', nn, x, count)
#                     break
#                 else:
#                     count += 1
#                     if count:
#                         print('line:', xx , 'does not match', 'range:', ran[(2*xx) : (2*xx+2)])

for rangeNum in range(7):
    for k, x in enumerate(ran[(2*rangeNum) : (2*rangeNum+2)]):
        # print(ran[(2*rangeNum) : (2*rangeNum+2)])
        x[1] = int(x[1])
        x[0] = int(x[0])
        for xx, line in enumerate(colValid):
            # print('xx:', xx, 'line:', line)
            for yy in range(238):
                count = 0
                if colValid[xx][yy] != 0:
                    if x[0] <=  colValid[xx][yy] and  colValid[xx][yy] <= x[1]:
                        if colValid[xx][yy] == colValid[xx][-1]:
                            print('Range', ran[(2*rangeNum) : (2*rangeNum+2)], 'is good for colvalid',  xx)
                    if x[0] > colValid[xx][yy] or colValid[xx][yy] > x[1]:
                        break


















# p1 = 0
# for i in invalid:
#     p1 += i
# print(p1)


