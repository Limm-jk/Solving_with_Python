#하노이의 탑
#다 옮기면 세상 끝이라는 그거 맞음 ㅇㅇ

def hanoi(N):
    if N == 1:
        return 1
    return 2*hanoi(N-1)+1
def hanoiN(N,Num,locArr):
    if N == 1:
        print("%d %d"%(locArr[N-1], Num))
        locArr[N-1] = Num
    else:
        hanoiN(N-1,6-Num-locArr[N-1],locArr)
        print("%d %d"%(locArr[N-1], Num))
        locArr[N-1] = Num
        hanoiN(N-1,Num,locArr)

N = int(input())
locate = [1 for i in range(N)]
print(hanoi(N))
hanoiN(N,3,locate)