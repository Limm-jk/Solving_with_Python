import random
import time

parti = ['강효정','배재홍','황근영','조은빈','최윤선','서유경','김민지','주혜원','김가영','김민규']


for _ in range(5):
    arr = [0 for _ in range(len(parti))]
    coffee = ''
    # 2500번 랜덤
    for _ in range(2500):
        a = random.randint(0,len(parti)-1)
        arr[a] += 1

    # 당첨자 체크
    maxN = max(arr)
    dangchum = []
    for i in range(len(parti)):
        if arr[i] == maxN:
            dangchum.append(i)

    # 중복 처리
    if len(dangchum) != 1:
        b = random.randint(0,len(dangchum)-1)
        coffee = parti.pop(dangchum[b])
    else:
        coffee = parti.pop(dangchum[0])

    print(coffee)
    
    time.sleep(1)
