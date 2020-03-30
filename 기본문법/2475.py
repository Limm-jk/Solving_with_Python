# /**
#  * @author [Limm-jk]
#  * @email [201602057@cs-cnu.org]
#  * @create date 2020-03-30 13:09:31
#  * @modify date 2020-03-30 13:09:31
#  * @desc [검증수]
#  */
arr = []
sum = 0
arr = list(map(int,input().split()))

for i in range(len(arr)):
    sum += arr[i]**2

print(sum%10)