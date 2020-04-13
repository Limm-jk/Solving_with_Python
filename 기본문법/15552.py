import sys

for _ in range(int(sys.stdin.readline())):
    arr = map(int, sys.stdin.readline().split())
    print(sum(arr))
