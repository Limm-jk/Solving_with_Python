#Fly me to the Alpha Centauri
#k로 이동시 다음 이동은 k-1 k k+1중 하나
#마지막은 1이 되어야함
#최소 구하기

T = int(input())

for i in range(3,T):
    x,y=map(int, input().split())
    length = y-x
    # mph = 1
    # locate = 0
    # ans = 0
    # while 1:
    #     locate += mph
    #     if locate + mph+1 >= length/2:
    #         if locate+((mph+1)/2) == length/2:
    #             ans = 2*mph+1
    #         elif locate + mph+1 == length/2:
    #             ans = 2*mph+2
    #         elif locate+((mph+1)/2) > length/2:
    #             ans = 2*mph+1
    #         elif locate+((mph+1)/2) < length/2:
    #             ans = 2*mph+2
    #         break
    #     mph += 1
    count = 1
    sumN = 2
    while 1:
        sumN += 2+2*count
        if sumN >= length:
            break
        count += 1
    if sumN-count-1 < length:
        print(2+2*count)
    else:
        print(1+2*count)


