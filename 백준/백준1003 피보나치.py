zmemo = {
    0:1,
    1:0,
    2:1
}

omemo = {
    0:0,
    1:1,
    2:1
}    

def Zero(n):
    if n in zmemo:
        return zmemo[n]
    else:
        a = Zero(n-1) + Zero(n-2)
        zmemo[n] = a
        return a

def One(n):
    if n in omemo:
        return omemo[n]
    else:
        a = One(n-1) + One(n-2)
        omemo[n] = a
        return a

for i in range(int(input())):
    n = int(input())
    z = Zero(n)
    o = One(n)
    print(z,o)
#---------------------------------------일단 이렇게 길게 풀었는데 규칙 찾아서 답나오게 만들면 이렇게 짧아진다ㅡㅡ
# 1 0     0                             # n일때 1갯수+0갯수는  n+1 의 1갯수 이고
# 0 1     1                             # n일때 1갯수는        n+1의 0갯수 이다
# 1 1     2
# 1 2     3
# 2 3     4
# 3 5     5
# 5 8     6
# 8 13    7
# 13 21   8
# 21 34   9
# 34 55   10

t = int(input())
for i in range(t):
    n = int(input())
    zero = 1
    one = 0
    tmp = 0
    for _ in range(n):
        tmp = one
        one = one + zero
        zero = tmp
    print(zero, one)
