# /**
#  * @author [Limm-jk]
#  * @email [201602057@cs-cnu.org]
#  * @create date 2020-03-20 14:52:57
#  * @modify date 2020-03-20 14:52:57
#  * @desc [백준 배낭문제]
#  */

N,K = map(int,input().split())  # 물품수와 최대무게

table = [[0 for _ in range(K+1)] for _ in range(N+1)] # table[물품수][최대무게]
products = [[0,0]]

for i in range(N):
    products.append(list(map(int,input().split()))) # [무게,가치]

for i in range(1, N+1):
    for j in range(1, K+1):
        weight = products[i][0]
        value = products[i][1]

        if j >= weight:
            table[i][j] = max(value + table[i-1][j-weight], table[i-1][j]) 
            # 타겟이 된 짐을 넣을 수 있으면, 그 짐을 넣고 남는 무게의 최댓값을 더해서 위의 값과 비교한다.
        else:
            table[i][j] = table[i-1][j] # 타겟이된 짐을 넣을 수 없다면 위의 값을 가져온다.

print(table[N][K])