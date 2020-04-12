# /**
#  * @author [Limm-jk]
#  * @email [201602057@cs-cnu.org]
#  * @create date 2020-04-11 16:50:36
#  * @modify date 2020-04-11 16:50:36
#  * @desc [DFS BFS]
#  */

# 0 = 연결 안됨 1 = 연결됨 2 = 탐색함

import queue

arr = []
arr2 = []
def adj(G, p1, p2):
    if G[p1][p2] == 1:
        return True
    else:
        return False

def dfs(G,v):
    arr.append(v)
    for i in range(1,len(G)):
        if (adj(G,v,i)) and (i not in arr):
            dfs(G,i)

def bfs(G,v):
    qu = queue.Queue()
    qu.put(v)
    while qu.empty:
        X = qu.get()
        arr2.append(X)
        for i in range(1,len(G)):
            if (adj(G,v,i)) and (i not in arr2):
                qu.put(i)

N, M, V = map(int, input().split())

graph = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

dfs(graph,V)
bfs(graph,V)
print(arr)
print(arr2)