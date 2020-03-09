#알파벳찾기
#문자열에서 등장위치, 없으면 -1
#a~z => 97~122

N = list(input())
size = len(N)
Alarr = [-1 for i in range(26)]
for i in range(size):
    if Alarr[ord(N[i])-97] == -1:
        Alarr[ord(N[i])-97] = i

for i in range(26):
    print(Alarr[i], end=' ')
