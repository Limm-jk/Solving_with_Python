# 그룹단어체커
# 연속되지 않은 같은 단어의 존재 체크
# ex aabb O abab X
#아스키 소문 97~122

N = int(input())
resultArr = [0 for i in range(N)]

for i in range(N):
    sent = list(input())
    Listsize = len(sent)
    lastAlp = -1
    result = True
    AlpArr = [0 for i in range(26)]

    for j in range(Listsize):
        str2asc = ord(sent[j])
        str2asc -= 97
        if AlpArr[str2asc] != 0:
            if lastAlp != str2asc:
                result = False
                break
        AlpArr[str2asc] += 1
        lastAlp = str2asc
    if result:
        resultArr[i] += 1

print(sum(resultArr))