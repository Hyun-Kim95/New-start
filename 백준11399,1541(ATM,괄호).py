n = int(input())                    # 11399
a = list(map(int,input().split()))

a = sorted(a)
for i in range(1,n):
    a[i] += a[i-1]

print(sum(a))

#-------------------------
n = input().split('-')              # 1541    # 숫자와 + - 기호로 이루어진 문자를 -를 기준으로 받음
number = []
for i in n:
    a = 0
    k = i.split('+')                          # + 를 기준으로 나눔(없으면 그냥 내려옴)
    for j in k:
        a += int(j)                           # - 전 부분은 그냥 나오고, +가 있는 부분은 자기들 끼리 합침
    number.append(a)                          # 순서대로 넣어줌
b = number[0]                                 # 첫번째는 무조건 숫자라는 조건을 통해 +임을 알기 때문에
for w in range(1,len(number)):
    b -= number[w]                            # 첫번째 숫자에서 나머지 숫자들을 빼줌
print(b)                                      # 마이너스를 기준으로 괄호를 만든 최소 값이 출력됨
