ans = []
n, m = map(int, input().split())


def func(i):
    if len(ans) == m:
        print(' '.join(map(str, ans)))

    for i in range(i, n+1):
        if i not in ans:
            ans.append(i)
            func(i)
            ans.pop()


i = 1
func(i)
