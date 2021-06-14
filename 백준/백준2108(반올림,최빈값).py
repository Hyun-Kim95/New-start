def avg(n):
    return round(sum(n)/t)  # 소수점 반올림/내림

def midd(n):
    if len(n) % 2 != 0:
        return n[len(n)//2]
    else:
        if t % 2 != 0:
            return n[t//2]
        else:
            return round((n[t//2-1] + n[t//2])/2)

from collections import Counter
def maax(n):
    if t == 1:
        return a[0]
    c = Counter(n).most_common(2) # 가장 많은거부터 {[hh:3],[gg:2]} 이런식으로 정렬됨
    return (c[1][0] if c[0][1] == c[1][1] else c[0][0])

def rag(n):
    return max(n) - min(n)

t = int(input())
a = sorted([int(input()) for _ in range(t)])

print(avg(a))
print(midd(a))
print(maax(a))
print(rag(a))
