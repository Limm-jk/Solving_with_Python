max = 0
for i in range(0,9):
    a = int(input())
    if a > max:
        max = a
        maxN = i

print(max)
print(maxN+1)