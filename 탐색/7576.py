# /**
#  * @author [Limm-jk]
#  * @email [201602057@cs-cnu.org]
#  * @create date 2020-04-17 18:35:20
#  * @modify date 2020-04-17 18:35:20
#  * @desc [멋쟁이토마토마토마토]
#  */

def search(G,n):
    arr =[]
    for i in range(len(G)):
        for j in range(len(G[1])):
            if G[i][j] == n:
                arr.append([i,j])
    return arr

def bfs_oneStep(G, x, y):
    count = 0 # depth for bfs
    qu = []
    curNode = [x,y]
    adj_list = [[curNode[0]+1,curNode[1]],[curNode[0]-1,curNode[1]],[curNode[0],curNode[1]+1],[curNode[0],curNode[1]-1]]
    for p in adj_list:
        if p[0] < 0 or p[0] >= len(G) or p[1] < 0 or p[1] >= len(G[1]):
            continue
        if G[p[0]][p[1]] == 0:
            qu.append([p[0],p[1]])
            G[p[0]][p[1]] = 1
    return qu

# input
M,N = map(int,input().split())

# table
tomato = []
# set table
for _ in range(N):
    tomato.append(list(map(int,input().split())))

# search
first_arr = search(tomato,1)

# BFS
count = 0
next_arr = []
for p in first_arr:
    next_arr.extend(bfs_oneStep(tomato,p[0],p[1]))

while len(next_arr) != 0:
    count += 1
    arr = []
    for p in next_arr:
        arr.extend(bfs_oneStep(tomato,p[0],p[1]))
    next_arr = arr

if len(search(tomato,1)) != M*N-len(search(tomato,-1)):
    count = -1

print(count)