n = int(input())                                            # 1780 종이의 개수
paper = [list(map(int,input().split())) for _ in range(n)]  # 종이의 숫자가 들어옴(0,1,-1)
minus = 0
zero = 0
one = 0

def cut(x,y,n):                                     # 종이를 9등분할 함수(x: 행, y: 열, n: 변의 길이)
    global minus,zero,one                           # 함수 밖에 있는 minus,zero,one을 사용할거임
    check = paper[x][y]                             # check에 첫번째 자리의 색깔을 기억시킴
    for i in range(x,x+n):
        for j in range(y,y+n):
            if check!=paper[i][j]:                  # 정사각형을 돌다가 check와 색깔이 다르면 9등분
                cut(x,y,n//3)                       # 위 왼쪽
                cut(x,y+n//3,n//3)                  # 위 중앙
                cut(x,y+n//3+n//3,n//3)             # 위 오른쪽
                cut(x+n//3,y,n//3)                  # 중앙 왼쪽
                cut(x+n//3,y+n//3,n//3)             # 중앙 중앙
                cut(x+n//3,y+n//3+n//3,n//3)        # 중앙 오른쪽
                cut(x+n//3+n//3,y,n//3)             # 아래 왼쪽
                cut(x+n//3+n//3,y+n//3,n//3)        # 아래 중앙
                cut(x+n//3+n//3,y+n//3+n//3,n//3)   # 아래 오른쪽

                return                              # if 문을 안들어 와야 다음으로 넘어갈 수 있도록
    if check==0:                                    # 같은 숫자끼리 모이면 정사각형 하나 완성
        zero+=1
        return
    elif check==1:
        one+=1
        return
    else:
        minus+=1
        return

cut(0,0,n)                                          # 0,0(왼쪽 위) 부터 n까지 확인하도록 cut함수에 넣어줌
print(minus)
print(zero)
print(one)
