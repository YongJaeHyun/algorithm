n = int(input())
ans = [int(input()) for i in range(n)]
ans.sort()
for i in range(n):
    print(ans[i])
