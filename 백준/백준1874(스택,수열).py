n = int(input())                # 1874 스택 수열
a = []                          # 스택(LIFO)
pm = []                         # 출력해야할 '+','-' 기호
count = 1                       # 숫자비교용(1 ~ n)
temp = True                     # 가능한지 확인용
for i in range(n):
    num = int(input())          # 수열의 숫자가 하나씩 주어짐
    while count <= num:         # 주어진 수열의 숫자와 같아질 때까지 count와 기호 추가
        a.append(count)
        pm.append('+')
        count += 1
    if a[-1] == num:            # 스택의 마지막 숫자와 주어진 숫자가 같으면 스택의 마지막 숫자를 pop하고 '-'기호 추가
        a.pop()
        pm.append('-')
    else:                       # 스택의 마지막 숫자와 주어진 숫자가 다르다는 것은 만들 수 없는 수열이란 뜻이므로 False로 변결
        temp = False
if temp == False:
    print('NO')
else:
    for i in pm:
        print(i)
