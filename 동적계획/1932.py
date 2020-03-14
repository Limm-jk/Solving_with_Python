#정수 삼각형

N = int(input())

tri = []
for i in range(N):
    tri.append(list(map(int, input().split())))

for i in range(1,N):
    for j in range(i+1):
        if j == 0:
            tri[i][j] = tri[i][0] + tri[i-1][0]
        elif j == i:
            tri[i][j] = tri[i][j] + tri[i-1][j-1]
        else:
            tri[i][j] = tri[i][j] + max(tri[i-1][j],tri[i-1][j-1])

print(max(tri[N-1]))