N = int(input())

arr = list(map(int, input().split()))
maxN = max(arr)
for i in range(N):
    arr[i] = arr[i]/maxN*100

avg = sum(arr)/N

print(round(avg,3))