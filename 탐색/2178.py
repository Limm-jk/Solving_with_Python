# /**
#  * @author [Limm-jk]
#  * @email [201602057@cs-cnu.org]
#  * @create date 2020-04-17 16:50:39
#  * @modify date 2020-04-17 16:50:39
#  * @desc [미로찾기]
#  */


def bfs(G,x,y):
    count = 0 # depth for bfs
    qu = []
    qu.append([x,y,1])
    G[x][y] = 0
    while len(qu) != 0:
        curNode = qu.pop(0)
        if curNode[0] == len(G)-1 and curNode[1] == len(G[1])-1:
            return curNode[2]
        adj_list = [[curNode[0]+1,curNode[1]],[curNode[0]-1,curNode[1]],[curNode[0],curNode[1]+1],[curNode[0],curNode[1]-1]]
        for p in adj_list:
            if p[0] < 0 or p[0] >= len(G) or p[1] < 0 or p[1] >= len(G[1]):
                continue
            if G[p[0]][p[1]] == 1:
                qu.append([p[0],p[1],curNode[2]+1])
                G[p[0]][p[1]] = 0

# input
N,M = map(int, input().split())

# table
graph = []

# set table
for _ in range(N):
    list1 = list(map(int, input()))
    graph.append(list1)

# result
print(bfs(graph,0,0))