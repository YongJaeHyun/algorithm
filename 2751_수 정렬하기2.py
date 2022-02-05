import sys
n = int(sys.stdin.readline())
ans = [int(sys.stdin.readline()) for i in range(n)]
ans.sort()
for i in range(n):
    print(ans[i])
