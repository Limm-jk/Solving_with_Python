N = int(input())
for i in range(N):
    a = input()
    a = list(a)
    lenge = len(a)
    count = 0
    rank = 0
    for j in range(lenge):
        if a[j] == 'O':
            rank += count+1
            count += 1
        else:
            count = 0
    print(rank)

        
