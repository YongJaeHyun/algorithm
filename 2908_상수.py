a = input().split()
b,c = list(a[0]), list(a[1])
b.reverse()
c.reverse()
if b<c: print(int(''.join(c)))
else: print(int(''.join(b)))