# /**
#  * @author [Limm-jk]
#  * @email [201602057@cs-cnu.org]
#  * @create date 2020-04-07 14:46:32
#  * @modify date 2020-04-07 14:46:32
#  * @desc [요세푸스]
#  */

N, K = map(int, input().split())

arr = [0 for i in range(N)]
locate = 0
locate += K-1
locate = locate % len(arr)
arr2 = []
for i in range(N):
    arr[i] = i+1

for i in range(N-1):
    arr2.append(arr.pop(locate))
    locate %= len(arr)
    locate += K-1
    locate %= len(arr)
arr2.append(arr[0])

print("<", end="")
for i in range(N-1):
    print(arr2[i], end="")
    print(", ", end="")
print(arr2[N-1], end="")
print(">", end="")