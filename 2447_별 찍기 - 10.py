def star(n, st):
    ans = []
    if n == 3:
        return st
    else:
        for i in st:
            ans.append(i*3)
        for i in st:
            ans.append(i+' '*len(st)+i)
        for i in st:
            ans.append(i*3)
        return star(n//3, ans)


n = int(input())
st = ['***', '* *', '***']
ans = star(n, st)
for i in ans:
    print(i)
