def gcd(a, b):
	while(b!=0):
		r = a%b
		a = b
		b = r
	
	return a

def sol(w,h,x):
    ans = -(w/h*x)+w
    return int(ans)

def solution(w,h):
    answer = 0
    gcd1 = gcd(w, h)
    w1 = int(w/gcd1)
    h1 = int(h/gcd1)

    smallblock = 0
    for i in range(1,h1+1):
        smallblock += sol(w1,h1,i)
    smallblock = w1*h1 - 2*smallblock
    answer = w*h - (smallblock * gcd1)
    return answer

print(solution(8,12))