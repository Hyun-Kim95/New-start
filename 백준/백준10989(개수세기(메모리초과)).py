import sys

b = [0]*10001
for i in range(int(sys.stdin.readline())):
    b[(int(sys.stdin.readline()))] += 1

for j in range(10001):
    if b[j] != 0:
        for k in range(b[j]):
            print(j)
            
# 메모리 초과를 벗어나기 위한 코드
