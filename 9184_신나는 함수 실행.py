from sys import stdin


def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    elif arr[a][b][c]:
        return arr[a][b][c]
    elif a < b < c:
        arr[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return arr[a][b][c]
    else:
        arr[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + \
            w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return arr[a][b][c]


arr = [[[0] * 21 for _ in range(21)] for _ in range(21)]
while 1:
    a, b, c = map(int, stdin.readline().split())
    result = 0
    if a == -1 and b == -1 and c == -1:
        break
    else:
        result = w(a, b, c)
    print(f"w({a}, {b}, {c}) = {result}")
