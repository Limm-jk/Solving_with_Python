# /**
#  * @author [Limm-jk]
#  * @email [201602057@cs-cnu.org]
#  * @create date 2020-03-20 14:52:57
#  * @modify date 2020-03-20 14:52:57
#  * @desc [백준 배낭문제]
#  */

N,K = map(int,input().split())  # 물품수와 최대무게

for i in range(N):
    W,V = map(int,input().split())