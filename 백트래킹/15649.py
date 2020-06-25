# /**
#  * @author [Limm-jk]
#  * @email [201602057@cs-cnu.org]
#  * @create date 2020-06-25 18:01:05
#  * @modify date 2020-06-25 18:01:05
#  * @desc [N과 M]
#  */



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
        check_arr[i] = False

printer(0,N,M)

