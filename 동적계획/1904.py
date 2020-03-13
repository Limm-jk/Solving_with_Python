#01타일
#00은 붙어서만 쓸수있다
#몇개나 만들 수 있을까

N = int(input())

arr = [0 for i in range(N)]

arr[0] = 1
arr[1] = 2

for i in range(2,N):
    arr[i] = (arr[i-1]+arr[i-2])%15746

print(arr[N-1])