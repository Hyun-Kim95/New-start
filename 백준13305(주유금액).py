n = int(input())                        # 13305   리터 = 키로수
doro = list(map(int,input().split()))   # 도로의 길이
juyu = list(map(int,input().split()))   # 주유소 리터당 금액
cnt = 0                                 # 최소 주유 금액
a = 1000000001                          # 리터당 최대 금액 + 1

for i in range(n-1):
    if juyu[i] == min(juyu):            # i번째 도시의 주유소 금액이 최소금액이면 남은 도로의 길이만큼 여기서 주유함
        for j in range(i,len(doro)):
            cnt += juyu[i] * doro[j]
        break

    elif juyu[i] > juyu[i+1]:           # 다음 도시보다 지금 도시가 비쌀 경우
        if juyu[i] > a:
            cnt += a * doro[i]          # 이 전에 더 싼 도시가 있었으면 거기서 주유한 것으로 계산함
        else:
            cnt += juyu[i] * doro[i]    # 아니면 다음 도시까지 갈 정도만 주유함
    
    elif juyu[i] <= juyu[i+1]:          # 도시 중 최소 금액은 아니지만 다음 도시보다 싼 경우
        if juyu[i] > a:                 # 이전 도시들 중에 더 싼 곳이 있으면 거기서 주유한 것으로 계산
            cnt += a * doro[i]
        else:
            a = juyu[i]                 # 지금 도시가 지금까지 중 가장 싸면 다음 도시까지 갈 만큼 주유
            cnt += a * doro[i]

print(cnt)
