# /**
#  * @author [Limm-jk]
#  * @email [201602057@cs-cnu.org]
#  * @create date 2020-03-19 17:54:14
#  * @modify date 2020-03-19 17:54:14
#  * @desc [카카오 코페 2번 인형문제]
#  */
from math import *
N, K = map(int,input().split())

dolls = []

dolls = list(map(int,input().split()))


DParr = []

for i in range(N-K+1):
    sumN = 0
    avgarr = []
    for j in range(i, i+K):
        sumN+=dolls[j]

    avgarr.append(sumN/K)
    count = 1

    for j in range(i+K, N):
        sumN += dolls[j]
        avgarr.append(sumN/(K+count))
        count += 1
    #1개씩 더 넣어가며 가능한 평균을 다 집어넣음

    sumsum = 0
    for j in range(i, i+K):
        sumsum += (dolls[j])**2
    bunsan = sumsum/K
    bunsan -= avgarr[0]**2
    DParr.append(bunsan)

    count = 1
    for j in range(i+K, N):
        sumsum += (dolls[j])**2
        bunsan = sumsum/(K+count)
        bunsan -= avgarr[count]**2
        DParr.append(bunsan)
        count += 1

    # for count in range(1,len(avgarr)):
    #     bunsan = 0
    #     for j in range(i, i+K+count):
    #         bunsan += (dolls[j]-avgarr[count])**2
    #     bunsan /= (K+count)
    #     DParr.append(bunsan)
print(round(min(DParr), 11))   
print(round(sqrt(min(DParr)), 11))