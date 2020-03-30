# /**
#  * @author [Limm-jk]
#  * @email [201602057@cs-cnu.org]
#  * @create date 2020-03-26 19:34:23
#  * @modify date 2020-03-26 19:34:23
#  * @desc [음계]
#  */

arr =[]
arr = list(map(int,input().split()))

if arr == sorted(arr):
    print("ascending")
elif arr == sorted(arr,reverse=True):
    print("descending")
else:
    print("mixed")