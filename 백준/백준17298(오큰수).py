n = int(input())                          # 17298 오큰수: 주어진 수의 오른쪽에 있으면서 큰 수들 중에 가장 왼쪽에 있는 숫자찾기
a = list(map(int, input().split()))
stack = []                                # 인덱스가 들어갈 리스트
nge = [-1 for _ in range(n)]              # 오큰수가 없으면 -1을 출력하기 때문

for i in range(len(a)):
    try:                                  # stack의 마지막 숫자를 인덱스로 가지는 값보다 i인덱스의 값이 더 크면 stack의 마지막 값을 삭제하고 nge의 그 인덱스 값을 a[i]로 변경
        while a[stack[-1]] < a[i]:
            nge[stack.pop()] = a[i]
    except:                               # stack의 값이 없거나 a[i]의 값이 더 작으면 패스
        pass

    stack.append(i)                       # stack에 i추가

print(*nge)
