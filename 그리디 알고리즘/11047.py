# /**
#  * @author [Limm-jk]
#  * @email [201602057@cs-cnu.org]
#  * @create date 2020-03-26 19:05:09
#  * @modify date 2020-03-26 19:05:09
#  * @desc [그리디 준규의 동전]
#  */

N, K = map(int,input().split()) # N은 동전 수 K는 가치
arr = []

for i in range(N):
    arr.append(int(input()))

value = K
count = 0

for i in range(1,N+1):
    # while(1):
    #     if (value - arr[N-i]) < 0:
    #        break
    #     else:
    #         value -= arr[N-i]
    #         count += 1
    if (value - arr[N-i]) < 0:
        continue
    else:
        a = int(value/arr[N-i])
        value -= a*arr[N-i]
        count+=a

print(count)