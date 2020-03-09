#달팽이쉨
#낮에 A미터 밤에 -B미터 총길이 V미터
from math import *

A,B,V=map(int, input().split())
goal = V-A
One_Day = A-B
Day = ceil(goal/One_Day)
print(Day+1)