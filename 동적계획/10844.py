#쉬운계단수
#수가 1씩차이나는거 45656

N = int(input())
# arr = [0 for i in range(N+1)]

# for i in range(N+1):

arr = [0,1,1,1,1,1,1,1,1,1]
for i in range(N-1):
    newarr = [0 for i in range(10)]
    for j in range(10):
        if j == 0:
            newarr[1] += arr[0]
        elif j == 9:
            newarr[8] += arr[9]
        else:
            newarr[j+1] += arr[j]
            newarr[j-1] += arr[j]
    for i in range(10):
        arr[i] = newarr[i]%1000000000

print(sum(arr)%1000000000)
