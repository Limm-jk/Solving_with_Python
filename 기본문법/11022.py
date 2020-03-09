n = int(input())


for i in range(1, n+1):
    a, b = input().split()
    a = int(a)
    b = int(b)
    result = a+b
    print("Case #%d: %d + %d = %d"%(i, a, b, result))

