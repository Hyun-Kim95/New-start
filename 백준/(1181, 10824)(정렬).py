n = int(input())      # 1181
k = []
a = []
for i in range(n):
    k.append(str(input()))

for j in range(n):
    if k[j] not in a:
        a.append(k[j])

for l in range(len(a)):
    a[l] = [len(a[l]),a[l]]

a = sorted(a)

for q in range(len(a)):
    print(a[q][1])

#---------------------------------------------
# 10824
n = int(input())
k = []
for i in range(n):
    [a,b] = map(str,input().split())
    k.append([int(a),b])

k = sorted(k,key=lambda x:x[0])   # 숫자만 기준으로 정렬

for j in range(n):
    print(k[j][0],k[j][1])
