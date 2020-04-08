import random

arr = ['짱깨',  "국수", '냉면', '서브', '맘터','부리또','회덮', '피자','치킨','육비']
arr1 = [0 for i in range(10)]
sumN = 0
for i in range(550):
    A = random.randrange(10)
    arr1[A] += 1
    sumN += A
print(arr)
print(arr1)
print(arr[arr1.index(max(arr1))])