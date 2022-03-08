from sys import stdin

input = stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]
visited = [0 for _ in range(N)]
ans = int(1e9)


def func(idx, cnt):
    global ans
    if cnt == N//2:
        start, link = 0, 0

        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    start += arr[i][j]
                elif not visited[i] and not visited[j]:
                    link += arr[i][j]
        ans = min(ans, abs(start-link))

    for i in range(idx, N):
        if visited[i]:
            continue

        visited[i] = 1
        func(i + 1, cnt + 1)
        visited[i] = 0


func(0, 0)
print(ans)
