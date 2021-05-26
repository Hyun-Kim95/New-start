n,k = map(int,input().split())  # 11866 요세푸스 문제( 요세푸스 순열: 1번부터 n번까지의 사람이 원을 이루면서 앉아있고 순서대로 k번째 사람을 제거할때 제거되는 순서)
a = [i for i in range(1,n+1)]   # 1번부터 n번까지의 번호 리스트
b = []                          # 제거된 순서 리스트
kp = k                          # kp에 초기 k의 값 보관
while len(b) != n:              # 전부 제거될 경우까지 반복
    try:
        b.append(a[k-1])        # 정해진 순서대로 b에 추가
        k += kp
    except:                     # k가 리스트 범위를 넘어서면
        k -= len(a)             # k에서 a의 길이만큼 빼고
        for j in a:             # b에 추가한 인덱스들 제거
            if j in b:
                a.remove(j)

print("<",end="")               # 출력 형식 맞추려고(EX> 입력: 7 3, 출력: <3, 6, 2, 7, 5, 1, 4> )
for i in range(len(b)-1):
    print(b[i],end=", ")
print(b[-1],end="")
print(">")
