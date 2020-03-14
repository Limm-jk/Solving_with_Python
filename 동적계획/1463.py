#1로 만들기

N = int(input())
count = 0
arr = [0 for i in range(N+1)]

# for i in range(2, N+1)
#     if i%3 == 0:
#         arr[i] = arr[int(i/3)] + 1
#     elif i%2 == 0:
#         if (i-1)%3 == 0:
#             arr[i] = arr[i-1]+1
#         else:
#             arr[i] = arr[int(i/2)]+1
#     else:
#         arr[i] = arr[i-1]+1

for i in range(2, N+1):
    arr[i] = arr[i-1] + 1
    if i%3 == 0:
        arr[i] = min(arr[i],arr[int(i/3)]+1)
    if i%2 == 0:
        arr[i] = min(arr[i],arr[int(i/2)]+1)

print(arr[N])