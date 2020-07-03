N, M = map(int, input().split())
matrix = [[] for _ in range(N)]
for i in range(0, int(N)):
    temp = list(map(int, input().split()))
    matrix[i].extend(temp)
countlist = []
for _ in range(int(input())):
    i, j, x, y = map(int, input().split())
    count = 0
    for A in range(i - 1, x):
        for B in range(j - 1, y):
            count += matrix[A][B]
    countlist.append(count)

for i in countlist:
    print(i)