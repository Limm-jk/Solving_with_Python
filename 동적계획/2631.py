arr = []
N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

lisarr = [0 for i in range(N)] # 길이 저장

for i in range(N):
    for j in range(i):
        if (arr[j] < arr[i]) & (lisarr[i] < lisarr[j]):
            lisarr[i] = lisarr[j]
    lisarr[i] += 1

print(N-max(lisarr))