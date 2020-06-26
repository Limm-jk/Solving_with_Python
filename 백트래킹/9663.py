N = int(input())

count = 0
Str = [True for _ in range(N)]
R_cross = [True for _ in range(2*N)]
L_cross = [True for _ in range(2*N)]


def printer(n):
    # base case
    global count
    if n == N:
        count += 1

        return
    
    for i in range(N):
        if (Str[i] and R_cross[n-i+N-1] and L_cross[i+n]):
            Str[i] = False
            R_cross[n-i+N-1] = False
            L_cross[i+n] = False
            printer(n+1)
            Str[i] = True
            R_cross[n-i+N-1] = True
            L_cross[i+n] = True


printer(0)
print(count)