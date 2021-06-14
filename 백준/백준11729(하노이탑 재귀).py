n = int(input())
a = 0
def top(n):
    if n == 1:
        return 1
    else:
        return top(n-1) + 2**(n-1)

def hanoi(n,a,b,c):
    if n == 1:
        print(a,c)
    else:
        hanoi(n-1,a,c,b)
        print(a,c)
        hanoi(n-1,b,a,c)

print(top(n))
hanoi(n,1,2,3)
