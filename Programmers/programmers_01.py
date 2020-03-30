arr = []
arr = list(input())
ordarr = []
answerarr = []
newarr = []
for i in range(len(arr)):
    ordarr.append(ord(arr[i]))
newarr = sorted(ordarr,reverse=True)
for i in range(len(newarr)):
    answerarr.append(chr(newarr[i]))

answer = "".join(answerarr)
print(answer)
#급하게 짜느라 넘나 난잡한것....ㅠㅠㅠ