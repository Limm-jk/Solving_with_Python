# /**
#  * @author [Limm-jk]
#  * @email [201602057@cs-cnu.org]
#  * @create date 2020-06-15 09:55:17
#  * @modify date 2020-06-15 09:55:17
#  * @desc [description]
#  */
import sys 

sys.setrecursionlimit(10**8)# 재귀 늘려줌
input = sys.stdin.readline

# def adj(G, p1, p2):#인접한 경우 True를 리턴
#     if G[p1][p2] == 1:
#         return True
#     else:
#         return False

def dfs(v):
    visit[v] = 1
    for i in adj[v]:
        if visit[i] == 0:
            par_arr[i] = v
            dfs(i)
            

N = int(input())

adj = [ [] for _ in range(N+1) ]
visit = [0 for _ in range(N+1)]
par_arr = [0 for _ in range(N+1)]

for _ in range(N-1):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

dfs(1)

for i in range(2,N+1):
    print(par_arr[i])