from collections import deque                   # 1021 회전하는 큐 (rotate를 최소한으로 사용한 횟수 구하기)
n,m = map(int,input().split())                  # n: 큐의 크기      m: 뽑을 숫자의 갯수
a = list(map(int,input().split()))              # a: 뽑을 숫자들의 처음 위치
que = deque([i+1 for i in range(n)])            # 1 ~ n 까지의 리스트
cnt = 0                                         # rotate 횟수 체크
while len(a) != 0:
    if que[0] == a[0]:                          # rotate가 필요없으므로 a와 que의 첫번째 인덱스 삭제만 함
        del a[0]
        que.popleft()
    else:
        if que.index(a[0]) <= len(que) // 2:    # rotate를 어느방향으로 돌리는게 최선인지 확인 후 진행
            que.rotate(-1)
            cnt += 1
        else:
            que.rotate()
            cnt += 1
print(cnt)
