# /**
#  * @author [Limm-jk]
#  * @email [201602057@cs-cnu.org]
#  * @create date 2020-03-19 17:54:14
#  * @modify date 2020-03-19 17:54:14
#  * @desc [카카오 코페 2번]
#  */
from math import *
N, K = map(int,input().split())

dolls = []

dolls = list(map(int,input().split()))


DParr = []

for i in range(len(dolls)-K+1):
    sumN = 0
    for j in range(i, i+K):
        sumN+=dolls[j]
    avg = sumN/K
    bunsan = 0
    for j in range(i, i+K):
        bunsan += (dolls[j]-avg)**2
    bunsan /= K
    DParr.append(bunsan)

print(round(sqrt(min(DParr)), 7))