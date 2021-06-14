import sys
t = int(sys.stdin.readline())
for i in range(t):
    a,b = map(int,sys.stdin.readline().split())
    print(a + b)
#import sys
#sys.stdin.readline()
#숫자가 클 때 input() 대신에 sys.stdin.readline() 사용하면 훨씬 빠름
#--------------------------------------------------------------------
num = int(input())
check = num
new_num = 0
temp = 0
count = 0
while True:
    temp = num//10 + num%10
    new_num = (num%10)*10 + temp%10
    count += 1
    num = new_num
    if new_num == check:
        break
print(count)
