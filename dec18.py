import fileinput
import re
import numpy

input = [line.strip('\n') for line in (fileinput.input(files ='dec18.txt'))]

# print(input[0:5])


# s = '1 + 2 * 3 + 4 * 5 + 6'
# s = s.replace(' ', '')
# ans = int(s[0])
# for i in range(1, len(s)-1):
#     print('i:', i, 'char:', s[i])
#     if s[i] == '+':
#         ans += int(s[i+1])
#         print(ans)
#     if s[i] == '*':
#         ans *= int(s[i+1])
#         print(ans)



# s = '1 + (2 * 3) + (4 * (5 + 6))'
# s1 = list(s1.replace(' ', ''))

# 5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
s = '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'

# s = '6 * ((7 * 6) * 7 + 4 * 5 * 6 + 4) * (9 * (9 + 3) * 7)'
s = list(s.replace(' ', ''))
# answer: 13632
print(s)

def calPlusMulti(s):
    ans = int(s[0])
    for i in range(1, len(s)-1):
        print('i:', i, 'char:', s[i], 'next char:', s[i+1])
        if  s[i] == '+':
            ans += int(s[i+1])
            print(ans)
        if  s[i] == '*':
            ans *= int(s[i+1])
            print(ans)
    return ans

# calculate parentheses part
def calParen(s):
    for i in range(len(s)):
        if s[i] == '(' and s[i+1] != '(':
            print('i in for loop:', i)
            for c in s[i+1:]:
                end = s[i+1:].index(')')
            print('s[i+1: end+i+1]:', s[i+1: end+i+1])
            ans = calPlusMulti(s[i+1: end+i+1])
    return ans

order = []
pl = s.index('(')
print(pl)
pr = s.index(')')
print(pr)

print(' eter', s[pl+1:pr])
if '(' not in s[pl+1:pr] :
    print('pair:',s[pl:pr+1] )
else:
    pll = s[pl+1:pr].index('(')
    print('else pair:', s[pl+pll+1:pr+1] )
    

        

# print(order)

# pl = []
# pr = []
# for i in range(len(s)):
#     if s[i] == '(':
#         pl.append(i)
#     if s[i] == ')':
#         pr.append(i)

# print(pl)
# print(pr)

# pair = []

# for i in range(len(pl)-1):
#     print(i)
#     if pl[i+1] > pr[i]:
#         pair.append((pl[i],pr[i]))
#         print(pair)
#     if pl[i+1] < pr[i]:
#         if (i in range(len(pl)-2)):
#             if  pl[i+2] > pr[i+1]:
#                 pair.append((pl[i],pr[i+1]))
#                 pair.append(((pl[i+1], pr[i])))
#                 print(pair)
#             if  pl[i+2] < pr[i+1]:
#                 pair.append((pl[i],pr[i+2]))
#                 print(pair)
#         if i == len(pl)-2:
#             pair.append((pl[i],pr[i+1]))
#             print(pair)

# print(pair)



# 6 * ((7 * 6) * 7 + 4 * 5 * 6 + 4) * (9 * (9 + 3) * 7)

# for i in range(len(s)):
#     if s[i] == '(' :
#         print('i in for loop:', i)
#         for c in s[i+1:]:
#             end = s[i+1:].index(')')
#         print('end:', end, 'end char:', s[end+i+1] )
#         print('s[i+1: end+i+2]:', s[i+1: end+i+2])
#         pair.append((i, end+i+1))
#         print(pair)
#     print('-------------------------')






# if '(' < s[0]:
#     ans = s[0]
# elif '(' < s[1]:
#     ans = s[1]



# for i in range(len(pl)-1):
#     if pl[i+1] < pr[i] and pl[i+2] < pr[i+1]:
#         sub = s1[pl[i+1]: pr[i+1]]
#         print(sub)

#         pl = []
#         pr = []
#         for i in range(len(sub)):
#             if sub[i] == '(':
#                 pl.append(i)
#             if sub[i] == ')':
#                 pr.append(i)
#         print(pl)
#         print(pr)

#         for i in range(len(pl)-1):
#             if pl[i+1] < pr[i]:
#                 subb = sub[pl[i+1]: pr[i+1]]
#                 print(subb)






# pl = s.index('(')
# print(pl)
# pr = s.index(')')
# print(pr)

# subS = s[pl+1:pr]
# print(subS)
# subAns = int(subS[0])
# for i in range(1, len(subS)-1):
#     print('i:', i, 'char:', subS[i])
#     if  subS[i] == '+':
#         subAns += int( subS[i+1])
#         print(subAns)
#     if  subS[i] == '*':
#         subAns *= int( subS[i+1])
#         print(subAns)

# print('-----------------------')

# pll = s[pr+1:].index('(')
# print(pll)
# prr = s[pr+1:].index(')')
# print(prr)

# subsubS = s[pr+1:][pll+1:prr]
# print(subsubS)
# if '(' in subsubS:
#     pl3 = s.index('(')
# print(pl3)
# pr = s.index(')')
# print(pr)






# (5 * (7 * 9 + 8 * 2 + 5 * 4) + (6 + 7 + 6 + 9) + (5 + 3 + 6 + 9 * 7) + 7 + (4 + 9 + 2 * 3 * 4 + 5)) * 2 * 8 * (2 * 9 * (8 * 5 + 3 * 8 + 5)) + (5 + 4 * 4 * 2) * 2

# 