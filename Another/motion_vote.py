import random
import time

parti = ['최윤선','서유경','김가연','서홍석','조은빈','주혜원','이정준','김주하']


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
