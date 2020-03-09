#설탕
#3짜리 5짜리로 N 만들기
#나머지 1일때 5 -1 3 +2 = +1
#나머지 2일때 5 -2 3 +4 = +2
#나머지 3일때 3 +1 = +1
#나머지 4일때 5 -1 3 +3 = +2

N = int(input())
rem = N%5
quot = int(N/5)

if rem == 0:
    print(quot)
elif rem == 1:
    if N <= 5:
        print(-1)
    else:
        print(quot+1)
elif rem == 2:
    if N <= 10:
        print(-1)
    else:
        print(quot+2)
elif rem == 3:
    print(quot+1)
elif rem == 4:
    if N <= 5:
        print(-1)
    else:
        print(quot+2)
    