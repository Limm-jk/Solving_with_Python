# /**
#  * @author [Limm-jk]
#  * @email [201602057@cs-cnu.org]
#  * @create date 2020-06-15 10:42:57
#  * @modify date 2020-06-15 10:42:57
#  * @desc [description]
#  */


# def bfs(v):
#     qu = queue.Queue()
#     visit = [0 for _ in range(N+2)]
#     v1 = [v,0]
#     qu.put(v1)
#     visit[v1[0]] = 1
#     max_v, index = 0, 1
#     while not qu.empty():
#         X = qu.get()
#         if max_v < X[1]:
#             max_v = X[1]
#             index = X[0]

#         for i in adj[X[0]]:
#             if visit[i[0]] == 0:
#                 qu.put([i[0], X[1] + i[1]])
#                 visit[i[0]] = 1 # 중복확인겸 결과 배열

#     return [index, max_v]


import sys 
sys.setrecursionlimit(10**8)# 재귀 늘려줌

def dfs(v,adj,visit):
    for node, index in adj[v]:
        if visit[node] == 0:
            visit[node] = visit[v]+index
            dfs(node,adj,visit)

N = int(sys.stdin.readline())

adj = [[] for _ in range(N+1)]

for _ in range(N):
    path=list(map(int,sys.stdin.readline().split()))
    #1+2i
    path_len=len(path)
    for i in range(1,path_len//2):
        adj[path[0]].append([path[2*i-1],path[2*i]])


visit = [0 for _ in range(N+1)]
dfs(1,adj,visit)
visit[1] = 0
max_val = visit.index(max(visit))
visit2 = [0 for _ in range(N+1)]

dfs(max_val,adj,visit2)
visit2[max_val] = 0
print(max(visit2))

# for i in range(2,N+1):
#     print(visit[i])
