#소수 구하기
#M과 N사이의 소수 크기순으로 출력
#에라토스테네스의 체로 짜보자

M,N=map(int, input().split())

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

for i in range(len(sosu)):
    if M<=sosu[i]:
        print(sosu[i])