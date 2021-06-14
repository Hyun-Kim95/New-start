import sys        # 1931
n = int(input())                                                # 그날 있을 회의의 갯수
time = []                                                       # 회의시간
for i in range(n):
    time.append(list(map(int, sys.stdin.readline().split())))   # 시작시간, 끝나는 시간
time = sorted(time, key=lambda a: a[0])                         # 시작시간을 기준으로 정렬
time = sorted(time, key=lambda a: a[1])                         # 끝나는 시간을 기준으로 정렬
last = 0                                                        # 끝나는 시간
cnt = 0                                                         # 그날 회의의 최대 갯수 표시
for i, j in time:                                               # i = 시작, j = 끝
    if i >= last:                                               # 이전 회의의 끝난 시간보다 시작시간이 늦거나 같다면 회의 갯수 추가
        cnt += 1
        last = j                                                # 추가된 회의의 끝나는 시간으로 업데이트
print(cnt)
