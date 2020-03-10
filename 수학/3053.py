#택시기하학? 택시나 타자
#여기서의 원은 45도 기울어진 정사각형

from math import *

R = int(input())

uc = float((R**2)*pi)
taxi = float(2*R*R)

print(round(uc,5))
print(round(taxi,5))