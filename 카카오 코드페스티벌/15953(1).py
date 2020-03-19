# /**
#  * @author [Limm-jk]
#  * @email [201602057@cs-cnu.org]
#  * @create date 2020-03-19 17:26:59
#  * @modify date 2020-03-19 17:26:59
#  * @desc [카카오 1번문제.]
#  */
from math import log2
T = int(input())

com1 = [0,500,300,200,50,30,10]
com2 = [512,256,128,64,32, 0]

for i in range(T):
    a,b = map(int,input().split())
    count = 1
    people = 0
    result = 0
    while 1:
        people += count
        if people >= a:
            break
        if people == 21:
            count = 0
            break
        count += 1
    if a !=0:
        result += com1[count]

    count = 1
    people = 0
    while 1:
        people += count
        if people >= b:
            break
        if people == 31:
            count = 32
            break
        count *= 2
    if b != 0:
        result += com2[int(log2(count))]

    print(result*10000)