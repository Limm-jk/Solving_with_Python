# /**
#  * @author [Limm-jk]
#  * @email [201602057@cs-cnu.org]
#  * @create date 2020-04-17 16:14:57
#  * @modify date 2020-04-17 16:14:57
#  * @desc [배추맨]
#  */

import sys

sys.setrecursionlimit(10**8)

def dfs(G,x,y):
    G[x][y] = 0
    adj_list = [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]
    for p in adj_list:
        if p[0] < 0 or p[0] >= len(G) or p[1] < 0 or p[1] >= len(G[1]):
            continue
        if G[p[0]][p[1]] == 1:
            dfs(G,p[0],p[1])

def solve():
    # 테스트 케이스를 받아서 해결해주는 역할
    # 입력부
    xlen,ylen,k = map(int, input().split())
    graph = [[0 for _ in range(ylen)] for _ in range (xlen)]
    # 그래프 완성
    for _ in range(k):
        x,y = map(int, input().split())
        graph[x][y] = 1
    # 계산부
    count = 0
    for i in range(xlen):
        for j in range(ylen):
            if graph[i][j] == 1:
                dfs(graph,i,j)
                count += 1

    print(count)

for _ in range(int(input())):
    solve()