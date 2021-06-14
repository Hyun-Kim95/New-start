t = int(input())                            # 1966 프린터 큐
for i in range(t):                          # 테스트케이스의 수
    n, m = map(int, input().split())        # n: 자료의 수      m: 찾을 자료의 인덱스값
    a = list(map(int, input().split()))     # n개의 중요도 리스트
    a1 = [0 for _ in range(n)]              # m의 위치 변화 확인용
    a1[m] = 1                               # 1의 위치로 확인 ↑↑↑
    cnt = 0                                 # 출력 순서 체크
    while True:
        if a[0] == max(a):                  # 가장 큰 값이 맨 앞에 있으면
            cnt += 1                        # 출력 순서 하나 증가
            if a1[0] == 1:                  # 맨 앞에 있는 가장 큰 수가 m값이면
                print(cnt)                  # 프린트 후 반복종료(다음 테스트 케이스로 이동)
                break
            else:
                del a[0]                    # m값이 맨 앞이 아니면 맨앞 숫자 삭제, m의 위치 한칸 앞당겨짐
                del a1[0]
        else:
            a.append(a[0])                  # 맨 앞의 숫자가 가장 큰 수가 아니면 맨 앞의 숫자를 맨 뒤로 옮김
            del a[0]                        # del: 인덱스로 제거(a[3:]과 같이 범위 연산자 사용가능)
            a1.append(a1[0])                # remove: 값으로 제거
            del a1[0]
