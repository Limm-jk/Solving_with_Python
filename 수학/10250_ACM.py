#ACM호텔
#걷기 싫어하는 손님들

T = int(input())

for i in range(T):
    H,W,N=map(int, input().split())
    a = N%H
    b = int(N/H)+1
    if a == 0:
        print(100*H+b-1)
    else:
        print(100*a+b)