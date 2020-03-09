#피보나치
#0번째부터... N번째 피보나치수는?

arr = [0 for i in range(91)]
arr[0] = 0
arr[1] = 1
N = int(input())
for i in range(2, N+1):
    arr[i] = arr[i-1]+arr[i-2]

print(arr[N])