#베르트랑 공준
#n ~ 2n사이의 소수를 출력
#무한히 입력이 가능하므로 미리 소수만 만들어두고 출력

M = 1
N = 123456*2
Arr = [0 for i in range(N+1)]
sosu =[]


for i in range(2, N+1):
    Arr[i] = i

for i in range(2, N+1):
    if Arr[i] != 0:
        sosu.append(Arr[i])
        count = 1
        while 1:
            Arr[count*i] = 0
            count+=1
            if count*i > N:
                break
while 1:
    T = int(input())
    result = 0
    if T == 0:
        break
    for i in range(len(sosu)):
        if T<sosu[i]<=2*T:
            result += 1

    print(result)