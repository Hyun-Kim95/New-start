from collections import deque                           # 5430 AC

for i in range(int(input())):                           # 테스트케이스의 갯수 입력
    p = input().replace('RR', '')                       # R: 뒤집기         D: 제거         replace('a','b'): a를 b로 바꿈          RR이면 원래대로기 때문에 없애줌
    n = int(input())                                    # 리스트의 원소 수 입력
    x = input()                                         # 리스트형식으로 입력
    x = x.replace('[','')                               # x에서 리스트의 대괄호 제거
    x = x.replace(']','')
    if x:                                               # x가 빈 리스트가 아니라면 ','기준으로 나눈 숫자를 deque로 만들어줌
        x = deque(list(map(int, x.split(','))))
    Z = False                                           # p에 R이 들어왔을 때, 실제로 뒤집어 주면 시간초과 발생 → R이 나왔는지만 확인해서 진행
    for j in p:                                         # 받은 함수를 순서대로 진행시킴
        if j == 'R':                                    # R이면 Z를 변경
            Z = not Z
        elif j == 'D':                                  # D면 R이 나왔었는지 확인해서 안나왔으면 맨 앞 숫자 삭제, 나왔었으면 맨 뒤 숫자 삭제
            if x:
                if Z:
                    x.pop()
                else:
                    x.popleft()
            else:                                       # D가 나왔는데 x가 빈 리스트라면 error 출력 후 종료
                print('error')
                break
    else:                                               # for else: for문이 'break'로 종료된게 아니라 정상적으로 진행됐으면 else문 실행
        if len(x) == 0:                                 # error는 발생안했지만 x가 빈 리스트라면 [] 출력
            print('[]')
        elif Z:                                         # x가 빈 리스트도 아니고, R이 나왔던 상태라면 마지막 숫자부터 리스트형식으로 출력
            print('[',end='')
            for q in range(len(x)-1):
                print(x[len(x)-q-1],end=',')
            print(x[0],end='')
            print(']')
        else:                                           # 아니라면 첫번째 숫자부터 리스트 형식으로 출력
            print('[',end='')
            for q in range(len(x)-1):
                print(x[q],end=',')
            print(x[-1],end='')
            print(']')
