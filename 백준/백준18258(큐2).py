import sys                          # 18258 큐 2
from collections import deque       # deque를 사용하지 않으면 pop(0)를 사용할때 한칸씩 당기는 과정에서 시간초과 발생

input = sys.stdin.readline          # 시간을 줄이기 위해
que = deque()                       # que를 deque로 만듬
for i in range(int(input())):
    a = input().split()
    if a[0] == 'push':
        que.appendleft(a[1])        # deque에서는 pop(0) 쓸 수 없어서 아예 왼쪽으로 넣어줌
    elif a[0] == 'size':
        print(len(que))
    elif len(que) == 0:             # que가 비었을 경우
        if a[0] == 'empty':
            print(1)
        elif a[0] == 'front' or a[0] == 'back' or a[0] == 'pop':
            print(-1)
    else:                           # que에 숫자가 있을 경우
        if a[0] == 'pop':
            print(que[-1])
            que.pop()
        elif a[0] == 'empty':
            print(0)
        elif a[0] == 'front':
            print(que[-1])
        elif a[0] == 'back':
            print(que[0])
