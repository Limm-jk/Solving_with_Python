# /**
#  * @author [Limm-jk]
#  * @email [201602057@cs-cnu.org]
#  * @create date 2020-08-12 23:23:57
#  * @modify date 2020-08-12 23:23:57
#  * @desc [이중큐]
#  */

# 큐부터 만들자. 싫어
import queue

global_Q = queue.Queue
arr = []

def insert_arr(a):
    if len(arr) == 0:
        arr.append(a)
    else:
        for i in arr:
            


for _ in range(int(input())):
    for _ in range(int(input())):
        L, N = list(input().split())
        N = int(N)
        if L == "I":
            global_Q.put(N)
        else:
            if N == 1:
