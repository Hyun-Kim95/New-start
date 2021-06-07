# 페르마의 소정리
# (A + B) % C = (A%C + B%C) % C
# (A - B) % C = (A%C - B%C) % C
# (A X B) % C = (A%C X B%C) % C

# 위 공식들을 보면 나누기는 없음 따라서 이항계수를 곱샘의 형태로 바꿔줘야 함
# A^(P-1) % P = 1       # P는 소수, A는 P의 배수이면 안됨
# A^(P-2) % P = 1/A     # 분모 부분을 왼쪽 형식으로 변경 가능함을 확인

# 이항계수
# (n)           n!
# ( )   = -------------
# (k)       k!(n-k)!

# 즉, (n! // k!(n-k)!) % p = n! * (k!(n-k)!)^(P-2) % p = (n! % p * (k!(n-k)!)^(p-2) % p) % p
import sys
input = sys.stdin.readline
n,k = map(int,input().split())              # 11401 이항계수3   이항계수로 n,k를 1000000007로 나눈 나머지를 구하시오
p = 1000000007

def z(a,b):                                 # a^b 구하는 함수
    if b == 0:                              # 0제곱은 1
        return 1
    elif b % 2 != 0:                        # b의 수를 줄이면서 계산
        return (z(a,b//2) ** 2 * a) % p
    else:
        return (z(a,b//2) ** 2) % p

fac = [1 for _ in range(n+1)]               # 펙토리얼을 구해줌
for i in range(2,n+1):
    fac[i] = fac[i-1] * i % p

A = fac[n]                                  # 이항계수의 분자
B = (fac[n-k] * fac[k]) % p                 # 이항계수의 분모 % p
print((A%p * z(B,p-2)%p)%p)                 # 페르마의 소정리 이용
