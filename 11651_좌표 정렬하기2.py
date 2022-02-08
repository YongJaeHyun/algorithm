import sys
ans = [list(map(int, sys.stdin.readline().split()))
       for _ in range(int(sys.stdin.readline()))]
ans.sort()
ans = sorted(ans, key=lambda x: x[:][1])
for i in range(len(ans)):
    print(str(ans[i][0]) + ' ' + str(ans[i][1]))
