import csv
import re

with open('dec04.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = '\n')
    input = []
    for row in reader:
        input.append(row)
length = len(input)

for i in range(1,length):
    if input[i] != []:
        input[i].extend(input[i-1])
input.append('[]')

tempInput = []
for i in range(len(input)):
    if input[i] == []:
        qq = ' '.join(input[i-1])
        tempInput.append(qq)

count = 0
checkInfo = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']

valid = []
for item in tempInput:
    checkFlag = 1
    for info in checkInfo:
        if info not in item:
            checkFlag = 0
    if checkFlag == 1:
        count = count +1 
        valid.append(item)

# print(count)
print('Part 1 Answer:', len(valid))
   
def checkEcl(ecl):
    listEcl = ['amb','blu','brn','gry','grn','hzl','oth']
    for color in listEcl: 
        if ecl == color:
            return True
    else:
        print('invalid ecl:', ecl)   

def checkByr(byr):
    if int(byr) >= 1920 and int(byr) <= 2002:
        return True
    else:
        print('invalid byr:', byr)

def checkIyr(iyr):
    if  int(iyr) >= 2010 and int(iyr) <= 2020:
        return True
    else:
        print('invalid iyr:', iyr)

def checkEyr(eyr):
    if int(eyr) >= 2020 and int(eyr) <= 2030:
        return True
    else:
        print('invalid eyr:', eyr)

def checkHgt(hgt):
    if 'cm' in hgt:
        if int(hgt.strip('cm')) >= 150 and int(hgt.strip('cm')) <= 193:
            return True
    if 'in' in hgt:
        if int(hgt.strip('in')) >= 59 and int(hgt.strip('in')) <= 76:
            return True
    else:
        print('invalid hgt:', hgt)

def checkHcl(hcl):
    if '#' in hcl[0] and len(hcl) == 7:
        return True
    else:
        print('invalid hcl:', hcl)

def checkHclChar(hcl):
    subhcl = re.findall(r'[0-9a-f]', hcl)
    if len(subhcl)+1 == len(hcl):
        return True
    else:
        print('invalid hcl:', hcl)

def checkPidLen(pid):
    if len(pid) == 9:
       return True
    else:
        print('invalid PID length:', pid)

def checkPidFirEle(pid):
    if int(pid[0]) >= 0 and int(pid[0]) <= 9:
       return True
    else:
        print('invalid PID first element:', pid)

countB = 0

for item in valid:
    ecl = item.split('ecl:')[1].split(' ')[0]
    pid = item.split('pid:')[1].split(' ')[0]
    eyr = item.split('eyr:')[1].split(' ')[0]
    iyr = item.split('iyr:')[1].split(' ')[0]
    hcl = item.split('hcl:')[1].split(' ')[0]
    hgt = item.split('hgt:')[1].split(' ')[0]
    byr = item.split('byr:')[1].split(' ')[0]
    if checkEyr(eyr):
        if checkHclChar(hcl):
            if checkHgt(hgt):
                if checkIyr(iyr):
                    if checkPidLen(pid):
                        if checkByr(byr):
                            if checkPidFirEle(pid): 
                                if checkEcl(ecl):
                                    if checkHcl(hcl):
                                        countB = countB +1

print('Part 2 Answer:', countB)

