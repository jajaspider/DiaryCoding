import sys,queue

sys.setrecursionlimit(100000)
A = 0
B = 0
visit = [0 for i in range(100001)]


def BFS(start, end, count):
    global visit
    dstart = [start + A, start - A, start + B, start - B, start * A, start * B, start + 1, start - 1]
    visit[start] = 1
    q = queue.Queue()
    q.put(start)
    while q:
        q.
    for i in dstart:
        print(A, B, i)
        if 0 <= i <= 100000 and visit[i] == 0:
            count += 1
            if i == end:
                print(count)
                return
            BFS(i, end, count)


def solution():
    global A, B
    A, B, N, M = map(int, sys.stdin.readline().split())
    BFS(N, M, 0)


solution()
