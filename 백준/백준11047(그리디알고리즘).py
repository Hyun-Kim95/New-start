n,k = map(int, input().split())   # 동전의 갯수, 목표 금액
a = []
ea = 0
for i in range(n):
    A = int(input())              # 동전 종류
    if A <= k:                    # 목표 금액보다 작거나 같은 것만 추가
        a.append(A)

while True:
    if len(a) == 0:
        break
    if k == a[-1]:
        ea += 1
        break
    elif k - a[-1] in a:
        ea += 2
        break
    else:
        ea += k // a[-1]
        k = k % a[-1]
        for q in a:
            if q > k:
                a.remove(q)

print(ea)                         # 필요한 동전의 갯수 출력
