import collections
from openpyxl import load_workbook
wb = load_workbook("lotto.xlsx")
ws = wb.active

num = [] * 6
alpha = [ "J", "K", "L", "M", "N", "O"]
maxalpha = ["Q1", "R1", "S1", "T1", "U1", "V1"]

while True:
    for i in range(6):
        전체숫자 = []
        최근숫자 = []
        다음숫자 = []
        부호 = []
        for row in ws.rows:
            전체숫자.append(row[i+1].value)

        최근숫자.append(전체숫자[0])
        전체숫자[0] = 0
        while 최근숫자[0] in 전체숫자:
            a = 전체숫자.index(최근숫자[0])
            다음숫자.append(전체숫자[a-1])
            전체숫자[a] = 0

        while 0 in 다음숫자:
            다음숫자.remove(0)
        

        for j in range(len(다음숫자)):
            ws[alpha[i]][j].value = 다음숫자[j]

        counts = collections.Counter(다음숫자)

        ws[maxalpha[i]].value = counts.most_common(1)[0][0]
    break

wb.save("lotto.xlsx")
wb.close()