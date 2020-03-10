#직각 삼각형

while 1:
    a,b,c = map(int, input().split())
    if (a == 0) & (b == 0) & (c == 0):
        break
    a2 = a**2
    b2 = b**2
    c2 = c**2
    
    maxN = a2 if a2 > b2 else (b2 if b2>c2 else c2)
    sumN = a2+b2+c2
    if sumN == 2*maxN:
        print('right')
    else:
        print('wrong')