def fac(n):             #팩토리얼
    if n == 0:
        return 1
    else:
        return n * fac(n-1)

n = int(input())
print(fac(n))
#-----------------------------
def fib(n):             #피보나치수열
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

n = int(input())
print(fib(n))
