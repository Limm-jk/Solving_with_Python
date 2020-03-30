# /**
#  * @author [Limm-jk]
#  * @email [201602057@cs-cnu.org]
#  * @create date 2020-03-20 16:01:34
#  * @modify date 2020-03-20 16:01:34
#  * @desc [시.공.조.아]
#  */

count = 1
cha = []
result = 0

N, K = map(int,input().split()) #N은 캐릭수 K는 총렙

for i in range(N):
    cha.append(int(input()))

cha = sorted(cha)

rest = K

while 1:
    gap = cha[count]-cha[count-1]
    if rest < gap*count:
        break
    rest -= gap*count
    count +=1

    if count == N:
        cha[count-2] = cha[count-1] 
        break

result = int(rest/count)

cha[count-1] += result

print(cha[count-1])
