n = int(input())    #2565
a = []
dp = [1 for i in range(n)]
for i in range(n):
    a.append(list(map(int,input().split())))

a.sort()              # 첫번째 전봇대를 기준으로 정렬

for j in range(n):    # 가장 긴 증가하는 수열
    for k in range(j):
        if a[j][1] > a[k][1]:
            dp[j] = max(dp[j], dp[k] + 1)

print(n-max(dp))      # 전체 전기줄 갯수 - 가장 긴 수열의 길이 = 없앨 전기줄의 갯수
