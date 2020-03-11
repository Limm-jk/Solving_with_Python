#덩치
#키와 몸무게 입력
#둘 다 커야 덩치가 크다라고 말함
#X는 몸무게 Y는 키

rank = []

N = int(input())

for i in range(N):
    X,Y=map(int, input().split())
    rank.append((X,Y))

for i in range(len(rank)):
    rankN = 1
    for j in range(len(rank)):
        if (rank[i][0] < rank[j][0]) & (rank[i][1] < rank[j][1]):
            rankN +=1

    print(rankN, end=' ')