# /**
#  * @author [Limm-jk]
#  * @email [201602057@cs-cnu.org]
#  * @create date 2020-04-18 01:16:37
#  * @modify date 2020-04-18 01:16:37
#  * @desc [색종이]
#  */

bl_count = 0
wt_count = 0

def quad(x,y,k):
    global bl_count, wt_count
    # 비교할 값 저장(이것과 비교하여 다르면 4분할)
    temp = table[x][y]
    for i in range(x, x+k):
        for j in range(y, y+k):
            # 하나라도 다를 시 4분할면 호출
            if table[i][j] != temp:
                a = int(k/2)
                quad(x,y,a)
                quad(x,y+a,a)
                quad(x+a,y,a)
                quad(x+a,y+a,a)
                return
    # 다른 것이 하나도 없을 시 temp의 값을 통해 색 확인
    if temp == 1:
        bl_count += 1
    elif temp == 0:
        wt_count += 1

# input & table
table = []
N = int(input())
for _ in range(N):
    table.append(list(map(int, input().split())))
# solve
quad(0,0,N)

# output
print(wt_count)
print(bl_count)
