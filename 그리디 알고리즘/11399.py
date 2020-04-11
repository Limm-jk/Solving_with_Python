# /**
#  * @author [Limm-jk]
#  * @email [201602057@cs-cnu.org]
#  * @create date 2020-04-11 16:22:47
#  * @modify date 2020-04-11 16:22:47
#  * @desc [ATM]
#  */

input()

arr = list(map(int, input().split()))

arr.sort()

for i in range(len(arr)-1):
    arr[i+1] += arr[i]

print(sum(arr))