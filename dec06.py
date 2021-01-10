import csv

with open('dec06.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = '\n')
    input = []
    for row in reader:
        input.append(row)
length = len(input)

for i in range(length):
    if input[i] != []:
        input[i].extend(input[i-1])

tempInput = []
for i in range(len(input)):
    if input[i] == []:
        qq = ''.join(input[i-1])
        tempInput.append(qq)

def uniqueNumber(list1): 
    # intilize a null list 
    unique_list = [] 
    # traverse for all elements 
    for x in list1: 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x) 
    return len(unique_list)

sumAnswer = 0
for group in tempInput:
    yesCount = uniqueNumber(group)
    sumAnswer = sumAnswer + yesCount

print('Part 1 Answer:', sumAnswer)

############### PART TWO  ################

tempInputB = []
for i in range(len(input)):
    if input[i] == []:
        qq = ' '.join(input[i-1])
        tempInputB.append(qq)

def uniqueList(list1): 
    # intilize a null list 
    unique_list = [] 
    # traverse for all elements 
    for x in list1: 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x) 
    return unique_list

sumB = 0
for string in tempInputB:
    answerList = string.split(' ')
    baseLetter = []
    for c in answerList[0]:
        baseLetter.append(c)
    removeLetter = []
    for letter in baseLetter:
        for answer in answerList:    
            if letter not in answer:
                removeLetter.append(letter)
    commonLetter = list(set(baseLetter) - set(removeLetter))
    sumB = sumB + len(commonLetter)

print('Part 2 Answer:', sumB)
