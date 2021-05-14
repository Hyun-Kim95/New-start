def number(i, j):                                               # 2의 갯수와 5의 갯수를 확인하는 함수
    count = 0
    while(i != 0):
        i = i // j
        count += i
    return count

n, m = list(map(int, input().split()))                          # 2004 조합 0의 갯수

five = number(n, 5) - number(m, 5) - number(n-m, 5)             # 5의 갯수를 확인해서 나온 0의 갯수
two = number(n, 2) - number(m, 2) - number(n-m, 2)              # 2의 갯수를 확인해서 나온 0의 갯수

print(min(five, two))                                           # 위 둘중에 작은 값이 정답


# nCm(조합) 의 공식은 ↓

# (n)        n!
# ( )   = --------
# (m)     m!(n-m)!

# 0의 갯수를 구하는 것이므로 ↓

# n! // (m! * (n-m)!)
# n! - (m! + (n-m)!)
# n! - m! - (n-m)!

# ↑↑↑
# 진짜 팩토리얼로 구해서 문제를 해결하게 되면 시간초과 발생
# 끝자리가 0이라는 것은 10의 배수
# 10은 2와 5로 구성되어 있음
# 2와 5 짝이 맞아야 10이 되므로 2의 개수와 5의 개수중 더 작은게 10의 개수이다.
