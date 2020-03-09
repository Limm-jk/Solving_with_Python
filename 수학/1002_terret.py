from math import *

N = int(input())

for i in range(N):
    result = 0
    locate = list(input().split())
    for j in range(len(locate)):
        locate[j] = int(locate[j])
    a = locate[0]-locate[3] #x간의 거리
    b = locate[1]-locate[4] #y간의 거리
    two_size_add = locate[2] + locate[5]
    short_side = locate[2] if locate[2] <= locate[5] else locate[5]
    side = sqrt(a**2 + b**2)
    if side == 0:
        if locate[2] == locate[5]:
            result = -1
    elif two_size_add > side:
        if (side + short_side) < (two_size_add - short_side):
            result = 0
        elif (side + short_side) == (two_size_add - short_side):
            result = 1
        else : 
            result = 2
    elif two_size_add == side:
        result = 1
    print(result)