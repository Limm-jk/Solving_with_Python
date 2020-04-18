# /**
#  * @author [Limm-jk]
#  * @email [201602057@cs-cnu.org]
#  * @create date 2020-04-19 01:16:59
#  * @modify date 2020-04-19 01:16:59
#  * @desc [0 1 -1 종이 갯수]
#  */

z_count = 0
mi_count = 0
pl_count = 0

def NonaTree(x,y,k):
    # x축시작점 y축시작점 종이길이
    temp = table[x][y]
    global z_count,mi_count,pl_count
    for i in range(x,x+k):
        for j in range(y,y+k):
            if temp != table[i][j]:
                # 9분할
                tri = int(k/3)
                s1 = NonaTree(x,y,tri) #00
                s2 = NonaTree(x+tri,y,tri)#10
                s3 = NonaTree(x+2*tri,y,tri)#20
                s4 = NonaTree(x,y+tri,tri)#01
                s5 = NonaTree(x+tri,y+tri,tri)#11
                s6 = NonaTree(x+2*tri,y+tri,tri)#21
                s7 = NonaTree(x,y+2*tri,tri)#02
                s8 = NonaTree(x+tri,y+2*tri,tri)#12
                s9 = NonaTree(x+2*tri,y+2*tri,tri)#22

                return

    if temp == -1:
        mi_count += 1
    elif temp == 0:
        z_count += 1
    elif temp == 1:
        pl_count += 1


# input
N = int(input())

table = []
for _ in range(N):
    table.append(list(map(int,input().split())))

# solve
NonaTree(0,0,N)

print(mi_count)
print(z_count)
print(pl_count)