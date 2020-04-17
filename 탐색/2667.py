# /**
#  * @author [Limm-jk]
#  * @email [201602057@cs-cnu.org]
#  * @create date 2020-04-15 23:54:08
#  * @modify date 2020-04-15 23:54:08
#  * @desc [단지번호 / 탐색]
#  */

import sys

sys.setrecursionlimit(10**8)

def DFS(G, v1, v2):
    G[v1][v2] = count
    global danji_count
    danji_count += 1
    n = len(G)
    adj_arr = [[v1+1,v2],[v1,v2+1],[v1,v2-1],[v1-1,v2]]
    for i in adj_arr:
        if i[0] < 0 or i[0] >= n or i[1] < 0 or i[1] >=n:
            continue
        if G[i[0]][i[1]] == 1:
            DFS(G,i[0], i[1])

N = int(input())
danji_arr = [0]*N
ful_arr = []
danji_count = 0
count = 1
for i in range(N):
    danji_arr[i] = list(map(int, input()))

for i in range(N):
    for j in range(N):
        if danji_arr[i][j] == 1:
            count += 1
            DFS(danji_arr, i, j)
            ful_arr.append(danji_count)
            danji_count = 0

ful_arr.sort()

print(len(ful_arr))
for i in ful_arr:
    print(i)