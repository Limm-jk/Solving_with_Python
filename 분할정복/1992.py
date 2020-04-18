# /**
#  * @author [Limm-jk]
#  * @email [201602057@cs-cnu.org]
#  * @create date 2020-04-18 01:53:14
#  * @modify date 2020-04-18 01:53:14
#  * @desc [quad Tree]
#  */

def quadTree(x,y,k):
    temp = image[x][y]

    for i in range(x,x+k):
        for j in range(y,y+k):
            if image[i][j] != temp:
                a = int(k/2)
                S1 = quadTree(x,y,a)
                S2 = quadTree(x,y+a,a)
                S3 = quadTree(x+a,y,a)
                S4 = quadTree(x+a,y+a,a)
                sumarr = ['(',S1,S2,S3,S4,')']
                result = "".join(sumarr)
                return result

    if temp == 1:
        return '1'
    elif temp == 0:
        return '0'
# iamge array
image = []

# input
N = int(input())

# table
for _ in range(N):
    image.append(list(map(int,input())))

# output
result = quadTree(0,0,N)
print(result)