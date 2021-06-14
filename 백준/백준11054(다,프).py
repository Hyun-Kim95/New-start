n = int(input())
a = list(map(int, input().split()))
     # ↓ 최소 1이라서
dpp = [1 for i in range(n)]     # 증가하는 수열
dpm = [1 for i in range(n)]     # 감소하는 수열

for i in range(n):
    for j in range(i):
        if a[i] > a[j]:         # i번째가 그 전까지보다 클때
            dpp[i] = max(dpp[i], dpp[j] + 1)
a.reverse()                     # 감소하는 수열 확인하려고
for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dpm[i] = max(dpm[i], dpm[j] + 1)
dpm.reverse()                   # 원래대로 전환
dpb = [0 for i in range(n)]     # 바이토닉 부분수열
for i in range(n):
    dpb[i] = dpp[i] + dpm[i]    # 합친 수를 넣음
print(max(dpb) - 1)             # 최고점이 겹쳐서 1을 빼줌
