#벌집
#1-6-12-18-24-...

N = int(input())
count = 1
ans = 1
if N == 1:
    print(1)
else:
    while 1:
        ans += 6*count
        if ans >= N:
            break
        count += 1
    print(count+1)
        