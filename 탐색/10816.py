# /**
#  * @author [Limm-jk]
#  * @email [201602057@cs-cnu.org]
#  * @create date 2020-04-25 16:33:21
#  * @modify date 2020-04-25 16:33:21
#  * @desc [description]
#  */

def lower(key):
    low = 0
    high = len(arr)
    while low < high:
        mid = int(low + (high - low)/2)
        if key <= arr[mid]:
            high = mid
        else:
            low = mid +1

    return low

def upper(key):
    low = 0
    high = len(arr)
    while low < high:
        mid = int(low + (high - low)/2)
        if key >= arr[mid]:
            low = mid + 1
        else:
            high = mid

    return low

arr = []
arr2 = []
answer = []

input()
arr = list(map(int,input().split()))
input()
arr2 = list(map(int,input().split()))

arr.sort()

for i in range(len(arr2)):
    ans = upper(arr2[i]) - lower(arr2[i])
    answer.append(ans)

for j in range(len(answer)-1):
    print(answer[j], end = " ")

print(answer[len(answer)-1])