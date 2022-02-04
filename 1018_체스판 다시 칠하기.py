n, m = map(int, input().split())
ans = []
board = [list(input()) for i in range(n)]
for i in range(n - 7):
    for j in range(m - 7):
        W_cnt, B_cnt = 0, 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0:
                    if board[a][b] != 'W':
                        W_cnt += 1
                    if board[a][b] != 'B':
                        B_cnt += 1
                else:
                    if board[a][b] != 'W':
                        B_cnt += 1
                    if board[a][b] != 'B':
                        W_cnt += 1
        ans.append(W_cnt)
        ans.append(B_cnt)
print(min(ans))
