#직사각형 탈출

x,y,w,h = map(int, input().split())
arr = [x,y,h-y,w-x]

print(min(arr))
