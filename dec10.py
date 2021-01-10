import csv

with open('dec10.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = '\n')
    input = []
    for line in reader:
        input.extend(line)

# max 168 

qq = input
qq.sort()

pp = []

for i in qq:
    rr = int(i)
    pp.append(rr)

pp.sort()
dd = []
for i in range(len(pp)-1):
    diff = int(pp[i+1])-int(pp[i])
    dd.append(diff)
print(dd)

ee = 3+1+3+2+2+3+2+2+2+3+2+1+1+1+1+3+3+2+1+3+3

print(ee)


uu = 2**ee
print(uu)

sum1 = 0
sum3 = 0

# for i in range(len(pp)-1):
#     if int(pp[i+1])-int(pp[i]) == 1:
#         sum1 = sum1 +1
#     if int(pp[i+1])- int(pp[i]) == 3:
#         sum3 = sum3 +1

# print(sum1)
# print(sum3)
# print(sum1*sum3)




































# def findChoice(rating, collect):
#     qq = rating + 3
#     subCollect = []
#     subSubCollect = []
#     # for i in collect:
#     #     if i not in used:
#     #         subCollect.append(i)
#     for j in collect:
#         if qq - j < 3:
#             subSubCollect.append(j)
#     subSubCollect.sort(reverse=True)
#     if subSubCollect:
#         choice = subSubCollect[-1]
#     else:
#         choice = None
#     return choice



# for rating in beMatched:
#     rating = int(rating)
#     print('rating', rating)
#     collect = []
#     for i in match:
#         if int(i) <= rating+3:
#             collect.append(int(i))
#     collect.sort(reverse=True)
#     print(collect)
#     choice = findChoice(rating, collect) 
#     print('choice:', choice)
#     used.append(choice)
#     if choice:
#         if abs(rating - choice) == 1:
#             sum1 = sum1 + 1
#         if abs(rating - choice) == 3:
#             sum3 = sum3 + 1


