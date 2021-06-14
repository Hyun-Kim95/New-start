n = int(input())
a = list(map(int, input().split()))

k = [a[0]]

for i in range(len(a) - 1):
    k.append(max(k[i] + a[i + 1], a[i + 1]))

print(max(k))
