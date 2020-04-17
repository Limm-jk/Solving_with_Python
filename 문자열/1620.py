# /**
#  * @author [Limm-jk]
#  * @email [201602057@cs-cnu.org]
#  * @create date 2020-04-13 15:46:31
#  * @modify date 2020-04-13 15:46:31
#  * @desc [description]
#  */

from numpy.core.defchararray import isdigit
import sys

poke_arr = []

x,y = map(int, sys.stdin.readline().split())

for _ in range(x):
    poke_arr.append(sys.stdin.readline().rstrip())

for _ in range(y):
    input1 = sys.stdin.readline().rstrip()
    if(isdigit(input1)):
        print(poke_arr[int(input1)-1])

    else:
        print(poke_arr.index(input1)+1)

