from functools import reduce

# arr = reduce(lambda x, y : y+x, "abcde")
# # 타입은 넣어준 자료형을 따라감.
# print(type(arr))
# N = 5
# arr = [5, 10, 15, 20, 25, 30]
# print(list(map(lambda x: x/N,arr)))


arr = [[1,2],[2,1],[3,2],[4,1]]

arr1 = sorted(arr, key=lambda x: x[1])
arr.sort
print(arr1)
print(arr)