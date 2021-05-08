import math
n = int(input())                                    # 2981  -> 주어진 숫자를 어떤 수'M'으로 나누어 나머지가 전부 같은 'M'을 찾기
num = []                                            # n개의 숫자
a = []                                              # 정답 리스트
gcd = 0
for i in range(n):
    num.append(int(input()))                        # a, b, c, d(a>b>c>d)의 나머지가 같은 수를 구하고자 할 때는 a-b, b-c, c-d 의 최대공약수를 구하면 됨
    if i == 1:                                      # 두번 째 숫자가 주어졌을 때, 첫번째 숫자와의 차의 절대값
        gcd = abs(num[1] - num[0])
    gcd = math.gcd(abs(num[i] - num[i - 1]), gcd)   # math.gcd : 최대공약수, abs : 절대값   -> 이전 최대 공약수를 이번숫자에서 바로전 숫자를 뺀 값과의 최대공약수로 변경
gcd_a = int(gcd ** 0.5)                             # gcd의 제곱근(최대공약수만큼 for문을 돌리면 시간초과가 나기 때문)
for i in range(2, gcd_a + 1):                       # 결과는 1보다 커야함
    if gcd % i == 0:                                # 최대공약수의 약수를 찾음
        a.append(i)                                 # 그 수를 정답리스트에 추가
        a.append(gcd // i)                          # 제곱근을 이용해 돌리고 있기 때문에 i로 나눈 몫도 추가
a.append(gcd)                                       # 2부터 시작했기 때문에 마지막에 최대공약수 추가
a = list(sorted(set(a)))                            # 정렬과 중복제거
print(*a)
