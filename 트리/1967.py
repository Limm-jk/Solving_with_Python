import sys 
sys.setrecursionlimit(10**8)# 재귀 늘려줌

def dfs(v,adj,visit):
    for node, index in adj[v]:
        if visit[node] == 0:
            visit[node] = visit[v]+index
            dfs(node,adj,visit)

N = int(sys.stdin.readline())

adj = [[] for _ in range(N+1)]

for _ in range(N-1):
    path=list(map(int,sys.stdin.readline().split()))
    #1+2i
    path_len=len(path)
    adj[path[0]].append([path[1],path[2]])
    adj[path[1]].append([path[0],path[2]])


visit = [0 for _ in range(N+1)]
dfs(1,adj,visit)
visit[1] = 0
max_val = visit.index(max(visit))
visit2 = [0 for _ in range(N+1)]

dfs(max_val,adj,visit2)
visit2[max_val] = 0
print(max(visit2))