import sys

N, M = map(int, sys.stdin.readline().split())
# matrix = [[] * M for _ in range(0, N)]
matrix = []

for _ in range(0, N):
    matrix.append(list(map(int, sys.stdin.readline().split())))
countlist = []
for _ in range(int(sys.stdin.readline())):
    i, j, x, y = map(int, sys.stdin.readline().split())
    count = 0
    for A in range(i - 1, x):
        for B in range(j - 1, y):
            count += matrix[A][B]
    countlist.append(count)

for i in countlist:
    print(i)
