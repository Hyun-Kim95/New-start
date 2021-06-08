n,m = map(int,input().split())                  # 2740 행렬 곱셈    n: 첫번째 행렬의 행     m = 첫번째 행렬의 열
A = []                                          # 첫번째 행렬
for i in range(n):
    A.append(list(map(int,input().split())))


a,k = map(int,input().split())                  # a: 첫번째 행열의 m과 같음     k: 두번째 행렬의 열
B = []                                          # 두번째 행렬
for j in range(m):
    B.append(list(map(int,input().split())))

C = [[0 for _ in range(k)] for _ in range(n)]   # 행렬 곱셈의 결과 리스트(A의 행의 갯수, B의 열의 갯수를 가지고 있음)
for p in range(n):                              # 테스트 케이스 A(3,2) B(2,3) 일 때, C는 (3,3)의 크기를 가짐
    for q in range(m):                          # 이때, C[0][0]을 구하는 방법은 아래와 같음
        for w in range(k):
            C[p][w] += A[p][q] * B[q][w]        # C[0][0] = A[0][0]*B[0][0] + A[0][1]*B[0][1]
                                                #   A           B           C
for c in C:                                     # (1 2)     (-1 -2 0)   (-1 -2  6)
    print(*c)                                   # (3 4)     ( 0  0 3)   (-3 -6  12)
                                                # (5 6)                 (-5 -10 18)
