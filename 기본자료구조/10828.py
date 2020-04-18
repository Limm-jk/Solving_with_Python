# /**
#  * @author [Limm-jk]
#  * @email [201602057@cs-cnu.org]
#  * @create date 2020-04-19 00:37:35
#  * @modify date 2020-04-19 00:37:35
#  * @desc [스택]
#  */

import sys

stack = []

stack_len = 0

def push(a):
    stack.append(a)
    global stack_len
    stack_len += 1

def pop():
    a = -1
    global stack_len
    if stack_len != 0:
        a = stack.pop()
        stack_len -= 1
    return a

def size():
    return stack_len

def empty():
    result = 0
    if stack_len == 0:
        result = 1
    return result

def top():
    result = -1
    if stack_len != 0:
        result = stack[len(stack)-1]
    return result

for _ in range(int(input())):
    index = sys.stdin.readline().split()

    if index[0] == 'push':
        push(int(index[1]))
    elif index[0] == 'pop':
        print(pop())
    elif index[0] == 'size':
        print(size())
    elif index[0] == 'empty':
        print(empty())
    elif index[0] == 'top':
        print(top())