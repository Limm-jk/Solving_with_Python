N, M = map(int, input().split())

answer_arr = [0 for _ in range(M)]

check_arr = [False for _ in range(N+1)]

def printer(index, N, M):
    # base case
    if index == M:
        for i in answer_arr:
            print(i, end=' ')
        print()

        return
    
    for i in range(1, N+1):
        if check_arr[i]:
            continue
            # check_arr를 확인하여 
            # 탐색했을 시 패스
        
        # 아니면
        check_arr[i] = True
        answer_arr[index] = i
        printer(index+1, N, M)
        # check_arr[i] = False
        # if index == 0:
        for j in range(i+1, N+1):
            check_arr[j] = False

printer(0,N,M)
