# /**
#  * @author [Limm-jk]
#  * @email [201602057@cs-cnu.org]
#  * @create date 2020-03-20 14:57:03
#  * @modify date 2020-03-20 14:57:03
#  * @desc [LCS]
#  */

arr1 = (list(input()))
arr2 = (list(input()))

DParr = [[0]*(len(arr2)+1) for i in range(len(arr1)+1)]

for i in range(1,len(arr1)+1):
    for j in range(1,len(arr2)+1):
        DParr[i][j] = max(DParr[i-1][j],DParr[i][j-1])
        if arr1[i-1] == arr2[j-1]:
            DParr[i][j] = DParr[i-1][j-1] + 1

print(DParr[len(arr1)][len(arr2)])