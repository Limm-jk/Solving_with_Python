#피보나치
#0과 1이 몇번 호출되냐

arr0 = [0 for i in range(41)]
arr1 = [0 for i in range(41)]
arr0[0] = 1
arr1[1] = 1

for i in range(2,41):
    arr0[i] = arr0[i-1]+arr0[i-2]
    arr1[i] = arr1[i-1]+arr1[i-2]

for i in range(int(input())):
    N = int(input())
    print("%d %d"%(arr0[N],arr1[N]))