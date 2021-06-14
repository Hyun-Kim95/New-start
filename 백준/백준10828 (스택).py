# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑문제에서 주어진 조건
import sys                            # 10828 스택
input = sys.stdin.readline            # 시간초과 해결
num = []
for i in range(int(input())):
    a = input().split()
    if a[0] == 'push':                # num에 순서대로 넣어줌(최근에 넣은 것이 마지막에 들어감)
        num.append(a[1])
    elif a[0] == 'pop':               # 리스트에 숫자가 있을 때, 마지막 숫자 출력 후 제거
        if len(num) != 0:
            print(num[-1])
            num.pop(-1)               # remove를 사용하면 그 숫자를 첫번째 인덱스부터 순서대로 찾다가 없애기 때문에 pop을 사용
        else:
            print(-1)
    elif a[0] == 'size':              # 리스트의 길이 출력
        print(len(num))
    elif a[0] == 'empty':             # 리스트가 비었으면 1 출력
        if len(num) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == 'top':               # 리스트에 숫자가 있을 때, 맨 마지막 숫자 출력
        if len(num) != 0:
            print(num[-1])
        else:
            print(-1)
