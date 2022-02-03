n = int(input())
xy = [list(map(int, input().split())) for i in range(n)]
for i in range(n):
    cnt = 0
    for j in xy:
        if xy[i][0] < j[0] and xy[i][1] < j[1]:
            cnt += 1
    print(cnt+1, end=' ')
