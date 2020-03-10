#소수찾기
#주어진 수 중 소수 몇개?
T = int(input())
count = T

Arr = list(input().split())
for j in range(len(Arr)):
    Arr[j] = int(Arr[j])
    if Arr[j] == 1:
        count -= 1
    else:
        for i in range(2,Arr[j]):
            if Arr[j]%i == 0:
                count -= 1
                break
print(count)