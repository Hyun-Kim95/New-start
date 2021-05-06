N = list(map(int,input().split()))
a = max(N)                        # 둘중에 큰수
b = min(N)                        # 나머지 숫자
i = 1
j = 1
while True:                       # 최대 공약수 구하기
    if a % j == 0:
        if b % (a // j) == 0:
            print(a // j)
            break
        else:
            j += 1
    else:
        j += 1

while True:                       # 최소 공배수 구하기
    if a * i % b == 0:
        print(a*i)
        break
    else:
        i += 1
