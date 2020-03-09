#공백없는 문자열 총합

N = int(input())
arr = [0 for i in range(N)]
arr = list(input())
for i in range(N):
    arr[i] = int(arr[i])
print(sum(arr))