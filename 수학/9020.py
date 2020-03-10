#골드바흐의 추측
# 2보다 큰 짝수는 두개의 소수로 표현가능
# 10000까지 가능

def isIn(arr, N):
    result = False
    for i in range(len(arr)):
        if arr[i] == N:
            result = True
            break
    return result

N = 10000
Arr = [0 for i in range(N+1)]

for i in range(2, N+1):
    Arr[i] = 1

for i in range(2, N+1):
    if Arr[i] != 0:
        count = 2
        while 1:
            if count*i > N:
                break
            Arr[count*i] = 0
            count+=1


for i in range(int(input())):
    T = int(input())
    a = int(T/2)
    b = int(T/2)
    while 1:
        if Arr[a]+Arr[b]==2:
            print("%d %d"%(a,b))
            break
        elif a<0:
            break
        a-=1
        b+=1