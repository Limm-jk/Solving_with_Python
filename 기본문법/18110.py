arr = []

N = int(input())

for _ in range(N):
    arr.append(int(input()))

arr.sort()
cut = int(round(N*0.15))

sum = 0
for i in range(cut,N-cut):
    sum += arr[i]

answer = int(round(sum/(N-2*cut)))

print(answer)