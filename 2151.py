import sys

matrix = [[0] * 50 for i in range(50)]

N = sys.stdin.readline()
# 세로만큼의 입력을 추가로 한줄씩 받아온다
for j in range(0, int(N)):
    tempstring = input()
    for i in range(0, int(N)):
        # 받아온데이터를 map배열에 입력
        matrix[j][i] = tempstring[i]
