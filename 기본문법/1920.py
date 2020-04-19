# /**
#  * @author [Limm-jk]
#  * @email [201602057@cs-cnu.org]
#  * @create date 2020-04-19 02:00:20
#  * @modify date 2020-04-19 02:00:20
#  * @desc [이분탐색]
#  */
import sys 

sys.setrecursionlimit(10**8)# 재귀 늘려줌

def midNum(start,end,key):
    mid = int((end - start)/2)+start
    answer = 0
    if mid == start:
        if (key == arr[start]) or (key == arr[end]):
            answer = 1
        return answer
    if arr[mid] < key:
        answer = midNum(mid+1,end,key)
    elif arr[mid] > key:
        answer = midNum(start,mid, key)
    elif arr[mid] == key:
        answer = 1
    return answer
# input
arr = []
Q_arr =[]
input()
arr = list(map(int,input().split()))

# pred
arr.sort()
mid = int(len(arr)-0.5)

# input2
input()
Q_arr = list(map(int,input().split()))

for i in range(len(Q_arr)):
    print(midNum(0,len(arr)-1,Q_arr[i]))