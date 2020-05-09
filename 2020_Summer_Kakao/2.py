import re
import copy
from functools import reduce

def minfi(num1,exp1):
    ans = []
    num = copy.deepcopy(num1)
    exp = copy.deepcopy(exp1)
    count = 0
    leng = len(exp)
    for i in range(leng):
        if exp[i] == '-':
            num[i-count] -= num[i-count+1]
            
            num.pop(i+1-count)
            count += 1
    exp = list(filter(lambda x: x != '-', exp))
    count = 0

    #1. 곱하기 연산
    num3 = copy.deepcopy(num)
    exp3 = copy.deepcopy(exp)
    for i in range(len(exp3)):
        if exp3[i] == '*':
            num3[i+1-count] *= num3[i-count]
            num3.pop(i-count)
            count += 1
    ans.append(abs(sum(num3)))
    count = 0

    #2. 덧셈선
    for i in range(len(exp)):
        if exp[i] == '+':
            num[i+1-count] += num[i-count]
            num.pop(i-count)
            count += 1

    ans.append(abs(reduce(lambda x,y:x*y, num)))


    return max(ans)

def plfi(num1,exp1):
    ans = []
    num = copy.deepcopy(num1)
    exp = copy.deepcopy(exp1)
    count = 0
    leng = len(exp)
    for i in range(leng):
        if exp[i] == '+':
            num[i+1-count] += num[i-count]
            
            num.pop(i-count)
            count += 1
    exp = list(filter(lambda x: x != '+', exp))
    count = 0

    #1. 곱하기 연산
    num3 = copy.deepcopy(num)
    exp3 = copy.deepcopy(exp)
    for i in range(len(exp3)):
        if exp3[i] == '*':
            num3[i+1-count] *= num3[i-count]
            num3.pop(i-count)
            count += 1
    ans.append(abs(reduce(lambda x,y: x-y,num3)))
    count = 0

    #2. 빼기선
    for i in range(len(exp)):
        if exp[i] == '-':
            num[i-count] -= num[i+1-count]
            num.pop(i+1-count)
            count += 1

    ans.append(abs(reduce(lambda x,y:x*y, num)))

    
    return max(ans)

def mulfi(num1,exp1):
    ans = []
    num = copy.deepcopy(num1)
    exp = copy.deepcopy(exp1)
    count = 0
    leng = len(exp)
    for i in range(leng):
        if exp[i] == '*':
            num[i+1-count] *= num[i-count]
            num.pop(i-count)
            count += 1
    exp = list(filter(lambda x: x != '*', exp))
    count = 0

    #1. - 연산
    num3 = copy.deepcopy(num)
    exp3 = copy.deepcopy(exp)
    for i in range(len(exp3)):
        if exp3[i] == '-':
            num3[i-count] -= num3[i+1-count]
            num3.pop(i+1-count)
            count += 1
    ans.append(abs(sum(num3)))
    count = 0

    #2. 덧셈선
    for i in range(len(exp)):
        if exp[i] == '+':
            num[i+1-count] += num[i-count]
            num.pop(i-count)
            count += 1

    ans.append(abs(reduce(lambda x,y: x-y,num)))

    return max(ans)
        
            
def popop(num):
    num1 = num
    num1.pop(1)
    
def solution(expression):
    Num_arr = list(map(int,re.findall("\d+",expression)))
    exp_arr = re.findall("\D",expression)
    answer_arr = [1]
    answer_arr.append(minfi(Num_arr,exp_arr))
    answer_arr.append(plfi(Num_arr,exp_arr))
    answer_arr.append(mulfi(Num_arr,exp_arr))
    
    answer = max(answer_arr)
    return answer

a = "100-200*300-500+20"

print(solution(a))
