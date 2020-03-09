# 크로아티아 알파벳
# j,-,=와 뭔가 함께 알파벳이됨
# 알파벳 수를 세보자

inputSTR = list(input())
count = 0

for i in range(len(inputSTR)):
    if (inputSTR[i] != '=') & (inputSTR[i] != '-') & (inputSTR[i] != 'j'):
        count += 1
    elif inputSTR[i] == 'j':
        if (i == 0) | ((inputSTR[i-1] != 'l') & (inputSTR[i-1] != 'n')):
            count += 1
    elif (inputSTR[i] == '=') & (inputSTR[i-1] == 'z') & (inputSTR[i-2] == 'd'):
        count -= 1

print(count)