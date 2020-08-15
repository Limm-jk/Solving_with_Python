A,B,C = map(int, input().split())

arr = []

def solve(root):
    if root == 1:
        return A%C
    elif root == 0:
        return 1
    elif (root % 2) == 0:
        return (solve(root/2)%C)**2
    else:
        return (solve(root-1)%C) * (A%C)

print(solve(B)%C)