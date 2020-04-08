# /**
#  * @author [Limm-jk]
#  * @email [201602057@cs-cnu.org]
#  * @create date 2020-04-07 16:16:04
#  * @modify date 2020-04-07 16:16:04
#  * @desc [좌표정렬하기]
#  */

arr = []

for _ in range(int(input())):
    arr.append(list(map(int, input().split())))

arr.sort(key = lambda x: (x[0],x[1]))

for i in arr:
    print(i[0],i[1])