while True:                             # 4949 균형잡힌 세상
    chek1 = 0                           # [] 체크
    chek2 = 0                           # () 체크
    chek3 = []                          # 마지막 열린괄호 확인용 리스트
    a = list(input().rstrip())          # 문장을 하나씩 쪼개서 받음(ex) So when I die (the [first] I will see in (heaven) is a score list).)
    if a[0] == "." and len(a) == 1:     # 종료조건
        break
    for i in range(len(a)):
        if a[i] == ']':                 # 닫힌 대괄호가 나오면 체크를 하나 뺌
            chek1 -= 1
            if chek1 < 0:               # 열린괄호 전에 닫힌 괄호가 먼저 나왔으므로 break (chek는 마이너스인 상태)
                break
            elif chek3[-1] == '(':      # 마지막에 열린 괄호와 한쌍이 아니면 chek를 마이너스로 바꾸고 break
                chek1 = -1
                break
            else:
                chek3.pop(-1)           # 마지막 열린 괄호와 모양이 맞으면 마지막 열린괄호를 chek3에서 삭제
        if a[i] == ')':
            chek2 -= 1
            if chek2 < 0:
                break
            elif chek3[-1] == '[':
                chek2 = -1
                break
            else:
                chek3.pop(-1)
        if a[i] == '[':                 # chek +1, 마지막 열린괄호에 추가
            chek1 += 1
            chek3.append(a[i])
        if a[i] == '(':
            chek2 += 1
            chek3.append(a[i])

    if chek1 == 0 and chek2 == 0:       # 반복문 종료 후 제대로 괄호를 사용한 문장이면 yes 출력
        print("yes")
    else:
        print("no")
