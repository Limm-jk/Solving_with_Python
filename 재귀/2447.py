#별 찍기
#ㅇㅇ재귀
#N은 3의 거듭제곱
#3X3일때 가운데 빼고 별 9X9일때 가운데 세개 빼고 별..
from math import *

def star(N):
    if N == 1:
        print("***\n* *\n***")
    print()

N = int(input())

a = int(log(N,3))
