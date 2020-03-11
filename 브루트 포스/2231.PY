#분해합
#어디서 본거같은데...
#245 부분합 = 245+2+4+5 = 256
#245는 256의 생성자
#가장 작은 생성자는?

N = int(input())
mini = 0
def sumsum(N):
    Num = N
    arr = []
    while 1:
        if Num == 0:
            break
        a = Num%10
        arr.append(a)
        Num = int(Num/10)
    return N+(sum(arr))

for i in range(1,N):
    if sumsum(i) == N:
        mini = i
        break

print(mini)