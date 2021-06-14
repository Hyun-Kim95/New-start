x = int(input())                        # a의 갯수      # 18870
a = list(map(int,input().split()))
a1 = list(sorted(set(a)))               # 중복제거, 오름차순 정렬(인덱스 순서로 작은 수들의 갯수를 보려고)  ex) 0번째 인덱스의 값은 가장 작은 값이라서 0 출력

dic = {a1[i]:i for i in range(len(a1))} # 딕셔너리 형태로 만듬(시간 초과 해결용)                            ex) {999: 0, 1000: 1, 1001: 2} 이런식으로 저장됨

print(*[dic[i] for i in a])             # a의 첫번째 요소부터 끝까지 딕셔너리 값을 불러냄(겉에 리스트 제거 후 출력)
