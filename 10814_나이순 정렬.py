from sys import stdin
ans = []
for i in range(int(stdin.readline())):
    a, b = stdin.readline().split()
    a = int(a)
    ans.extend([[a, b]])
ans.sort(key=lambda x: x[:][0])
for i in range(len(ans)):
    print(str(ans[i][0]) + ' ' + ans[i][1])
