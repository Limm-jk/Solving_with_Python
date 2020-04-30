# /**
#  * @author [Limm-jk]
#  * @email [201602057@cs-cnu.org]
#  * @create date 2020-04-30 17:22:51
#  * @modify date 2020-04-30 17:22:51
#  * @desc [description]
#  */

def isEmpty(arr):
    res = True
    if len(arr) != 0:
        res = False
    return res

#input
for i in range(int(input())):
    inp_arr = list(input())
    stack_front = []
    stack_back = []

    # 문자열 처리
    for cnt in range(len(inp_arr)):
        if inp_arr[cnt] == '<':
            if not isEmpty(stack_front):
                stack_back.append(stack_front.pop())
        elif inp_arr[cnt] == '>':
            if not isEmpty(stack_back):
                stack_front.append(stack_back.pop())
        elif inp_arr[cnt] == '-':
            if not isEmpty(stack_front):
                stack_front.pop()
        else:
            stack_front.append(inp_arr[cnt])

    # 해답 도출
    while not isEmpty(stack_back):
        stack_front.append(stack_back.pop())
    
    answer = "".join(stack_front)

    print(answer)
