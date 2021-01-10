import csv

with open('dec09.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = '\n')
    input = []
    for line in reader:
        input.extend(line)


check = input[25:]

for i, x  in enumerate(check):
    temp = []
    for j in input[i: (i+25)]:
        for k in input[i: (i+25)]:
            if int(j) + int(k) == int(x):
                if int(j) != int(k):
                    break
                else:
                    temp.append(x)
            else:
                temp.append(x)
    # if len(temp) == (25*25):
    #     print(temp)   # part 1


target = 675280050
# print(input[0:5])
# print('-------------------------')
for i, x in enumerate(input[0:999]):
    sum = int(x) + int(input[i+1])
    # print('sum:', sum,'i:', i ,'x:', x, 'input[i+1]:', input[i+1])
    for j in range((i+2) , len(input)):
        # print('j:', j, 'sum:', sum)
        sum = sum + int(input[j])
        if sum == target:
            print('i:', i, 'j:', j)
        if sum > target:
            # print('Bigger', 'i:', i, 'j:', j)
            break
        # print('sum:',sum, 'input[j]:', input[j])




for i in input[504:520]:
    print(i)
