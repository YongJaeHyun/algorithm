from sys import stdin
ans = set()
for _ in range(int(stdin.readline())):
    ans.add(stdin.readline())
ans = sorted(list(ans))
ans.sort(key=lambda x: len(x))
for i in range(len(ans)):
    print(ans[i], end='')
