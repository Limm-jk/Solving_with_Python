# /**
#  * @author [Limm-jk]
#  * @email [201602057@cs-cnu.org]
#  * @create date 2020-04-08 12:26:50
#  * @modify date 2020-04-08 12:26:50
#  * @desc [단어정렬하기]
#  */

arr = []

for _ in range(int(input())):
    arr.append(input())

arr.sort(key = lambda x : (len(x), x))
log = ""

for i in range(len(arr)):
    if arr[i] != log:
        print(arr[i])
        log = arr[i]