N, M = map(int, input().split())

num_list = [i + 1 for i in range(N)]
check_list = [False] * N

arr = []


def dfs(cnt, start):
    if cnt == M:
        print(*arr)
        return

    for i in range(start, N):
        if check_list[i]:
            continue

        check_list[i] = True
        arr.append(num_list[i])
        dfs(cnt + 1, i + 1)
        arr.pop()
        check_list[i] = False


dfs(0, 0)
