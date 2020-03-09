#분수찾기
#등비수열
#수열영역마다 위 아래의 합이 1씩 증가

N = int(input())
count = 1
sumN = 0
a = 0
b = 0
while 1:
    sumN += count
    if sumN >= N:
        break
    count += 1
side = sumN-N
if count%2 == 0:
    a = count-side
    b = 1+side
else:
    b = count-side
    a = 1+side

print("%d/%d"%(a,b))

