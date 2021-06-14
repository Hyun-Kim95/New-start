import sys                                                      # 12865
(N, K) = map(int, sys.stdin.readline().split())                 # 짐의 개수, 들 수 있는 무게
item = [[0, 0]]                                                 # 짐의 무게와 가치
for i in range(1, N + 1):
    item.append(list(map(int, sys.stdin.readline().split())))
dp = [[0] * (K + 1) for _ in range(N + 1)]                      # 무게와 가치의 표를 만듬

for i in range(1, N + 1):
    for j in range(1, K + 1):
        if j >= item[i][0]:                                     # i번 아이템의 무게가 들 수 있는 무게일 때
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-item[i][0]] + item[i][1])  # 이전 아이템일 때 최대가치, 이전 아이템에서 지금 아이템 무게를 뺀 것의 가치 + 지금가치 중에 최대값
        else:
            dp[i][j] = dp[i-1][j]
print(dp[N][K])
