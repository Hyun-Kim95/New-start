from collections import Counter         # 9375 패션왕

for i in range(int(input())):           # 테스트 케이스의 갯수
    s = []                              # 옷의 종류
    for j in range(int(input())):       # 옷의 총 갯수
        a, b = input().split()          # a: 옷의 이름, b: 옷의 종류
        s.append(b)
    num = 1                             # 경우의 수
    cnt = Counter(s)                    # 종류별 옷의 갯수를 구함
    for w in cnt:
        num *= cnt[w] + 1
    print(num - 1)                      # (종류별 옷의 갯수 + 1) * (종류별 옷의 갯수 + 1) * ... -1을 하면 결과가 나옴
                                        # ↑↑↑ 각각의 옷을 입는 경우 + 안입는 경우               ↑↑알몸인 경우 제외
