from math import comb                   # 1010 다리 놓기(경우의 수)
                                        # 왼쪽에 놓을 수 있는 다리 수 = n, 오른쪽 = m, m > n
for i in range(0, int(input())):
    n, m = map(int, input().split())
    print(comb(m,n))                    # comb: mCn과 같은 조합 값을 반환한다. (m개의 수에서 n개를 선택, m > n)
