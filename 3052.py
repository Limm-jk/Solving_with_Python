arr = [0 for i in range(42)]

for i in range(10):
    a = int(input())
    sub = a%42
    arr[sub] += 1
count = 0
for i in range(42):
    if arr[i] != 0:
        count += 1

print(count)