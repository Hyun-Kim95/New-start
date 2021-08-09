# n개의 음이 아닌 정수가 있습니다. 이 수를 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다.
# 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
# 사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서
# 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
# 각 숫자는 1 이상 50 이하인 자연수입니다.
# 타겟 넘버는 1 이상 1000 이하인 자연수입니다.

def solution(numbers, target):
    answer = 0                              # 경우의 수 확인
    def sol(num, i):                        # 첫번째 요소부터 부호를 바꿔가면서 진행
        nonlocal answer                     # 지역변수 answer를 사용(global은 사용 자제하라 함)

        if i == len(numbers):               # 마지막 요소까지 더했으면
            if num == target:               # 타켓넘버랑 같은지 확인
                answer += 1
            return

        if i == 1:                          # 첫번째 요소이면  이번 요소와 다음 요소의 부호를 가능한 만큼 재귀돌림
            sol(-num + numbers[i], i + 1)
            sol(-num - numbers[i], i + 1)
            sol(num + numbers[i], i + 1)
            sol(num - numbers[i], i + 1)
        else:                               # 첫번째 요소가 아니면 다음 요소의 부호만 가능한 만큼 재귀 돌림
            sol(num + numbers[i], i + 1)
            sol(num - numbers[i], i + 1)

    sol(numbers[0], 1)                      # 처음에는 0번째 요소와 1을 넣어줌
    return answer                           # 다 합쳐진 answer 리턴
  
print(solution([1,1,1,1,1],3))              # 테스트 확인용 프린트문
