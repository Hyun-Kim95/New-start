import sys
n = int(sys.stdin.readline())

tyle = [0] * 1000001                                  # 정답지
tyle[1] = 1
tyle[2] = 2
for k in range(3,n+1):
    tyle[k] = (tyle[k-1]+ tyle[k-2])%15746

print(tyle[n])

#------------------------------------------------
import sys
sys.setrecursionlimit(10**6)  # 최대 재귀 깊이를 변경해서 런타임에러를 피하긴 했는데...
n = int(sys.stdin.readline())

memo = {
    1:1,
    2:2,
    3:3                                             # 메모리초과
}

def tyle(n):
    if n in memo:
        return memo[n]
    else:
        a = tyle(n-1) + tyle(n-2)
        memo[n] = a
        return a
    


print(tyle(n) % 15746)
