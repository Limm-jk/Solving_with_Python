#수-퍼 블랙잭
#N장의 카드를 깔고, M보다 크진않지만 가장 가까운 
#세장의 합을 찾는다.

N,M=map(int, input().split())

arr = list(input().split())
sim = 0

for i in range(N):
    arr[i] = int(arr[i])

for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if sim < arr[i]+arr[j]+arr[k] <= M:
                sim = arr[i]+arr[j]+arr[k]
                if sim == 500:
                    print(arr[i],arr[j],arr[k])

print(sim)