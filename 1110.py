N = int(input())
result = N
count = 1
# a는 뒷자리 b는 앞자리
while 1:
    a = result%10 
    b = int(result/10)
    sum = a+b
    sumN = sum%10
    result = 10*a+sumN

    if N == result:
        print(count)
        break
    else:
        count+=1
