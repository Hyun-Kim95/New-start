for i in range(int(input())):       # 9012 괄호들이 모양이 바른지 확인하는 문제
    chek = 0                        # 확인용 변수
    a = list(input().rstrip())      # 정보를 하나씩 구분하여 받음
    for j in range(len(a)):
        if a[0] == ')':             # 첫번째가 닫힘이면 -1로 바꾸고 break
            chek = -1
            break
        elif a[j] == '(':           # 열림이면 +1
            chek += 1
        else:
            chek -= 1               # 닫힘이면 -1
            if chek < 0:            # 단, chek가 마이너스면 break
                break
    if chek == 0:                   # 결과로 chek가 0이면 YES 출력
        print('YES')
    else:
        print('NO')
