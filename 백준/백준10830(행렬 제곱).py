import sys                                                          # 행렬 제곱
n,b=map(int,sys.stdin.readline().split())                           # 행,열이 같고 한 행의 크기가 n인 행렬을 거듭제곱하여 1000으로 나눈 나머지를 출력하시오
a=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]   # 크기가 n인 행렬 a

def hang(a,b):                                                      # 행렬의 제곱 함수
    if b==1:                                                        # 제곱횟수가 1 이면 행렬의 각 값을 1000으로 나눈 나머지로 바꿈
        for i in range(n):
            for j in range(n):
                a[i][j]%=1000
        return a

    elif b%2==1:                                                    # 이 조건문으로 들어오면 짝수개의 거듭제곱을 하고 마지막에 a를 한번 더 곱해주면 됨
        a0=[[0 for _ in range(n)] for _ in range(n)]                # a^5 = a^4 * a
        c=hang(a,b-1)                                               # 거듭제곱할 횟수에서 1을 빼고 재귀함수로 a의 거듭제곱 진행
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    a0[i][j]+=c[i][k]*a[k][j]
                a0[i][j]%=1000

        return a0

    else:
        a1=[[0 for _ in range(n)] for _ in range(n)]                # 짝수개의 거듭제곱을 할 경우 절반만 한것끼리 곱해주면 됨
        c=hang(a,b//2)                                              # 거듭제곱할 횟수의 절반을 재귀함수로 진행
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    a1[i][j]+=c[i][k]*c[k][j]
                a1[i][j]%=1000
        return a1

A=hang(a,b)                                                         # 함수의 결과를 받아서 출력
for li in A:
    print(*li)
