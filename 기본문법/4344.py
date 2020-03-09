C = int(input())
for i in range(C):
    arr = [0 for i in range(1002)]
    arr = list(map(int, input().split()))
    sumN = 0
    count = 0
    for j in range(1, arr[0]+1):
        sumN += arr[j]
    avg = sumN/arr[0]
    for j in range(1, arr[0]+1):
        if arr[j] > avg:
            count += 1
    per = (count/arr[0])*100
    print("%.3f"%(round(per,3))+ "%")



