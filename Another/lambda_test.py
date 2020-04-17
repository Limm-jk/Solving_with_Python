from functools import reduce

# arr = reduce(lambda x, y : y+x, "abcde")
# # 타입은 넣어준 자료형을 따라감.
# print(type(arr))
N = 5
arr = [5, 10, 15, 20, 25, 30]
print(list(map(lambda x: x/N,arr)))