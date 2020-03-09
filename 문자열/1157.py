#단어공부
#대소문자 구분X 가장 많이 이용된 알파벳
#대문 65~90 소문 97~122

inputStr = list(input())
Listsize = len(inputStr)
AlpArr = [0 for i in range(26)]

overlap = False
maxCount = 0
maxloc = 0

for i in range(Listsize):
    str2asc = ord(inputStr[i])
    if str2asc > 91:
        str2asc -= 97
    else:
        str2asc -= 65
    AlpArr[str2asc] += 1

for i in range(26):
    if AlpArr[i] > maxCount:
        maxCount = AlpArr[i]
        maxloc = i
        overlap = False
    elif AlpArr[i] == maxCount:
        overlap = True

if overlap:
    print('?')
else:
    print(chr(maxloc+65))
