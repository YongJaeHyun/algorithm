import sys
n = int(sys.stdin.readline())
ans = 0
row = [0] * n


def is_empty(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x]-row[i]) == abs(x-i):
            return False
    return True


def queen(x):
    global ans
    if x == n:
        ans += 1
    else:
        for i in range(n):
            row[x] = i
            if is_empty(x):
                queen(x+1)


queen(0)
print(ans)
