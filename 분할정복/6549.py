# /**
#  * @author [Limm-jk]
#  * @email [201602057@cs-cnu.org]
#  * @create date 2020-08-14 16:15:23
#  * @modify date 2020-08-14 16:15:23
#  * @desc [분할 정복 아닌거같은데...]
#  */

while True:

    stack = []
    index = 0 # 스택의 크기
    answer = 0

    # input
    N, *his = list(map(int, input().split()))
    if N == 0:
        break

    # 스택을 이용하여 N 전체탐색 Solution
    for i in range(N):
        if index == 0 or his[stack[index-1]] <= his[i]:
            stack.append(i)
            index += 1
        else:
            while index != 0 and his[stack[index-1]] > his[i]:
                sq = his[stack[index-1]]
                index -= 1
                stack.pop()
                wei = 0
                if index != 0:
                    wei = stack[index-1]+1

                sq *= i-wei

                if sq > answer:
                    answer = sq

            stack.append(i)
            index += 1

    while index != 0:
        sq = his[stack[index-1]]

        index -= 1
        stack.pop()
        wei = 0
        if index != 0:
            wei = stack[index-1]+1

        sq *= N-wei
        
        if sq > answer:
            answer = sq
    
    print(answer)