from functools import reduce

arr = reduce(lambda x, y : y+x, "abcde")
# 타입은 넣어준 자료형을 따라감.
print(type(arr))