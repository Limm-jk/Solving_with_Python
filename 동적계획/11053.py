#가장 긴 증가하는 수열

arr = []
N = int(input())
arr = list(map(int, input().split()))

lisarr = [0 for i in range(N)]

for i in range(N):
    for j in range(i):
        if (arr[j] < arr[i]) & (lisarr[i] < lisarr[j]):
            lisarr[i] = lisarr[j]
    lisarr[i] += 1

print(max(lisarr))