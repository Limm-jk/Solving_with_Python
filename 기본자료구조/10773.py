# /**
#  * @author [Limm-jk]
#  * @email [201602057@cs-cnu.org]
#  * @create date 2020-04-19 01:33:58
#  * @modify date 2020-04-19 01:33:58
#  * @desc [틀리면 0으로 지우기 스택]
#  */

stack = []

for _ in range(int(input())):
    inp = int(input())
    if inp == 0:
        stack.pop()
        continue
    stack.append(inp)

print(sum(stack))
    