ans = []
n, m = map(int, input().split())


def func():
    if len(ans) == m:
        print(' '.join(map(str, ans)))

    for i in range(1, n+1):
        if i not in ans:
            ans.append(i)
            func()
            ans.pop()


func()
