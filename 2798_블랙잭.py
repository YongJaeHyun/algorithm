n, m = map(int, input().split())
num = list(map(int, input().split()))
ans = []
for i in num:
    for j in num:
        for k in num:
            if i+j+k <= m and i != j != k != i:
                ans.append(m-(i+j+k))
            else:
                pass
print(m - min(ans))
