#부녀회장
#a층 b호에 살려면 아래층 b호 까지의 사람만큼 살아야됨
#0층의 i호에는 i명이삼
#이때 k층의 n호에 몇명?

T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())
    apt = [[0]*(k+1) for i in range(n+1)]
    for j in range(n+1):
        apt[j][0] = j
    for j in range(1,n+1):
        for k in range(1,k+1):
            apt[j][k] = apt[j][k-1]+apt[j-1][k]
    print(apt[j][k])