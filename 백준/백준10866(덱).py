import sys
from collections import deque
input = sys.stdin.readline
que = deque()
for i in range(int(input())):       # 10866 덱
    a = input().split()
    if a[0] == 'push_front':
        que.append(a[1])
    if a[0] == 'push_back':
        que.appendleft(a[1])
    elif a[0] == 'size':
        print(len(que))
    elif len(que) == 0:
        if a[0] == 'empty':
            print(1)
        elif a[0] == 'front' or a[0] == 'back' or a[0] == 'pop' or a[0] == 'pop_front' or a[0] == 'pop_back':
            print(-1)
    else:
        if a[0] == 'pop_front':
            print(que.pop())
        if a[0] == 'pop_back':
            print(que.popleft())
        elif a[0] == 'empty':
            print(0)
        elif a[0] == 'front':
            print(que[-1])
        elif a[0] == 'back':
            print(que[0])
