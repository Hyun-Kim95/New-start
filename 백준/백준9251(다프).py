import sys                                                  # 9251

string_a = ' ' + sys.stdin.readline().rstrip()              # 글자 입력
string_b = ' ' + sys.stdin.readline().rstrip()              # 글자 입력
dp = [[0] * len(string_b) for _ in range(len(string_a))]    # 빈칸 생성

for i in range(1, len(string_a)):                           # a의 처음꺼 부터 비교 시작
    for j in range(1, len(string_b)):                       # b의 처음꺼 부터 비교 시작
        if string_a[i] == string_b[j]:                      # 같을 경우
            dp[i][j] = dp[i - 1][j - 1] + 1                 # 같을 경우 실행
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])      # 다를 경우 실행
            
print(dp[-1][-1])                                           # 마지막 가장 큰 수 출력
