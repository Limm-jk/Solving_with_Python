#Fly me to the Alpha Centauri
#k로 이동시 다음 이동은 k-1 k k+1중 하나
#마지막은 1이 되어야함
#최소 구하기

T = int(input())

for i in range(T):
    x,y=map(int, input().split())
    length = y-x
    count = 1
    sumN = 1
    while 1:
        if count**2+count >= length:
            break
        count += 1
    if count**2 >= length:
        print(2*count-1)
    else:
        print(2*count)


        