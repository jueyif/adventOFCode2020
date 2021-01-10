import csv
import re

with open('dec13.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = '\n')
    input = []
    for line in reader:
        input.extend(line)

# timestamp = int(input[0])
# print(timestamp)

# busID =  re.findall(r'\d{1,3}',input[1])
# print(busID)

busList = input[1].split(',')



# busList = [67,7,59,61]
# print(busList)
# print(len(busList))


time = 1
differT = [i for i in range(len(busList))]

busIDt = []

for i, x in enumerate(busList):
    if x != 'x':
        ID, t  = int(x), i
        busIDt.append([ID, t])

# print(busIDt)

# busIDt.sort()
# print(busIDt)

# ans = 754018
# print(ans/67)
# print(ans/7)
# print(ans/59)
# print(ans/61)
# print('-------------------')
# print(ans - 11254*67)
# print(ans+1 - 107717 * 7)
# print(ans+2 - 12780 * 59)
# print(ans+3 - 12361 * 61)

# newBusIDt = []
# for i, pair in enumerate(busIDt):
#     newDifferT = pair[1] - 72
#     newBusIDt.append([pair[0], newDifferT])

# print(newBusIDt)


for i, pair in enumerate(busIDt):
    qq = abs(busIDt[i][0] - busIDt[i][1])
    busIDt[i].append(qq)
print(busIDt)

busIDt = [ [37, 35, 2], [659, 41, 618], [23, 49, 26], [13, 54, 41], [19, 60, 41], [29, 70, 41], [937, 72, 865], [17, 89, 72]]
moShuChengJi = 1
for i, pair in enumerate(busIDt):
    moShuChengJi = moShuChengJi * pair[2]

# moShuChengJi = 35 * 41 * 49 * 54 * 60 * 70 * 72 * 89
# # print(min, max)
print(moShuChengJi)
# xinMoShuChengJi = 2 * 618 * 20 * 11 * 16 * 17 * 865 * 13

mm = []  # 除该数本身外，所有数的乘积
jj = []  # shu lun dao shu 
# xinbusIDt = [[37, 35,2], [659, 41,618], [23, 49,20], [13, 54,11], [19, 60,16], [29, 70,17], [937, 72,865], [17, 89,13]]
for i, pair in enumerate(busIDt):
    print(pair, pair[1])
    m = int(moShuChengJi / pair[2])
    mm.append(m)
    
    daoShu = 1
    for j in range(1,1000):
        kk = (m * j) % pair[0]
        # print('kk:', kk, '--->', j)
        if kk == 1:
            daoShu = j
            print('kk:', kk, '--->', j)
            break
    
    jj.append(daoShu)


# print(2919748809600 * 7 % 37)

# yy=[[37, 35], [659, 41], [23, 49], [13, 54], [19, 60], [29, 70], [937, 72], [17, 89]]
print(mm, jj)
ans11 = 0
for i in range(8):
    ans11 = ans11 + (mm[i] * jj[i] * busIDt[i][0])
    print(mm[i], jj[i], busIDt[i][0])

print(ans11)
ans = ans11 % moShuChengJi +35
print(ans)
print(ans % 37)







# # for n in range(0, 500000):
# #     # p2 = 937 * n
# p2 =  ans
# # if ((((p2 + 17 ) % 17)) != 0):
#     # continue
# check = [0 for h in range(len(busIDt))]
# for i, pair in enumerate(busIDt):
#     # print(i)
#     if ( ((p2 + pair[1]) % (pair[0])) != 0):
#         break
#     else:
#         check[i] = 1
# # result = all(qq == 1 for qq in check)
# print(check)
# if not (0 in check):
#     print('DONE!!!',p2)
#     # break












# for i, pair in enumerate(busIDt):
#     print(i, pair, time)
#     while ((time + pair[1]) % pair[0] != 0):
#         time = time + 1
#         # print(time)
#     if  ((time + pair[1]) % pair[0] == 0):
#         print( 'time + pair[1]', time , '+', pair[1], '=', time + pair[1], '% ', pair[0])
#         recordZheng = []
#         for i, pair in enumerate(busIDt):
#             zheng = time // pair[0]
#             recordZheng.append(zheng)
#         print('recordZheng:', recordZheng)
#         result = all(zheng == recordZheng[0] for zheng in recordZheng)
            # if (result):
            #     print(recordZheng)
            #     break
        # if (time > 20000):
        #     break



# while (time<754020):
#     for i, pair in enumerate(busIDt):
#         meet = [0,0,0,0]
#         if  ((time + pair[1]) % pair[0] != 0):
#             time = time + 1 
#         else: 
#            meet[i] = 1 
#     result = all(mee == 1 for mee in meet)
#     if (result):
#         print('dui!!!!', time)
#     if not (result):
#         time = time +1
        # print(time)

# def loop(time):
#     newTime = time + 1
#     check = [0,0,0,0]
#     for i, pair in enumerate(busIDt):
#         if  ((newTime + pair[1]) % pair[0] == 0):
#             print(newTime)
#         else: 
#            return loop(newTime)
#     result = all(qq == r1 for qq in check)
#     if (result):
#         print('dui', newTime)


# loop(time)


#     for i, pair in enumerate(busIDt):
#         zheng = timeG // pair[0]
#         recordZheng.append(zheng)
#         print(recordZheng)
#         result = all(zheng == recordZheng[0] for zheng in recordZheng)
#         if (result):
#             print('dui', recordZheng)
#             break
#         else: timeRound = abc(timeStart)



# # diff = []
# for id in busID:
#     yu = timestamp % int(id)
#     zheng = timestamp // int(id)
#     print('id:', id, 'yu:', yu, 'zheng:', zheng)
#     differ = (zheng+1) * int(id) -  timestamp
#     print('differ:', differ)

# print(5*23)



