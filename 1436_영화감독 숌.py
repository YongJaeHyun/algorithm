n = int(input())
a = 666
cnt = 0
while 1:
    if '666' in str(a):
        cnt += 1
    if n == cnt:
        break
    a += 1
print(a)
