n = int(input())
s = [0 for i in range(16)]
result = 0
def isTrue(x):
    for i in range(1, x):
        if s[x] == s[i] or abs(s[x] - s[i]) == x - i:
            return False
    return True
def dfs(cnt):
    global result
    if cnt > n:
        result += 1
    else:
        for i in range(1, n + 1):
            s[cnt] = i
            if isTrue(cnt):
                dfs(cnt + 1)
dfs(1)
print(result)

# cnt: 퀸의 열위치
# s[cnt]: cnt에 퀸이 있을 때 행의 값
# abs: 절대값
# abs(s[x] - s[i]) == x - i : 대각선위치에 존재
# s[x] == s[i] : 같은 행
# if cnt > n: result += 1 : 무한루프 탈출용
