st = input().upper()
str = list(set(st))
ans = [st.count(i) for i in str]
if ans.count(max(ans)) > 1: print("?")
else: print(str[ans.index(max(ans))])