# /**
#  * @author [Limm-jk]
#  * @email [201602057@cs-cnu.org]
#  * @create date 2020-04-15 23:43:49
#  * @modify date 2020-04-15 23:43:49
#  * @desc [description]
#  */

import sys

check_arr = []

sys.setrecursionlimit(10**8)

def adj(G, v1, v2):
    if G[v1][v2] == 1:
        return True
    else:
        return False

def DFS(G, v):
    check_arr.append(v)
    for i in range(1, len(G)):
        if(adj(G,v,i)) & (i not in check_arr):
            DFS(G,i)


N = int(input())
graph = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(int(input())):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

DFS(graph,1)

print(len(check_arr)-1)