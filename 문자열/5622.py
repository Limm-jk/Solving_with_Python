# 다이얼
# 1을 입력하려면 2초, 숫자 1당 1초씩 더.
# 아스키 65 ~ 90

inputSTR = list(input())
time = 0
for i in range(len(inputSTR)):
    Nnum = ord(inputSTR[i])-65
    count = 0
    if Nnum < 18:
        count = int(Nnum/3)+3
    elif Nnum < 25:
        count = int((Nnum-1)/3)+3
    else:
        count = 10
    time += count
print(time)