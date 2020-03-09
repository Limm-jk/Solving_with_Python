#손익분기점

arr = list(input().split())
A = int(arr[0])
B = int(arr[1])
C = int(arr[2])

count = 1
if B >= C:
    print(-1)
    exit()
else:
    print(int((A/(C-B)))+1)
