import queue

def adj(G, p):
    N =len(G)
    arr = []
    adj_arr = [[p[0]-1,p[1]-1],[p[0],p[1]-1],[p[0]+1,p[1]-1],[p[0]+1,p[1]],[p[0]+1,p[1]+1],[p[0],p[1]+1],[p[0]-1,p[1]+1],[p[0]-1,p[1]]]
    for i in adj_arr:
        if (i[0]>0) & (i[0]<N) & (i[1]>0) & (i[1]<N):
            bomb = G[i[0]][i[1]]
            if bomb == 1:
                arr = []
                break
            elif bomb == 0: 
                arr.append(i)

    return arr
def solution(N, mine, P):
    answer = 0
    arr = [[0 for i in range(N+1)] for j in range(N+1)]
    # 1일때 마인
    for i in mine:
        arr[i[0]][i[1]] = 1
    qu = queue.Queue()
    qu.put(P)
    if arr[P[0]][P[1]] == 1:
        return answer
    arr[P[0]][P[1]] = 3
    while not qu.empty():
        x = qu.get()
        answer += 1
        adj_arr = adj(arr,x)

        for ad in adj_arr:
            # if x == [4,2]:   

            qu.put(ad)
            arr[ad[0]][ad[1]] = 2


    return answer