import sys

sys.setrecursionlimit(100000)


def dfs(current, N, visit, money):
    visit.append(current)
    if matrix[current - 1][0] == 'L':
        if money <= int(matrix[current - 1][1]):
            money = int(matrix[current - 1][1])
    elif matrix[current - 1][0] == 'T':
        money -= int(matrix[current - 1][1])
        if money < 0:
            return

    if current == N:
        moneys.append(money)
        return

    for i in range(2, len(matrix[current - 1])):
        if matrix[current - 1][i] == 0:
            return
        if int(matrix[current - 1][i]) not in visit:
            dfs(int(matrix[current - 1][i]), N, visit, money)


while True:
    N = int(input())
    if N == 0:
        break
    current_money = 0
    matrix = []
    visit = []
    moneys = []
    for i in range(0, N):
        matrix.append(sys.stdin.readline().replace("\n", "").split(" "))
    # print(matrix)
    flag = 0
    dfs(1, N, visit, 0)
    for i in range(0, len(moneys)):
        if int(moneys[i]) >= 0:
            print("Yes")
            flag = 1
            break
    if flag == 0:
        print("No")
