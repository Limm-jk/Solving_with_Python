# /**
#  * @author [Limm-jk]
#  * @email [201602057@cs-cnu.org]
#  * @create date 2020-04-11 16:50:36
#  * @modify date 2020-04-11 16:50:36
#  * @desc [DFS BFS]
#  */


import queue
import sys 

sys.setrecursionlimit(10**8)# 재귀 늘려줌

arr = []
arr2 = []

def adj(G, p1, p2):#인접한 경우 True를 리턴
    if G[p1][p2] == 1:
        return True
    else:
        return False

def dfs(G,v):
    arr.append(v)# 중복확인겸 결과 배열
    for i in range(1,len(G)):
        if (adj(G,v,i)) and (i not in arr):
            dfs(G,i)

def bfs(G,v):
    qu = queue.Queue()
    qu.put(v)
    arr2.append(v)# 중복확인겸 결과 배열
    while not qu.empty():
        X = qu.get()
        for i in range(1,len(G)):
            if (adj(G,X,i)) and (i not in arr2):
                qu.put(i)
                arr2.append(i)# 중복확인겸 결과 배열




N, M, V = map(int, input().split())

graph = [[0] * (N + 1) for _ in range(N + 1)]

# for _ in range(M):
#     x, y = map(int, input().split())
#     graph[x][y] = 1
#     graph[y][x] = 1

for i in range(1000):
    graph[i][i+1] = 1


dfs(graph,V)
bfs(graph,V)


# 출력
for i in range(len(arr)-1):
    print(arr[i], end = " ")
print(arr[len(arr)-1])

for i in range(len(arr2)-1):
    print(arr2[i], end = " ")
print(arr2[len(arr2)-1])