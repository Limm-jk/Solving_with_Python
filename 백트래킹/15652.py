N, M = map(int, input().split())

answer_arr = [0 for _ in range(M)]


def printer(index, N, M):
    # base case
    if index == M:
        for i in answer_arr:
            print(i, end=' ')
        print()

        return
    a=0
    if index == 0:
        a = 1
    else:
        a = answer_arr[index-1]
    for i in range(a, N+1):

        answer_arr[index] = i
        printer(index+1, N, M)


printer(0,N,M)
