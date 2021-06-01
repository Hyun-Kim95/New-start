n = int(input())                                    # 2630 색종이 만들기(정사각형 내에서 색깔이 다르면 4등분해서 정사각형 모양의 같은 색깔들로 나누기)
paper = []                                          # 종이의 색깔들이 들어옴
white = 0                                           # 0 이면 흰색
blue = 0                                            # 1 이면 파란색
for i in range(n):
    paper.append(list(map(int,input().split())))

white = 0
blue = 0
def cut(x,y,n):                                     # 종이를 4등분할 함수(x: 행, y: 열, n: 변의 길이)
    global blue,white                               # 함수 밖에 있는 white, blue를 사용할거임
    check = paper[x][y]                             # check에 첫번째 자리의 색깔을 기억시킴
    for i in range(x,x+n):
        for j in range(y,y+n):
            if check!=paper[i][j]:                  # 정사각형을 돌다가 check와 색깔이 다르면 4등분
                cut(x,y,n//2)                       # 1사분면을 재귀함수로
                cut(x,y+n//2,n//2)                  # 2사분면을 재귀함수로
                cut(x+n//2,y,n//2)                  # 3사분면을 재귀함수로
                cut(x+n//2,y+n//2,n//2)             # 4사분면을 재귀함수로
                return                              # if 문을 안들어 와야 다음으로 넘어갈 수 있도록
    if check==0:                                    # 흰색 정사각형 하나 완성
        white+=1
        return
    else:                                           # 파란색 정사각형 하나 완성
        blue+=1
        return

cut(0,0,n)                                          # 0,0(왼쪽 위) 부터 n까지 확인하도록 cut함수에 넣어줌
print(white)                                        # 결과의 흰색 갯수 출력
print(blue)                                         # 결과의 파란색 갯수 출력
