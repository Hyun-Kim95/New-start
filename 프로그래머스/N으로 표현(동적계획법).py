# 아래와 같이 5와 사칙연산만으로 12를 표현할 수 있습니다.

# 12 = 5 + 5 + (5 / 5) + (5 / 5)
# 12 = 55 / 5 + 5 / 5
# 12 = (55 + 5) / 5

# 5를 사용한 횟수는 각각 6,5,4 입니다. 그리고 이중 가장 작은 경우는 4입니다.
# 이처럼 숫자 N과 number가 주어질 때, N과 사칙연산만 사용해서 표현 할 수 있는 방법 중 N 사용횟수의 최솟값을 return 하도록 solution 함수를 작성하세요.

# 제한사항
# N은 1 이상 9 이하입니다.
# number는 1 이상 32,000 이하입니다.
# 수식에는 괄호와 사칙연산만 가능하며 나누기 연산에서 나머지는 무시합니다.
# 최솟값이 8보다 크면 -1을 return 합니다.

# 3개를 사용해서 만들 수 있는 종류들은 1개를 이용해서 만들 수 있는 종류들과 2개를 이용해서 만들 수 있는 종류들을 사칙연산으로 만든 종류들과 같다를 이용해서 해결
def solution(N, number):
    list = [0,[N]]                          # 조합으로 나올수 있는 가능한 숫자들, 여기에 계속 append하며 이후에 사용함(인덱스 == N을 사용한 개수)
    if N == number:                         # 주어진 숫자와 같은 경우는 1 리턴
        return 1
    for i in range(2, 9):                   # 2부터 8까지로 횟수를 늘려 감
        list_a = []                         # 임시로 사용할 리스트, 각 i 별로 리스트를 만들어 전체리스트에 붙인다.
        num = int(str(N)*i)                 # 같은 숫자 반복되는 거 하나를 추가
        list_a.append(num)
        for j in range(1, i//2+1):          # 사용되는 숫자의 횟수를 구해야 하는데, 절반 이상 넘어가면 같은 결과가 나와서
            for x in list[j]:
                for y in list[i-j]:         # x와 y를 더하면 i 가 되도록 만든 수다. 
                    if (x+y) not in list_a:
                        list_a.append(x+y)  # 각 사칙연산 결과를 더한다.
                    if (x-y) not in list_a:
                        list_a.append(x-y)
                    if (y-x) not in list_a:
                        list_a.append(y-x)
                    if (x*y) not in list_a:
                        list_a.append(x*y)
                    if y !=0 and x//y not in list_a:
                        list_a.append(x//y)
                    if x !=0 and y//x not in list_a:
                        list_a.append(y//x)
        if number in list_a:                # 답이 있으면 사용한개수(i) 리턴
            return i
        list.append(list_a)                 # 전체리스트에 사칙 연산 결과를 더함

    return -1                               # N 이 8까지 답이 없으면 -1을 출력


print(solution(5,1010),7)                   # 정답 확인용
print(solution(2,22223),7)
print(solution(2,22224),6)
print(solution(2,11111),6)
