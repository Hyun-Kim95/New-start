# 행렬로 피보나치수열 구하기
# (Fn+1  Fn  )   (1  1) ^ n
# (          ) = (    )
# (Fn    Fn-1)   (1  0)
import sys                  # 11444 피보나치 수 6
input = sys.stdin.readline  # n번째 피보나치 수를 1000000007로 나눈 나머지를 구하여라
n = int(input())
a = 1000000007
F = [[1,1],[1,0]]           # 주어지는 n이 최대 1,000,000,000,000,000,000까지 주어지기 때문에
def hang(f,b):              # 일반적인 방법으로 계산하면 안되고 행렬을 이용한 방법을 이용해야 함
    k = [[0,0],[0,0]]
    if b == 0:
        return k
    elif b==1:
        return f
    elif b%2==1:
        a0=k
        c=hang(f,b-1)
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    a0[i][j]+=c[i][k]*f[k][j]
                a0[i][j]%=a
        return a0
    else:
        a1=[[0,0],[0,0]]
        c=hang(f,b//2)
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    a1[i][j]+=c[i][k]*c[k][j]
                a1[i][j]%=a
        return a1

ans = hang(F,n)
print(ans[0][1])
