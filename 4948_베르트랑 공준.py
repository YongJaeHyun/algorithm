import sys
arr = ([False]+[True])*(123456+1)
arr[1], arr[2] = False, True
for i in range(3, int((123456*2)**.5)+1):
    if arr[i] == True:
        j = 2
        while i*j <= 123456*2:
            arr[i*j] = False
            j += 1
        else:
            pass
while 1:
    ans = 0
    n = int(sys.stdin.readline())
    if n == 0:
        break
    for i in range(n+1, 2*n+1):
        if arr[i]:
            ans += 1
    print(ans)
