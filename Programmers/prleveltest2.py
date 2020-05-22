# /**
#  * @author [Limm-jk]
#  * @email [201602057@cs-cnu.org]
#  * @create date 2020-05-22 20:36:30
#  * @modify date 2020-05-22 20:36:30
#  * @desc [description]
#  */

def solution(nums):
    leng = len(nums)
    answer = 0
    sosu = primes(3000)
    for i in range(leng-2):
        for j in range(i+1, leng-1):
            for k in range(j+1, leng):
                if nums[i]+nums[j]+nums[k] in sosu:
                    answer+=1

    return answer
def primes(n:int):
    sosu = [False,False] + [True]*(n-1)

    for i in range(2, int(n**0.5 + 1.5)):
        if sosu[i]:
            sosu[i*2::i] = [False] * ((n-i) // i)
    return [x for x in range(n+1) if sosu[x]]

arr = []

arr = list(input())

print(primes(101))