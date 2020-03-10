#소수
#M과 N사이의 소수를 찾아라
#총합과 최솟값을 출력 없으면 -1

M = int(input())
N = int(input())
count = 0
sumN = 0
minimal = 100001

for j in range(M,N+1):
    sosu = True
    if j == 1:
        sosu = False
    else:
        for i in range(2,j):
            if j%i == 0:
                sosu = False
                break

    if sosu:
        sumN += j
        if minimal > j:
            minimal = j
if sumN == 0:
    print(-1)
else:
    print(sumN)
    print(minimal)