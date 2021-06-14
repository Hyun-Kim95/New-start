n = int(input())                                        # R P G 의 갯수

p = []

for i in range(n):
    p.append(list(map(int, input().split())))           # R P G 각 각의 숫자

for i in range(1, len(p)):                              # 2번째 거에 첫번째에서 작은것을 더함(안겹치는 색깔) -> 마지막 줄까지 진행
    p[i][0] = min(p[i - 1][1], p[i - 1][2]) + p[i][0]
    p[i][1] = min(p[i - 1][0], p[i - 1][2]) + p[i][1]
    p[i][2] = min(p[i - 1][0], p[i - 1][1]) + p[i][2]

print(min(p[n - 1][0], p[n - 1][1], p[n - 1][2]))       # 가장 작은 값 출력
