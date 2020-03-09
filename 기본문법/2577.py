A = int(input())
B = int(input())
C = int(input())
arr = [0 for ar in range(10)]

EX = A*B*C
while 1:
    Num = EX%10
    arr[Num] +=1
    EX = int(EX/10)
    if EX == 0:
        for i in range(10):
            print(arr[i])
        break