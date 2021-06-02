n = int(input())                            # 1992 쿼드트리
qt = [list(input()) for _ in range(n)]      # 띄어쓰기 없이 들어오기 때문에 그냥 리스트로 받아옴
ans = []                                    # 정답 보관용 리스트

def cut(x,y,n):
    chk = qt[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if chk != qt[i][j]:
                ans.append('(')             # 4등분 시작될때, 열린 괄호 추가
                cut(x,y,n//2)
                cut(x,y+n//2,n//2)
                cut(x+n//2,y,n//2)
                cut(x+n//2,y+n//2,n//2)
                ans.append(')')             # 4등분 후 함수 돌고 오면 닫힌 괄호 추가
                return
    if chk == '1':
        ans.append('1')
        return
    else:
        ans.append('0')
        return

cut(0,0,n)
print(*ans,sep="")                          # ''랑 띄어쓰기 없애주고 출력
